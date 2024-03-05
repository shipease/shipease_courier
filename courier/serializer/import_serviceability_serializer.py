from rest_framework import serializers

from courier.models import ServiceablePincode


class ImportServiceabilitySerializer(serializers.ModelSerializer):
    partner_id = serializers.ReadOnlyField()
    courier_partner = serializers.ReadOnlyField()

    class Meta:
        model = ServiceablePincode
        fields = ('courier_partner', 'pincode', 'is_cod', 'partner_id')
