from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('upload/', upload_file, name='upload_file'),
    path('anomaly_detection/', anomaly, name='anomaly'),
    path('get_threat_solution/', get_threat_solution, name='nlp'),
    path('llama/', llama, name='llama'),
    
    
    path('linear_input/', linear_regression_input, name='linear_regression_input'),
    path('linear_model/', linear_regression_model, name='linear_regression_model'),
    path('cost_exp_visualization/', cost_exp_visualization, name='cost_exp_visualization'),
    path('ec2_instance_vis/', ec2_instance_vis, name='ec2_instance_vis'),
    path('rds_vis/', rds_vis, name='rds_vis'),
    path('rds_pred/', rds_pred, name='rds_pred'),
]