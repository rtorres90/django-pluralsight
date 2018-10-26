# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name='game_first_player')
    second_player = models.ForeignKey(User, related_name='game_second_player')
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(now_add=True)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
