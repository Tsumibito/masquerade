from django.contrib import admin
from shop.models import Product, ProductCategory, ProductImage, Reservation


class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 0

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('product', 'start_date', 'end_date')

    class Meta:
        model = Reservation

admin.site.register(Reservation, ReservationAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'price')
    inlines = [ProductImageInline, ReservationInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
