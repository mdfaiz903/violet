from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(unique=True,max_length=255)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    title = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(unique=True,max_length=255)
    featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    thumbnail = models.URLField()
    description = models.TextField(null=True,blank=True,default='N/A')
    in_stock = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-id']

    @property
    def related(self):
        #products from related_name
        return self.category.products.all().exclude(pk=self.pk)

    def __str__(self) -> str:
        return self.title
    

class slider(models.Model):
    title = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='sliders/')
    show=models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

    