from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("contact", views.contact, name="contact"),
    path("cliente/<str:profile>", views.profile, name="cliente")
]
