from django.db import models

# clinical data.


class Albumin(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:

        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Albumin"
        verbose_name = 'Albumin'
        verbose_name_plural = 'Albumin'


class Alkaline_Phosphatase(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Alkaline_Phosphatase"
        verbose_name = 'Alkaline_Phosphatase'
        verbose_name_plural = 'Alkaline_Phosphatase'


class Bicarbonate(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Bicarbonate"
        verbose_name = 'Bicarbonate'
        verbose_name_plural = 'Bicarbonate'


class BUN(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "BUN"
        verbose_name = 'BUN'
        verbose_name_plural = 'BUN'


class Calcium(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Calcium"
        verbose_name = 'Calcium'
        verbose_name_plural = 'Calcium'


class Creatinine(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Creatinine"
        verbose_name = 'Creatinine'
        verbose_name_plural = 'Creatinine'


class Hemoglobin(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Hemoglobin"
        verbose_name = 'Hemoglobin'
        verbose_name_plural = 'Hemoglobin'


class Phosphorus(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Phosphorus"
        verbose_name = 'Phosphorus'
        verbose_name_plural = 'Phosphorus'


class Potassium(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Potassium"
        verbose_name = 'Potassium'
        verbose_name_plural = 'Potassium'


class PTH(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "PTH"
        verbose_name = 'PTH'
        verbose_name_plural = 'PTH'


class Sodium(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    value = models.FloatField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Sodium"
        verbose_name = 'Sodium'
        verbose_name_plural = 'Sodium'

# dialysis data


class Dialysis(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    weight = models.FloatField()
    temperature = models.FloatField(null=True)
    bp = models.CharField(max_length=6)
    pulse_rate = models.IntegerField(null=True)
    kt_v_ratio = models.FloatField(null=True)
    dialysis_duration = models.DecimalField(
        max_digits=3, decimal_places=2, null=True)

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Dialysis"
        verbose_name = 'Dialysis'
        verbose_name_plural = 'Dialysis'

# comorbidities data


class Comorbidities(models.Model):
    patient_ID = models.CharField(max_length=6)
    date_time = models.DateTimeField(auto_now_add=False)
    diabetes = models.BooleanField()
    hypertension = models.BooleanField()
    cardiovascular_disease = models.BooleanField()
    typhoid = models.BooleanField()

    class Meta:
        ordering = ['-date_time']
        unique_together = (('patient_ID', 'date_time'),)
        db_table = "Comorbidities"
        verbose_name = 'Comorbidities'
        verbose_name_plural = 'Comorbidities'

# demographic data


class Demography(models.Model):
    user_ID = models.CharField(max_length=6, primary_key=True)
    date_time = models.DateTimeField(auto_now_add=False)
    age = models.IntegerField()
    choice = (('M', 'M'), ('F', 'F'))
    gender = models.CharField(max_length=1, choices=choice)

    class Meta:
        ordering = ['-date_time']
        db_table = "Demography"
        verbose_name = 'Demography'
        verbose_name_plural = 'Demography'


class Medical_Info(models.Model):
    patient_ID = models.CharField(max_length=6, primary_key=True)
    date_time = models.DateTimeField(auto_now_add=False)
    ckd = models.IntegerField(null=True)
    first_dialysis_date = models.DateTimeField(auto_now_add=False, null=True)
    number_of_dialysis = models.IntegerField(null=True)
    expected_number_of_dialysis = models.IntegerField(null=True)
    dialysis_frequency = models.IntegerField(null=True)

    class Meta:
        ordering = ['-date_time']
        db_table = "Medical_Info"
        verbose_name = 'Medical_Info'
        verbose_name_plural = 'Medical_Info'


class Baseline_Survey(models.Model):
    patient_ID = models.CharField(max_length=6, primary_key=True)
    date_time = models.DateTimeField(auto_now_add=False)
    mobility = models.IntegerField(null=True)
    self_care = models.IntegerField(null=True)
    usual_activities = models.IntegerField(null=True)
    pain_level = models.IntegerField(null=True)
    anxiety_level = models.IntegerField(null=True)
    health_rating = models.IntegerField(null=True)

    class Meta:
        ordering = ['-date_time']
        db_table = "Baseline_Survey"
        verbose_name = "Baseline_Survey"
        verbose_name_plural = "Baseline_Survey"


class Third_Month_Survey(models.Model):
    patient_ID = models.CharField(max_length=6, primary_key=True)
    date_time = models.DateTimeField(auto_now_add=False)
    performance_status_score = models.IntegerField(null=True)

    class Meta:
        ordering = ['-date_time']
        db_table = "Third_Month_Survey"
        verbose_name = "Third_Month_Survey"
        verbose_name_plural = "Third_Month_Survey"
