from django.contrib import admin
from django.urls import path, include
from. import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hosted/',include('hosted.urls')),
    path('aid_org_list/',include('aid_org.urls')),
    path('about/',views.about, name='about'),
    path('',views.homepage, name='homepage'),
    path('success_story/', include('success_story.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)