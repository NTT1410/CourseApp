from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from .models import Category, Course, Tag, Lesson
from django.contrib.auth.models import Permission
from django.utils.html import mark_safe
from django import forms

# Register your models here.
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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Permission)
admin.site.register(Lesson)
admin.site.register(Tag)