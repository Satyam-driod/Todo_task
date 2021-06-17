from django.urls import path
from . import views

urlpatterns=[
    path('',views.mainfunc,name='work'),
    path('delete_work/<str:pk>/',views.deleteWork,name="delete_work"),
    path('update_work/<str:pk>/',views.updateWork,name='update_work')
]