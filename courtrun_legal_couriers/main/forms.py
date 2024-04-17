from django import forms
from django.forms import ModelForm
from .models import *

# Create custom widget in your forms.py file.
class DateInput(forms.widgets.DateInput):
    input_type = 'date'



class CollectionDropoffOrderForm(ModelForm):

    delivery_date= forms.DateField(widget=DateInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = CollectionDropoffOrder
        fields = "__all__"

        widgets = {
            'pickup_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the sender, as well as any messages that should be conveyed to the sender.'}),
            'dropoff_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
        }



class SummonOrderForm(ModelForm):


    delivery_date= forms.DateField(widget=DateInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = SummonOrder
        fields = "__all__"

        widgets = {
            'pickup_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the sender, as well as any messages that should be conveyed to the sender.'}),
            'dropoff_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'casenumber_establishment_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the sender.'}),
            'sc_establishment_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'ros_establishment_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
        }



class ServeOrderForm(ModelForm):

    delivery_date= forms.DateField(widget=DateInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = ServeOrder
        fields = "__all__"

        widgets = {
            'pickup_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the sender, as well as any messages that should be conveyed to the sender.'}),
            'dropoff_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'serve_establishment_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),

        }



class NoticeOrderForm(ModelForm):

    delivery_date= forms.DateField(widget=DateInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = NoticeOrder
        fields = "__all__"

        widgets = {
            'pickup_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the sender, as well as any messages that should be conveyed to the sender.'}),
            'res1_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'res2_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'res3_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'res4_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'res5_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'res6_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'dropoff_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
        }



class FileOrderForm(ModelForm):

    delivery_date= forms.DateField(widget=DateInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = FileOrder
        fields = "__all__"

        widgets = {
            'pickup_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the sender, as well as any messages that should be conveyed to the sender.'}),
            'file_establishment_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'dropoff_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
        }



class CorrespondenceOrderForm(ModelForm):

    delivery_date= forms.DateField(widget=DateInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = CorrespondenceOrder
        fields = "__all__"

        widgets = {
            'pickup_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the sender, as well as any messages that should be conveyed to the sender.'}),
            'stop1_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the sender, as well as any messages that should be conveyed to the sender.'}),
            'stop2_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'stop3_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the sender, as well as any messages that should be conveyed to the sender.'}),
            'stop4_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'stop5_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the sender, as well as any messages that should be conveyed to the sender.'}),
            'stop6_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),
            'dropoff_notes': forms.Textarea(attrs={'placeholder': 'Please provide us with the necessary contact information of the recipient, as well as any messages that should be conveyed to the recipient.'}),

        }



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

