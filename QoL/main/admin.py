from django.contrib import admin
from .models import Third_Month_Survey, Baseline_Survey, Medical_Info, Albumin, Sodium, Alkaline_Phosphatase, Bicarbonate, Hemoglobin, BUN, Calcium, Creatinine, Phosphorus, Potassium, PTH, Dialysis, Comorbidities, Demography


@admin.register(Albumin)
class AlbuminAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(Alkaline_Phosphatase)
class Alkaline_PhosphataseAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(Bicarbonate)
class BicarbonateAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(BUN)
class BUNAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(Calcium)
class CalciumAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(Creatinine)
class CreatinineAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(Hemoglobin)
class HemoglobinAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(Phosphorus)
class PhosphorusAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(Potassium)
class PotassiumAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(PTH)
class PTHAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(Sodium)
class SodiumAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'value')


@admin.register(Dialysis)
class DialysisAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'weight', "pulse_rate",
                    'temperature', 'bp', 'kt_v_ratio', 'dialysis_duration')


@admin.register(Comorbidities)
class ComorbiditiesAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'diabetes',
                    'hypertension', 'cardiovascular_disease', 'typhoid')


@admin.register(Demography)
class DemographyAdmin(admin.ModelAdmin):
    list_display = ('user_ID', 'date_time', 'age', 'gender')


@admin.register(Medical_Info)
class Medical_InfoAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'ckd', 'first_dialysis_date',
                    'number_of_dialysis', 'expected_number_of_dialysis', 'dialysis_frequency')


@admin.register(Baseline_Survey)
class Baseline_SurveyAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'mobility', 'self_care',
                    'usual_activities', 'pain_level', 'anxiety_level', 'health_rating')


@admin.register(Third_Month_Survey)
class Third_Month_SurveyAdmin(admin.ModelAdmin):
    list_display = ('patient_ID', 'date_time', 'performance_status_score')
