from django.urls import path

from .views import SearchStudentAPIView, StatisticsReportAPIView, TopStudentsAPIView

urlpatterns = [
    path('search_student/<str:sbd>/', SearchStudentAPIView.as_view(), name='search_student'),
    path('statistics_report/', StatisticsReportAPIView.as_view(), name='statistics_report'),
    path('top_students/', TopStudentsAPIView.as_view(), name='top_students'),
]
