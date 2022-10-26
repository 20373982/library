from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class qualify(MiddlewareMixin):

    def process_request(self, request):

        # 排除非登录状态下可访问的页面
        if request.path_info == "/loginC/":
            return
        if request.path_info == "/loginA/":
            return

        # 获取session信息
        info = request.session.get("info")
        if info:
            return

        # session信息为空，返回登录页面
        return redirect("/login/")
