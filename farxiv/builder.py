from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from farxiv.forms import *

@login_required
def farticle_builder_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        authors = request.POST['authors']
        summary = request.POST['summary']
        steps = request.POST['steps']
        problems = request.POST['problems']
        suggestions = request.POST['problems']
        images = request.POST['images']
        return render(request, 'view.html', {'farticle': farticle_id})
    else:
        return render(request, 'builder.html')
