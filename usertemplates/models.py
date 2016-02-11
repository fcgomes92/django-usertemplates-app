from django.db import models
from django.utils import timezone
from django.template import Context as DjangoContext
from django.template import Template as DjangoTemplate
from usertemplates import config


class Render(models.Model):
    '''
    Class to represent all the redenred templates that a user can make.
    Related to:
    * Template
    * Custom model (Custom)
    '''

    __slots__ = ['full_text', 'file_type', 'created', 'updated', 'template', ]

    full_text = models.TextField(null=False, blank=True, default="")
    file_type = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(null=False, blank=False)
    updated = models.DateTimeField(null=False, blank=False)
    template = models.ForeignKey('Template', on_delete=models.CASCADE,
                                 null=False, blank=False)

    class Meta:
        app_label = config.APP_LABEL
        db_tablespace = config.TABLESPACE
        db_table = config.TABLE_RENDER

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Render, self).save(*args, **kwargs)


class Template(models.Model):
    '''
    Class to represent all the templates a user can create.
    Related to:
    * Render
    * Creator (Custom)
    '''

    __slots__ = ['html', 'created', 'updated', ]

    html = models.TextField(null=False, blank=True, default="")
    created = models.DateTimeField(null=False, blank=False)
    updated = models.DateTimeField(null=False, blank=False)

    def render_template(self, context={}, file_type='pdf'):
        t = DjangoTemplate(template_string=self.html)
        c = DjangoContext(context)
        rendered = t.render(c)
        Render.objects.update_or_create(full_text=rendered,
                                        file_type=file_type,
                                        template=self)
        return rendered

    class Meta:
        app_label = config.APP_LABEL
        db_tablespace = config.TABLESPACE
        db_table = config.TABLE_TEMPLATE

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Template, self).save(*args, **kwargs)
