
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import views
from . import forms

contact_forms = [forms.GuestForm1, forms.GuestForm2]

urlpatterns = [
    path('', views.index, name="home"),
    path('rsvp/', views.RSVPWizardView.as_view(contact_forms), name="addrsvp"),
    path('our_story/', TemplateView.as_view(template_name="our_story/our_story.html"), name="ourstory"),
    path('info/', TemplateView.as_view(template_name="info/info.html"), name="info"),
    path('photo/', views.photo_gallery, name="photogallery"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
