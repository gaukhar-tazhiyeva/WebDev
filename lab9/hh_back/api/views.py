from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Company, Vacancy

# Create your views here.

def index(request):
    return render(request, 'api/index.html', locals() )

def all_companies(request):
    try:
        comp = Company.objects.all()
    except:
        return HttpResponse("No companies yet")

    
    return JsonResponse([i.to_json() for i in comp], safe=False)

def all_vacancies(request):
    try:
        vac = Vacancy.objects.all()
    except:
        return HttpResponse("No vacancies yet")

   
    return JsonResponse([i.to_json() for i in vac], safe=False)

def a_company(request,id):
    try:
        comp = Company.objects.get(id=id)
    except:
        return HttpResponse("No info about a company")

   
    return JsonResponse(comp.to_json())

def a_vacancy(request,id):
    try:
        vac = Vacancy.objects.get(id=id)
    except:
        return HttpResponse("No info about a vacancy")

   
    return JsonResponse(vac.to_json())

def get_vacancies(request, id):
    try:
        vac = Vacancy.objects.filter(company=id)
    except:
        return HttpResponse('Company has no vacancies yet')

    
    return JsonResponse([i.to_json() for i in vac], safe=False)

def top_ten(request):
    vac = Vacancy.objects.order_by('-salary')

    return JsonResponse([i.to_json() for i in vac], safe=False)