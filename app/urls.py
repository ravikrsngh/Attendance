from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name='app'
urlpatterns=[
            path('',views.home,name='home'),
            path('r_teacher/',views.r_teacher,name='r_teacher'),
            path('r_student/',views.r_student,name='r_student'),
            path('start/',views.start,name='start'),
            path('user_login/',views.user_login,name="user_login"),
            path('user_logout/',views.user_logout,name="user_logout"),
            path('reinsert/<int:u>/<int:n>/',views.reinsert,name="reinsert"),
            path('manual/<slug:slot>/<slug:date>/',views.edit_manual,name="manual"),
            ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
