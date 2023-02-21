from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
import string
import random


class Category(models.Model):
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)
    category_title = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.category_title


class SubCategory(models.Model):
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_title = models.CharField(max_length=255)

    def __str__(self):
        return self.sub_category_title


class Brand(models.Model):
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)
    brand_name = models.CharField(max_length=255)
    brand_logo = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.brand_name


class MultiImage(models.Model):
    image_uid = models.IntegerField()
    images = models.ImageField(upload_to="images/")

    class Meta:
        ordering = ["-id"]
        verbose_name = "MultiImage"
        verbose_name_plural = "MultiImages"

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)
    product_title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    main_product_image = models.ImageField(upload_to="images/")
    multiple_image = models.ManyToManyField(MultiImage, blank=True)
    product_description = models.TextField()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def get_thumbnail(self):
        if self.main_product_image:
            return "http://127.0.0.1:8000" + self.main_product_image.url
        else:
            return " "

    def __str__(self):
        return self.product_title


class Cart(models.Model):
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cart_id = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return str(self.cart_id)

    def generate_random_id(self):
        length = 12
        return "".join(random.choices(string.ascii_lowercase, k=length))

    def save(self, *args, **kwargs):
        self.cart_id = self.generate_random_id()
        super(Cart, self).save(*args, **kwargs)


class DeliveryMethod(models.Model):
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)
    method_name = models.CharField(max_length=255)
    charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "DeliveryMethod"
        verbose_name_plural = "DeliveryMethods"


class PaymentMethod(models.Model):
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)
    payment_method_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "DeliveryMethod"
        verbose_name_plural = "DeliveryMethods"


class Order(models.Model):
    created_at = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order_id = models.CharField(max_length=255)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.order_id

    def generate_random_id(self):
        length = 12
        return "".join(random.choices(random.randint, k=length))

    def save(self, *args, **kwargs):
        self.order_id = self.generate_random_id()
        super(Order, self).save(*args, **kwargs)