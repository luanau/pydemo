from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'pydemo.views.home', name='home'),
    url(r'^$', 'pydemo.views.home_page', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/', 'accounts.views.my_view'),
)
