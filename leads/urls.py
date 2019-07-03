from django.urls import path
from . import views
urlpatterns = [
    path('all-leads/', views.LeadListCreate.as_view() ),
]