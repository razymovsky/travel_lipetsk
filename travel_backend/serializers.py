from rest_framework import serializers
from .models import *

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Place
		fields = ('place_id', 'address', 'work_time', 'place_phone', 'latitude', 'longitude')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Player
		fields = ('player_id', 'name', 'last_name', 'surname', 'age')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Question
		fields = ('question_id','question_text', 'question_answer')

class PlayerAnswersSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PlayerAnswers
		fields = ('answer_id', 'player', 'place', 'question', 'player_answer', 'is_correct')