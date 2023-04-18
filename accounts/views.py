from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import ProfileForm, SignInForm, SignUpForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, authenticate, logout
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from accounts.models import Profile
from django.urls import reverse_lazy
from django.conf import settings


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('accounts:profile')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = SignInForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


class UserProfileDeailsView(LoginRequiredMixin, DetailView):

    model = Profile
    template_name = 'profile/index.html'
    fields = ['home_address', 'phone_number', 'location', 'picture']
    context_object_name = 'profile'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView, FormMixin):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('accounts:profile')
    success_message = "Profile updated successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def map_view(request):
    profiles = Profile.objects.all()
    locations = []
    for profile in profiles:
        locations.append({
            'name': profile.user.username,
            'address': profile.home_address,
            'picture_url': profile.get_picture_url,
            'city': profile.city,
            'phone': profile.phone_number,
            'first_name': profile.user.first_name,
            'last_name': profile.user.last_name,
            'lat': profile.location.y,
            'lng': profile.location.x,
        })
    context = {
        'locations': locations,
        'api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'profile/map.html', context)
