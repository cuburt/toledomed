from django.conf.urls import url
from . import views, class_views


app_name = 'calendarium'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^result/$', views.result, name='result'),
    url(r'^view_record/user=(?P<identity_id>[0-9]+)/$', views.generate_patient_rec, name='generate_patient_rec'),
    url(r'^calendarium/user=(?P<identity_id>[0-9]+)/$', views.welcome_calendar, name='welcome_calendar'),
    url(r'^calendarium/next_month/user=(?P<identity_id>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.next_month, name='next_month'),
    url(r'^calendarium/prev_month/user=(?P<identity_id>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.prev_month, name='prev_month'),
    url(r'^calendarium/set_appointment/$', views.set_appointment, name='set_appointment'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^user=(?P<identity_id>[0-9]+)/$',views.profile, name='profile'),
    url(r'^user=(?P<identity_id>[0-9]+)/edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^user=(?P<identity_id>[0-9]+)/edit_patient_info/$', views.edit_patient_info, name='edit_patient_info'),
    url(r'^user=(?P<identity_id>[0-9]+)/create_patient_info/$', views.create_patient_info, name='create_patient_info'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/create_patient_history/$', views.create_patient_hist, name='create_patient_hist'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/patient_hist=(?P<patient_hist_id>[0-9]+)/create_lab_results/$', views.create_lab_results, name='create_lab_results'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/create_operation/$', views.create_operation, name='create_operation'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/create_anesthesia_record/$', views.create_anesthesia_rec, name='create_anesthesia_rec'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/create_nurse_record/$', views.create_nurse_rec, name='create_nurse_rec'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/create_operations_record/$', views.create_operation_rec, name='create_operation_rec'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/view_patient_hist/$', views.view_patient_hist, name='view_patient_hist'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/patient_hist=(?P<patient_hist_id>[0-9]+)/view_patient_records/$',views.view_patient_rec, name='view_patient_rec'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/patient_hist=(?P<patient_hist_id>[0-9]+)/view_lab_results/$', views.view_lab_results, name='view_lab_results'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/view_anesthesia_rec/$', views.view_anesthesia_rec, name='view_anesthesia_rec'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/view_nurse_rec/$', views.view_nurse_rec, name='view_nurse_rec'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/view_operation_rec/$', views.view_operation_rec, name='view_operation_rec'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/patient_hist=(?P<patient_hist_id>[0-9]+)/edit_patient_hist/$',views.edit_patient_hist, name='edit_patient_hist'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/patient_hist=(?P<patient_hist_id>[0-9]+)/lab_rep=(?P<lab_rep_id>[0-9]+)/edit_lab_results/$',views.edit_lab_results, name='edit_lab_results'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/anesthesia_rec_id=(?P<anesthesia_rec_id>[0-9]+)/edit_anesthesia_rec/$',views.edit_anesthesia_rec, name='edit_anesthesia_rec'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/nurse_rec=(?P<nurse_rec_id>[0-9]+)/edit_nurse_rec/$',views.edit_nurse_rec, name='edit_nurse_rec'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/op_rec=(?P<op_rec_id>[0-9]+)/edit_operation_rec/$',views.edit_operation_rec, name='edit_operation_rec'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/patient_hist=(?P<patient_hist_id>[0-9]+)/patient_rec=(?P<patient_rec_id>[0-9]+)/view_patient_rec_details/$',views.view_patient_rec_details, name='view_patient_rec_details'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/patient_hist=(?P<patient_hist_id>[0-9]+)/lab_rep=(?P<lab_rep_id>[0-9]+)/view_lab_results_details/$',views.view_lab_results_details, name='view_lab_results_details'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/anesthesia_rec_id=(?P<anesthesia_rec_id>[0-9]+)/view_anesthesia_rec_details/$',views.view_anesthesia_rec_details, name='view_anesthesia_rec_details'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/anesthesia_rec_id=(?P<anesthesia_rec_id>[0-9]+)/view_oi_rec_details/$',views.view_oi_rec_details, name='view_oi_rec_details'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/nurse_rec=(?P<nurse_rec_id>[0-9]+)/view_nurse_rec_details/$',views.view_nurse_rec_details, name='view_nurse_rec_details'),
    url(r'^user=(?P<identity_id>[0-9]+)/patient=(?P<patient_id>[0-9]+)/assessment=(?P<assessment_id>[0-9]+)/operation=(?P<operation_id>[0-9]+)/ops_rec=(?P<ops_rec_id>[0-9]+)/op_rec=(?P<op_rec_id>[0-9]+)/view_operation_rec_details/$',views.view_operation_rec_details, name='view_operation_rec_details'),

]
