#from django.shortcuts import render

# chaliwebpage/views.py
from django.shortcuts import render, reverse, redirect
from .forms import UserProfileForm
#from django.views.generic.detail import DetailView
#from easy_pdf.views import PDFTemplateResponseMixin

def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('success'))  # Redirect to a success page after submission
    else:
        form = UserProfileForm()

    return render(request, 'user_profile.html', {'form': form})

def success(request):
    return render(request, 'success.html')