""" REST views for the query API
"""
from core_explore_common_app.rest.query.views import ExecuteLocalQueryView
from core_explore_example_type_app.components.data_item import api as data_item_api


class ExecuteLocalQueryDataItemView(ExecuteLocalQueryView):
    sub_document_root = 'list_content'

    def execute_raw_query(self, raw_query):
        # Distinct result by the data field
        return data_item_api.execute_query(raw_query, self.request.user).distinct("data")
