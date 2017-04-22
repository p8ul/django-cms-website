from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import redirect
from models import Booking
from .forms import BookingForm

from datetime import datetime

def index(request):
    form = BookingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.save()
    if request.method == "POST":
        check_in  = request.POST['check_in_date']
        check_out = request.POST['check_out_date']
        room_type = request.POST['room_type']
        return render(request, 'bookingForm.html', context={'form':form,'check_in':check_in,'check_out':check_out,'room_type':room_type})
    return redirect('/')

def BookingView(request):
    form = BookingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.save()
        return render(request, 'BookingSuccessful.html',context={'form':form})
    return render(request, 'bookingForm.html',
                      context={'form': form, 'check_in': request.POST['check_in_date']})


def reservation(request):
    if request.method == "POST":
        check_in  = request.POST['check-in-date']
        check_out = request.POST['check-out-date']
        room_type = request.POST['room-type']
        '''
        send_mail(
            'Kigwa Room Booking',
            room_type + ' booking from ' + check_in + '  to ' + check_out,
            'admin@web.com',
            ['to@example.com'],
            fail_silently=True,
        )
        '''
    if check_in != '' and check_in != '':
        check_in = datetime.strptime(request.POST['check-in-date'], '%B %d, %Y').strftime('%Y-%m-%d')
        check_out = datetime.strptime(request.POST['check-out-date'], '%B %d, %Y').strftime('%Y-%m-%d')
        book = Booking.objects.create(check_in_date=check_in, check_out_date =check_out, room_type = room_type)
        book.save()
    return redirect('/reservation')

def ContactForm(request):
    if request.method == "POST":
        name  = request.POST['your-name']
        email = request.POST['your-email']
        subject = request.POST['your-subject']
        message = request.POST['your-message']
        '''
        send_mail(
            'Kigwa Room Booking',
            room_type + ' booking from ' + check_in + '  to ' + check_out,
            'admin@web.com',
            ['to@example.com'],
            fail_silently=True,
        )
        '''
    if name != '' and email != '' and subject != '' and message != '':
        check_in = datetime.strptime(request.POST['check-in-date'], '%B %d, %Y').strftime('%Y-%m-%d')
        check_out = datetime.strptime(request.POST['check-out-date'], '%B %d, %Y').strftime('%Y-%m-%d')
        contact = ContactForm.objects.create(name=name, email =email, subject = subject,message=message)
        contact.save()
    return redirect('/contact_us')




