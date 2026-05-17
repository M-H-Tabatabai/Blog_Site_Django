from django.contrib import admin
from blog.models import Post
from blog.models import Category


class PostAdmin(admin.ModelAdmin):
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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
