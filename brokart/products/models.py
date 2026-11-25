from django.db import models

<<<<<<< HEAD
# Model for product
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
=======
# create the model in products and important columns in product related
class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE, 'Live'), (DELETE, 'Delete')) # This is the set deletion option, delete the any one and move to the trace
    
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to= 'media/')
    priority = models.IntegerField()
    
    delete_status = models.IntegerField(choices= DELETE_CHOICE, default= LIVE) # This column is designed for deleted element keep to the tempraly 
    create_at = models.DateTimeField(auto_now_add=True) # This column store the new create data time
    updated_at = models.DateTimeField(auto_now=True) # This column store the updated data time

    def __str__(self) -> str:  # This is the model object disply name (str)
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
        return self.title
