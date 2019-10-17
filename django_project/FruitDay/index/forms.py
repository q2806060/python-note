from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["uphone","upwd"]
        labels = {
            "uphone":"手机号",
            "upwd":"密码",
        }
        widgets = {
            "uphone": forms.TextInput(
                attrs={
                    "placeholder":"请输入手机号",
                    "class":"uinput"
                }
            ),
            "upwd":forms.PasswordInput(
                attrs={
                    "placeholder":"请输入密码",
                    "class":"uinput"
                }
            )
        }
