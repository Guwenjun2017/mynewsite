from django.db import models
from django.utils import timezone

class Article(models.Model):
    tag = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=999)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title

class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    kucun = models.IntegerField(verbose_name='库存', default=0)
    size = models.CharField(max_length=1, choices=SIZES)

    def __str__(self):
        return self.name
