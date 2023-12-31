from django.contrib import admin
from .models import *


class pradeepAdmin(admin.ModelAdmin):
    list = []


admin.site.register(Personaldetailsmodels, pradeepAdmin)
admin.site.register(SkillsModel)
admin.site.register(EducationModel)
admin.site.register(CertificationModel)
admin.site.register(ExperienceModel)
admin.site.register(SocialModel)
admin.site.register(GmailModel, admin.ModelAdmin)
admin.site.register(UploadedFile, admin.ModelAdmin)
