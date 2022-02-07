from django.shortcuts import render,redirect
from .forms import QuoteModelForms
from .bot import send_form_bot
from .models import QuoteModel
# Create your views here.

def home(request):
    added = False
    if request.method == 'POST':
        form = QuoteModelForms(request.POST)
        form.save(commit=False)
        if not QuoteModel.objects.filter(tel=request.POST.get('tel')):
            if form.is_valid():
                form.save(commit=True)
                send_form_bot(request.POST.get('name'),request.POST.get('email'),request.POST.get('tel'),request.POST.get('company_name'),request.POST.get('mc'),request.POST.get('dry_van'),request.POST.get('reefer'),request.POST.get('flat_bed'),request.POST.get('message'),request.POST.get('need_driver_assistence'))
                return redirect("/")
            else:
                pass
        else:
            added = True
            context = {
                "form": form,
                "added": added
            }
            return render(request, 'main/index.html', context)
    else:
        form = QuoteModelForms()
    context = {
        "form":form,
        "added":added
    }
    return render(request,'main/index.html',context)


