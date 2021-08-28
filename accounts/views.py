from django.shortcuts import render
from django.shortcuts import redirect
from website.forms import NewUserForm
from accounts.forms import ProfileEditForm
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.models import NewUser


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


def profile(request):
    return render(
        request,
        'accounts/profile.html'
    )



@login_required
def edit_profile(request):

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:profile'))
        else:
            args = {'form': form}
            return render(request, 'accounts/edit_profile.html', args)

    else:
        form = ProfileEditForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)
