#  _*_ coding:utf-8 _*_
__author__ = 'daqing'
__date__ = '2017/7/4 22:43'

import xadmin

from xadmin.plugins.auth import UserAdmin

from .models import EmailVerifyRecord, Banner, WebInfo, UserProfile
from xadmin import views


class UserProfileAdmin(UserAdmin):
    pass

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "fox education"
    site_footer = "fox education online"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    model_icon = 'fa fa-group'


class BannerAdmin(object):
    list_display = ['title','image','url','index', 'add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index', 'add_time']

class WebInfoAdmin(object):
    list_display = ['title', 'top_logo', 'foot_logo', 'foot_code', 'add_time']
    search_fields = ['title', 'top_logo', 'foot_logo', 'foot_code']
    list_filter = ['title', 'top_logo', 'foot_logo', 'foot_code', 'add_time']

#from django.contrib.auth.models import User
#xadmin.site.unregister(User)

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(WebInfo, WebInfoAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
#xadmin.site.register(UserProfile, UserProfileAdmin)