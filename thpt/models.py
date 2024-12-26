from django.db import models


class DiemThiTHPT(models.Model):
    sbd = models.IntegerField(null=False, primary_key=True)
    toan = models.FloatField(null=True, blank=True)
    ngu_van = models.FloatField(null=True, blank=True)
    ngoai_ngu = models.FloatField(null=True, blank=True)
    vat_li = models.FloatField(null=True, blank=True)
    hoa_hoc = models.FloatField(null=True, blank=True)
    sinh_hoc = models.FloatField(null=True, blank=True)
    lich_su = models.FloatField(null=True, blank=True)
    dia_li = models.FloatField(null=True, blank=True)
    gdcd = models.FloatField(null=True, blank=True)
    ma_ngoai_ngu = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['sbd']), ]

    def __str__(self):
        return self.sbd
