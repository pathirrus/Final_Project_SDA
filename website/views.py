from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.conf import settings
from .models import *
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin


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


def reservation(request):
    return render(
        request,
        'website/reservation.html'
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



def register_new_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Rejestracja zakończona powodzeniem.")
            return redirect("website:welcome")
        messages.error(request, "Niepowodzenie! Błąd przy wprowadzaniu danych.")
    form = NewUserForm()
    return render(request, template_name="website/register_new_user.html", context={"register_form": form})


def welcome(request):
    return render(
        request,
        'website/welcome.html'
    )

def logout_user(request):
    return render(
        request,
        'website/logout_user.html'
    )


def user_account(request):
    return render(
        request,
        'website/user_account.html'
    )
