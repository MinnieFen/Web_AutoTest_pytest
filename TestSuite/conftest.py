# coding:utf-8
import pytest
from Base.GetLoginCookie import Cookie
from Base.BasePage import BasePage
from config import readconfig

def login(phone = readconfig.inputPhone_cookie,psw = readconfig.inputPsw_cookie,url = readconfig.url_login):
    cookie = Cookie(BasePage)
    cookie.login(phone,psw,url)
