from courier.models import ServiceablePincode, ServiceablePincodeFM
from master_app.stub_models import Partner


class ServiceabilityCheckHandler:

    def __init__(self, pin_code) -> None:
        self.pin_code = pin_code

    def check_fm_serviceability(self):
        pass

    def check_lm_serviceability(self):
        partner_ids = ServiceablePincode.objects.values_list(
            'partner_id', flat=True).filter(pincode=self.pin_code)

        response = []
        for partner_id in partner_ids:
            partner_obj = Partner.objects.using('user_db').values('id',
                                                                  'title', 'mps_enabled', 'reverse_enabled', 'weight_initial', 'extra_limit').get(id=partner_id)
            response.append(partner_obj)

        return response

    def check_fm_serviceability(self):
        partner_ids = ServiceablePincodeFM.objects.values_list(
            'partner_id', flat=True).filter(pincode=self.pin_code)

        response = []
        for partner_id in partner_ids:
            partner_obj = Partner.objects.using('user_db').values('id',
                                                                  'title', 'mps_enabled', 'reverse_enabled', 'weight_initial', 'extra_limit').get(id=partner_id)
            response.append(partner_obj)

        return response
