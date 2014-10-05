from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from farxiv.forms import *

class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        print self.request.user.username
        context['user']=self.request.user
        return context
    
class SubmitFarticle(TemplateView):
    template_name = 'submit.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['form'] = FarticleForm(instance=self.request.user)
        return context

