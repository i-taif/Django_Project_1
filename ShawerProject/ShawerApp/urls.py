from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('cons/',views.consolt,name='consolt'),
    path('profile/<pk>', views.comment_detile, name='profile'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('courses', views.courses, name='courses')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)