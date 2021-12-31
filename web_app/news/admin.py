from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from .models import Project, Article, Mention, Message, Comment
from .crawlers.hacker_crawler import crawl_one


def recrawl_article(modeladmin, request, quertset):
    for article in quertset:
        crawl_one(article.source)


recrawl_article.short_description = "recrawl article"


def moderate(modeladmin, request, quertset):
    for comment in quertset:
        comment.is_moderated = True
        comment.save()


moderate.short_description = "Mark as moderated"


class CommentInline(admin.TabularInline):
    model = Comment


class ArticleModelAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created', 'source_code')
    summernote_fields = '__all__'
    actions = (recrawl_article, )
    inlines = [
        CommentInline
    ]

    def source_code(self, obj):
        return format_html(f"<a href='{obj.source}'>{obj.source}</a>")


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('article', 'nickname', 'email', 'created', "is_active")
    list_filter = ('is_active', )
    actions = (moderate, )


class MentionModelAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'author_position')
    search_fields = ('author',)


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'image_code')
    search_fields = ('title',)

    def image_code(self, obj):
        return format_html('<img src="{}" style="max-width: 100px"/>', obj.photo.url)


class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'is_read')
    list_filter = ('is_read', )
    search_fields = ('name', 'subject', 'email')


admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Mention, MentionModelAdmin)
admin.site.register(Message, MessageModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
