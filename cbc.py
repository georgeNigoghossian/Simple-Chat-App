from django.http import JsonResponse
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from django.views.decorators.csrf import csrf_exempt
import base64
import json

@csrf_exempt
def cbc_encrypt_message(request):
    if request.method == 'POST':
        data = request.POST.get('data', '')

    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    ct = b64encode(ct_bytes).decode('utf-8')

    key_str = b64encode(key).decode('utf-8')
    iv_str = b64encode(iv).decode('utf-8')
    response_data = {'key': key_str, 'iv': iv_str, 'ct': ct}

    return JsonResponse(response_data, safe=False)

@csrf_exempt
def cbc_decrypt_message(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        key = json_data.get('key', '').encode('utf-8')
        iv = json_data.get('iv', '').encode('utf-8')
        ciphertext = json_data.get('ciphertext', '').encode('utf-8')
        username = json_data.get('username', '')

    key = b64decode(key)
    iv = b64decode(iv)
    print("****************************")
    print(iv)
    print("****************************")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = b64decode(ciphertext)
    pt_bytes = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    plaintext = pt_bytes.decode('utf-8')

    response_data = {
                        'message': plaintext,
                        'username': username,
                        'ciphertext': json_data.get('ciphertext', ''),
                        'key': json_data.get('key', ''),
                        'iv': json_data.get('iv', '')
                    }
    
    return JsonResponse(response_data, safe=False)


