# -*- coding: utf-8 -*-
import json

import recsys.algorithm

from app.mongo_models import Sushi

recsys.algorithm.VERBOSE = True
from recsys.algorithm.factorize import SVD


def recommend(choices, user_id):
    """
    :param choices: list of choices which is perpesentated as tuples of two elements - user's id and list of sushi id
    :param user_id: user's id
    :return:
    """
    svd = SVD()
    for user_choice in choices:
        for choice in user_choice[1]:
            svd.add_tuple((1, user_choice[0], choice))
    svd.compute(k=10)
    return svd.recommend(user_id)


def save_sushi_db():
    with open('data/sushi_results.json') as file:
        sushi = json.load(file)
        if not Sushi.objects.count():
            for s in sushi:
                Sushi(**s).save()
