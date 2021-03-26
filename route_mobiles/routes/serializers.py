from rest_framework import serializers
from .models import Items
from pprint import pprint
from marshmallow import Schema, fields, ValidationError




class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Items
        fields = ("id","status", "items",)
        
# class ItemsSchemaSerializer(serializers.ModelSerializer):

class ItemsSchema(Schema):
    id = fields.Int()
    status = fields.Str()
    items = fields.Str()


items_data = [
    {"items": "book"},
    {"items": "pen"},
    {"items": "folder"},
    {"items": "bag"}
]

try:
    ItemsSchema(many=True).load(items_data)
    
except ValidationError as err:
    pprint(err.messages)