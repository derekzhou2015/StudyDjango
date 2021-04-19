from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from .form import UploadSoundForm, ChoiceWordForm
from .models import Words, Category
from .handle import *
from django.contrib.admin import helpers
from django.contrib.messages import success
from random import sample
from json import dumps
# Create your views here.

INFO = Words._meta.app_label, Words._meta.model_name


def Choice(request):
    if request.method == 'GET':
        form = ChoiceWordForm()
        return render(request, 'dictation/choice.html', {'form': form})
    else:
        form = ChoiceWordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            d_c, d_l = data['category'], data['level']
            d_f, f_l = {}, []
            if len(d_c) > 0:
                d_f.update({'category__in': d_c})
            if len(d_l) > 0:
                d_f.update({'level__in': d_l})
            if len(d_f.items()) > 0:
                f_l = Words.objects.filter(**d_f)
            f_l = sample([word.as__dict() for word in f_l], len(f_l))

            context = {'results': f_l}
            return render(request, 'dictation/dictation.html', context)


def Upload_Sound(request, model, **kwargs):
    context = dict(
        model.admin_site.each_context(request),
        has_view_permission=model.has_view_permission(request),
        upload=True,
        opts=model.opts,
        verbose_name='Sound',
        title='Upload Sound',
        has_file_field=True
    )

    if request.method == 'GET':
        form1 = UploadSoundForm()
        context = dict(context, **dict(
            show_save=True,
            adminform=helpers.AdminForm(form1, list(
                [(None, {'fields': form1.base_fields})]), {})
        ))
    elif not 'c_l' in kwargs:
        form1 = UploadSoundForm(request.POST, request.FILES)
        if form1.is_valid():
            data = form1.cleaned_data
            result_headers = ('No.', 'Sound', 'Text')
            s_l = get_sound_list(data['sound'])
            context['results'] = s_l
            context['result_headers'] = result_headers
            context['c_l'] = '%s-%s' % (data['category'].id, data['level'])
            return TemplateResponse(request, 'admin/dictation/dict_upload_list.html', context)
    else:
        f_d = dict(request.POST)
        s_f = f_d['s_f']
        s_t = f_d['s_t']
        c_l = kwargs.get('c_l').split('-', 1)
        s_l = []
        for i in range(len(s_f)):
            obj = Words()
            obj.text = s_t[i]
            obj.sounds = s_f[i]
            obj.category_id = c_l[0]
            obj.level = c_l[1]
            s_l.append(obj)
        Words.objects.bulk_create(s_l)

        success(request, 'Successfully add %d Words.' % len(s_l))

        return redirect(reverse("admin:%s_%s_changelist" %
                                INFO))
    return TemplateResponse(request, 'admin/dictation/dict_upload_form.html', context)
