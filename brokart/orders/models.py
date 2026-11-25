from django.db import models
from customers.models import Customer
<<<<<<< HEAD
# Create your models here.
from products.models import Product

#data model for order
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (ORDER_DELIVERED,"ORDER_DELIVERED"),
                   (ORDER_REJECTED,"ORDER_REJECTED"),
                   (ORDER_CONFIRMED,"ORDER_CONFIRMED")
                   )
    
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    total_price=models.FloatField(default=0)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True, related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:

        return "order-{}-{}".format(self.id,self.owner.name)

#model for ordered item
class OrderedItem(models.Model):
    product=models.ForeignKey(Product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
    
 
=======
from products.models import Product
# Create your models here.
class Order(models.Model):  #save the liked items into the cart 
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE, 'Live'), (DELETE, 'Delete')) # This is the set deletion option, delete the any one and move to the trace

    #This is the order relted options 
    CART_STAGE = 0
    ORDER_CONFORMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = ((ORDER_PROCESSED, "ORDER_PROCESSED"),(ORDER_DELIVERED, "ORDER_DELIVERED"), (ORDER_REJECTED, "ORDER_REJECTED"))
    order_status = models.IntegerField(choices = STATUS_CHOICE, default=CART_STAGE)

    owner = models.ForeignKey(Customer, on_delete= models.SET_NULL, null= True, related_name= "orders")  # cart is the related to the customer, this a reason of the customer imported in cart and create foreign key used to referenced

    delete_status = models.IntegerField(choices= DELETE_CHOICE, default= LIVE) # This column is designed for deleted element keep to the tempraly 
    create_at = models.DateTimeField(auto_now_add=True) # This column store the new create data time
    updated_at = models.DateTimeField(auto_now=True) # This column store the updated data time

class OrderedItem(models.Model):   # This model is inside Carts many fields are included
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, null = True, related_name= 'added_carts')
    quantity = models.IntegerField(default=1)  #quentity filed is used how many elemnts in parchased
    owner = models.ForeignKey(Order, on_delete= models.CASCADE, related_name="added_items")  
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
