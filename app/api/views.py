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
        choices = UserChoices.objects.scalar('user_id', 'choices')
        recommends = recommend(choices, int(self.request.GET['user_id']))

        fields = ('price', 'title', 'description', 'image', 'sushi_id',)
        sushis = Sushi.objects.scalar(*fields).order_by('sushi_id')
        response = []

        for rec in recommends:
            if rec[0] not in filter(lambda c: c[0] == int(self.request.GET['user_id']), choices)[0][1]:
                # sushi contains a tuple (price, title, descr, img, id)
                sushi = sushis[rec[0] - 1]
                response.append({
                    'price': sushi[0],
                    'title': sushi[1],
                    'description': sushi[2],
                    'image': sushi[3],
                    'sushi_id': sushi[4],
                    'rec': rec[1],
                })

        return Response({
            'result': 'success',
            'data': response
        })


class SetUserChoice(BaseAPI):
    def get_data(self, *args, **kwargs):
        return Response(u"Используйте POST")

    def set_data(self, *args, **kwargs):
        data = self.request.data
        choice = data['choice']
        if data.get('user_id'):
            choices = UserChoices.objects.filter(user_id=data['user_id']).scalar('choices').first()
            if choice not in choices:
                UserChoices.objects.filter(user_id=data['user_id']).update(add_to_set__choices=[choice])
                return Response({
                    'user_id': data.get('user_id')
                })
            return Response(u"Вы уже выбирали эти суши")

        user_id = self.gen_user_id()
        UserChoices(user_id=user_id, choices=[choice]).save()
        return Response({
            'user_id': user_id
        })

    def gen_user_id(self):
        user_id = max(User.objects().values_list('user_id') or [1]) + 1
        User(user_id=user_id, name="noname").save()
        return user_id
