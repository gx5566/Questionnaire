'''
＃模型
－客户
－问卷
－审核批注
－管理员
－问题
－问题选项
－用户
－参与问卷
－问卷答案
'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#

class Image(models.Model):
    filename = models.CharField(max_length=128)
    savename = models.CharField(max_length=128)
    size = models.IntegerField()


class Customer(models.Model):
    '''
        ＃客户模型
    '''
    user = models.OneToOneField(User,help_text='系统登录用户')
    company_name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)#公司地址
    phone = models.CharField(max_length=32)#座机
    industry = models.CharField(max_length=16)#行业
    web_site = models.CharField(max_length=128)#网址
    # tax_code = models.CharField(max_length=128)#税号
    uscc = models.CharField(max_length=128)#统一社会代码
    create_date = models.DateField(max_length=128)# 创建时间
    logo =models.OneToOneField('Image')#　公司图标
    regist_amount = models.IntegerField()#注册资金
    corporation = models.CharField(max_length=128)#法人
    wechat = models.CharField(max_length=128)#微信公众号
    email = models.CharField(max_length=128)#邮箱
    employee_number = models.IntegerField()#企业人数
    business_nature = models.CharField(max_length=128)# 企业性质
    business_scope = models.TextField()#经营范围
    description = models.TextField()#公司简介
    stock_code = models.CharField(default='',max_length=128)#股票代码


class UserInfo(models.Model):
    '''
        ＃用户
    '''
    user = models.OneToOneField(User,help_text='系统登录用户')
    name = models.CharField(max_length=128)#姓名
    gender = models.CharField(max_length=128)#性别
    birthday = models.DateField()#出生年月
    marital_status = models.CharField(max_length=128)#婚否
    mobile = models.CharField(max_length=32)#手机号
    qq = models.CharField(max_length=32)#qq
    wechat = models.CharField(max_length=128)#微信
    job = models.CharField(max_length=128)#工作
    address = models.CharField(max_length=128)#地址
    email = models.CharField(max_length=128)#邮箱
    photo = models.OneToOneField('Image')#头像
    education = models.CharField(max_length=128)#学历
    major = models.CharField(max_length=128)#专业
    

class Questionnaire(models.Model):
    '''
        ＃问卷模型
    '''
    customer = models.ForeignKey('Customer')
    title = models.CharField(max_length=128)#标题
    create_date = models.DateField()#
    expire_date = models.DateField()#
    quantity =  models.IntegerField()#
    left =  models.IntegerField()#剩余问卷答案
    state = models.IntegerField()#状态

class Question(models.Model):
    '''
        ＃问题
    '''
    questionnaire = models.ForeignKey('Questionnaire')
    title = models.CharField(max_length=128)#
    is_checkbox = models.BooleanField()#是否多选
 
class Item(models.Model):
    '''
        ＃选项
    '''
    
    question = models.ForeignKey('Question')#题目
    content = models.CharField(max_length=128)#选项内容



class QuestionnaireComment(models.Model):
    
    '''
        ＃审核批注

    '''
    questionnaire = models.ForeignKey('Questionnaire')#审核问卷
    create_date = models.DateField(auto_now=True)#审核时间
    comment = models.TextField()#审核内容
    admin = models.ForeignKey('Admin')#审核人

class Admin(models.Model):
    user = models.OneToOneField(User)#登录账号
    name = models.CharField(max_length=32)#姓名
    job_id = models.CharField(max_length=128)


class JoinQuestionnaire(models.Model):
    '''
        ＃问卷参与
    '''
    
    questionnaire = models.ForeignKey('Questionnaire')
    userinfo = models.ForeignKey('UserInfo')
    create_date = models.DateField()
    is_done = models.BooleanField()

class AnswerQuestionnaire(models.Model):
    '''
        ＃问卷答案
    '''
    userinfo = models.ForeignKey('UserInfo')
    item = models.ForeignKey('Item')


