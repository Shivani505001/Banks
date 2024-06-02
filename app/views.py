from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.db import connection

# def test_db_connection(request):
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT 1")
#         return HttpResponse("Database connection is working!")
#     except Exception as e:
#         return HttpResponse(f"Error: {str(e)}")

#show list of banks 
#from django.http import JsonResponse
from rest_framework.response import Response
from .models import bank
from rest_framework.decorators import api_view
from .serializers import BankSerializer
from .serializers import BranchSerializer
from django.shortcuts import render, get_object_or_404

@api_view(['GET'])
def get_banks(request):
    #to get unique bank names 
    banks = bank.objects.exclude(bank_name__isnull=True).exclude(bank_name__exact='').values('bank_name').distinct() #exclude null values 
    seri = BankSerializer(banks,many=True)
    context = {'banks': seri.data}
    return render(request, 'banks.html', context)
    
#show list of branches of a bank

@api_view(['GET'])
def get_branches(request,bank_name):
    #print(f"Received bank_name: {bank_name}")  # Debug statement
    
    branches = bank.objects.filter(bank_name=bank_name)
    #print(f"Branches: {branches}")  # Print the queryset for debugging
    seri = BranchSerializer(branches, many=True)
    #print(f"Serialized Data: {seri.data}")  # Debug statement
    context = {'branches': seri.data}
    return render(request, 'branches.html', context)
    
@api_view(['GET'])
def get_branch_details(request,ifsc):
    
    branch = get_object_or_404(bank, ifsc=ifsc)
    seri = BranchSerializer(branch)
    context = {'branch': seri.data}
    return render(request, 'details.html', context)