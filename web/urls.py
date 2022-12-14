"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from apps.user import views as user_views
from apps.seats import views as seats_views
from django.views.generic.base import RedirectView
from web import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # 静态文件
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}, name='static'),
    # favicon.cio
    re_path(r"^favicon.ico$", RedirectView.as_view(url=r'static/favicon.ico'), name="favicon"),

    # 注册
    re_path("registered", user_views.registered, name="registered"),

    # 登录
    re_path("login", user_views.login_post, name="login"),

    # 测试 数据库 orm 与数据库交互
    re_path("test", user_views.test, name="test"),

    # 预定桌子
    re_path("reserve", seats_views.reserve, name="reserve")

]
