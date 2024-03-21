from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from .models import Category, Course, Tag, Lesson
from django.contrib.auth.models import Permission
from django.utils.html import mark_safe
from django import forms

from .dao import count_course_by_cate

# Register your models here.

class CourseAppAdminSite(admin.AdminSite):
    site_header = "KHOA HOC TRUC TUYEN"

    def get_urls(self):
        return [
            path('course-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        stats = count_course_by_cate()
        return  TemplateResponse(request, 'admin/stats_view.html', {
            'stats': stats
        })

class CourseTagInlineAdmin(admin.TabularInline):
    model = Course.tags.through

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    readonly_fields = ['img']
    form = CourseForm
    inlines = [CourseTagInlineAdmin]

    def img(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=obj.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

admin_site = CourseAppAdminSite(name="myapp")

admin_site.register(Category, CategoryAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(Permission)
admin_site.register(Lesson)
admin_site.register(Tag)