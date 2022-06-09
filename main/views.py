from django.shortcuts import render
from .forms import QuoteModelForms,RegisterModelForms
from .bot import send_form_bot,send_form_bot_drivers
from .models import QuoteModel,Drivers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    data = {}
    if request.method == 'POST':
        form = QuoteModelForms(request.POST)
        form.save(commit=False)
        try:
            if form.is_valid():
                form.save(commit=True)
                send_form_bot('Quote',form.data.get('name'),form.data.get('email'),form.data.get('tel'),form.data.get('company_name'),form.data.get('mc'),form.data.get('dry_van'),form.data.get('reefer'),form.data.get('flat_bed'),form.data.get('message'),form.data.get('need_driver_assistence'))
                data['status'] = 200
                return JsonResponse(data)
            else:
                pass
        except:
            data['status'] = 100
            return JsonResponse(data)
    else:
        form = QuoteModelForms()
    context = {
        "form":form
    }
    return render(request,'main/index.html',context)

@csrf_exempt
def register(request):
    data = {}
    if request.method == "POST":
        form = RegisterModelForms(request.POST)
        form.save(commit=False)
        try:
            if form.is_valid():
                data['status'] = 200
                form.save(commit=True)
                send_form_bot_drivers('Driver',form.data.get('first_name'),form.data.get('last_name'),form.data.get('email'),form.data.get('phone'),form.data.get('driver_license'),form.data.get('state'),form.data.get('driving_information'),form.data.get('how_many_years'),form.data.get('previus_employer'),form.data.get('which_position'))
                return JsonResponse(data)
            else:
                pass
        except:
            data['status'] = 100
            return JsonResponse(data)
    else:   
        form = RegisterModelForms()   

    context = {
            "form":form
    }

    return render(request,'register/register.html',context)
