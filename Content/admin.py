from typing import List

from django.contrib import admin

from Content.models import Category, Content, Images
class ContentImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'category', 'city', 'country', 'konum', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category', 'country']
    inlines = [ContentImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['Content', 'title', 'image_tag']
    readonly_fields = ('image_tag',)
# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Images, ImagesAdmin)
