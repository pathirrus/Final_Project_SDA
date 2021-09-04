from datetime import datetime, date, timedelta

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from website.models import Service
from website.models import Reservation
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from website.forms import ReservationForm


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def handle_no_permission(self):
        return redirect('login')

    def test_func(self):
        return self.request.user.is_staff


class ServiceCreateView(StaffRequiredMixin, CreateView):
    model = Service
    fields = [
        'service_name',
        "price",
        'time_of_service'
    ]


class ServiceUpdateView(StaffRequiredMixin, UpdateView):

    model = Service
    fields = [
        'service_name',
        "price",
        'time_of_service'
    ]
    template_name_suffix = '_update'


class ServiceDeleteView(StaffRequiredMixin, DeleteView):
    model = Service
    success_url = reverse_lazy('website:services')


def home(request):
    return render(
        request,
        'website/index.html'

    )


def services(request):
    service = Service.objects.all()
    context = {
        "services": service,
    }

    return render(
        request,
        'website/services.html',
        context)

####################################################


def reservation(request):

    return render(
        request,
        'website/reservation.html',
    )


def contact(request):
    return render(
        request,
        'website/contact.html'
    )


def about(request):
    return render(
        request,
        'website/about.html'
    )


def gallery(request):
    return render(
        request,
        'website/gallery.html'
    )


class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user_id = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('website:reservation'))


def get_available_hours(request):
    service_id = request.GET.get('service_id')
    visit_date = request.GET.get('date')

    available_hours = Reservation().get_available_hours(
        service_id,
        visit_date
    ) if service_id and visit_date else []

    return render(
        request,
        'website/available_hours_dropdown_list_option.html',
        context={
            'available_hours': available_hours
        }
    )