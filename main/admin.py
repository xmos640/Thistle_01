from django.contrib import admin

# Register your models here.
from .models import Product,prod_images,Review,CouponCode,Orders


class PostProdImage(admin.StackedInline):
    model=prod_images

@admin.register(Product)
class imgUpload(admin.ModelAdmin):
    inlines = [PostProdImage]

    class Meta:
        model = Product

@admin.register(prod_images)
class PostProdImage(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
@admin.register(CouponCode)
class couponAdmin(admin.ModelAdmin):
    pass
@admin.register(Orders)
class orderAdmin(admin.ModelAdmin):
    pass
