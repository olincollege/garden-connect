"""
Establishing URL pathways accessible for specific users
"""
from django.urls import path
from django.contrib.auth import views as authViews
from authy.views import (signup, password_change, password_change_done, # pylint: disable=E0401
edit_profile, explore, cucumber, lettuce, tomato, kale)



urlpatterns = [
    path('profile/edit', edit_profile, name='edit-profile'),
   	path('signup/', signup, name='signup'),
   	path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
   	path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
   	path('changepassword/', password_change, name='change_password'),
   	path('changepassword/done', password_change_done, name='change_password_done'),
   	path('passwordreset/', authViews.PasswordResetView.as_view(),
         name='password_reset'),
   	path('passwordreset/done', authViews.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
   	path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
   	path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path("explore/", explore, name="explore"),
    path("kale/", kale, name="kale"),
    path("tomato/", tomato, name="tomato"),
    path("lettuce/", lettuce, name="lettuce"),
    path("cucumber/", cucumber, name="cucumber"),
]
