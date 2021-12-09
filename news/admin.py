from django.contrib import admin
from .models import Project, Article, Comment, Message
from django_summernote.admin import SummernoteModelAdmin

class ArticleModelAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'

admin.site.register(Project)
admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Comment)
admin.site.register(Message)