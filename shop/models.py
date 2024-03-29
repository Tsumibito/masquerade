from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'

class Size(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размер'

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    code = models.CharField(max_length=7, blank=True, null=True, default=None, unique=True, verbose_name='Артикул')
    slug = models.SlugField(max_length=64, unique=True, default='', verbose_name='Slug')
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.ProtectedError)
    size = models.ForeignKey(Size, blank=True, null=True, default=None, on_delete=models.ProtectedError)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    tags = TaggableManager()

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    shows = models.PositiveIntegerField(blank=True, null=True, default=0)
    clicks = models.PositiveIntegerField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    @property
    def ctr(self):
        return self.shows/self.clicks

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

class ProductSet(models.Model):
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    item = models.CharField(max_length=128, blank=True, null=True, default=None)
    size = models.CharField(max_length=128, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image1 = models.ImageField(upload_to='product_set_images/')
    image2 = models.ImageField(upload_to='product_set_images/')
    image3 = models.ImageField(upload_to='product_set_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.item

    class Meta:
        verbose_name = 'Комплект'
        verbose_name_plural = 'Комплект'


class Reservation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.ProtectedError)
    start_date = models.DateField()
    end_date = models.DateField()
