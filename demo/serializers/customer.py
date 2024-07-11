from rest_framework import serializers
from demo.models.customer import Customer


class CustomerModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
