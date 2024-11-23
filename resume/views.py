from django.shortcuts import render
from .models import Profile, Social, Info, Language, LatestProject, \
    Experience, Skill, Education
from django.http import HttpResponse
# Create your views here.



def index(request):
    profile = Profile.objects.all()
    profile = profile[::-1]
    socials = Social.objects.all()
    info = Info.objects.all()
    languages = Language.objects.all()
    latest_projects = LatestProject.objects.all()
    latest_projects = latest_projects[::-1]
    experiences = Experience.objects.all()
    skills = Skill.objects.filter(type__contains='KS')
    additional_skills = Skill.objects.filter(type__contains='AS')
    educations = Education.objects.all()
    context = {
        'profile': profile[0],
        'socials': socials,
        'info': info,
        'languages': languages,
        'latest_projects': latest_projects[:6],
        'experiences': experiences,
        'skills': skills,
        'additional_skills': additional_skills,
        'educations': educations,
    }
    return render(request, 'index.html', context=context)