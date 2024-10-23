from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from paisapp.users.api.views import UserViewSet
from paisapp.directory.api.views import CategoriaViewSet
from paisapp.directory.api.views import TipoViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("categorias", CategoriaViewSet)
router.register("tipos", TipoViewSet)


app_name = "api"
urlpatterns = router.urls
