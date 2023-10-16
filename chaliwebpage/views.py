from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
from .forms import UserProfileForm

# from django.views.generic.detail import DetailView
# from easy_pdf.views import PDFTemplateResponseMixin
@login_required
def UseProfile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page after submission
            return redirect('success')
        # redirect('pdf_generate')
    else:
        form = UserProfileForm()

    return render(request, 'user_profile.html', {'form': form})

@login_required

#def UserProfile_list(request):
 #   UserProfile= UserProfile.objects.all()
  #  return render(request, 'chaliwebpage/userprofile_list.html',{'userprofiles=users'})

def success(request):
    return render(request, 'success.html')


def create_pdf(UserProfile):
    """Generates a PDF file for the given user."""

    pdf = canvas.Canvas('user_data.pdf')

    pdf.drawString(10, 10, 'User Data')
    pdf.drawString(10, 20, f'First name: {UserProfile.first_name}')
    pdf.drawString(10, 30, f'Last name: {UserProfile.last_name}')
    pdf.drawString(10, 40, f'Phone number: {UserProfile.phone_number}')
    pdf.drawString(10, 50, f'Email: {UserProfile.email}')

    pdf.save()

    return HttpResponse(open('user_data.pdf', 'rb'), content_type='application/pdf')
