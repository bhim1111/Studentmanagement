from django.contrib import admin
from django.urls import path



from .views import DashboardView, StudentCreateView, StudentListView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),
    path('student-list/', StudentListView.as_view(), name='student-list'),
    path('student-create/', StudentCreateView.as_view(), name='student-create') ,
    path('student-update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'), 
    path('student-delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
]







