

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

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
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(name__icontains=query).order_by("name")
        return Student.objects.all().order_by("name")
    
    
class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    fields = ['name', 'image', 'age', 'course']
    template_name = 'students/student_form.html'
    success_url = '/student-create/'
    success_message = "Student created successfully!"
    
    def form_invalid(self, form):
        messages.error(self.request, "Failed to create student. Please correct the errors below.")
        return super().form_invalid(form)


class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    fields = ['name', 'image', 'age', 'course']
    template_name = 'students/student_update.html'
    success_url = reverse_lazy('student-list')
    success_message = "Student updated successfully!"
    
    def form_invalid(self, form):
        messages.error(self.request, "Failed to update student. Please correct the errors below.")
        return super().form_invalid(form)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_delete.html'
    success_url = reverse_lazy('student-list')
    
    def form_valid(self, form):
        messages.success(self.request, "Student deleted successfully!")
        return super().form_valid(form)
    
    

    
    

    





   
   
    
    
    
    
    
    
    
    
    

