from django.conf.urls import *
from mysite.views import current_datetime, hours_ahead

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^time/$', current_datetime),
                       (r'^time/plus/(\d{1,2})/$', hours_ahead),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
)
