from views import doc

urlpatterns = [ 
    '',
    (r'^api/$', doc),
    (r'^example/(?P<resource_name>.+)/', 'tastydocs.views.example_data'),
]
