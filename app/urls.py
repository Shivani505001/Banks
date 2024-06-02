from django.urls import path
#from .views import test_db_connection
from . import views


urlpatterns = [
    #path('test/', test_db_connection),
    path('banks/',views.get_banks,name='get_banks'),
    path('banks/<str:bank_name>/', views.get_branches, name='get_branches'),
    path('branch/<str:ifsc>/', views.get_branch_details, name='get_branch_details'),
]
