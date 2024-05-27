from  django import forms 
from app.models import *



def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('started with a')
    
def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('Length must be more than 5')
    
    
    
class  Topicpage(forms.Form):
    tn=forms.CharField(validators=[validate_for_a,validate_for_len])
    
class webpage(forms.Form):
    tn=forms.ModelChoiceField(queryset=TOPIC.objects.all())
    na=forms.CharField(validators=[validate_for_a],label='NAME',help_text='name should not started with a')
    ur=forms.URLField()
    em=forms.EmailField()
    rem=forms.EmailField()
    def clean(self):
        em=self.cleaned_data['em']
        rem=self.cleaned_data['rem']
        if em != rem:
            raise forms.ValidationError('Both email should be same')


class accessrecord(forms.Form):
    na=forms.ModelChoiceField(queryset=WEBPAGE.objects.all())
    da=forms.DateField()
    au=forms.CharField(validators=[validate_for_a])
    
    
    