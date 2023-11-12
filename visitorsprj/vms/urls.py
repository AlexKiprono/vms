from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('login/', views.loginView, name='login'),
    # path('logout/', views.logoutView, name='logout'),
    # path('register/', views.registerView, name='register'),
    path('visitor/', views.visitor, name='visitor'),
    path('visitors_view/', views.visitors_view, name='visitors_view'),
    path('edit-visitor/<int:id>/', views.edit_visitor, name='edit_visitor'),
    path('delete-visitor/<int:id>/', views.delete_visitor, name='delete_visitor'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
