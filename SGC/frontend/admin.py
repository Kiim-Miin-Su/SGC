from django.contrib import admin
from .models import UsedInstrument, Job, CommunityPost, Lesson

admin.site.register(UsedInstrument)
admin.site.register(Job)
admin.site.register(CommunityPost)
admin.site.register(Lesson)
