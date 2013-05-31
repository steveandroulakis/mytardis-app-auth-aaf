from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    'tardis.apps.aaf',
    (r'^authorize/$', 'views.authorize'),
)
