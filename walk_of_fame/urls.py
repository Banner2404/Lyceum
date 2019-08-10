from django.urls import path
from walk_of_fame import views
from walk_of_fame.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="walk_of_fame/home.html"
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("hello/<name>", views.hello, name="hello"),
    path("log/", views.log_message, name="log"),
]