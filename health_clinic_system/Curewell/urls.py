from django.contrib import admin
from django.urls import path, include

from Curewell import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.alldoctors, name='alldoctors'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('booking/', views.booking, name='booking'),
    path('patient/', views.patient, name='patient'),
    path('ourdoctors/', views.ourdoctors, name='ourdoctors'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('record', views.record, name='record'),
    path('patient_record', views.patient_record, name='patient_record'),
    path('<slug:slug_c>/', views.alldoctors, name='doctors_by_department'),
]