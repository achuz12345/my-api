# urls.py

from django.urls import path
from .views import LocationList, LocationDetail, ExperienceList, ExperienceDetail

urlpatterns = [
    path('locations/', LocationList.as_view(), name='location-list'),
    path('locations/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('experiences/', ExperienceList.as_view(), name='experience-list'),
    path('experiences/<int:pk>/', ExperienceDetail.as_view(), name='experience-detail'),
]
