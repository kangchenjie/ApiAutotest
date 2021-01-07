import pytest
import requests


# def test_login():
#     # 注册用户
#     # 下发登录的请求
#     # 检查结果
#     # 删除注册的用户
#     pass
from zonghe.baw import Db, Member
from zonghe.caw import DataRead, Asserts


@pytest.fixture(params=DataRead.read_yaml(r"data_case/login_setup.yaml"))
def setup_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml(r"data_case/login_data.yaml"))
def login_data(request):
    return request.param

@pytest.fixture()
def register(setup_data,url,db,baserequests):
    ###1###
    mobilephone =setup_data['casedata']['mobilephone']
    Db.delete_user(db,mobilephone)
    Member.register(url,baserequests,setup_data['casedata'])
    yield
    ###3###
    Db.delete_user(db,mobilephone)
    # print("注册用户")
    # yield
    # print("删除注册用户")

def test_login2(register,url,baserequests,login_data):
    ###2###
    # print("下发登录的请求")
    r = Member.login(url, baserequests,login_data['casedata'])
    print(r.text)
    print("检查结果")
    # assert r.json()['msg'] == str(login_data['expect']['msg'])
    # assert r.json()['code'] == str(login_data['expect']['code'])
    # assert r.json()['status'] == str(login_data['expect']['status'])
    # r = Member.list(url, baserequests)
    # print(r.text)
    Asserts.check(r.json(),login_data['expect'],"code,msg,status")