from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^addfakulte/$', 'home.views.fakulte', name='fakulte'),
    url(r'^addbolum/$', 'home.views.bolum', name='bolum'),
    url(r'^addogrenci/$', 'home.views.ogrenci', name='ogrenci'),
    url(r'^ogrencisorgu/$', 'home.views.sorgu', name='sorgu'),
    url(r'^ekle/$', 'home.views.ekle', name='ekle'),
    url(r'^sorgula/$', 'home.views.sorgula', name='sorgula'),
    # url(r'^$', include('proje.home.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
