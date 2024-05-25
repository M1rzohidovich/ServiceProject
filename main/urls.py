from django.urls import path

from main.views import AnnouncementListApiView, GetInternalBlog, GetExternalBlog, GetWorkerContact


urlpatterns = [
    path('get-announcement-list', AnnouncementListApiView.as_view(), name='get-announcement-list'),
    path('get-internal-blog', GetInternalBlog.as_view(), name='get-internal-blog'),
    path('get-external-blog', GetExternalBlog.as_view(), name='get-external-blog'),
    path('get-contact', GetWorkerContact.as_view(), name='get-contact')
]