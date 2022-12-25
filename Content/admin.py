from typing import List

from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

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


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Content,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Content,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

# Register your models here.
admin.site.register(Category, CategoryAdmin2)
admin.site.register(Content, ContentAdmin)
admin.site.register(Images, ImagesAdmin)
