from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from courier.models import ServiceablePincode
from courier.utils.handlers.serviceability_check import ServiceabilityCheckHandler


class ServiceablePinDownloadApiView(APIView):

    def get(self, request, *args, **kwargs):
        """
        This api will return list of serviceable pin codes list for the given partner_id in query params. \n

        query_params: \n
            1. partner_ids=1,2
        """
        response = []
        partsner_ids = request.query_params.get('partner_ids').split(',')
        for p_id in partsner_ids:
            partner_name = ServiceablePincode.partner_name_by_id(p_id)
            pins_list = ServiceablePincode.service_pin_list(partner_id=p_id)
            result = {"partner_name": partner_name, "pin_list": pins_list}
            response.append(result)

        return Response(response, status=HTTP_200_OK)


class CheckServiceabilityApiView(APIView):
    def get(self, request, *args, **kwargs):

        pincode_type = request.query_params['pincode_type']
        pincode = request.query_params['pincode']

        if pincode_type.strip().lower() == "lm":
            result = ServiceabilityCheckHandler(
                pin_code=pincode).check_lm_serviceability()

        elif pincode_type.strip().lower() == "fm":
            result = ServiceabilityCheckHandler(
                pin_code=pincode).check_fm_serviceability()

        return Response(result, status=200)


class CheckPairServiceabilityApiView(APIView):
    def get(self, request, *args, **kwargs):

        pickup_pincode = request.query_params.get('pickup_pincode')
        delivery_pincode = request.query_params.get('delivery_pincode')

        result = ServiceabilityCheckHandler(pin_code=None).check_pair_serviceability(
            pickup_pincode=pickup_pincode, delivery_pincode=delivery_pincode)
        return Response(result, status=200)
