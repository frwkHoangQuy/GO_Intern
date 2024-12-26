from rest_framework import serializers

from .models import DiemThiTHPT


class DiemThiTHPTSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiemThiTHPT
        fields = '__all__'


class DiemThiTHPTKhoiASerializer(serializers.ModelSerializer):
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = DiemThiTHPT
        fields = ['sbd', 'toan', 'vat_li', 'hoa_hoc', 'total_score']

    def get_total_score(self, obj):
        return obj.toan + obj.vat_li + obj.hoa_hoc
