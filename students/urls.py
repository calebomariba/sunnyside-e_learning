from django.urls import path
# from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path(
        'register/',
        views.StudentRegistrationView.as_view(),
        name='student_registration',
    ),

]