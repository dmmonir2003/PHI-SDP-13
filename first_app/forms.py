
from django import forms
from django.core import validators

class cotactForm(forms.Form):
      name=forms.CharField(label='full name',required=False,initial='md monir',widget=forms.Textarea)
      # file=forms.FileField()
      email=forms.EmailField(label='userEmail')
      # age=forms.IntegerField()
      # hight=forms.FloatField()
      age=forms.CharField(widget=forms.NumberInput)
      check=forms.BooleanField()
      balace=forms.DecimalField()
      birthday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
      appoontMent=forms.CharField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
      CHOICES=[('s','small'),('m','medeium'),('l','large')]
      # size=forms.ChoiceField(choices=CHOICES)
      size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
      meal=[('m','mashroom'),('c','chikan'),('f',('fish'))]

      chochoiseMeal=forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#       name=forms.CharField(widget=forms.TextInput)
#       email=forms.CharField(widget=forms.EmailInput)
      # def clean_name(self):
      #       nameVal=self.cleaned_data['name']
      #       if len(nameVal)<10:
      #             raise forms.ValidationError('name must be 10 chahrecter')
      #       return nameVal
      # def clean_email(self):
      #       emailVal=self.cleaned_data['email']
      #       if '.com' not in emailVal:
      #             raise forms.ValidationError('your email must be contain .com')
      #       return emailVal

      # def clean(self):
      #       cleaned_data=super().clean()
      #       nameVal=self.cleaned_data['name']
      #       emailVal=self.cleaned_data['email']
      #       if len(nameVal)<10:
      #             raise forms.ValidationError('name must be 10 chahrecter')

      #       if '.com' not in emailVal:
      #             raise forms.ValidationError('your email must be contain .com')
            

def castom_valided(value):
       if len(value)<10:
         raise forms.ValidationError('name must be 10 chahrecter')


class StudentData(forms.Form):
      name=forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(9,message='name must be 10 chahrecter')])
      email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='invalid email')])
      age=forms.IntegerField(validators=[validators.MinValueValidator(18,message='minimum value atlest 18'),validators.MaxValueValidator(60,message='maximum value 60 ')])

      text=forms.CharField(widget=forms.Textarea,validators=[castom_valided])

class PasswordValidationProject(forms.Form):
     name=forms.CharField(widget=forms.TextInput)
     password=forms.CharField(widget=forms.PasswordInput)
     confirm_password=forms.CharField(widget=forms.PasswordInput)

     def clean(self):
          cleaned_data=super().clean()
          val_pass=self.cleaned_data['password']
          val_con_pass=self.cleaned_data['confirm_password']
          if val_pass!=val_con_pass:
               raise forms.ValidationError("password doesn't metch")
