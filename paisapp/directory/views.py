from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from paisapp.directory.models import Categoria, Tipo

class CategoriaDetailView(LoginRequiredMixin, DetailView):
	model = Categoria
	slug_field = "id"
	slug_url_kwarg = "id"

categoria_detail_view = CategoriaDetailView.as_view()

class TipoDetailView(LoginRequiredMixin, DetailView):
	model = Tipo
	slug_field = "id"
	slug_url_kwarg = "id"

tipo_detail_view = TipoDetailView.as_view()

class CategoriaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Categoria
	fields = ["name"]
	success_message = _("Information successfully updated")

	def get_success_url(self) -> str:
		assert self.request.user.is_staff  # type guard
		return self.request.user.get_absolute_url()

	def get_object(self, queryset: QuerySet | None=None) -> Categoria:
		assert self.request.user.is_staff  # type guard
		return self.request.user

categoria_update_view = CategoriaUpdateView.as_view()

class TipoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Tipo
	fields = ["name"]
	success_message = _("Information successfully updated")

	def get_success_url(self) -> str:
		assert self.request.user.is_staff  # type guard
		return self.request.user.get_absolute_url()

	def get_object(self, queryset: QuerySet | None=None) -> Tipo:
		assert self.request.user.is_staff  # type guard
		return self.request.user
	
tipo_update_view = TipoUpdateView.as_view()

class CategoriaRedirectView(LoginRequiredMixin, RedirectView):
	permanent = False

	def get_redirect_url(self) -> str:
		return reverse("directory:categoria-detail", kwargs={"id": self.request.user.pk})
	
categoria_redirect_view = CategoriaRedirectView.as_view()

class TipoRedirectView(LoginRequiredMixin, RedirectView):
	permanent = False

	def get_redirect_url(self) -> str:
		return reverse("directory:tipo-detail", kwargs={"id": self.request.user.pk})
	
tipo_redirect_view = TipoRedirectView.as_view()

