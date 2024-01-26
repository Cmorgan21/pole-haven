from django import forms

class ContactForm(forms.Form):
    subject_choices = [
        ('general', 'General Inquiry'),
        ('support', 'Customer Support'),
        ('account', 'Account Support'),
        ('advice', 'Poling Advice'),
    ]

    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    subject = forms.ChoiceField(choices=subject_choices, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')