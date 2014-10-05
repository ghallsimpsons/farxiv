from django.conf.urls import patterns, include, url

from farxiv import views, builder

urlpatterns = [
        url(r'^$', views.Index.as_view(), name='index'),
        url(r'^submit$', views.SubmitFarticle.as_view(), name='submit'),
        url(r'^build$', 'farxiv.builder.farticle_builder_view', name='build'),
        ]
