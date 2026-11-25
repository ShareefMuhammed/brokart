from django.contrib import admin
<<<<<<< HEAD
from orders.models import Order,OrderedItem
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_filter = [
         "owner",
         "order_status",
    ]
    search_fields = (
        "owner",
        "id",
    )
  
admin.site.register(Order,OrderAdmin)
=======

# Register your models here.
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
