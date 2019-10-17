from django import forms
from .models import *

#为 level 控件 初始化数据
LEVEL_CHOICE = (
    ("1","好评"),
    ("2","中评"),
    ("3","差评"),
)
#表示评论内容的表单控件们
#控件1 - 评论标题(subject) - 文本框
#控件2 - Email(email) - Email框
#控件3 - 评论内容(message) - Textarea
#控件4 - 评论级别(level) - Select
#控件5 - 是否保存(isSaved) - Checkbox
class RemarkForm(forms.Form):
    subject = forms.CharField(label="标题")
    email = forms.EmailField(label="邮箱")
    message = forms.CharField(label="评论内容", widget=forms.Textarea)
    level = forms.ChoiceField(label="评论级别",choices=LEVEL_CHOICE)
    isSaved = forms.BooleanField(label="是否保存")

class RegisterForm(forms.Form):
    uname = forms.CharField(label="用户名称")
    upwd = forms.CharField(label="用户密码", widget=forms.PasswordInput)
    uage = forms.IntegerField(label="用户年龄")
    uemail = forms.EmailField(label="电子邮箱")

class AuthorForm(forms.ModelForm):
    class Meta:
        #1.指定关联的Model类
        model = Author
        #2.指定从Model类中取哪些属性生成控件
        fields = "__all__"
        #3.指定Model类中的属性对应的label值
        labels = {
            "name":"姓名",
            "age":"年龄",
            "email":"邮箱",
            "isActive":"激活",
        }
        
class WidgetForm(forms.Form):
    uname = forms.CharField(label="用户名称", widget=forms.TextInput(attrs={
        "placeholder":"请输入用户名",
        "class":"form-input",
    }))
    upwd = forms.CharField(label="用户密码", widget=forms.PasswordInput(attrs={
        "placeholder":"请输入密码",
        "class":"form-input",
    }))

class WidgetModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "email"]
        labels = {
            "name":"姓名",
            "email":"邮箱",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder":"请输入姓名",
                    "class":"form-input",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder":"请输入您的邮箱",
                    "class":"form-input",
                }
            ),
        }