from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from.models import Type


class TypeList(ListView):
    model =Type
    context_object_name= 'type'

class TypeDetail(DetailView):
    model = Type
    context_object_name='type-detail'


