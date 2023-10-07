from django.contrib import admin

from .models import Question , Choice

# Register your models here.

admin.site.site_header = 'Polls Admin'
admin.site.site_title = 'Polss Admin Area'
admin.site.index_title = 'Welcome to the Polls Admin area'

class ChoicesInline(admin.TabularInline):
    model = Choice
    extra = 3
    
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
                 ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoicesInline]
    
admin.site.register(Question , QuestionAdmin)