from rest_framework import serializers
from .models import Selfie


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class SelfieSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Selfie
        fields = '__all__'
