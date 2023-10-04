from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View


class Criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')


class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')
