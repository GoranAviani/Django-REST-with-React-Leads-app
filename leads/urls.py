from django.urls import path
from . import views
urlpatterns = [
    path('add-lead/', views.LeadListCreate.as_view() ),
]