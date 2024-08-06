from django import forms
c=[('MALE','male'),('FEMALE','female')]
s=[('PYTHON','python'),('SQL','sql')]
class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100)
    Sage=forms.IntegerField()
    Semail=forms.EmailField()
    Surl=forms.URLField()
    #DOB=forms.DateTimeField()
    gender=forms.ChoiceField(choices=c)
    #gender=forms.ChoiceField(choices=c,widget=forms.RadioSelect)
    subjects=forms.MultipleChoiceField(choices=s)
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':10,'rows':5}))


