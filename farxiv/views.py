from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from farxiv.forms import *

class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['user']=self.request.user
        return context
    
class SubmitFarticle(TemplateView):
    template_name = 'submit.html'
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['form'] = FarticleForm(instance=self.request.user)
        return context

class ViewFarticle(TemplateView):
    template_name='view.html'
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        farticle_id = self.kwargs['fid']
        farticle = Farticle.objects.get(id = farticle_id)
        context['author'] = farticle.author
        context['title'] = farticle.title
        if farticle.render_type=="quick":
            # Does this actually work? Doubt it...
            template_name='view.html'
            farticle = QuickFarticle.objects.get(id = farticle_id)
            context['steps'] = farticle.steps
            context['problems'] = farticle.problems
            context['suggestions'] = farticle.suggestions
            return context
        else:
            return context

class ViewExampleFarticle(TemplateView):
    template_name='farticle.html'
