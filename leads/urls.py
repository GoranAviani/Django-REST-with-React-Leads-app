from django.urls import path
from . import views
urlpatterns = [
    path('add-lead/', views.CreateLead.as_view() ),
    path('all-leads/', views.ShowLeadsList.as_view() ),
    path('proc-data/', views.NoModelView.as_view() )
]