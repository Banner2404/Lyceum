from django.urls import path
from walk_of_fame import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create", views.CreateRecord.as_view(), name="create_record"),
]