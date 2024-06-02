from rest_framework.serializers import ModelSerializer
from .models import bank

class BankSerializer(ModelSerializer):
    class Meta:
        model = bank
        fields = ['bank_name']
class BranchSerializer(ModelSerializer):
    class Meta:
        model = bank
        fields = ['ifsc', 'branch', 'address', 'city', 'district', 'state', 'bank_name']



