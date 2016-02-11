from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from usertemplates import models, forms


class TemplateEditorView(TemplateView):
    http_method_names = ['get', 'post', ]
    template_name = 'templateEditorView.html'

    def get(self, request, template_id=None, *args, **kwargs):
        context = self.get_context_data()
        context['page_title'] = 'Template Editor'

        if template_id is None:
            context['template_form'] = forms.TemplateForm()
        else:
            template = models.Template.objects.get(pk=template_id)
            context['template_form'] = forms.TemplateForm(instance=template)
            context['template_id'] = template_id
        return self.render_to_response(context=context)

    def post(self, request, template_id=None, *args, **kwargs):
        if template_id is None:
            form = forms.TemplateForm(request.POST)
        else:
            template = models.Template.objects.get(pk=template_id)
            form = forms.TemplateForm(request.POST,
                                      instance=template)
        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponse(content="Tudo certo...")
        else:
            return HttpResponse(content="Verifique os campos...")
