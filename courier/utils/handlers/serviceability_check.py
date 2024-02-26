from courier.models import ServiceablePincode, ServiceablePincodeFM
from master_app.stub_models import Partner


class ServiceabilityCheckHandler:
    """
    FM >> First Mile, pickup pincode, partner who can pick from pincode
    LM >> Last Mile, delivery pincode, partners who deliver to this pincode
    """

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

    def check_pair_serviceability(self, pickup_pincode, delivery_pincode):
        fm_partners = ServiceablePincodeFM.objects.values_list(
            'partner_id', flat=True).filter(pincode=pickup_pincode)

        lm_partners = ServiceablePincode.objects.values_list(
            'partner_id', flat=True).filter(pincode=delivery_pincode)

        common_partners = list(filter(lambda x: x in fm_partners, lm_partners))

        response = []
        for partner_id in common_partners:
            partner_obj = Partner.objects.using('user_db').values('id',
                                                                  'title', 'mps_enabled', 'reverse_enabled', 'weight_initial', 'extra_limit').get(id=partner_id)
            response.append(partner_obj)

        return response

