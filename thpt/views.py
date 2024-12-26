from django.core.cache import cache
from django.db.models import F
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DiemThiTHPT
from .serializers import DiemThiTHPTSerializer, DiemThiTHPTKhoiASerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class SearchStudentAPIView(APIView):
    def get(self, request, sbd):
        cache_key = f'student_{sbd}'
        student = cache.get(cache_key)

        if not student:
            try:
                student = DiemThiTHPT.objects.get(sbd=sbd)
                cache.set(cache_key, student, timeout=60 * 60)
            except DiemThiTHPT.DoesNotExist:
                return Response({'error': 'Không tồn tại thí sinh!'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DiemThiTHPTSerializer(student)
        return Response(serializer.data)


class StatisticsReportAPIView(APIView):
    def get(self, request):
        subjects = ['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc', 'lich_su', 'dia_li', 'gdcd']
        ranges = ['>=8', '8> && >=6', '6> && >=4', '<4']
        statistics = cache.get('statistics_report')

        if not statistics:
            statistics = {subject: {range_: 0 for range_ in ranges} for subject in subjects}

            for subject in subjects:
                statistics[subject]['>=8'] = DiemThiTHPT.objects.filter(**{subject + '__gte': 8}).count()
                statistics[subject]['8> && >=6'] = DiemThiTHPT.objects.filter(
                    **{subject + '__lt': 8, subject + '__gte': 6}).count()
                statistics[subject]['6> && >=4'] = DiemThiTHPT.objects.filter(
                    **{subject + '__lt': 6, subject + '__gte': 4}).count()
                statistics[subject]['<4'] = DiemThiTHPT.objects.filter(**{subject + '__lt': 4}).count()

            cache.set('statistics_report', statistics, timeout=60 * 60)

        return Response(statistics)


class TopStudentsAPIView(APIView):
    def get(self, request):
        top = int(request.query_params.get('top', 10))
        page = request.query_params.get('page', None)

        top_students = DiemThiTHPT.objects.annotate(
            total_score=F('toan') + F('vat_li') + F('hoa_hoc')
        ).order_by('-total_score')[:top]

        if page:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(top_students, request)
            serializer = DiemThiTHPTKhoiASerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = DiemThiTHPTKhoiASerializer(top_students, many=True)
            return Response(serializer.data)
