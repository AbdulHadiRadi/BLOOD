from datetime import datetime, timedelta, date
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode
from rest_framework.utils import json
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .tokens import account_activation_token
from notify.signals import notify
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)
from .forms import SignUpForm, HospitalSignUpForm, AddressForm
from api.models import User, Request, Donor, Account, Notification


def home(request):
    return render(request, 'bloodonor/index.html')



def profile(request):
    current_time = datetime.now()
    threshold_time = current_time - timedelta(days=90)
    Donor.objects.filter(last_donated_date__lte= threshold_time).update(capable=True)
    Donor.objects.filter(last_donated_date__gt= threshold_time).update(capable=False)
    return render(request, 'bloodonor/profile.html')


def notification(request):
    current_time = datetime.now()
    threshold_time = current_time - timedelta(days=1)
    Request.objects.filter(time__lt=threshold_time).delete()
    req = Notification.objects.filter(user=request.user)
    req_ids = list(Request.objects.filter(user=request.user).values_list("id", flat=True))
    my_req = list(Notification.objects.filter(request__in=req_ids).order_by('request'))
    return render(request, 'bloodonor/notification.html', {'req':req , 'my_req':my_req})


def donor_signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(prefix="user", data=request.POST)
        address_form = AddressForm(prefix="address", data=request.POST)
        if all([user_form.is_valid(), address_form.is_valid()]):
            user = user_form.save(commit=False)
            user.is_active = True
            user.is_donor = True
            user.save()
            user.account.street = address_form.cleaned_data.get('street_number')
            user.account.road = address_form.cleaned_data.get('road')
            user.account.city = address_form.cleaned_data.get('city')
            user.account.state = address_form.cleaned_data.get('state')
            user.account.country = address_form.cleaned_data.get('country')
            user.account.post_code = address_form.cleaned_data.get('postal_code')
            user.account.phone_number = user_form.cleaned_data.get('phone_number')
            user.account.phone_number = user_form.cleaned_data.get('phone_number')
            user.donor.bloodGroup = user_form.cleaned_data.get('blood_group')
            user.donor.birth_date = user_form.cleaned_data.get('birth_date')
            user.donor.capable = True;
            user.save()
            user.account.save()
            user.donor.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        user_form = SignUpForm(prefix="user")
        address_form = AddressForm(prefix="address")
    return render(request, 'bloodonor/signup.html', {'user_form': user_form, 'address_form': address_form})


def account_activation_sent(request):
    return render(request, 'bloodonor/account_activation_sent.html')



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.account.email_confirmed = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend' )
        return redirect('home')
    else:
        return render(request, 'bloodonor/account_activation_invalid.html')




def hospital_signup(request):
    if request.method == 'POST':
        user_form = HospitalSignUpForm(prefix="user", data=request.POST)
        address_form = AddressForm(prefix="address", data=request.POST)
        if all([user_form.is_valid(), address_form.is_valid()]):
            user = user_form.save(commit=False)
            user.is_active = False
            user.is_donor = False
            user.save()
            user.account.phone_number = user_form.cleaned_data.get('phone_number')
            user.account.street = address_form.cleaned_data.get('street_number')
            user.account.road = address_form.cleaned_data.get('road')
            user.account.city = address_form.cleaned_data.get('city')
            user.account.state = address_form.cleaned_data.get('state')
            user.account.country = address_form.cleaned_data.get('country')
            user.account.post_code = address_form.cleaned_data.get('postal_code')
            user.save()
            user.account.save()
            current_site = get_current_site(request)
            subject = 'Activate Your BlooDonor Account'
            message = render_to_string('bloodonor/account_activation_email.html',
                                       {'user': user, 'domain': current_site.domain,
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                                        'token': account_activation_token.make_token(user)})

            user.email_user(subject, message)
            return render(request, 'bloodonor/account_activation_sent.html')
    else:
        user_form = HospitalSignUpForm (prefix="user")
        address_form = AddressForm(prefix="address")
    return render(request, 'bloodonor/signup.html', {'user_form': user_form, 'address_form': address_form})


def logout_view(request):
    logout(request)
    return redirect("login")



