from os import name
from typing import ContextManager
from django.contrib import admin
from django.template.base import constant_string
from DictationModel.models import Category, Words
from django.urls import path
from django.template.response import TemplateResponse
from django.core.exceptions import PermissionDenied
from django.contrib.admin.actions import delete_selected as delete_selected_
from django.utils.safestring import mark_safe

from . import views

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    def get_lesson(self, obj): return '第{0}课'.format(obj.lesson)
    list_display = ('get_lesson', 'unit', 'grade')

    def get_changelist_instance(self, request, **kwargs):
        cl = super(CategoryAdmin, self).get_changelist_instance(
            request, **kwargs)
        print(cl.__dict__)
        for k, v in cl.__dict__.items():
            print(k, '---------------', v)
        return cl


class WordsAdmin(admin.ModelAdmin):
    def get_sounds(self, obj):
        return mark_safe('<a href="javascript:on_play(\'/media/{0}\');">{0}</a>'.format(obj.sounds))

    list_display = ('text', 'get_sounds', 'category',
                    'level', 'used_times', 'add_time')
    readonly_fields = ('used_times', 'add_time')
    change_list_template = 'admin/dictation/dict_change_list.html'
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for item in queryset:
            item.sounds.delete()
        return delete_selected_(self, request, queryset)

    def get_urls(self):
        urls = super().get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name
        my_urls = [
            path('upload/', self.admin_site.admin_view(views.Upload_Sound),
                 kwargs={'model': self}, name="%s_%s_upload" % info),
            path('upload/<str:c_l>', self.admin_site.admin_view(views.Upload_Sound),
                 kwargs={'model': self}, name="%s_%s_upload" % info)
        ]
        return my_urls + urls


admin.site.register(Category, CategoryAdmin)
admin.site.register(Words, WordsAdmin)
