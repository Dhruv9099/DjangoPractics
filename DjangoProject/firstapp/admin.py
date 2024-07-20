from django.contrib import admin
from .models import scriptingLang,ScriptLangReview, ScriptsStore,scriptCertificates


# Register your models here.
class ScriptReviewInline(admin.TabularInline):
    model = ScriptLangReview
    extra = 2


class ScriptVarietyAdmin(admin.ModelAdmin):
    list_display =('name','type','date_added')
    inlines =[ScriptReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display =('name','location')
    filter_horizontal =('script_varieties',)

class ScriptCertificateAdmin(admin.ModelAdmin):
    list_display =('script','certificate_number')



# add new class into it

# admin.site.register(scriptingLang)
# (modelclassname,adminclassname)
admin.site.register(scriptingLang,ScriptVarietyAdmin)
admin.site.register(ScriptsStore,StoreAdmin)
admin.site.register(scriptCertificates,ScriptCertificateAdmin)