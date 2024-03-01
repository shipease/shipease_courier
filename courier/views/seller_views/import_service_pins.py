from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from courier.models import ServiceablePincode
from courier.serializer.import_serviceability_serializer import ImportServiceabilitySerializer
from courier.utils.handlers.serviceability_check import ServiceabilityCheckHandler
from master_app.stub_models import Partner
from master_app.utils.xlsx_handler import XlsxHander
from rest_framework.permissions import IsAuthenticated


class ImportServiceablePincode(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        This api will save serviceable pincode of courier partners. \n
        body : { \n
            [\n
            {\n
            "pincode" : "pincode",\n
            "is_cod" : true/false,\n
            },\n
            {\n
            "pincode" : "pincode",\n
            "is_cod" : true/false,\n
            }\n
            ]
        }
        query_params: \n
            1. partner_id=1
        """
        partner = request.query_params.get('partner_id')
        partner_data = Partner.objects.using('user_db').get(id=partner)
        if not partner_data:
            return Response({'message': 'Invalid Partner ID'}, status=HTTP_400_BAD_REQUEST)
        serializer = ImportServiceabilitySerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        ServiceablePincode.objects.filter(partner_id=partner_data.id).delete()
        serializer.save(partner_id=partner_data.id, courier_partner=partner_data.keyword)
        return Response({'message': 'Pincode imported successfully done'}, status=HTTP_200_OK)
