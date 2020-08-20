from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('add-complain',views.add_complain,name='add-complain'),
    path('add-suggestion',views.add_suggestion,name='add-suggestion'),
]
