# coding:utf-8
import pytest
@pytest.fixture(scope="module", autouse=True)
def start(request):
    print('\n-----开始执行moule----')
    print('module      : %s' % request.module.__name__)
    print('----------启动浏览器---------')
    yield
    print("------------结束测试 end!-----------")



@pytest.fixture(scope="function", autouse=True)
def open_home(request):
    print("function：%s \n--------回到首页--------" % request.function.__name__)


def test_01():
    print('-----------用例01--------------')

def test_02():
    print('-----------用例02------------')

if __name__ == "__main__":
    pytest.main(["-s", "test_08.py"])

