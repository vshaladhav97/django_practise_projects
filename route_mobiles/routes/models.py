from django.db import models
from pprint import pprint
from marshmallow import Schema, fields, ValidationError
import marshmallow

# Create your models here.

items_data=(
        ("book", "book"),
        ("pen", "pen"),
        ("folder", "folder"),
        ("bag", "bag")
    )
class Items(models.Model):

    id = models.AutoField(primary_key = True)
    status = models.CharField(max_length=20, default="pending")
    items = models.CharField(max_length=20, choices= items_data)
    

# try:
#     Items(many=True).load(items_data)
    
# except ValidationError as err:
#     pprint(err.messages) 

# class SimpleListInput(marshmallow.Schema):
#     items = marshmallow.fields.List(marshmallow.fields.String(), required=True)

# payload = ['book', 'pen', 'folder', 'bag']
# data, errors = SimpleListInput().load({'items': payload})


# class ItemsSchema(Schema):
#     id = fields.Integer()
#     status = fields.String()
#     items = fields.String()


# items_data = [
#     {"items": "book"},
#     {"items": "pen"},
#     {"items": "folder"},
#     {"items": "bag"}
# ]

# try:
#     ItemsSchema(many=True).load(items_data)
    
# except ValidationError as err:
#     pprint(err.messages)