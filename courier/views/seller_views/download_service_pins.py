from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from courier.models import ServiceablePincode


class ServiceablePinDownloadApiView(APIView):

    def get(self, request, *args, **kwargs):
        """
        This api will return list of serviceable pin codes list for the given partner_id in query params. \n

        query_params: \n
            1. partner_id=1
        """

        pins_list = ServiceablePincode.service_pin_list(partner_id=request.query_params.get('partner_id'))

        return Response({'pins':pins_list}, status=HTTP_200_OK)