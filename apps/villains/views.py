from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
class Villains(View):
	attack = -5
	pass

class Kur(Villains, View):
	attack = -20
