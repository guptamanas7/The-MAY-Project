from django.shortcuts import render
import imp
from multiprocessing import context
from telnetlib import STATUS
from unicodedata import name
from django import shortcuts

from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import ListView
from django.http import FileResponse, Http404
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import re_path, reverse
from datetime import datetime
from datetime import timedelta
# from catalog.forms import RenewBookForm,NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .models import *

# def index(request):
#     num_employees = Employee.objects.count()
#     nums_visits=request.session.get('num_visit',0)
#     request.session['num_visit']=nums_visits+1
#     context = {
#         'num_books':num_employees,
#         'num_visit':nums_visits,
#     }
#     return render(request, 'index.html',context=context)
class EmployeeListView(ListView):
    paginate_by = 2
    model = Employee
