from django.urls import path
from .views import SignUpView, activate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
#    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
