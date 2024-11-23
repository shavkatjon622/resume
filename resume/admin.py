from django.contrib import admin
from resume.models import Profile, Social, Info, Language, \
    LatestProject, Experience, Skill, Education

# Register your models here.

admin.site.register(Profile)
admin.site.register(Social)
admin.site.register(Info)
admin.site.register(Language)
admin.site.register(LatestProject)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Education)