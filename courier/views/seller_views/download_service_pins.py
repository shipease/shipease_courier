from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from courier.models import ServiceablePincode
from courier.utils.handlers.serviceability_check import ServiceabilityCheckHandler
from master_app.utils.xlsx_handler import XlsxHander
from rest_framework.permissions import IsAuthenticated


class ServiceablePinDownloadApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        This api will return list of serviceable pin codes list for the given partner_id in query params. \n

        query_params: \n
            1. partner_ids=1,2
        """
        response = []

        partsner_ids = request.query_params.get('partner_ids').split(',')

        valid_partners = []
        for i in partsner_ids:
            try:
                if ServiceablePincode.objects.filter(partner_id=i).exists():
                    valid_partners.append(i)
            except:
                pass

        for p_id in valid_partners:
            partner_name = ServiceablePincode.partner_name_by_id(p_id)
            pins_list = ServiceablePincode.service_pin_list(partner_id=p_id)
            result = {"partner_name": partner_name, "pin_list": pins_list}
            response.append(result)

        workbook, worksheet, output = XlsxHander.get_workbook()

        data_list = []
        for col_index, partner_pin_list in enumerate(response):

            data = list(partner_pin_list['pin_list'])
            data.insert(0, partner_pin_list['partner_name'])
            # worksheet.write_column(0, col_index, data)
            data_list.append(data)
        XlsxHander.write_list_into_columns(
            workbook=workbook, worksheet=worksheet, data_list=data_list)

        return XlsxHander.return_file_response(output=output, file_name="serviceable_pincodes")

class CheckServiceabilityApiView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        """
        This api will return the pickup and delivery serviceability for particular pincode. \n
        query_params: \n
            pincode_type=LM/FM
            pincode=122001
        """

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
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        This api will return list of serviceable partner for the given pickup and delivery pincode. \n
        query_params: \n
            pickup_pincode=122001
            delivery_pincode=122002

        """

        pickup_pincode = request.query_params.get('pickup_pincode')
        delivery_pincode = request.query_params.get('delivery_pincode')

        result = ServiceabilityCheckHandler(pin_code=None).check_pair_serviceability(
            pickup_pincode=pickup_pincode, delivery_pincode=delivery_pincode)
        return Response(result, status=200)
    

class ShipeaseServiceabilityPinCodeDownload(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        """
        This api will download the list of all serviceable pincodes by Shipease.
        """
        serviceable_pincodes = ServiceablePincode.objects.values_list('pincode', flat=True).filter(active=True).distinct('pincode')
        workbook, worksheet, output = XlsxHander.get_workbook()
        XlsxHander.write_list_into_columns(
            workbook=workbook, worksheet=worksheet, data_list=[list(serviceable_pincodes)])
        return XlsxHander.return_file_response(output=output, file_name="shipease_serviceable_pincodes")
        return Response({'details':serviceable_pincodes}, status=HTTP_200_OK)
