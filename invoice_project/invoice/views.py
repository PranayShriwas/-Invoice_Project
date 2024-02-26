# invoice/views.py
from django.shortcuts import render, redirect
from .forms import UserDetailsForm, InvoiceDetailsForm
from .models import UserDetails, InvoiceDetails

def create_invoice(request):
    user_form = UserDetailsForm(request.POST or None)
    invoice_form = InvoiceDetailsForm(request.POST or None)
    if request.method == 'POST':
        if user_form.is_valid() and invoice_form.is_valid():
            user = user_form.save()
            invoice = invoice_form.save(commit=False)
            invoice.user = user
            invoice.save()
            return redirect('invoice:invoice_detail')
    return render(request, 'create_invoice.html', {'user_form': user_form, 'invoice_form': invoice_form})

def invoice_detail(request):
    invoices = InvoiceDetails.objects.all()
    return render(request, 'invoice_detail.html', {'invoices': invoices})
