from django.db import models

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
        return self.title
