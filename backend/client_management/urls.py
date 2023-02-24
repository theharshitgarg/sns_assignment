from django.urls import path

from client_management.views import *

# urlpatterns = [
#     path('works/', admin.site.urls),
#     path('register', '')
# ]


from django.urls import include, path
from rest_framework import routers
from client_management import views

router = routers.DefaultRouter()
router.register(r'works', views.WorkViewSet)
router.register(r'clients', views.ClientViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('hello', views.hello),
    path('', include(router.urls)),
    path('register', ClientRegistrationView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]