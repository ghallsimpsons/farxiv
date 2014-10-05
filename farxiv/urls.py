from django.conf.urls import patterns, include, url

from farxiv import views, builder

urlpatterns = [
        url(r'^$', views.Index.as_view(), name='index'),
        url(r'^submit$', views.SubmitFarticle.as_view(), name='submit'),
        url(r'^build$', 'farxiv.builder.farticle_builder_view', name='build'),
        url(r'^farticle/(?P<fid>\d+)$', views.ViewFarticle.as_view(), name='view'),
        url(r'^sample$', views.ViewExampleFarticle.as_view(), name='sample'),
        ]
