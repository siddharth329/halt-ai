from rest_framework import serializers
from api.models import LLMQuery
# from api.utils import mask_personally_identifiable_information

# from api.model.langchain.main import get_llm_response_langchain
from api.model.gemini.main import get_llm_response_gemini


class LLMQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = LLMQuery
        exclude = ['created_at', 'updated_at']
        read_only_fields = ['user', 'errors']

    def create(self, validated_data):

        source = validated_data['source']
        content = validated_data['content']
        machine_id = validated_data['machine_id']
        # masked_content = mask_personally_identifiable_information(content)

        # LLM Model Query
        # llm_response_json = get_llm_response_gemini(masked_content.text)
        llm_response_json = get_llm_response_gemini(content)
        print(llm_response_json)

        blocked = True if llm_response_json['flag'] == 1 else False
        action_required = True if llm_response_json['critical'] == 1 else False
        action_level = 2 if llm_response_json['critical'] == 1 else (0 if blocked is False else 1)  # 0=>CLEAR, 1=>WARNING, 2=>ALERT

        # Saving the user query into the database for forensics
        query = LLMQuery(
            machine_id=machine_id,
            content=content,
            source=source,
            error=llm_response_json['errors'],
            blocked=blocked,
            action_required=action_required,
            action_level=action_level
        )
        query.save()

        return query
