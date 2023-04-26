from django import forms

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('value should be start with a')



class StudentForms(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a])
    age=forms.IntegerField()
    email=forms.EmailField()
    reenter_email=forms.EmailField()
    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reenter_email']
        if e!=r:
            raise forms.ValidationError('vijji absent ')
        



    