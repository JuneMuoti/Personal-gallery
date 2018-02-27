from django.db import models
#Image model class to hold all image details

class Category(models.Model):
    name=models.CharField(max_length=60)


    def __str__(self):
        return self.name


class Location(models.Model):
    location=models.CharField(max_length=60)
    def __str__(self):
        return self.location


class Image(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField()
    gallery_image=models.ImageField(upload_to='images/',blank=True)
    location=models.ForeignKey(Location,null=True,blank=True)
    category=models.ForeignKey(Category,null=True,blank=True)
    url=models.CharField(max_length=100,blank=True)

    @classmethod
    def my_image(cls):
        images=Image.objects.all()

        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.save()

    def update_image(self):
        img= Image.objects.filter(id = 2).update()

        return  imager
    def get_image(image_id):
        imager = Image.objects.get(id = image_id)
        return  imager



    @classmethod
    def search_by_category(cls,query):
        result = cls.objects.filter(category__name__icontains=query)
        return result
    def __str__(self):
        return self.name
    @classmethod
    def filter_by_location(cls):
        result = cls.objects.filter(location__location__icontains='canada')
        return result










# Create your models here.
