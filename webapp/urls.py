from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home, name='home'),
    # path('all_unis', views.all_unis, name='all_unis'),
    path('listOfUniversities', views.listOfUniversities, name='listOfUniversities'),
    path('UniversityList',views.UniversityList.as_view())
]

# http://127.0.0.1:8000/listOfUniversities gives the Json format of all the universities.(localHost)
# all_unis : gives the table format of the universities present in the database