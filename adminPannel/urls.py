from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('table/', views.tableVw),
    path('formSave/', views.formSave, name= 'formSave'),
    path('form/', views.formLoad , name='form')
]
