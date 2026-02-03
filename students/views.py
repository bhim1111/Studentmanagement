

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView

from students.models import Student


class DashboardView(TemplateView):
    template_name = 'students/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_students'] = Student.objects.count()
        context['active_students'] = Student.objects.filter().count()
        context['graduated_students'] = Student.objects.filter().count()
        return context
   
    
   

# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        return Student.objects.filter().order_by("name")
    
    
class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'image', 'age', 'course']
    template_name = 'students/student_form.html'
    success_url = '/student-create/'
    
    
class StudentUpdateView(CreateView):
    model = Student
    fields = ['name', 'image', 'age', 'course']
    template_name = 'students/student_update.html'
    success_url = reverse_lazy('student-list')
    

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_delete.html'
    success_url = reverse_lazy('student-list')
    
    

    
    

    





   
   
    
    
    
    
    
    
    
    
    

