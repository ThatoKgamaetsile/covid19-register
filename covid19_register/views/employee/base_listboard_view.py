from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import (
    ListboardFilterViewMixin, SearchFormViewMixin)
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin
import re

from ...model_wrappers import EmployeeModelWrapper


class BaseListBoardView(NavbarViewMixin, EdcBaseViewMixin,
                        ListboardFilterViewMixin, SearchFormViewMixin,
                        ListboardView):

    listboard_template = 'employee_listboard_template'
    listboard_url = None
    listboard_panel_style = 'info'
    listboard_fa_icon = "fa-user-plus"

    model = 'covid19_register.employee'
    model_wrapper_cls = EmployeeModelWrapper
    navbar_name = 'covid_19_sites'
    ordering = '-modified'
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            contact='employee',
            site_name=kwargs.get('site_name'),
            contact_add_url=self.model_cls().get_absolute_url())
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('cell'):
            options.update(
                {'cell': kwargs.get('cell')})
        options.update(
            {'site_name': kwargs.get('site_name')})
        return options

    def get_wrapped_queryset(self, queryset):
        """Returns a list of wrapped model instances.
        """
        object_list = []

        for obj in queryset:
            next_url_name = settings.DASHBOARD_URL_NAMES.get(
                self.listboard_url)
            object_list.append(
                self.model_wrapper_cls(obj, next_url_name=next_url_name))
        return object_list

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q
