from .base_listboard_view import BaseListBoardView


class MmabanaVisitorListBoardView(BaseListBoardView):

    listboard_url = 'mmabana_visitor_listboard_url'
    navbar_selected_item = 'mmabana_visitor'
    search_form_url = 'mmabana_visitor_listboard_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(site_name='mmabana', **kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request,
                                                      site_name='mmabana',
                                                      *args, **kwargs)

        return options
