from django.core.management.base import BaseCommand
import json
from courier.models import ServiceablePincode


class Command(BaseCommand):
    help = 'command to seed serviceability pin code'

    def handle(self, *args, **options):
        with open("courier/fixtures/serviceability_pin.json") as f:
            data = json.load(f)

            print("....................Starting seeding serviceabile pincodes..................")
            for d in data:
                try:
                    ServiceablePincode.objects.get_or_create(
                        partner_id=d['partner_id'],
                        courier_partner=d['courier_partner'], 
                        pincode=d['pincode'], 
                        city=d['city'], 
                        state=d['state'], 
                        branch_code=d['branch_code'],
                        is_cod= True if d['is_cod'] == "y" else False, 
                        status= True if d['status'] == "y" else False, 
                        active= True if d['active'] == 'y' else False, 
                        remark=d['remark'], cluster_code=d['cluster_code'])
                except Exception as e:
                    print(str(e))
                    pass
            print("Ending seeding serviceabile pincodes")
