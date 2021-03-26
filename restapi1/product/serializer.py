from rest_framework import serializers
from .models import Products
from datetime import datetime 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','name', 'description', 'price')
        
        
# class CommentSerializer(serializers.Serializer): 
#     # intialize fields 
#     email = serializers.EmailField() 
#     content = serializers.CharField(max_length = 200) 
#     created = serializers.DateTimeField() 
    
# class Comment(object): 
#     def __init__(self, email, content, created = None): 
#         self.email = email 
#         self.content = content 
#         self.created = created or datetime.now() 
# # create a object 
# comment = Comment(email ='leila@example.com', content ='foo bar') 