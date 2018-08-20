from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
# from django.core.mail import EmailMessage, send_mail
# from django.template import Context
# from django.template.loader import get_template
# from django.contrib import messages, auth
# from .forms import ContactForm

def contacts (request):
    return render(request, 'contacts.html')