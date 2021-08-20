from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from .models import *
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

# def test(request):
#     now = datetime.now()
#
#     return render(
#         request,
#         'website/test.html',
#         context = {
#         "now": now
#         }
#     )


def home(request):
    return render(
        request,
        'website/index.html'

    )


def services(request):
    services = Service.objects.all()
    context = {
        "services": services,
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
            return redirect("website:home")
        messages.error(request, "Niepowodzenie! Błąd przy wprowadzaniu danych.")
    form = NewUserForm()
    return render(request, template_name="website/register_new_user.html", context={"register_form": form})
