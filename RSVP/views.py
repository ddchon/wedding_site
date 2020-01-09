import os
from django.conf import settings
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

from .forms import GuestForm1, GuestForm2
from .models import Guest, GuestParty
# Create your views here.

def index(request):
    return render(request, 'RSVP/home.html')


class RSVPWizardView(SessionWizardView):

    instance = None
    form_list = [GuestForm1, GuestForm2]

    def get_form_instance(self, step):

        if self.instance is None:
            self.instance = Guest()
        return self.instance

    def done(self, form_list, form_dict, **kwargs):

        parent = form_dict.get('0')
        child = form_dict.get('1')

        guest_party_first_name = child.cleaned_data['party_first_name']
        guest_party_last_name = child.cleaned_data['party_last_name']

        guest_party = GuestParty.objects.create(
            guest=parent.instance,
            party_first_name=guest_party_first_name,
            party_last_name=guest_party_last_name,
        )

        guest_party.save()


        return render(self.request, 'RSVP/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

def photo_gallery(request):

    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/images')
    context = {'images': img_list}

    return render(request, "photo/photo_gallery.html", context)
