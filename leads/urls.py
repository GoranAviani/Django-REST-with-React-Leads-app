from django.urls import path
from . import views
urlpatterns = [
    path('add-lead/', views.LeadListCreate.as_view() ),
    path('all-leads/', views.ShowLeadsList.as_view() ),
]