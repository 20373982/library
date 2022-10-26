from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from backend import models


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
        # backend = models.backend.objects.get(user_name=username, user_pwd=request.POST['password'])
        # 请导入library_model后,在数据库查找用户，没找到请报错
        request.session['info'] = {'name': username, 'limit': 1}
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
        # backend = models.admin.objects.get(admin_name=username, admin_pwd=request.POST['password'])
        # 数据库查找管理员，没找到请报错
        request.session['info'] = {'name': username, 'limit': 2}
        return redirect('/home/')
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
    return redirect('/loginA/')


def logout(request):
    request.session.clear()
    return redirect("/loginC/")
