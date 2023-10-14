#create views for displaying the form and generating the PDF
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml12pdf import pisa
from .forms import UserProfileForm
#from django.views.generic.detail import DetailView
#from easy_pdf.views import PDFTemplateResponseMixin

def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('success'))  # Redirect to a success page after submission
        redirect('pdf_generate')
    else:
        form = UserProfileForm()

    return render(request, 'user_profile.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def generate_pdf(request)
    user_profile=UserProfileForm.objects.last()     # Get the latest user input
    template_path= 'pdf_template.html'
    context = {'user_profile':user_profile}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='filename="User_Profile.pdf"'

    template = get_template(template_path)
    html=template.render(context)

    # Create a PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def user_profile_url():
    return reverse('user_profile')

    