from interface import views
from interface import handlers
from django.urls import path


urlpatterns = [
    path("", views.home_view),
    path("send", handlers.send_topic),
    path("<topic_name>/sample", handlers.sample_topic)
]