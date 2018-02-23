from django.db import models
#Image model class to hold all image details

class Category(models.Model):
    category=models.CharField(max_length=60)


    def __str__(self):
        return self.category


class Location(models.Model):
    location=models.CharField(max_length=60)
    def __str__(self):
        return self.location


class Image(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField()
    gallery_image=models.ImageField(upload_to='images/')
    location=models.ForeignKey(Location,null=True,blank=True)
    category=models.ForeignKey(Category,null=True,blank=True)

    @classmethod
    def my_image(cls):
        images=Image.objects.all()

        return images

    def save_image(self):
        self.save()

    def __str__(self):
        return self.name


    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__icontains=search_term)
        return image





# Create your models here.
