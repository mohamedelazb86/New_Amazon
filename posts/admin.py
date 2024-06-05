from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post,Category,Comment


class PostAdmin(SummernoteModelAdmin):
    list_display=['user','title','publish_date']
    search_fields=['title','content']
    list_filter=['category','draft']

    summernote_fields = ('content',)





admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
