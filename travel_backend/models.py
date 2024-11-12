# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Как сделать проверку на коректность и автоматически выставлять флаг корректности?
#  



from django.db import models

class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    work_time = models.CharField(max_length=50, blank=True, null=True)
    place_phone = models.CharField(max_length=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place'


class PlaceQuestion(models.Model):
    place = models.OneToOneField(Place, models.DO_NOTHING, primary_key=True)
    question = models.ForeignKey('Question', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'place_question'
        unique_together = (('place', 'question'),)


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class PlayerAnswers(models.Model):
    answer_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, models.DO_NOTHING, blank=True, null=True)
    place = models.ForeignKey(Place, models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey('Question', models.DO_NOTHING, blank=True, null=True)
    player_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'player_answers'


class PlayerPlace(models.Model):
    player = models.OneToOneField(Player, models.DO_NOTHING, primary_key=True)
    place = models.ForeignKey(Place, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'player_place'
        unique_together = (('player', 'place'),)


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    question_answer = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'question'
