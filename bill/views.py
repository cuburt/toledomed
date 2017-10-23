from django.shortcuts import render,redirect
from django.shortcuts import *
from bill.models import *
from calendarium.models import *
from .forms import *
from django.template.loader import get_template
from calendarium.utils import render_to_pdf
# Create your views here.
def index(request, identity_id):
    billing_form = BillingForm(request.POST or None)
    id_info = Identity_Information.objects.get(pk=identity_id)
    try:
        if billing_form.is_valid():
                a = billing_form.save(commit=False)
                a.identity = id_info
                a.recieved_from = str(id_info.First_Name)+" "+str(id_info.Mid_Name)+" "+str(id_info.Last_Name)
                sum = int(request.POST['sum'])
                a.total_sales_vat_inclusive = sum
                less_vat = sum*.12
                a.less_vat = less_vat
                a.total = sum - less_vat
                a.amount_due = sum - less_vat
                a.vat_amount = less_vat
                a.total_sales = sum
                a.save()
                return redirect('/billing/view_bill/user='+str(identity_id)+'/')
    except:
        pass

    return render(request, 'bill/billing_form.html', {'form': billing_form,
                                                      'id_info':id_info    })



def generate_bill(request, identity_id, *args, **kwargs):
    profiles = Identity_Information.objects.filter(pk = identity_id)
    id_info = Identity_Information.objects.get(pk=identity_id)
    bill_info = bill.objects.filter(identity = id_info.id)
    template = get_template('bill/bill_pdf.html')
    context = {'profiles': profiles, 'bill_info':bill_info}
    html = template.render(context)
    pdf = render_to_pdf('bill/bill_pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Bill_%s.pdf" % (id_info.Last_Name)
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")
