from django.contrib import admin
from test1.models import ItemB, ItemC, PersonInfo, Students, Teacher, ItemA, PersonInfo, UserModel, Users, Post, Item, Customer,MyModel, Purchase
# Register your models here.

# @admin.register(Students)
# class StudentAdmin(admin.ModelAdmin):
#     list_display =('stuid', 'stuname', 'stuemail', 'stupass', 'comment')

# admin.site.register(Students, StudentAdmin)

admin.site.register(Students)
admin.site.register(Teacher)

admin.site.register(ItemA)
admin.site.register(ItemB)
admin.site.register(ItemC)
admin.site.register(PersonInfo)
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password')
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'publish_date', 'user_name',]
    # list_display = ('user','user_name')
    def user_name(self, obj):
        return obj.user.name
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('item', 'customer', 'date_purchased', 'quantity_purchased')
    
@admin.register(UserModel)
class UsersAdmin(admin.ModelAdmin):
    list_display = [('email')]
    
      
# admin.site.register(UserModel)
admin.site.register(MyModel)