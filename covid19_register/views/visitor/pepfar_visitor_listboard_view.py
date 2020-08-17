from .base_listboard_view import BaseListBoardView


class PepfarVisitorListBoardView(BaseListBoardView):

    listboard_url = 'pepfar_visitor_listboard_url'
    navbar_selected_item = 'pepfar_visitor'
    search_form_url = 'pepfar_visitor_listboard_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(site_name='pepfar', **kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request,
                                                      site_name='pepfar',
                                                      *args, **kwargs)

        return options
