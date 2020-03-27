from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Portfollio, Education, Service, Skill, Contact, Blog
from .forms import MessageMeForm
from django.contrib import messages
# Create your views here.


class PortfollioHomeView(ListView):
    model = Portfollio
    context_object_name = 'portfollios'
    template_name = "portfollio/home.html"


class PortfollioAboutView(ListView):
    model = Portfollio
    context_object_name = 'portfollios'
    template_name = "portfollio/about.html"


class PortfollioResumeView(ListView):
    model = Education
    context_object_name = 'educations'
    template_name = "portfollio/resume.html"


class PortfollioServicesView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = "portfollio/services.html"


class PortfollioSkillsView(ListView):
    model = Skill
    context_object_name = 'skills'
    template_name = "portfollio/skills.html"


class PortfollioProjectsView(TemplateView):
    template_name = "portfollio/projects.html"


class PortfollioContactView(View):
    def get(self, request, *args, **kwargs):
        form = MessageMeForm()
        contacts = Contact.objects.all()
        portfollio = Portfollio.objects.get(id=1)
        image_url = portfollio.image.url
        return render(request, "portfollio/contact.html", {"contacts": contacts, "form": form, "image_url": image_url})

    def post(self, request, *args, **kwargs):
        contacts = Contact.objects.all()
        form = MessageMeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            form.save()
            messages.success(
                request, f'Message Delivered Succesfully! Your will be contacted soon {name}!')
        return redirect("portfollio-home")


class BlogView(ListView):
    model = Blog
    template_name = "portfollio/blog.html"
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "portfollio/blog-detail.html"
    context_object_name = "blog"
