"""
URL configuration for fees_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from fees_project.fees_tracker.views import index_page
from fees_tracker.views import index_page, classroom_view, academic_session_view, bill_item_view, payment_view, pupil_view, pupil_bill_view, add_classroom_view, add_Bill_item_view, add_academic_session_view, add_payment_view, add_pupil_bill_view, add_pupil_view, edit_academic_session_view, edit_bill_item_view, edit_payment_view, edit_pupil_view, edit_pupil_bill_view, edit_classroom_view, delete_classroom_view, delete_academic_session_view, delete_bill_item_view, delete_payment_view, delete_pupil_bill_view, delete_pupil_view, sign_up_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name= 'index_page'),
    path('sign_up/', sign_up_view, name = 'sign_up_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('classroom/', classroom_view, name='classroom_page'),
    path('academic_session/', academic_session_view, name = 'academic_session_page'),
    path('bill_item/', bill_item_view, name = 'bill_item_page'),
    path('payment/', payment_view, name = 'payment_page'),
    path('pupil/', pupil_view, name = 'pupil_page'),
    path('pupil_bill/', pupil_bill_view, name = 'pupil_bill_page'),
    path('add_classroom/', add_classroom_view, name = "add_classroom_page"),
    path('add_bill_item/', add_Bill_item_view, name = 'add_bill_item_page'),
    path('add_academic_session/', add_academic_session_view, name = 'add_academic_session_page'),
    path('add_payment/', add_payment_view, name = 'add_payment_page'),
    path('add_pupil_bill/', add_pupil_bill_view, name = 'add_pupil_bill_page'),
    path('add_pupil/', add_pupil_view, name = 'add_pupil_page'),
    path('edit_academic_session/<int:academic_session_id>/', edit_academic_session_view, name = 'edit_academic_session_page'),
    path('edit_bill_item/ <int:bill_item_id>/', edit_bill_item_view, name = 'edit_bill_item_page'),
    path('edit_payment/ <int:payment_id>/' , edit_payment_view, name = 'edit_payment_page'),
    path('edit_pupil/ <int:pupil_id>/', edit_pupil_view, name = 'edit_pupil_page'),
    path('edit_pupil_bill/ <int:pupil_bill_id>/', edit_pupil_bill_view, name = 'edit_pupil_bill_page'),
    path('edit_classroom/ <int:classroom_id>/', edit_classroom_view, name = 'edit_classroom_page'),
    path('delete_classroom/<int:classroom_id>/', delete_classroom_view, name = 'delete_classroom_page'),
    path('delete_academic_session/<int:academic_session_id>/', delete_academic_session_view, name = 'delete_academic_session_page'),
    path('delete_bill_item/<int:bill_item_id>/', delete_bill_item_view, name = 'delete_bill_item_page'),
    path('delete_payment/<int:payment_id>/', delete_payment_view, name = 'delete_payment_page'),
    path('delete_pupil_bill/<int:pupil_bill_id>/', delete_pupil_bill_view, name = 'delete_pupil_bill_page'),
    path('delete_pupil/<int:pupil_id>/', delete_pupil_view, name = 'delete_pupil_page')
]
