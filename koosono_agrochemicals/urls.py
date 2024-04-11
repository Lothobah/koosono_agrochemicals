"""koosono_agrochemicals URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from koosono_agrochemicals import settings
from agrochemicals_management_system import views,HodViews
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="admin_templates/password_reset_form.html"), name="reset_password"),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="admin_templates/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="admin_templates/password_reset_done.html"),
         name="password_reset_done"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="admin_templates/password_reset_complete.html"),
         name="password_reset_complete"),
    path('do_login', views.DoLogin, name="do_login"),
    path('do_logout', views.Logout_User, name="do_logout"),
    path('admin_profile', HodViews.admin_profile, name="admin_profile"),
    path('edit_admin_profile_save', HodViews.edit_admin_profile_save,
         name="edit_admin_profile_save"),
    path('add_product', HodViews.add_product, name="add_product"),
    path('products',HodViews.products, name="products"),
    path('add_product_save', HodViews.add_product_save, name="add_product_save"),
    path('update_product_save', HodViews.update_product_save, name="update_product_save"),
    path('update_product/<str:product_id>',
         HodViews.update_product, name="update_product"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
