from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user import models


# Create your views here.

class loginManager(forms.Form):
    manager_name = forms.CharField(label="账户", required=True)
    manager_pwd = forms.CharField(label="密码", required=True)


class loginBorrower(forms.Form):
    borrower_name = forms.CharField(label="账户", required=True)
    borrower_pwd = forms.CharField(label="密码", required=True)


def user_login(request):
    if request.method == 'GET':
        form = loginBorrower()
        return render(request, 'login.html', {"form": form})

    form = loginBorrower(data=request.POST)
    if form.is_valid():
        #为了便捷，这里我用了Django自带的方法，这一步主要是对获取的登录信息，到对应的表中进行筛选，如果结果为空，说明账户或密码错误。
        borrower_object = models.Borrower.objects.filter(**form.cleaned_data).first()
        if not borrower_object:
            form.add_error("borrower_pwd", "账户或密码错误")
            return render(request, 'login.html', {"form": form})
        else:
            request.session["info"] = {'name': borrower_object.borrower_name, 'pwd': borrower_object.borrower_pwd}
            return redirect("/top/", request)

    return render(request, 'login.html', {"form": form})
    # server_data = {
    #
    # }
    #return render(request, 'login.html', server_data)


def admin_login(request):
    if request.method == 'GET':
        form = loginManager()
        return render(request, 'admin.html', {"form": form})

    form = loginManager(data=request.POST)
    if form.is_valid():
        manager_object = models.Manager.objects.filter(**form.cleaned_data).first()
        if not manager_object:
            form.add_error("manager_pwd", "账户或密码错误")
            return render(request, 'login.html', {"form": form})
        else:
            request.session["info"] = {"name": manager_object.manager_name, "pwd": manager_object.manager_pwd}
            return redirect("/top/")

    return render(request, 'login.html', {"form": form})


def top_page(request):
    return render(request, 'top.html')


def logout(request):
    request.session.clear()
    return redirect("/login/")
