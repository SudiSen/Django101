# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Choice, Question
from django.contrib.auth import *

def mark_close(modeladmin, request, queryset):
    queryset.update(question_text='Too Confusing to compare!')
mark_close.short_description = "Mark selected Questions as Close!"

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # inlines = [ChoiceInline]
    actions = [mark_close]
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#     actions = [highlight_question]

admin.site.register(Question)
admin.site.register(Choice)
