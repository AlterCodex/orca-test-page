from django import forms
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from landingJobsPage.forms import WorkingContactForm
from landingJobsPage.models import JobPosting


def index(request):
    return render(request, 'landingJobsPage/index.html', {})


def carers(request):
    jobs_post = list(JobPosting.objects.all())
    template = loader.get_template('landingJobsPage/carers.html')
    context = {
        'jobs_post': jobs_post,
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def jobDetail(request, job_id):
    job = JobPosting.objects.filter(id=job_id).first()
    if request.method == "POST":
        form = WorkingContactForm(request.POST)
        if form.is_valid():
            send_mail(
                'found a lead in ' + request.POST.get('user_name'),
                'is an application for: ' + job.tittle + "by " + request.POST.get('user_name')
                + " contact Info" + request.POST.get(
                    "mail"),
                'recluting@orca-test.com',
                ['francisco.beltran@orca-test.com'],
                fail_silently=False,
            )
            response = redirect('/index/')
            return response
    else:
        form = WorkingContactForm()
    template = loader.get_template('landingJobsPage/detail-job.html')
    rendered_form = form.render()
    context = {
        'job': job,
        'apply_form': rendered_form
    }
    return HttpResponse(template.render(context, request))
