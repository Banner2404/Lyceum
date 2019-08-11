from django.urls import path
from walk_of_fame import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("create", views.CreateRecordView.as_view(), name="create_record"),
]