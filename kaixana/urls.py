from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

from rest_framework_nested import routers

from authentication.views import AccountViewSet, LoginView, LogoutView
from posts.views import AccountPostsViewSet, PostViewSet
from country.views import CountryViewset
from kaixana.views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)
router.register(r'country', CountryViewset)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'posts', AccountPostsViewSet)

urlpatterns = patterns(
    '',
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    #url(r'^country/$', CountryViewset.as_view, name='country'),
    url(r'^.*$', IndexView.as_view(), name='index'),
)
