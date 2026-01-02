# from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mass_mail
# from django.template.loader import render_to_string
# from django.conf import settings
from django.http import HttpResponse


def send_test(request):
    message1 = ('Wecome User 1', 'Hello User 1, Welcome to our platform..','anshu.stackcraft@gmail.com',['anshulyadav1971@gmail.com'])
    message2 = ('Wecome User 2', 'Hello User 2, Welcome to our platform..','anshu.stackcraft@gmail.com',['anshuramchandra555@gmail.com'])
    message3 = ('Priya......... 3', 'Hello User 3, Welcome to our platform..','anshu.stackcraft@gmail.com',['yvishakha299@gmail.com'])
    message4 = ('Wecome User 4', 'Hello User 4, Welcome to our platform..','anshu.stackcraft@gmail.com',['yadavpriya3034@gmail.com'])

    send_mass_mail((message1, message2, message3, message4), fail_silently=False)
    return HttpResponse(f"Email succ...........")


# def send_test(request):
#     try:
#         subject = "Welcome to my Blog 🎉"
#         from_email = settings.DEFAULT_FROM_EMAIL
#         to_email = ["anshulyadav1791@gmail.com"]

#         text_content = "Thank you for subscribing to my blog."

#         html_content = render_to_string(
#             "emails/welcome_email.html",
#             {"user": "Subscriber"}
#         )

#         email = EmailMultiAlternatives(
#             subject=subject,
#             body=text_content,
#             from_email=from_email,
#             to=to_email,
#         )

#         email.attach_alternative(html_content, "text/html")
#         email.send()

#         return HttpResponse("Advanced email sent successfully ✅")

#     except Exception as e:
#         return HttpResponse(f"Email failed ❌ <br>{str(e)}")

