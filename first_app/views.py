from django.shortcuts import render

from  . forms  import cotactForm,StudentData,PasswordValidationProject


# Create your views here.


def home(request):
    return render(request,('./first_app/home.html'))
def about(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render(request,('./first_app/about.html'),{'name':name,'email':email,'select':select})
    else:
         return render(request,('./first_app/about.html'))
    
    
    
def form(request):
    return render(request,('./first_app/form.html'))

def django_form(request):

    if request.method=='POST':
        form=cotactForm(request.POST,request.FILES)
   
        if form.is_valid():
        #  file=form.cleaned_data['file']
        #  with open('./first_app/upload/'+file.name,'wb+')as destination:
        #      for chunk in file.chunks():
        #          destination.write(chunk)

         print(form.cleaned_data)

    else:
        form=cotactForm()

    return render(request,('./first_app/django_form.html'),{'form':form})

def studentData(request):
    if request.method=='POST':
        form=StudentData(request.POST,request.FILES)
        if form.is_valid():
         print(form.cleaned_data)

    else:
        form=StudentData()

    return render(request,('./first_app/django_form.html'),{'form':form})
def passwordValidation(request):
    if request.method=='POST':
        form=PasswordValidationProject(request.POST)
        if form.is_valid():
         print(form.cleaned_data)

    else:
        form=PasswordValidationProject()

    return render(request,('./first_app/django_form.html'),{'form':form})
