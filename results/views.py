import io
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Student, StudentClass, Subject, Result
from django.db.models import Avg, Sum, Count

class HomeView(TemplateView):
    template_name = 'results/home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'results/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_students'] = Student.objects.count()
        context['total_classes'] = StudentClass.objects.count()
        context['total_subjects'] = Subject.objects.count()
        context['recent_results'] = Result.objects.select_related('student', 'subject').order_by('-id')[:5]
        return context

# Student Views
class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'results/student_list.html'
    context_object_name = 'students'

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['roll_number', 'full_name', 'email', 'student_class']
    template_name = 'results/form.html'
    success_url = reverse_lazy('student_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add New Student"
        return context

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['roll_number', 'full_name', 'email', 'student_class']
    template_name = 'results/form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'results/confirm_delete.html'
    success_url = reverse_lazy('student_list')

# Result Views
class ResultListView(LoginRequiredMixin, ListView):
    model = Result
    template_name = 'results/result_list.html'
    context_object_name = 'results'

class ResultCreateView(LoginRequiredMixin, CreateView):
    model = Result
    fields = ['student', 'subject', 'marks_obtained']
    template_name = 'results/form.html'
    success_url = reverse_lazy('result_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Declare Result"
        return context

class ResultUpdateView(LoginRequiredMixin, UpdateView):
    model = Result
    fields = ['student', 'subject', 'marks_obtained']
    template_name = 'results/form.html'
    success_url = reverse_lazy('result_list')

class ResultDeleteView(LoginRequiredMixin, DeleteView):
    model = Result
    template_name = 'results/confirm_delete.html'
    success_url = reverse_lazy('result_list')

# Class & Subject Views
class StudentClassListView(LoginRequiredMixin, ListView):
    model = StudentClass
    template_name = 'results/class_list.html'

class StudentClassCreateView(LoginRequiredMixin, CreateView):
    model = StudentClass
    fields = ['class_name', 'section']
    template_name = 'results/form.html'
    success_url = reverse_lazy('class_list')

class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'results/subject_list.html'

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ['subject_code', 'subject_name']
    template_name = 'results/form.html'
    success_url = reverse_lazy('subject_list')

# Search & PDF
class StudentResultSearchView(View):
    def post(self, request):
        roll_number = request.POST.get('roll_number')
        student = get_object_or_404(Student, roll_number=roll_number)
        results = Result.objects.filter(student=student).select_related('subject')
        
        total_marks = results.aggregate(Sum('marks_obtained'))['marks_obtained__sum'] or 0
        subject_count = results.count()
        percentage = (total_marks / (subject_count * 100)) * 100 if subject_count > 0 else 0
        
        return render(request, 'results/report.html', {
            'student': student,
            'results': results,
            'total_marks': total_marks,
            'max_marks': subject_count * 100,
            'percentage': round(percentage, 2)
        })

class GeneratePDFReport(View):
    def get(self, request, roll_number):
        student = get_object_or_404(Student, roll_number=roll_number)
        results = Result.objects.filter(student=student).select_related('subject')
        
        total_marks = results.aggregate(Sum('marks_obtained'))['marks_obtained__sum'] or 0
        subject_count = results.count()
        percentage = (total_marks / (subject_count * 100)) * 100 if subject_count > 0 else 0
        
        context = {
            'student': student,
            'results': results,
            'total_marks': total_marks,
            'max_marks': subject_count * 100,
            'percentage': round(percentage, 2)
        }
        
        template = get_template('results/pdf_report.html')
        html = template.render(context)
        
        result = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
        
        if not pdf.err:
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            # Using a simplified filename to avoid header issues with non-ASCII or complex strings
            response['Content-Disposition'] = f'inline; filename="Report_{student.roll_number}.pdf"'
            return response
        return HttpResponse("Error generating PDF", status=400)
