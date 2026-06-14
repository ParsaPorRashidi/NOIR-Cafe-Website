from django.contrib import admin
from django.utils.html import format_html
from .models import BaristaOffer, Banner, Category, Product, FavoriteProduct, Event , WaiterCall
from django.contrib import admin

@admin.register(BaristaOffer)
class BaristaOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'label', 'show_image_thumbnail', 'created_at')
    readonly_fields = ('show_image_preview',)
    fields = ('label', 'title', 'image', 'show_image_preview')

    def show_image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />',
                obj.image.url)
        return "بدون تصویر"

    show_image_thumbnail.short_description = "پیش‌نمایش تصویر"

    def show_image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px; object-fit: cover; border-radius: 12px;" />',
                obj.image.url)
        return "تصویری ثبت نشده است"

    show_image_preview.short_description = "تصویر فعلی"


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'show_image_thumbnail', 'created_at')
    search_fields = ('title', 'subtitle')
    readonly_fields = ('show_image_preview',)
    fields = ('title', 'subtitle', 'image', 'show_image_preview')

    def show_image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 80px; height: 45px; object-fit: cover; border-radius: 6px;" />',
                obj.image.url)
        return "بدون تصویر"

    show_image_thumbnail.short_description = "تصویر بنر"

    def show_image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 100%; max-height: 250px; object-fit: cover; border-radius: 12px;" />',
                obj.image.url)
        return "تصویری ثبت نشده است"

    show_image_preview.short_description = "تصویر بنر اصلی"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'formatted_price', 'show_image_thumbnail', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'desc')
    ordering = ('-created_at',)
    readonly_fields = ('show_image_preview',)

    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name', 'category', 'price')
        }),
        ('توضیحات و رسانه', {
            'fields': ('desc', 'image', 'show_image_preview')
        }),
    )

    def formatted_price(self, obj):
        return format_html('<b>{}</b> تومان', f"{obj.price:,}")

    formatted_price.short_description = "قیمت"
    formatted_price.admin_order_field = "price"

    def show_image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />',
                obj.image.url)
        return "بدون تصویر"

    show_image_thumbnail.short_description = "عکس"

    def show_image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 200px; max-height: 200px; object-fit: cover; border-radius: 12px;" />',
                obj.image.url)
        return "تصویری ثبت نشده است"

    show_image_preview.short_description = "عکس محصول"


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'get_category', 'get_product_price', 'created_at')
    list_filter = ('product__category', 'created_at')
    search_fields = ('product__name',)

    autocomplete_fields = ['product']

    def get_category(self, obj):
        return obj.product.category.name

    get_category.short_description = "دسته‌بندی"

    def get_product_price(self, obj):
        return f"{obj.product.price:,} تومان"

    get_product_price.short_description = "قیمت محصول"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'jalali_date', 'time_range', 'show_image_thumbnail', 'created_at')
    list_filter = ('jalali_date', 'created_at')
    search_fields = ('title', 'desc')
    readonly_fields = ('show_image_preview',)

    fields = ('title', 'desc', 'jalali_date', 'time_range', 'image', 'show_image_preview')

    def show_image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 6px;" />',
                obj.image.url)
        return "بدون تصویر"

    show_image_thumbnail.short_description = "پوستر رویداد"

    def show_image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 200px; object-fit: cover; border-radius: 12px;" />',
                obj.image.url)
        return "تصویری ثبت نشده است"

    show_image_preview.short_description = "پوستر اصلی"

class CustomAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        return super().index(request, extra_context=extra_context)
