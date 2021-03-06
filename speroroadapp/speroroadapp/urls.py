from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('roads.views',
	

	url(r'^speroroadapp/(?P<ident>\d+)/$','roads_view.rest'),
	url(r'^export/$', 'roads_view.export_csv'),
	url(r'^$','roads_view.index'),
	
) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)