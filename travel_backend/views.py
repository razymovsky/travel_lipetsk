from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.


class PlaceViewSet(viewsets.ModelViewSet):
	queryset = Place.objects.all().order_by('place_id')
	serializer_class = PlaceSerializer

class PlayerViewSet(viewsets.ModelViewSet):
	queryset = Player.objects.all().order_by('player_id')
	serializer_class = PlayerSerializer

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all().order_by('question_id')
	serializer_class = QuestionSerializer

class PlayerAnswersViewSet(viewsets.ModelViewSet):
	queryset = PlayerAnswers.objects.all()
	serializer_class = PlayerAnswersSerializer

	