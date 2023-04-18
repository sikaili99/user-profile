from django.urls import path
from .views import ProfileUpdateView, UserProfileDeailsView, logout_view, map_view, signin, signup

app_name = 'accounts'
urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', signin, name='login'),
    path('register/', signup, name='signup'),
    path('profile/', UserProfileDeailsView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('map/', map_view, name='map')

]
