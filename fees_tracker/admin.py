from django.contrib import admin
from .models import Academic_session, Bill_items, Classroom, Payment, Pupil_bill, Pupil

# Register your models here.

class Academic_sessionAdmin(admin.ModelAdmin):
    list_display = ("year","term", "beginning_date", "ending_date", "status")

admin.site.register(Academic_session, Academic_sessionAdmin)

class Bill_itemsAdmin(admin.ModelAdmin):
    list_display = ("item_name", "item_cost")

admin.site.register(Bill_items, Bill_itemsAdmin)

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("class_number",)

admin.site.register(Classroom, ClassroomAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("pupil_bill_id", "pupil_id", "payment_date", "payment_method", "received_by")

admin.site.register(Payment, PaymentAdmin)

class Pupil_billAdmin(admin.ModelAdmin):
    list_display = ("pupil_id", "academic_session_id", "bill_item_id", "amount")

admin.site.register(Pupil_bill, Pupil_billAdmin)

class PupilAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "class_number", "birth_date", "address", "parent", "contact")

admin.site.register(Pupil, PupilAdmin)
