from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'places', views.PlaceViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.PlayerAnswersViewSet)
urlpatterns = [
	path('', include(router.urls)),
	path('api/', include('rest_framework.urls', namespace='rest_framework'))
]