# -*- coding: utf-8 -*-
from mongoengine import *


class User(Document):
    user_id = IntField()
    name = StringField(max_length=255)


class Sushi(Document):
    sushi_id = IntField()
    price = StringField(max_length=255)
    description = StringField()
    image = URLField()
    title = StringField(max_length=255)


class UserChoices(Document):
    user_id = IntField()
    choices = ListField(IntField())
