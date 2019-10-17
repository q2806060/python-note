from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    #list_display:定义在列表页上显示的字段
    list_display = ("name", "age", "email")

    #list_display_links:定义在列表页中能连接到详情页的字段们
    list_display_links = ("name", "email")

    #list_editable:定义在列表页中就允许编译的字段们
    #注意：取值不能出现在list_display_links中
    list_editable = ("age",)

    #list_filter:列表页的右侧增加一个过滤器实现筛选
    list_filter = ("name", "email")

    #search_fields:添加允许被搜索的字段们
    search_fields = ("name","email")

    #fields:定义在详情页要显示的字段及其顺序
    # fields = ("isActive", "name", "email")

    #fieldsets:定义在详情页中的字段分组
    #注意：fieldsets 属性 和 fields 不能共存
    fieldsets = (
        #分组1
        ("基本选项",{
            "fields":("name","email"),
            "classes":("collapse",)
        }),
        #分组2
        ("可选选项",{
            "fields":("age","isActive"),
        }),
    )

# class BookAdmin(admin.ModelAdmin):
#     #date_hierarchy:在列表页中增加一个时间分层选择器
#     date_hierarchy = "publicate_date"

class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "city")
    list_editable = ("address", "city")
    list_filter = ("city",)
    search_fields = ("name", "website")
    fieldsets = (
        ("基本信息", {
            "fields":("name", 'address', "city"),
        }),
        ("高级信息", {
            "fields":("country", "website"),
        })
    )

# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book)
admin.site.register(Wife)