from django import forms


class Fib_seqForm(forms.Form):
    number = forms.IntegerField()
