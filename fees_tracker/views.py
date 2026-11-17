from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


from .models import Academic_session, Bill_items, Classroom, Payment, Pupil_bill, Pupil
from fees_tracker.forms import ClassroomForm, Bill_itemForm, Academic_sessionForm, PaymentForm, Pupil_billForm, PupilForm
from django.contrib.auth.decorators import login_required

from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.shortcuts import render
from django.db.models import F, Q
import json

from .models import (
    Pupil,
    Pupil_bill,
    Payment,
    Bill_items,
    Academic_session,
    Classroom
)
# Create your views here.

@ login_required(login_url='login')
def index_page(request):

    # Total registered pupils
    total_pupils = Pupil.objects.count()

    # Total fees billed
    total_billed = (
        Pupil_bill.objects.aggregate(
            total=Sum('amount')
        )['total'] or 0
    )

    # Total payments received
    total_payments = (
        Payment.objects.aggregate(
            total=Sum('amount_paid')
        )['total'] or 0
    )

    # Outstanding balance
    outstanding_balance = total_billed - total_payments

    # Get all pupil bills with their payments
    bills = Pupil_bill.objects.annotate(
        paid=Sum('payment__amount_paid')
    )

    paid_count = 0
    partial_count = 0
    unpaid_count = 0

    for bill in bills:

        paid = bill.paid or 0

        if paid >= bill.amount:
            paid_count += 1

        elif paid > 0:
            partial_count += 1

        else:
            unpaid_count += 1

    # Monthly payment collections
    monthly_payments = (
        Payment.objects
        .annotate(month=TruncMonth('payment_date'))
        .values('month')
        .annotate(total=Sum('amount_paid'))
        .order_by('month')
    )

    months = [
        item['month'].strftime('%b %Y')
        for item in monthly_payments
    ]

    monthly_amounts = [
        item['total']
        for item in monthly_payments
    ]

    # Recent transactions
    recent_payments = Payment.objects.select_related(
        'pupil_id',
        'pupil_bill_id'
    ).order_by('-payment_date')[:5]

    context = {
        'total_pupils': total_pupils,
        'total_billed': total_billed,
        'total_payments': total_payments,
        'outstanding_balance': outstanding_balance,

        'paid_count': paid_count,
        'partial_count': partial_count,
        'unpaid_count': unpaid_count,

        'months': json.dumps(months),
        'monthly_amounts': json.dumps(monthly_amounts),

        'recent_payments': recent_payments,
    }

    return render(request, 'index.html', context)

@ login_required
def classroom_view(request):
    return render(request, 'classroom.html')

def academic_session_view(request):
    return render(request, 'academic_session.html')

def bill_item_view(request):
    return render(request, 'bill_item.html')

def payment_view(request):
    return render(request, 'payment.html')

def pupil_view(request):
    return render(request, 'pupil.html')  

def pupil_bill_view(request):
    return render(request, 'pupil_bill.html')  

def add_classroom_view(request):
    message = ''
    if request.method == "POST":
        classroom_form = ClassroomForm(request.POST)  

        if classroom_form.is_valid():
            classroom_form.save()

            message = 'Classroom added successfully'

    else:
        classroom_form = ClassroomForm() 

    classrooms = Classroom.objects.all()

    context = {
         'form': classroom_form,
         'message': message,
         'classrooms': classrooms,
    } 

    return render(request, "add_classroom.html", context)    

def add_Bill_item_view(request):
    message = ''
    if request.method == "POST":
        Bill_item_form = Bill_itemForm(request.POST)  

        if Bill_item_form.is_valid():
            Bill_item_form.save()
            message = 'Bill item added successfully'

    else:
        Bill_item_form = Bill_itemForm() 

    bill_items = Bill_items.objects.all()
    
    context = {
             'form': Bill_item_form,
             'message': message,
            'bill_items': bill_items,
    } 
    
    return render(request, "add_bill_item.html", context) 

def add_academic_session_view(request):
    message = ''
    if request.method == "POST":
        academic_session_form = Academic_sessionForm(request.POST)  

        if academic_session_form.is_valid():
            academic_session_form.save()
            message = 'Academic session added successfully'

    else:
        academic_session_form = Academic_sessionForm() 

    academic_sessions = Academic_session.objects.all()
    
    context = {
             'form': academic_session_form,
             'message': message,
            'academic_sessions': academic_sessions,
    } 
    
    return render(request, "add_academic_session.html", context)    

def add_payment_view(request):
    message = ''
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)  

        if payment_form.is_valid():
            payment_form.save()
            message = 'Payment added successfully'

    else:
        payment_form = PaymentForm()

    payments = Payment.objects.all()     

    context = {
             'form': payment_form,
             'message': message,
            'payments': payments,
    } 
    
    return render(request, "add_payment.html", context)

def add_pupil_bill_view(request):
    message = ''
    if request.method == "POST":
        pupil_bill_form = Pupil_billForm(request.POST)  

        if pupil_bill_form.is_valid():
            pupil_bill_form.save()
            message = 'Pupil bill added successfully'
            pupil_bill_form = Pupil_billForm

    else:
        pupil_bill_form = Pupil_billForm()
    pupil_bills = Pupil_bill.objects.all() 

    context = {
             'form': pupil_bill_form,
             'message': message,
            'pupil_bills': pupil_bills,
    } 
    
    return render(request, "add_pupil_bill.html", context)

def add_pupil_view(request):
    message = ''
    if request.method == "POST":
        pupil_form = PupilForm(request.POST)  

        if pupil_form.is_valid():
            pupil_form.save()
            message = 'Pupil added successfully'

    else:
        pupil_form = PupilForm()

    pupils = Pupil.objects.all()     

    context = {
             'form': pupil_form,
             'message': message,
            'pupils': pupils,
    } 
    
    return render(request, "add_pupil.html", context)

def edit_classroom_view(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    message = ''
    if request.method == "POST":
        classroom_form = ClassroomForm(request.POST, instance=classroom)  

        if classroom_form.is_valid():
            classroom_form.save()
            message = 'Classroom updated successfully'
        else:
            message = 'Error updating classroom'

    else:
        classroom_form = ClassroomForm(request.POST,instance=classroom) 

    classrooms = Classroom.objects.all()

    context = {
         'form': classroom_form,
         'message': message,
         'classrooms': classrooms,
    } 

    return render(request, 'edit_classroom.html', context)

def edit_bill_item_view(request, bill_item_id):
    bill_item = Bill_items.objects.get(id=bill_item_id)
    message = ''
    if request.method == "POST":
        bill_item_form = Bill_itemForm(request.POST, instance=bill_item)  

        if bill_item_form.is_valid():
            bill_item_form.save()
            message = 'Bill item updated successfully'
        else:
            message = 'Error updating bill item'

    else:
        bill_item_form = Bill_itemForm(instance=bill_item) 

    bill_items = Bill_items.objects.all()

    context = {
         'form': bill_item_form,
         'message': message,
         'bill_items': bill_items,
    } 

    return render(request, 'edit_bill_item.html', context)

def edit_academic_session_view(request, academic_session_id):
    academic_session = Academic_session.objects.get(id=academic_session_id)
    message = ''
    if request.method == "POST":
        academic_session_form = Academic_sessionForm(request.POST, instance=academic_session)  

        if academic_session_form.is_valid():
            academic_session_form.save()
            message = 'Academic session updated successfully'
        else:
            message = 'Error updating academic session'

    else:
        academic_session_form = Academic_sessionForm(request.POST,instance=academic_session) 

    academic_sessions = Academic_session.objects.all()

    context = {
         'form': academic_session_form,
         'message': message,
         'academic_sessions': academic_sessions,
    } 

    return render(request, 'edit_academic_session.html', context)

def edit_pupil_view(request, pupil_id):
    pupil = Pupil.objects.get(id=pupil_id)
    message = ''
    if request.method == "POST":
        pupil_form = PupilForm(request.POST, instance=pupil)  

        if pupil_form.is_valid():
            pupil_form.save()
            message = 'Pupil updated successfully'
        else:
            message = 'Error updating pupil'

    else:
        pupil_form = PupilForm(instance=pupil) 

    pupils = Pupil.objects.all()

    context = {
         'form': pupil_form,
         'message': message,
         'pupils': pupils,
    } 

    return render(request, 'edit_pupil.html', context)

def edit_payment_view(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    message = ''
    if request.method == "POST":
        payment_form = PaymentForm(request.POST, instance=payment)  

        if payment_form.is_valid():
            payment_form.save()
            message = 'Payment updated successfully'
        else:
            message = 'Error updating payment'

    else:
        payment_form = PaymentForm(instance=payment) 

    payments = Payment.objects.all()

    context = {
         'form': payment_form,
         'message': message,
         'payments': payments,
    } 

    return render(request, 'edit_payment.html', context)

def edit_pupil_bill_view(request, pupil_bill_id):
    pupil_bill = Pupil_bill.objects.get(id=pupil_bill_id)
    message = ''
    if request.method == "POST":
        pupil_bill_form = Pupil_billForm(request.POST, instance=pupil_bill)  

        if pupil_bill_form.is_valid():
            pupil_bill_form.save()
            message = 'Pupil bill updated successfully'
        else:
            message = 'Error updating pupil bill'

    else:
        pupil_bill_form = Pupil_billForm(instance=pupil_bill) 

    pupil_bills = Pupil_bill.objects.all()

    context = {
         'form': pupil_bill_form,
         'message': message,
         'pupil_bills': pupil_bills,
    } 

    return render(request, 'edit_pupil_bill.html', context)

def delete_classroom_view(request, classroom_id):
    classroom = Classroom.objects.get(id = classroom_id)

    classroom.delete()

    return redirect(add_classroom_view)

def delete_academic_session_view(request, academic_session_id):
    academic_session = Academic_session.objects.get(id = academic_session_id)

    academic_session.delete()

    return redirect(add_academic_session_view)

def delete_bill_item_view(request, bill_item_id):
    bill_item = Bill_items.objects.get(id = bill_item_id)

    bill_item.delete()

    return redirect(add_Bill_item_view)

def delete_payment_view(request, payment_id):
    payment = Payment.objects.get(id = payment_id)

    payment.delete()

    return redirect(add_payment_view)

def delete_pupil_bill_view(request, pupil_bill_id):
    pupil_bill = Pupil_bill.objects.get(id = pupil_bill_id)

    pupil_bill.delete()

    return redirect(add_pupil_bill_view)

def delete_pupil_view(request, pupil_id):
    pupil = Pupil.objects.get(id = pupil_id)

    pupil.delete()

    return redirect(add_pupil_view)

def sign_up_view(request):
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()
            message = 'User created successfully'
        else:
            message = "Something went wrong"

    else:
        sign_up_form = UserCreationForm()

    context = {
        'form': sign_up_form
    }

    return render(request, 'registration/sign_up.html', context)

