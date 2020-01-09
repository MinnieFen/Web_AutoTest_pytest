# coding:utf-8
import configparser
import os
cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件路径
cfg_path = os.path.join(cur_path,'config.ini')

conf = configparser.ConfigParser()
conf.read(cfg_path)

# 读取服务器配置
sql_host = conf.get('sql_info','host')
sql_uer = conf.get('sql_info','user')
sql_port = conf.get('sql_info','port')
sql_password = conf.get('sql_info','password')
sql_db_yx = conf.get('sql_info','db_yx')
sql_db_qiyuebao = conf.get('sql_info','db_qiyuebao')
sql_charset = conf.get('sql_info','charset')

# 读取浏览器配置
browserName = conf.get('browserType','browserName')

# 读取测试url
url_login = conf.get('testServer','url_login')
url_admin = conf.get('testServer','url_admin')

# 读取登录账号、密码
inputPhone_cookie = conf.get('user_info','inputPhone_cookie')
inputPsw_cookie = conf.get('user_info','inputPsw_cookie')
inputPhone_login = conf.get('user_info','inputPhone_login')
inputPsw_login = conf.get('user_info','inputPsw_login')

# 读取email
mail_host = conf.get('email','mail_host')
mail_pass = conf.get('email','mail_pass')
mail_user = conf.get('email','mail_user')
sender = conf.get('email','sender')
receiver = conf.get('email','receivers')