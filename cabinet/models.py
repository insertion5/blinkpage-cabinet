from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    SITE_CHOICES = [
        ('landing', 'Лендинг'),
        ('multipage', 'Многостраничник'),
        ('ecommerce', 'Интернет-магазин'),
    ]
    STATUS_CHOICES = [
        ('new', 'Ожидает связи'),
        ('in_progress', 'В работе'),
        ('done', 'Готово'),
        ('paid', 'Оплачено'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_type = models.CharField(max_length=20, choices=SITE_CHOICES)
    services = models.ManyToManyField(Service, blank=True)
    total_price = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.get_site_type_display()}"

class Comment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.author.email} — {self.created_at}"
