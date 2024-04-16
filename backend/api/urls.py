from django.urls import path
from api.views.llm_query import LLMQueryCreateView

urlpatterns = [
    path('query/', LLMQueryCreateView.as_view(), name='query_create_view')
]
