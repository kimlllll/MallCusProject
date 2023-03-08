from django.shortcuts import render,redirect
from django.views import View
from django import http
import re
from user.models import User
from django.urls import reverse
from django.db import DatabaseError
from django.contrib.auth import login
from MallCusProject.utils.response_code import RETCODE

# Create your views here.
class UsernameCountView(View):
    """判断用户名是否重复注册
       username ： url中的key值，在这里接收"""
    def get(self,request,username):
        # 接收和校验参数
        # 实现主体逻辑 使用username查询对应的记录条数 (filter返回的是满足条件的结果集)
        count =  User.objects.filter(username=username).count()
        #响应结果
        return http.JsonResponse({'code':RETCODE.OK,'errmsg':'OK','count':count})


class RegisterView(View):
    """用户注册"""
    #1. 编写与请求方法同名的函数 get post
    def get(self,request):
        """提供用户注册页面"""
        return render(request,'register.html')


    def post(self,request):
        """实现用户注册业务逻辑"""
        # 1.接收参数
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        mobile = request.POST.get("mobile")
        allow = request.POST.get("allow")
        # 2.校验参数 前后端的校验分开
        # 是否缺少参数
        if not all([username,password,password2,mobile,allow]):
            return http.HttpResponseForbidden('缺少必传参数')

        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$',username):
            return http.HttpResponseForbidden('请输入5-20个字符的用户名')

        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return http.HttpResponseForbidden('请输入8-20位的密码')
        # 判断两次密码是否一致
        if password != password2:
            return http.HttpResponseForbidden('两次输入的密码不一致')
        # 判断手机号是否合法
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return http.HttpResponseForbidden('请输入正确的手机号码')
        # 判断是否勾选用户协议
        if allow != 'on':
            return http.HttpResponseForbidden('请勾选用户协议')
        # 3.保存注册数据 ：是注册业务的核心
        try:
            user = User.objects.create_user(username=username,password=password,mobile=mobile)
        except DatabaseError:
            return render(request,"register.html",{'register_errmsg':'注册失败'})
        #状态保持
        login(request,user)

        # 4.响应结果 重定向到首页
        # return redirect('/index')
        return redirect(reverse('contents:index'))
