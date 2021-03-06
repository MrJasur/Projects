from django.urls import path, reverse_lazy
from .views import (
    ProfileUpdateView, RegisterView, 
    LoginView, ProfileView, LogoutView, 
    ProfileUpdateView, NewPasswordView,
    PasswordResetFormOverride
)
from django.contrib.auth import views as auth_views

app_name = 'users' #agar view ni pathini ozgartirsak ham ishlayveradi
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit', ProfileUpdateView.as_view(), name='profile_edit'),
    path('password/change', NewPasswordView.as_view(), name='password_change'),

    path('password-reset/',auth_views.PasswordResetView.as_view(
                            success_url=reverse_lazy('users:password_reset_done'),
                            template_name='registration/password_reset_form.html',
                            form_class = PasswordResetFormOverride,
                            ),name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(
                            template_name='registration/password_reset_done.html'
                            ),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
                            success_url=reverse_lazy('users:password_reset_complete'),
                            template_name='registration/password_reset_confirm.html'
                            ),name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(
                            template_name='registration/password_reset_complete.html'
                            ),name='password_reset_complete'),

]