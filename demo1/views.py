
import base64
import hashlib
import io
import os
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import uuid
import pdfkit
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
import qrcode
from django.contrib.auth.decorators import login_required

   


def eventinfo(request):
    if request.method == "POST":
        url_event_id = request.POST.get('eventdetails')   #eventdetails is url name

        event = Event.objects.filter(event_id=url_event_id)  #we get primarykey from sql and we pass as a filter
        maxtickets = Event.objects.filter(event_id=url_event_id).values_list('maxtickets', flat=True).first()
        clientid = Event.objects.filter(event_id=url_event_id).values_list('Client_id', flat=True).first()
        clientname = Client.objects.filter(client_id = clientid).values_list('client_name', flat=True).first()
        location = Event_locations.objects.filter(event_id=url_event_id)
        


         

        ticketdetail = tickettype.objects.filter(event_id=url_event_id)
        
        

        context = {'event_list' : event, 'ticketdetail':ticketdetail, 'clientname':clientname,'location': location,}
        

    return render(request, 'ticket.html', context)


def eventhome(request):
    event = Event.objects.all()
    context = {'evnt' : event}
    return render(request, 'index.html', context)







def thankyou(request):
    if request.method == "POST":

        order_id = str(uuid.uuid1())

        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        eventid = request.POST.get('event_id')
        eventname = request.POST.get('eventname')
        ticketdetail = request.POST.get('ticket_type')
        ticketcount = request.POST.get('ticketcount')
        updatedticketcount = int(ticketcount)    
        ticket = ticketdetail.split('|')
        ticket_type = ticket[0]
        ticket_price = ticket[1]
        updateprice = int(ticket_price)*updatedticketcount

        tax = ((float(updateprice) * 18) / 100)
        final_amount_tax = float(updateprice) + float(tax)





        data = "Dear " + name + " , " + "Your "
        data += "Invoice number is " + str(order_id) + "  "

        # Generate QR code image
        qr = qrcode.QRCode(version=1, box_size=5, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")


        buffer_qr = io.BytesIO()  
        img.save(buffer_qr, format='PNG')
        image_bytes = buffer_qr.getvalue()
        img_str = base64.b64encode(image_bytes).decode('utf-8')

    
        event = Event.objects.filter(event_id=eventid)
        event_location = Event_locations.objects.filter(event_id=eventid)
        clientid = Event.objects.filter(event_id=eventid).values_list('Client_id', flat=True).first()
        clientname = Client.objects.filter(client_id = clientid)
        
        
        
        
        context = {'fetchedevent' : event, 
                    'name':name, 
                    'email':email, 
                    'phonenumber':phonenumber, 
                    'eventloc': event_location, 
                    'order_id':order_id, 
                    'clientdetails':clientname,
                    'tax': tax,
                    'finalamount': final_amount_tax,
                    'ticket_type':ticket_type,
                    'ticket_price':updateprice,
                    'ticketcount':updatedticketcount,
                    'img_str':img_str,
                    }
   

            # Whole Html is sent into mail
        template = get_template('thanks.html')
        html_content = template.render(context)

        # Configure PDF options
        options = {
            'page-size': 'Letter',
            'margin-top': '0mm',
            'margin-right': '0mm',
            'margin-bottom': '0mm',
            'margin-left': '0mm',
        }

        # Configure wkhtmltopdf executable path
        # path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
        path_wkhtmltopdf = r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        # Generate PDF from HTML content and options
        pdf_file = 'invoice_'+str(order_id)+'.pdf'
        pdf_file_path = os.path.join('static/pdf', pdf_file)
        pdf = pdfkit.from_string(
            html_content, False, options=options, configuration=config)
        with open(pdf_file_path, 'wb') as f:
                f.write(pdf)
        
         

        user_detail = Participant(name=name, eventname=eventname, email=email, phonenumber=phonenumber, eventid=eventid, order_id=order_id, file = pdf_file_path,)
        
        user_detail.save()
        # data saved to model
        

        # Create and send the email
        subject = 'Invoice of your event: ' + str(eventname)
        body = 'Thank you for registering for {}. Your details are as follows:\nName: {}\nEmail: {}\nPhone Number: {}\nOrder ID: {}'.format(eventname, name, email, phonenumber, order_id)
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        cc = ['dhruvinkalathiya96@gmail.com']
        msg = EmailMultiAlternatives(subject, body, from_email, to_email, cc=cc)

        msg.attach(pdf_file, pdf, 'application/pdf')
        msg.send()
        


        # Create a HTTP response with PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
        # Set the Content-Disposition header to force download
    response['Content-Disposition'] = 'attachment; filename="invoices.pdf"'



    return render(request, 'thankyou2.html', context)





@login_required
def sendemail(request):
        userdetail = Participant.objects.all()

        context = {'userdetail':userdetail}
        

        return render(request, 'sendemail.html', context)



def emailbutton(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        eventname = request.POST.get('eventname')
        
        if not order_id or not email:
            return HttpResponseBadRequest('Missing order_id or email')
        pdf_path = 'pdf/invoice_'+str(order_id)+'.pdf'
        print(pdf_path)
        subject = 'Invoice of your event: ' + str(eventname)
        body = 'Thank you for registering for {}. Your details are as follows:\nName: {}\nEmail: {}\nOrder ID: {}'.format(eventname, name, email, order_id)
        from_email = settings.EMAIL_HOST_USER # Replace with your email
        to_email = [email]
        msg = EmailMultiAlternatives(subject, body, from_email, to_email)
        msg.attach_file(pdf_path)
        msg.send()
        return redirect('sendemail')
    else:
        return HttpResponseBadRequest('Invalid request method')






















