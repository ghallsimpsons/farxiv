from django.forms import ModelForm
from farxiv.models import *

class FarticleForm(ModelForm):
    class Meta:
        def __init__(self, user, *args, **kwargs):
            self.author = user
            super(FarticleForm, self).__init__(*args, **kwargs)
        model = Farticle
        fields = ['topic', 'title', 'farticle', 'failure_reasons', 'keywords']
        
