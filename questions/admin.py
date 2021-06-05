from django.contrib import admin
from questions.models import Answer, Question

# Register your models here.

admin.site.register(Answer)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('content', 'author')

# admin.site.register(QuestionAdmin)
