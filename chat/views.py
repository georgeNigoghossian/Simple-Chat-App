from django.shortcuts import render, redirect
from Crypto.Random import get_random_bytes
from ecb import encrypt_message, decrypt_message
from cbc import cbc_encrypt_message, cbc_decrypt_message

shared_key = get_random_bytes(16)


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")

    context = {
        'encrypt_message': encrypt_message,
        'decrypt_message': decrypt_message,
        'cbc_encrypt_message': cbc_encrypt_message,
        'cbc_decrypt_message': cbc_decrypt_message,
        'shared_key': shared_key,
    }

    return render(request, "chat/chatPage.html", context)