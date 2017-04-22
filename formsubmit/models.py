from django.db import models

ROOMS = (
    ('Single', 'Single Room'),
    ('Double', 'Double Rooms'),
    ('Triple', 'Triple Rooms' ),
    ('Ensuite', 'Ensuite' ),
)

class Booking(models.Model):
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room_type = models.CharField(max_length= 120, choices=ROOMS)
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(default='user@example.com')
    phone = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.room_type + ' - from ' + str(self.check_in_date) + ' to ' + str(self.check_out_date)

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name + ' - from ' + str(self.email) + '  ' + str(self.subject)