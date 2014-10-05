from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from farxiv.forms import *
import json

@login_required
def farticle_builder_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        authors = request.POST['authors']
        summary = request.POST['summary']
        data = json.load(request.POST['data'])
        steps = data.steps
        problems = data.problems
        suggestions = data.suggestions
        images = data.images
        links = data.links
        for link in links:
            # Link the lists and images in the DB
            pass
        return render(request, 'view.html', {'farticle': farticle_id})
    else:
        return render(request, 'builder.html')
