from django.shortcuts import render,redirect
from .forms import QuoteModelForms,RegisterModelForms
from .bot import send_form_bot,send_form_bot_drivers
from .models import QuoteModel,Drivers
# Create your views here.

def home(request):
    added = False
    if request.method == 'POST':
        form = QuoteModelForms(request.POST)
        form.save(commit=False)
        if not QuoteModel.objects.filter(tel=request.POST.get('tel')):
            if form.is_valid():
                form.save(commit=True)
                send_form_bot('Quote',request.POST.get('name'),request.POST.get('email'),request.POST.get('tel'),request.POST.get('company_name'),request.POST.get('mc'),request.POST.get('dry_van'),request.POST.get('reefer'),request.POST.get('flat_bed'),request.POST.get('message'),request.POST.get('need_driver_assistence'))
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


def register(request):
    registred = False
    if request.method == "POST":
        form = RegisterModelForms(request.POST)
        form.save(commit=False)
        if not Drivers.objects.filter(phone=request.POST.get('phone')):
            if form.is_valid():
                form.save(commit=True)
                send_form_bot_drivers('Driver',request.POST.get('first_name'),request.POST.get('last_name'),request.POST.get('email'),request.POST.get('phone'),request.POST.get('driver_license'),request.POST.get('state'),request.POST.get('driving_information'),request.POST.get('how_many_years'),request.POST.get('previus_employer'),request.POST.get('which_position'))
                return redirect("/")
            else:
                pass
        else:
            registred = True
            context = {
            "form":form,
            "registred":registred
            }

            return render(request,'register/register.html',context)
    else:   
        form = RegisterModelForms()   

    context = {
            "form":form
    }

    return render(request,'register/register.html',context)