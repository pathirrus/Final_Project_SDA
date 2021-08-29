from datetime import datetime, date, timedelta

from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from website.models import Service
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

    start_date = date.today()
    rdate = start_date
    end_date = start_date + timedelta(days=7)

    date_list = [start_date]

    while rdate < end_date:
        rdate += timedelta(days=1)
        date_list.append(rdate)


    if request.method == "POST":
        form = ReservationForm(request.POST)

    context = {

        'date_list': date_list,
        'start_date': start_date,
        'end_date':end_date,
    }

    return render(
        request,
        'website/reservation.html',
        context
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






