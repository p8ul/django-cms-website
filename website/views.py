from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    if request.method == "POST":
        check_in = request.POST['check_in']
        check_out = request.POST['check_in']
        room_type = request.POST['room-type']
        send_mail(
            'Kigwa Room Booking',
            room_type + ' booking from '+check_in+ '  to '+check_out,
            'admin@web.com',
            ['to@example.com'],
            fail_silently=True,
        )
    context = {'title':' Kigwa Hotel '}
    return redirect('/')