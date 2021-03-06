from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url(r'^$', 'pydat.views.index', name='index'),
  url(r'^domains/(?P<key>.*)/(?P<value>.*)/$', 'pydat.views.domains'),
  url(r'^domains/$', 'pydat.views.domains', name='domains'),
  url(r'^pdns/(?P<domain>.*)/$', 'pydat.views.pdns', name='pdns_rest'),
  url(r'^pdns/$', 'pydat.views.pdns', name='pdns'),
  url(r'^pdnsr/(?P<key>.*)/(?P<value>.*)/$', 'pydat.views.pdns_r', name='pdns_r_rest'),
  url(r'^pdnsr/$', 'pydat.views.pdns_r', name='pdns_r'),

  url(r'^ajax/domain/(?P<domainName>.*)/$', 'pydat.ajax.domain'),
  url(r'^ajax/domain/$', 'pydat.ajax.domain', name='ajax_domain'),
  url(r'^ajax/domains/(?P<key>.*)/(?P<value>.*)/$', 'pydat.ajax.domains' ),
  url(r'^ajax/domains/$', 'pydat.ajax.domains', name='ajax_domains'),
  url(r'^ajax/resolve/(?P<domainName>.*)/$', 'pydat.ajax.resolve'),
  url(r'^ajax/resolve/$', 'pydat.ajax.resolve', name='ajax_resolve'),
)
