from django.urls import path
from .views import (
    PortfollioHomeView, BlogDetailView, PortfollioAboutView, PortfollioResumeView,
    PortfollioServicesView, PortfollioSkillsView, PortfollioProjectsView, BlogView, PortfollioContactView
)

urlpatterns = [
    path("", PortfollioHomeView.as_view(), name="portfollio-home"),
    path("about", PortfollioAboutView.as_view(), name="portfollio-about"),
    path("resume", PortfollioResumeView.as_view(), name="portfollio-resume"),
    path("services", PortfollioServicesView.as_view(), name="portfollio-services"),
    path("skills", PortfollioSkillsView.as_view(), name="portfollio-skills"),
    path("projects", PortfollioProjectsView.as_view(), name="portfollio-projects"),
    path("contact", PortfollioContactView.as_view(), name="portfollio-contact"),
    path("blogs", BlogView.as_view(), name="portfollio-blog"),
    path("blogs/<str:slug>", BlogDetailView.as_view(), name="blog-detail"),
]
