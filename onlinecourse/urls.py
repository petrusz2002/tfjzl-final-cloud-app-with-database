from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # 🔹 Főoldal (course lista)
    path('', views.CourseListView.as_view(), name='index'),

    # 🔹 Auth
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    # 🔹 Course részletek
    # ex: /onlinecourse/5/
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),

    # 🔹 Beiratkozás
    # ex: /onlinecourse/5/enroll/
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # ✅ Vizsga beküldés (HIÁNYZOTT)
    # ex: /onlinecourse/submit/5/
    path('submit/<int:course_id>/', views.submit, name='submit'),

    # ✅ Vizsga eredmény (HIÁNYZOTT)
    # ex: /onlinecourse/result/3/
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name="exam_result"),

]

# 🔹 Media fájlok
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)