# -*- coding: utf8 -*-
from django.conf.urls import url
from .views import GetSushi, SetUserChoice, GetRecommendation

urlpatterns = [
    url(r'^$', GetSushi.as_view(), name='some_name'),
    url(r'^set-choice/', SetUserChoice.as_view(), name='set_user_choice'),
    url(r'^recommend/', GetRecommendation.as_view(), name='get_user_recommendation'),
]
