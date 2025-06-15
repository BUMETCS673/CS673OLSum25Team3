import random
from django.core.mail import send_mail
from django.conf import settings

def send_mfa_code(user_email, request):
    code = str(random.randint(100000, 999999))
    request.session['mfa_code'] = code

    print("Generated MFA Code:", code)

    try:
        result = send_mail(
            subject="Your MyMedic MFA Code",
            message=f"Your verification code is: {code}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            fail_silently=False
        )
        print("Email send result (1=success):", result)

    except Exception as e:
        print("Failed to send MFA email:", e)
