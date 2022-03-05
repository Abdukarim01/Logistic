from django.shortcuts import render,redirect
from .forms import QuoteModelForms,RegisterModelForms
from .bot import send_form_bot,send_form_bot_drivers
from .models import QuoteModel,Drivers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    added = False
    if request.method == 'POST':
        form = QuoteModelForms(request.POST)
        form.save(commit=False)
        if not QuoteModel.objects.filter(tel=request.POST.get('tel')):
            if form.is_valid():
                form.save(commit=True)
                send_form_bot('Quote',form.data.get('name'),form.data.get('email'),form.data.get('tel'),form.data.get('company_name'),form.data.get('mc'),form.data.get('dry_van'),form.data.get('reefer'),form.data.get('flat_bed'),form.data.get('message'),form.data.get('need_driver_assistence'))
                context = {
                "form": form,
                "success":True
                }
                return render(request, 'main/index.html', context)
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
                send_form_bot_drivers('Driver',form.data.get('first_name'),form.data.get('last_name'),form.data.get('email'),form.data.get('phone'),form.data.get('driver_license'),form.data.get('state'),form.data.get('driving_information'),form.data.get('how_many_years'),form.data.get('previus_employer'),form.data.get('which_position'))
                registred = True
                context = {
                "form":QuoteModelForms(),
                "success_register":registred
                }
                return render(request,'main/index.html',context)
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
