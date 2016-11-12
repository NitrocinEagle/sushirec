# -*- coding: utf8 -*-
from rest_framework.views import APIView


class BaseAPI(APIView):
    http_method_names = ['get', 'post', 'options']

    def get_data(self, *args, **kwargs):
        pass

    def set_data(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        return self.get_data(*args, **kwargs)

    def options(self, request, *args, **kwargs):
        return self.get_data(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.set_data(*args, **kwargs)