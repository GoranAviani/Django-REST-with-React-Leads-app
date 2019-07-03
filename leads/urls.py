from django.urls import path
from . import views
urlpatterns = [
    path('add-lead/', views.LeadListCreate.as_view() ),
    path('all-leads/', views.LeadListShow.as_view() ),
]