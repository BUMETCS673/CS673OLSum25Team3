import random
from django.core.mail import send_mail

def send_mfa_code(email, request):
    code = str(random.randint(100000, 999999))
    request.session['mfa_code'] = code
    send_mail(
        'Your MFA Code',
        f'Your MFA verification code is: {code}',
        'yourapp@gmail.com',
        [email],
        fail_silently=False,
    )