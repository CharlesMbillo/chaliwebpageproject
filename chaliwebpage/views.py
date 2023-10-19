from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from reportlab.pdfgen import canvas
from chaliwebpage.forms import UserProfileForm

#from chaliwebpageproject.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
#from reportlab.lib.pagesizes import letter

# from django.views.generic.detail import DetailView
# from easy_pdf.views import PDFTemplateResponseMixin
@login_required

def some_protected_view(request):
    return render(request, 'protected_view.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            #LOGIN_REDIRECT_URL(request)
            return redirect('/chaliwebpage')
        else:
            error_message = 'Invalid credentials'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def UserProfile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
    # Redirect to a success page after submission
            return redirect('success')
    else:
        form = UserProfileForm()

    return render(request, 'userprofile.html', {'form': form})

#@login_required

#def UserProfile_list(request):
 #   UserProfile_list= UserProfile.objects.all()
  #  return render(request, 'chaliwebpage/userprofile_list.html',{'userprofiles=users'})

def success(request):
    return render(request, 'success.html')


def create_pdf():
    """Generates a PDF file for the given user."""

    pdf = canvas.Canvas('userprofileform.pdf')

    pdf.setFont('Helvetica', 12)
    pdf.drawString(10, 10, 'UserProfileForm Information')

    pdf.drawString(10, 20, 'First Name:')
    pdf.drawString(100, 20, UserProfileForm,'first_name')

    pdf.drawString(10, 30, 'Last Name:')
    pdf.drawString(100, 30, UserProfileForm,'last_name')

    pdf.drawString(10, 40, 'Phone Number:')
    pdf.drawString(100, 40, UserProfileForm,'phone_number')

    pdf.drawString(10, 50, 'Email:')
    pdf.drawString(100, 50, UserProfileForm,'email')

    pdf.save()

def create_user():
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            UserProfileForm= form.save()
            create_user()
            return HttpResponseRedirect('/chaliwebpage')
    else:
        form = UserProfileForm()

    return render(request, 'userprofile.html', {'form': form})

def logout():
    #LOGOUT_REDIRECT_URL(request)
    return redirect('/chaliwebpage')
