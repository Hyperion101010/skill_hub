from django.urls import include, path ,re_path
from .import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.FirstPage.as_view(), name='First Page'),
    path('auditing/', TemplateView.as_view(template_name='user_form/auditing.html'), name='auditing'),
    path('balance/', TemplateView.as_view(template_name='user_form/balance_sheet_management.html'), name='balance'),
    re_path('predict/',views.predict_engine,name='prediction-engine'),
    path('ajax/load-skills/', views.load_skills, name='ajax_load_skills'),
]
