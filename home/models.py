from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(null=True,blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='home_project')
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True)


    def __str__(self):
        return self.title
    @property
    def ImageURL(self):
        try:
            url=self.image.url
        except:
            url = ''
        return url