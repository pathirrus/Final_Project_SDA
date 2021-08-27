from django.shortcuts import render
from django.shortcuts import redirect
from website.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.forms.models import model_to_dict
from .models import NewUser
# from .forms import UserEditForm

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


# def edit_profile(request, user_id):
#     user = get_object_or_404(NewUser, pk=user_id)
#     if request.method == "GET":
#         form = UserEditForm(initial=model_to_dict(user))
#         return render(request, 'accounts/edit_profile.html', {'form': form})
#     elif request.method == "POST":
#         form = UserEditForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('user_profile', kwargs={'uid': user.id}))
#         else:
#             return HttpResponseRedirect(reverse('some_fail_loc'))
