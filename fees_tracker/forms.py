from django.forms import ModelForm
from fees_tracker.models import Classroom, Bill_items, Academic_session, Payment, Pupil_bill, Pupil

class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'

class Bill_itemForm(ModelForm):
    class Meta:
        model = Bill_items
        fields = '__all__'

class Academic_sessionForm(ModelForm):
    class Meta:
        model = Academic_session
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class Pupil_billForm(ModelForm):
    class Meta:
        model = Pupil_bill
        fields = '__all__'

class PupilForm(ModelForm):
    class Meta:
        model = Pupil
        fields = '__all__'