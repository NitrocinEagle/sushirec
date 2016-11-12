# -*- coding: utf8 -*-
import json

from app.mongo_models import User, Sushi, UserChoices
from contrib import recommend
from contrib.views import BaseAPI
from django.conf import settings
from mongoengine import connect
from rest_framework.response import Response

connect(getattr(settings, 'MONGO_DB_NAME'))


class GetSushi(BaseAPI):
    def get_data(self, *args, **kwargs):
        fields = ('price', 'title', 'description', 'image', 'sushi_id',)
        return Response({
            'result': 'success',
            'data': json.loads(Sushi.objects.scalar(*fields).to_json())
        })


class GetRecommendation(BaseAPI):
    def get_data(self, *args, **kwargs):
        choices = UserChoices.objects.values_list('user_id', 'choices')

        return Response({
            'result': 'success',
            'data': recommend(choices, int(self.request.GET['user_id']))
        })


class SetUserChoice(BaseAPI):
    def get_data(self, *args, **kwargs):
        return Response(u"Используйте POST")

    def set_data(self, *args, **kwargs):
        data = self.request.data
        choice = data['choice']
        if data.get('user_id'):
            UserChoices.objects.filter(user_id=data['user_id']).update(add_to_set__choices=[choice])
            return Response({
                'user_id': data.get('user_id')
            })

        user_id = self.gen_user_id()
        UserChoices(user_id=user_id, choices=[choice]).save()
        return Response({
            'user_id': user_id
        })

    def gen_user_id(self):
        user_id = max(User.objects().values_list('user_id') or [1]) + 1
        User(user_id=user_id, name="noname").save()
        return user_id
