from django.db import models

# Create your models here.
class SiteSetting(models.Model):
<<<<<<< HEAD
    banner= models.ImageField(upload_to='media/site/')
    caption=models.TextField()


=======
    banner = models.ImageField(upload_to= 'media/site/')
    caption = models.TextField()
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
