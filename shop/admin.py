from django.contrib import admin
from shop.models import Product, ProductCategory, ProductImage, Reservation


#InLines
class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 0

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

#Admins
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('product', 'start_date', 'end_date')

    class Meta:
        model = Reservation

class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'price')
    inlines = [ProductImageInline, ReservationInline]

    class Meta:
        model = Product

#Register
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
