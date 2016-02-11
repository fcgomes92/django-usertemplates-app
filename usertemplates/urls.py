from django.conf.urls import url
from usertemplates import views

urlpatterns = [
    url('editor/$', views.TemplateEditorView.as_view(),
        name='template_editor_view'),
    url('editor/(?P<template_id>[0-9]+)/$', views.TemplateEditorView.as_view(),
        name='template_editor_view_id'),
]
