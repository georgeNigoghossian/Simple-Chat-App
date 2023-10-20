from django.urls import path, include

import ecb
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),

    # login-section
    path("auth/login/", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path('encrypt_ecb/', ecb.encrypt_message, name='encrypt_ecb'),
    path('decrypt_ecb/', ecb.decrypt_message, name='decrypt_ecb'),
]
