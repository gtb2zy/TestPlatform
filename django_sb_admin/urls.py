from django.urls import path

import django_sb_admin.views
app_name = 'manage'

urlpatterns = [

    path('', django_sb_admin.views.index, name='sb_admin_index'),
    path('dashboard/', django_sb_admin.views.dashboard, name='sb_admin_dashboard'),
    path('charts/', django_sb_admin.views.charts, name='sb_admin_charts'),
    path('tables/', django_sb_admin.views.tables, name='sb_admin_tables'),
    path('forms/', django_sb_admin.views.forms, name='sb_admin_forms'),
    path('bootstrap-elements/', django_sb_admin.views.bootstrap_elements, name='sb_admin_bootstrap_elements'),
    path('bootstrap-grid/', django_sb_admin.views.bootstrap_grid, name='sb_admin_bootstrap_grid'),
    path('rtl-dashboard/', django_sb_admin.views.rtl_dashboard, name='sb_admin_rtl_dashboard'),
    path('blank/', django_sb_admin.views.blank, name='sb_admin_blank'),
    path('login/', django_sb_admin.views.login, name='login'),
]