from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render

from accounts.forms import RegisterForm

User = get_user_model()


# Create your views here.
def register(request):
    register_form = RegisterForm(request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You may now login.')
            return HttpResponseRedirect("/")

    return render(
        request,
        template_name="accounts/register.html",
        context={'title': "registration", "form": register_form}
    )