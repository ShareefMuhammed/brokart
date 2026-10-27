from django.db import models

# create the customer model
from django.contrib.auth.models import User   # This is user login default authentication

class Customer(models.Model):  # This is the customer model and included fileds
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE, 'Live'), (DELETE, 'Delete')) # This is the set deletion option, delete the any one and move to the trace

    name = models.CharField(max_length=200)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'customer_profile') # extending the default user data with custom profile information
    phone = models.CharField(max_length=10)
    
    delete_status = models.IntegerField(choices= DELETE_CHOICE, default= LIVE) # This column is designed for deleted element keep to the tempraly 
    create_at = models.DateTimeField(auto_now_add=True) # This column store the new create data time
    updated_at = models.DateTimeField(auto_now=True) # This column store the updated data time

    def __str__(self) -> str:  # This is the model object disply name (str)
        return self.name