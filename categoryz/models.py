from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class categ(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):

        return '{}'.format(self.name)
    def get_url(self):
        return reverse('cat_list',args=[self.slug])
    

class products(models.Model):
    name=models.CharField(max_length=150,unique=True)
    img = models.ImageField(upload_to='picture')
    desc=models.TextField(max_length=100)
    slug=models.SlugField(max_length=200,unique=True)
    stock=models.IntegerField()
    price=models.IntegerField()
    available=models.BooleanField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)
    def get_url(self):
        return reverse('proddetails',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)

