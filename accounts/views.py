from django.shortcuts import render
from django.shortcuts import redirect
from website.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.


def register_new_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Rejestracja zakończona powodzeniem.")
            return redirect("accounts:welcome")
        messages.error(request, "Niepowodzenie! Błąd przy wprowadzaniu danych.")
    form = NewUserForm()
    return render(request, template_name="accounts/register_new_user.html", context={"register_form": form})


def welcome(request):
    return render(
        request,
        'accounts/welcome.html'
    )


def logout_user(request):
    return render(
        request,
        'accounts/logout_user.html'
    )


def user_account(request):
    return render(
        request,
        'accounts/user_account.html'
    )
