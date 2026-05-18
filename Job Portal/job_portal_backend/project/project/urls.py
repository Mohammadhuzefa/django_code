from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import (
    RegisterEmployeeView, 
    LoginView, 
    get_jobs, 
    apply_job, 
    my_applications, 
    add_job, 
    all_applications, 
    update_app_status
)

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import (
    RegisterEmployeeView, 
    LoginView, 
    get_jobs, 
    job_detail,     # <--- Naya function jo Edit/Delete handle karega
    apply_job, 
    my_applications, 
    add_job, 
    all_applications, 
    update_app_status
)

urlpatterns = [
    # --- Django Admin Panel ---
    path('admin/', admin.site.urls), 
    
    # --- Auth Endpoints ---
    path('api/register/', RegisterEmployeeView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),

    # --- User Endpoints ---
    path('api/jobs/', get_jobs, name='get_jobs'),
    path('api/apply/<int:job_id>/', apply_job, name='apply_job'),
    path('api/my-applications/', my_applications, name='my_applications'),

    # --- Admin Endpoints ---
    path('api/add-job/', add_job, name='add_job'),
    
    # Sabse Important: Edit aur Delete isi path se chalenge
    # Isme <int:pk> wahi ID hai jo React se 'editingJob.id' ban kar aayegi
    path('api/jobs/<int:pk>/', job_detail, name='job_detail'), 
    
    path('api/all-apps/', all_applications, name='all_applications'),
    path('api/app-status/<int:pk>/', update_app_status, name='update_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# --- Media & Static Files Setup ---
# Iske bina uploaded resumes aur images React mein load nahi hongi
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)