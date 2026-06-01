from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = (
        "title",
        "author",
        "status",
        "counted_view",
        "created_date",
        "published_date",
        "updated_date",
    )
    list_filter = ("status", "created_date", "author")
    search_fields = ("title", "content", "author")
    list_editable = ("status",)
    ordering = ("-created_date",)
    list_per_page = 20  # نمایش ۲۰ رکورد در هر صفحه
    date_hierarchy = "created_date"

class CategoryAdmin(admin.ModelAdmin):
    list_display =("name",)

class CommentAdmin(admin.ModelAdmin):
    list_display =("name","email","approved","post_id", "created_date","updated_date",)
    list_filter = ("name", "approved", "post_id")
    search_fields = ("name", "email", "post_id")
    ordering = ("-created_date",)
    list_per_page = 20
    date_hierarchy = "created_date"

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
