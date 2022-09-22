from django.contrib import admin
from .models import Card, Tag
# Register your models here.
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['name']
admin.site.register(Tag, TagAdmin)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    model = Card
    list_display = ['title', 'slug', 'tag_name','date_modified', 'publish_date', 'published']
    list_filter = ['publish_date', 'date_created', 'date_modified', 'published']
    search_fields = ['title', 'desc']
    prepopulated_fields = {
        'slug':['title'],
    }
    


