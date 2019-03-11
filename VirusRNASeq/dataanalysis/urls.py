from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from dataanalysis import views

urlpatterns = [
    path('<slug:slug_project>/settings', views.whole_dataanalysis, name='dataanalysis_home'),
    path('<slug:slug_project>/data-upload', views.BasicUploadView.as_view(), name='dataanalysis_data_upload'),
    path('result/<slug:slug_project>/', views.show_result, name="dataanalysis_result"),
    path('result/<slug:slug_project>/overview/',
         views.show_result_overview, name="dataanalysis_result_overview"),
    path('result/<slug:slug_project>/current-status/',
         views.current_status, name="dataanalysis_result_current_status"),
    path('result/<slug:slug_project>/current-status/QC/pre/multiqc_before_report', views.pre_qc_html_view_multiqc, name="dataanalysis_result_current_status_pre_multiqc_html"),
    path('result/<slug:slug_project>/current-status/QC/pre/fastqc_r1_before_report', views.pre_qc_html_view_r1, name="dataanalysis_result_current_status_pre_fastqc_r1_html"),
    path('result/<slug:slug_project>/current-status/QC/pre/fastqc_r2_before_report', views.pre_qc_html_view_r2, name="dataanalysis_result_current_status_pre_fastqc_r2_html"),
    path('result/<slug:slug_project>/current-status/QC/post/multiqc_after_report', views.post_qc_html_view_multiqc, name="dataanalysis_result_current_status_post_multiqc_html"),
    path('result/<slug:slug_project>/current-status/QC/post/fastqc_r1_after_report', views.post_qc_html_view_r1, name="dataanalysis_result_current_status_post_fastqc_r1_html"),
    path('result/<slug:slug_project>/current-status/QC/post/fastqc_r2_after_report', views.post_qc_html_view_r2, name="dataanalysis_result_current_status_post_fastqc_r2_html"),


    # path('result/<slug:slug_project>/current-status/QC/post/<slug:slug_filename>', views.post_qc_html_view, name="dataanalysis_result_current_status_post_qc_html"),
    path('upload-progress/', views.upload_progress, name='upload_progress'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
