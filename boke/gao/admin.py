#coding:utf8
from django.contrib import admin
from models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

#后台显示
class UserAdmin(BaseUserAdmin):
    list_display = ('username','is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = ( # 编辑的时候字段
        ('基本', {'fields': ('username','password','nick','friend','avatar')}),
        ('权限', {'fields': ('is_superuser','is_staff','is_active','groups', 'user_permissions')}),
    )

    add_fieldsets = ( # 添加记录的时候字段
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'password1', 'password2','is_staff','is_active','is_superuser')}
        ),
    )
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','click_count','is_recommend','category')
    list_filter = ('is_recommend','date_publish')
    list_display_links = ('title','desc') #超链接
    list_editable = ('click_count',) #编辑相
    search_fields = ('title','desc') #搜索
    filter_horizontal = ('tag',)
    fieldsets = (
        ( '基本',{
            'fields':('title','desc','content','user','category','tag')
        }),
        (
            '高级',{
                'classes':('collapse',),
                'fields':('click_count','is_recommend'),
            }
        ),
    )
    #表情框
    class Media:
        js = (
            '/static/kindeditor/kindeditor-all-min.js', # kindeditor核心文件
            '/static/kindeditor/lang/zh_CN.js', # 语言文件
            '/static/kindeditor/config.js', # 自定义kindeditor配置文件
        )


admin.site.register(User,UserAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Ad)
admin.site.register(Links)
