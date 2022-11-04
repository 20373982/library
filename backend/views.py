import datetime

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from backend import models
from django.db import connection
import time

# Create your views here.
# 获得当前的用户名与权限(0:未登录,1:用户登录,2:管理员登录)
def get_name_limit(request):
    try:
        name = request.session['info']['name']
        limit = request.session['info']['limit']
    except:
        name = None
        limit = 0
    return name, limit


def test(request):
    name, limit = get_name_limit(request)
    back_data = {
        'name': name,  # 用户名
        'limit': limit,  # 权限
    }
    return render(request, 'base.html', back_data)


def user_login(request):
    name, limit = get_name_limit(request)
    if request.method == 'GET':
        back_data = {
            'name': name,  # 用户名
            'limit': limit,  # 权限
            'category': 0,  # 区别用户登录与管理员登录
            'error': False,  # 是否报错
        }
        return render(request, 'login.html', back_data)
    try:
        username = request.POST['username']
        password = request.POST['password']
        # backend = models.backend.objects.get(user_name=username, user_pwd=request.POST['password'])
        # 请导入library_model后,在数据库查找用户，没找到请报错
        user_info = models.Borrower.objects.filter(borrower_name=username, borrower_pwd=password)
        if not user_info:
            raise
        userid = user_info[0].borrower_id
        request.session['info'] = {'name': username, 'limit': 1, 'id': userid}
        return redirect('/home/')
    except:
        back_data = {
            'name': name,
            'limit': limit,
            'category': 0,
            'error': True,
        }
        return render(request, 'login.html', back_data)


def admin_login(request):
    name, limit = get_name_limit(request)
    if request.method == 'GET':
        back_data = {
            'name': name,  # 用户名
            'limit': limit,  # 权限
            'category': 1,  # 区别用户登录与管理员登录
            'error': False,  # 是否报错
        }
        return render(request, 'login.html', back_data)
    try:
        username = request.POST['username']
        password = request.POST['password']
        # backend = models.admin.objects.get(admin_name=username, admin_pwd=request.POST['password'])
        # 数据库查找管理员，没找到请报错
        user_info = models.Manager.objects.filter(manager_name=username, manager_pwd=password)
        if not user_info:
            raise
        userid = user_info[0].manager_id
        request.session['info'] = {'name': username, 'limit': 2, 'id': userid}
        return redirect('/homeA/')
    except:
        back_data = {
            'name': name,
            'limit': limit,
            'category': 1,
            'error': True,
        }
        return render(request, 'login.html', back_data)


def user_register(request):
    name, limit = get_name_limit(request)
    if request.method == 'GET':
        back_data = {
            'name': name,
            'limit': limit,
            'category': 0,
        }
        return render(request, 'register.html', back_data)
    # models.user.objects.create(user_name=request.POST['username'], user_pwd=request.POST['password'])
    # 请导入library_model后,在数据库创造用户
    # 检查是否重名
    check = models.Borrower.objects.filter(borrower_name=request.POST['username'])
    if check:
        # 这里填充一下错误信息
        return redirect('/registerC/')

    models.Borrower.objects.create(borrower_name=request.POST['username'],
                                   borrower_pwd=request.POST['password'],
                                   borrower_phone='0', borrower_credit=10)
    return redirect('/loginC/')


def admin_register(request):
    name, limit = get_name_limit(request)
    if request.method == 'GET':
        back_data = {
            'name': name,
            'limit': limit,
            'category': 1,
        }
        return render(request, 'register.html', back_data)
    # models.admin.objects.create(admin_name=request.POST['username'],
    #                                     admin_pwd=request.POST['password'])
    # 在数据库创造管理员
    # 检查是否重名
    check = models.Manager.objects.filter(manager_name=request.POST['username'])
    if check:
        # 这里填充一下错误信息
        return redirect('/registerA/')

    models.Manager.objects.create(manager_name=request.POST['username'],
                                  manager_pwd=request.POST['password'],
                                  manager_phone='0')
    return redirect('/loginA/')


def logout(request):
    request.session.clear()
    return redirect("/loginC/")


def home(request):
    books = models.Book.objects.filter()
    book_list = []
    for item in books:
        back_data_temp = {
            'id': item.book_id,
            'name': item.book_name,
            'writer': item.book_writer,
            'hot': item.book_hot,
            'intro': item.book_introduction,
            'path': item.book_path,
            'status': item.status,
        }
        book_list.append(back_data_temp)
    back_data = {
        'books': book_list,
    }
    return render(request, 'home.html', back_data)


def homeA(request):
    customers = models.Borrower.objects.filter()
    customers_list = []
    for item in customers:
        back_data_temp = {
            'id': item.borrower_id,
            'name': item.borrower_name,
            'phone': item.borrower_phone,
            'credit': item.borrower_credit,
        }
        customers_list.append(back_data_temp)
    back_data = {
        'customers': customers_list,
    }
    return render(request, 'homeA.html', back_data)


def forum(request):
    topic = request.GET.get('topic')
    if topic is None:
        topic = 0
    topic = int(topic)
    if topic != 0:
        comments = models.Message.objects.filter(message_reply=1, message_topic=topic)
        comment_list = []
        # 由于message_reply是一个依赖于message_id的属性，所以这里我在数据库中添加了一个id=reply=1的数据。
        # 这条数据是不显示的，仅用于指示评论是否为回复，reply=1则该评论不是回复，否则为对id=reply的评论的回复
        for item in comments:
            if item.message_id != 1:
                back_data_temp = {
                    'id': item.message_id,
                    'content': item.message_content,
                    'writer': item.message_writer.borrower_id,
                    'topic': item.message_topic.topic_id,
                }
                comment_list.append(back_data_temp)
        back_data = {
            'type': 1,
            'topic': topic,
            'comments': comment_list,
        }
        return render(request, 'forum.html', back_data)
    else:
        topics = models.Topic.objects.filter()
        topic_list = []
        for item in topics:
            print(item.topic_id)
            back_data_temp = {
                'id': item.topic_id,
                'title': item.topic_title,
                'intro': item.topic_intro,
            }
            topic_list.append(back_data_temp)
        back_data = {
            'type': 0,
            'topics': topic_list,
        }
        return render(request, 'forum.html', back_data)

def add_comment(request):
    if request.method == 'GET':
        # 这些参数后续需要通过POST传回，或者有其他方法请随意
        back_data = {
            'reply': request.GET.get('nid'),
            'topic': request.GET.get('topic')
        }
        return render(request, 'comment.html', back_data)
    # 前端需要传输评论内容(content)，评论作者的id(writer，session中就有)，
    # 评论主题(topic，选择范围视数据库topic而定)，回复id(reply，若该评论不是回复，该值传1)
    # 请前端同学在comment.html中完成对应功能
    content = request.POST['content']
    writer = models.Borrower.objects.get(borrower_id=request.session['info'].get('id'))
    topic = models.Topic.objects.get(topic_id=request.POST['topic'])
    reply = models.Message.objects.get(message_id=request.POST['reply'])
    models.Message.objects.create(message_content=content, message_writer=writer,
                                  message_topic=topic, message_reply=reply)
    return redirect('/forum/?topic=' + topic)


def delet_comment(request):
    # 权限的规定我不太清楚，请对删除操作进行权限校验
    message_id = request.GET.get('nid')
    topic = request.GET.get('topic')
    # message数据库中筛选 message_reply = message_id 的数据
    replys = models.Message.objects.filter(message_reply=message_id)
    # 删除
    for item in replys:
        item.delete()
    # 删除自己
    self = models.Message.objects.filter(message_id=message_id).first()
    self.delete()
    return redirect('/forum/?topic=' + topic)


def review(request):
    book_id = request.GET.get('nid')
    book_id = int(book_id)
    # review数据库筛选 review_book == book_id 的记录，并存放到back_data中
    reviews = models.Review.objects.filter(review_book=book_id)
    review_list = []
    for item in reviews:
        back_data_temp = {
            'id': item.review_id,
            'content': item.review_content,
            'mark': item.review_mark,
        }
        review_list.append(back_data_temp)
    back_data = {
        'book': book_id,
        'reviews': review_list,
    }
    return render(request, 'book_detail_page.html', back_data)


def add_reveiw(request):
    if request.method == 'GET':
        review_book = request.GET.get('nid')
        # 向前端传book_id，之后需要再传回来，假定用POST
        back_data = {
            'book': review_book,
        }
        return render(request, 'review.html', back_data)
    # 接收参数并在数据库中创建对应数据，请前端同学在review.html中完成对应功能
    review_book = models.Book.objects.get(book_id=request.POST['id'])
    review_content = request.POST['content']
    review_mark = request.POST['mark']
    models.Review.objects.create(review_book=review_book,
                                 review_content=review_content,
                                 review_mark=review_mark)
    return redirect('/review/?nid=' + review_book)


def delet_review(request):
    book_id = request.GET.get('nid')
    review_id = request.GET.get('rid')
    self = models.Review.objects.filter(review_id=review_id).first()
    self.delete()
    return redirect('/review/?nid=' + book_id)


def borrow_book(request):
    borrower_id = models.Borrower.objects.get(borrower_id=int(request.session['info'].get('id')))
    book_id = models.Book.objects.get(book_id=int(request.GET.get('nid')))
    borrow_time = datetime.date.today()
    return_time = datetime.date.today() + datetime.timedelta(days=30)
    models.Borrow_record.objects.create(borrower_id=borrower_id,
                                        book_id=book_id,
                                        borrow_time=borrow_time,
                                        return_time=return_time)
    t = models.Book.objects.filter(book_id=book_id.book_id).update(status=1)
    if t == 0:
        # 报错
        return redirect('/home/')
    m = models.Borrower_book.objects.create(borrower_id=borrower_id,
                                            book_id=book_id)
    if m == 0:
        # 报错
        return redirect('/home/')
    return redirect('/home/')


def mybook(request):
    borrower_id = request.session['info'].get('id')
    books = models.Borrower_book.objects.filter(borrower_id=borrower_id)
    book_list = []
    for item in books:
        back_data_temp = {
            'id': item.book_id.book_id,
        }
        book_list.append(back_data_temp)
    back_data = {
        'books': book_list,
    }
    return render(request, 'mybook.html', back_data)


def return_book(request):
    book_id = request.GET.get('nid')
    borrower_id = request.session['info'].get('id')
    record = models.Borrower_book.objects.get(borrower_id=borrower_id, book_id=book_id)
    record.delete()
    models.Book.objects.filter(book_id=book_id).update(status=0)
    return redirect('/mybook/')


def add_book(request):
    if request.method == 'GET':
        return render(request, 'addbook.html')
    # 请前端同学根据下面语句在addbook.html中完成对应功能
    book_name = request.POST['bookname']
    book_writer = request.POST['writer']
    book_introduction = request.POST['intro']
    book_path = request.POST['path']
    models.Book.objects.create(book_name=book_name,
                               book_writer=book_writer,
                               book_introduction=book_introduction,
                               book_hot=0, book_path=book_path, status=0)
    return redirect('/homeA/')
















