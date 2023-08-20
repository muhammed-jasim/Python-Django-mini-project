from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('teachers/',views.teachers,name='teachers'),
    path('courses/',views.courses,name='courses'),
    path('about/',views.about,name='about'),
    path('contacts/',views.contacts,name='contacts'),
    path('base/',views.base),
] 