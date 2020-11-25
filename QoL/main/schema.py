import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import *
import datetime


class AlbuminType(DjangoObjectType):
    class Meta:
        model = Albumin


class Alkaline_PhosphataseType(DjangoObjectType):
    class Meta:
        model = Alkaline_Phosphatase


class BicarbonateType(DjangoObjectType):
    class Meta:
        model = Bicarbonate


class BUNType(DjangoObjectType):
    class Meta:
        model = BUN


class CalciumType(DjangoObjectType):
    class Meta:
        model = Calcium


class CreatinineType(DjangoObjectType):
    class Meta:
        model = Creatinine


class HemoglobinType(DjangoObjectType):
    class Meta:
        model = Hemoglobin


class PhosphorusType(DjangoObjectType):
    class Meta:
        model = Phosphorus


class PotassiumType(DjangoObjectType):
    class Meta:
        model = Potassium


class PTHType(DjangoObjectType):
    class Meta:
        model = PTH


class SodiumType(DjangoObjectType):
    class Meta:
        model = Sodium


class DialysisType(DjangoObjectType):
    class Meta:
        model = Dialysis


class ComorbiditiesType(DjangoObjectType):
    class Meta:
        model = Comorbidities


class Medical_InfoType(DjangoObjectType):
    class Meta:
        model = Medical_Info


class Baseline_SurveyType(DjangoObjectType):
    class Meta:
        model = Baseline_Survey


def transferJSTime(s):
    t = None
    t = datetime.datetime.fromtimestamp(int(s) / 1000.0)
    print(t)
    return t


class Query(ObjectType):
    # _Albumin = graphene.Field(AlbuminType, id=graphene.Int())
    _Baseline_Survey = graphene.List(
        Baseline_SurveyType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Baseline_Survey(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        # start = transferJSTime(kwargs.get('start'))
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            print("####")
            print(end)
            return Baseline_Survey.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:

            return Baseline_Survey.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Baseline_Survey.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Baseline_Survey.objects.filter(patient_ID=patient_ID)
        return None

    _Medical_Info = graphene.List(
        Medical_InfoType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Medical_Info(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        # start = transferJSTime(kwargs.get('start'))
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            print("####")
            print(end)
            return Medical_Info.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:

            return Medical_Info.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Medical_Info.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Medical_Info.objects.filter(patient_ID=patient_ID)
        return None

    _Comorbidities = graphene.List(
        ComorbiditiesType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Comorbidities(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        # start = transferJSTime(kwargs.get('start'))
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            print("####")
            print(end)
            return Comorbidities.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:

            return Comorbidities.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Comorbidities.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Comorbidities.objects.filter(patient_ID=patient_ID)
        return None

    _Dialysis = graphene.List(
        DialysisType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Dialysis(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        # start = transferJSTime(kwargs.get('start'))
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            print("####")
            print(end)
            return Dialysis.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:

            return Dialysis.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Dialysis.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Dialysis.objects.filter(patient_ID=patient_ID)
        return None

    _Albumin = graphene.List(
        AlbuminType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Albumin(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        # start = transferJSTime(kwargs.get('start'))
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            print("####")
            print(end)
            return Albumin.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:

            return Albumin.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Albumin.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Albumin.objects.filter(patient_ID=patient_ID)
        return None

    _Alkaline_Phosphatase = graphene.List(
        Alkaline_PhosphataseType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Alkaline_Phosphatase(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            return Alkaline_Phosphatase.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:
            print(123)
            return Alkaline_Phosphatase.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Alkaline_Phosphatase.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Alkaline_Phosphatase.objects.filter(patient_ID=patient_ID)
        return None
    _Bicarbonate = graphene.List(
        BicarbonateType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Bicarbonate(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            return Bicarbonate.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:
            print(123)
            return Bicarbonate.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Bicarbonate.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Bicarbonate.objects.filter(patient_ID=patient_ID)
        return None

    _B_U_N = graphene.List(
        BUNType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__B_U_N(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            return BUN.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:
            print(123)
            return BUN.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return BUN.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return BUN.objects.filter(patient_ID=patient_ID)
        return None

    _Calcium = graphene.List(
        CalciumType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Calcium(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            return Calcium.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:
            print(123)
            return Calcium.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Calcium.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Calcium.objects.filter(patient_ID=patient_ID)
        return None

    _Creatinine = graphene.List(
        CreatinineType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Creatinine(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            return Creatinine.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:
            print(123)
            return Creatinine.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Creatinine.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Creatinine.objects.filter(patient_ID=patient_ID)
        return None

    _Hemoglobin = graphene.List(
        HemoglobinType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Hemoglobin(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            return Hemoglobin.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:
            print(123)
            return Hemoglobin.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Hemoglobin.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Hemoglobin.objects.filter(patient_ID=patient_ID)
        return None

    _Phosphorus = graphene.List(
        PhosphorusType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Phosphorus(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            return Phosphorus.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:
            print(123)
            return Phosphorus.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Phosphorus.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Phosphorus.objects.filter(patient_ID=patient_ID)
        return None

    _Potassium = graphene.List(
        PotassiumType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Potassium(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            return Potassium.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:
            print(123)
            return Potassium.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Potassium.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Potassium.objects.filter(patient_ID=patient_ID)
        return None

    _P_T_H = graphene.List(
        PTHType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__P_T_H(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            return PTH.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:
            print(123)
            return PTH.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return PTH.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return PTH.objects.filter(patient_ID=patient_ID)
        return None

    _Sodium = graphene.List(
        SodiumType, patient_ID=graphene.String(), start=graphene.String(required=False), end=graphene.String(required=False))

    def resolve__Sodium(self, info, **kwargs):
        patient_ID = kwargs.get('patient_ID')
        end, start = None, None

        if kwargs.get('start'):
            start = transferJSTime(kwargs.get('start'))
        if kwargs.get('end'):
            end = transferJSTime(kwargs.get('end'))
        if patient_ID and start and end:
            return Sodium.objects.filter(patient_ID=patient_ID, date_time__gt=start, date_time__lt=end)
        if patient_ID and start:
            print(123)
            return Sodium.objects.filter(patient_ID=patient_ID, date_time__gt=start)
        if patient_ID and end:
            return Sodium.objects.filter(patient_ID=patient_ID, date_time__lt=end)

        if patient_ID:
            return Sodium.objects.filter(patient_ID=patient_ID)
        return None


# class CreateAddress(graphene.Mutation):
# class Mutation(graphene.ObjectType):
#     pass
schema = graphene.Schema(query=Query)
