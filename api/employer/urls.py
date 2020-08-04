from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('employer', views.EmployerView)
router.register('contacts', views.ContactsView)

urlpatterns = [
    path('', include(router.urls)),
    path(r'xls/', views.export_xls, name='export_xls'),
    path('lastday/<int:y>/<int:m>/', views.last_day_of_month)

]
