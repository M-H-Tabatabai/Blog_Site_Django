from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','counted_view', 'created_date', 'published_date', 'updated_date')
    list_filter = ('status', 'created_date')
    search_fields = ('title', 'content')
    list_editable = ('status',)
    ordering = ('-created_date',)
    list_per_page = 20  # نمایش ۲۰ رکورد در هر صفحه
    date_hierarchy = 'created_date'

    
admin.site.register(Post, PostAdmin)
