from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    
    # Students
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    
    # Results
    path('results/', views.ResultListView.as_view(), name='result_list'),
    path('results/add/', views.ResultCreateView.as_view(), name='result_add'),
    path('results/<int:pk>/edit/', views.ResultUpdateView.as_view(), name='result_edit'),
    path('results/<int:pk>/delete/', views.ResultDeleteView.as_view(), name='result_delete'),
    
    # Classes & Subjects
    path('classes/', views.StudentClassListView.as_view(), name='class_list'),
    path('classes/add/', views.StudentClassCreateView.as_view(), name='class_add'),
    path('classes/<int:pk>/edit/', views.StudentClassUpdateView.as_view(), name='class_edit'),
    path('classes/<int:pk>/delete/', views.StudentClassDeleteView.as_view(), name='class_delete'),
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/add/', views.SubjectCreateView.as_view(), name='subject_add'),
    path('subjects/<int:pk>/edit/', views.SubjectUpdateView.as_view(), name='subject_edit'),
    path('subjects/<int:pk>/delete/', views.SubjectDeleteView.as_view(), name='subject_delete'),
    
    # Search and PDF
    path('search/', views.StudentResultSearchView.as_view(), name='student_search'),
    path('report/<str:roll_number>/', views.GeneratePDFReport.as_view(), name='generate_report'),
]
