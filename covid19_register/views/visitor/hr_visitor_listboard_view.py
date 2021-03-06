from .base_listboard_view import BaseListBoardView


class HrVisitorListBoardView(BaseListBoardView):
    listboard_url = 'hr_visitor_listboard_url'
    navbar_selected_item = 'finance_hr_visitor'
    search_form_url = 'hr_visitor_listboard_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(site_name='hr', **kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request,
                                                      site_name='hr',
                                                      *args, **kwargs)

        return options
