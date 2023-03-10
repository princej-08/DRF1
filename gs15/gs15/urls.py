from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentListCreate.as_view()),
    # path('studentapi/',views.StudentCreateView.as_view()),
    # path('studentapi/<int:pk>',views.StudentRetrieveView.as_view()),
    # path('studentapi/<int:pk>',views.StudentUpdateView.as_view()),
    path('studentapi/<int:pk>',views.StudentRUD.as_view()),
    # path('studentapi/<int:pk>', views.RUDStudentAPI.as_view()),

]
