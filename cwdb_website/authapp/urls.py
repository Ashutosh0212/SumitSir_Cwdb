from django.urls import path,reverse_lazy

from django.conf import settings
from django.conf.urls.static import static
from . import views

from .views import UserProfileView,EditProfileView,CustomLoginView
app_name = 'authapp'
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    #HomePage
    path('',views.index,name='index'),
    path('proposal/list/', views.proposal_list, name='proposal_list'),
    path('beneficiary-data/', views.beneficiary_data_table, name='beneficiary_data_table'),
    path('iwdp/', views.iwdp_view, name='iwdp_view'),
    path('wms-data/',views.wms_scheme_view,name='wms_scheme_view'),
    path('wps-data/',views.wps_scheme_view,name='wps_scheme_view'),
    path('pwds-data/',views.pwds_scheme_view,name='pwds_scheme_view'),
    path('hrdpa-data/',views.hrdpa_scheme_view,name='hrdpa_scheme_view'),
    path('admin_Expenses',views.admin_exp_view,name='admin_exp_view'),
     
    path('signup/', views.signup, name='register'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    # path('login/',user_login,name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/submit_proposal/', views.submit_proposal, name='submit_proposal'),
    path('dashboard/proposal_detail/<int:proposal_id>/', views.proposal_detail, name='proposal_detail'),
    path('dashboard/proposal_list/', views.proposal_list, name='proposal_list'),
    path('dashboard/admin_proposal_list/', views.admin_proposal_list, name='admin_proposal_list'),
    path('dashboard/admin_proposal_detail/<int:proposal_id>/', views.admin_proposal_detail, name='admin_proposal_detail'),
    path('dashboard/proposal_status/', views.proposal_status, name='proposal_status'),
    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='authapp:index'), name='logout'),
    path('admin/logout/',LogoutView.as_view(next_page='authapp:index'), name='logout'),
     path('dashboard/change-password/', PasswordChangeView.as_view(), name='change_password'),
    #proposal admin urls
    path('admin/submit_approval/<str:proposal_id>/', views.submit_approval, name='submit_approval'),
path('admin/submit_installment_sanction_letter/<str:proposal_id>/', views.submit_installment_sanction_letter, name='submit_installment_sanction_letter'),
 path('admin/submit_inspection_report/<str:proposal_id>/', views.submit_inspection_letter, name='submit_inspection_report'),

    # Password Reset URLs
    path('dashboard/forgot-password/', PasswordResetView.as_view(), name='forgot_password'),
    path('dashboard/5/password/', PasswordResetView.as_view(), name='forgot_password'),
    path('dashboard/forgot-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('dashboard/reset-password/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('dashboard/reset-password/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # #progress report urls 
    path('dashboard/progress_report/', views.progress_report, name='progress_report'),
    #wms subcomponents
    path('dashboard/revolving_fund_progress_report/<str:proposal_unique_id>/', views.revolving_fund_progress_report, name='revolving_fund_progress_report'),
    path('dashboard/eportal/<str:proposal_unique_id>/', views.eportal_progress_report, name='eportal_progress_report'),
    path('dashboard/selfhelpgroup_report/<str:proposal_unique_id>/', views.selfhelpgroup_report, name='selfhelpgroup_report'),
    path('dashboard/buyersellerexpo_report/<str:proposal_unique_id>/', views.buyersellerexpo_report, name='buyersellerexpo_report'),
    path('dashboard/infrastructuredevelopment_report/<str:proposal_unique_id>/', views.infrastructuredevelopment_report, name='infrastructuredevelopment_report'),
    path('dashboard/woolen_expo/<str:proposal_unique_id>/', views.woolen_expo, name='woolen_expo'),
    path('dashboard/woolen_expo_hiring/<str:proposal_unique_id>/', views.woolen_expo_hiring, name='woolen_expo_hiring'),
    #wps subcomponent
    path('dashboard/cfc_progress_report/<str:proposal_unique_id>/', views.cfc_progress_report, name='cfc_progress_report'),
    path('dashboard/sheep_shearing_machining/<str:proposal_unique_id>/', views.sheep_shearing_machining, name='sheep_shearing_machining'),
    path('dashboard/equipment/<str:proposal_unique_id>/', views.equipment, name='equipment'),
    path('dashboard/small_tools_distribution/<str:proposal_unique_id>/', views.small_tools_distribution, name='small_tools_distribution'),
   # hrd subcomponent
    path('dashboard/short_term_programme/<str:proposal_unique_id>/', views.short_term_programme, name='short_term_programme'),
    path('dashboard/onsite_training_progress_report/<str:proposal_unique_id>/', views.onsite_training_progress_report, name='onsite_training_progress_report'),
    path('dashboard/shearing_machine_training_report/<str:proposal_unique_id>/', views.shearing_machine_training_report, name='shearing_machine_training_report'),
    path('dashboard/rd_report/<str:proposal_unique_id>/', views.rd_report, name='rd_report'),
    path('dashboard/domestic_meeting_report/<str:proposal_unique_id>/', views.domestic_meeting_report, name='domestic_meeting_report'),
    path('dashboard/organising_seminar_report/<str:proposal_unique_id>/', views.organising_seminar_report, name='organising_seminar_report'),
    path('dashboard/wool_survey_report/<str:proposal_unique_id>/', views.wool_survey_report, name='wool_survey_report'),
    path('dashboard/wool_testing_lab_report/<str:proposal_unique_id>/', views.wool_testing_lab_report, name='wool_testing_lab_report'),
    path('dashboard/publicity_monitoring_report/<str:proposal_unique_id>/', views.publicity_monitoring_report, name='publicity_monitoring_report'),
    #pwds subcomponent
    path('dashboard/pashmina_revolving_fund_progress_report/<str:proposal_unique_id>/', views.pashmina_revolving_fund_progress_report, name='pashmina_revolving_fund_progress_report'),
    path('dashboard/pashmina_cfc_report/<str:proposal_unique_id>/', views.pashmina_cfc_report, name='pashmina_cfc_report'),
    path('dashboard/shelter_shed_report/<str:proposal_unique_id>/', views.shelter_shed_report, name='shelter_shed_report'),
    path('dashboard/portable_tent_report/<str:proposal_unique_id>/', views.portable_tent_report, name='portable_tent_report'),
    path('dashboard/predator_proof_lights_report/<str:proposal_unique_id>/', views.predator_proof_lights_report, name='predator_proof_lights_report'),
    path('dashboard/testing_equipment_report/<str:proposal_unique_id>/', views.testing_equipment_report, name='testing_equipment_report'),
    path('dashboard/showroom_development_report/<str:proposal_unique_id>/', views.showroom_development_report, name='showroom_development_report'),
    path('dashboard/fodder_land_development_report/<str:proposal_unique_id>/', views.fodder_land_development_report, name='fodder_land_development_report'),
    #admin
    # urls.py

# path('admin/view_progress_report/<str:proposal_id>/', views.view_progress_report, name='view_progress_report'),
    
#notifications
# path('dashboard/show-notifications/', views.show_notifications, name='show_notifications'),
path('dashboard/show-all-notifications/', views.show_all_notifications, name='show_all_notifications'),
path('dashboard/profile/', UserProfileView.as_view(), name='user_profile'),
path('dashboard/profile/edit/', EditProfileView.as_view(), name='edit_profile'),
# path('dashboard/updated', views.show_notifications, name='show_new_notifications'),
#staff dashboard
path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
path('staff_dashboard/all-proposals/', views.all_proposal_details, name='all_proposal_details'),
path('submit-approval/<str:proposal_id>/', views.submit_approval, name='submit_approval'),

    # Add more patterns as needed

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)