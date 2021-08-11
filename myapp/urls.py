
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('save/',views.save_data,name='save'),
    path('delete/',views.delete_data,name='delete'),
    path('edit/',views.edit,name='edit'),
    path('edit/<str:user_id>/',views.edit,name='edit'),

]
