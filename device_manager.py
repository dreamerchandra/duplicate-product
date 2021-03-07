from duplicate_manager import (get_duplicate_lap_target_id,
                               get_duplicate_phone_target_id,
                               get_duplicate_tv_target_id)
from phone_helper import get_phone_info_for_target
from phone_helper import label_from_tittle as phone_label_extractor
from pricing_manager import PricingManger
from product_manager import ProductManager


class DeviceManger:
    @staticmethod
    def is_tv(name):
        return name.lower().find(' tv') >= 0 or name.lower().find(' hd ready') >= 0

    @staticmethod
    def is_lap(name):
        possibility = ['amd', 'intel']
        # https://www.geeksforgeeks.org/python-test-if-string-contains-element-from-list/
        res = [ele for ele in possibility if(ele in name)]
        return bool(res)

    @staticmethod
    def update_info(laps, enum):
        # create_csv('./out/temp.csv', phone)
        for lap in laps:
            lap['info'] = {
                'enum': enum,
            }

    @staticmethod
    def _create_product_pricing(device, duplicate_cb, duplicate_cb_args, pricing_csv, product_csv):
        info = {
            'master_uuid': device.get('uuid'),
            'title': device.get('title') or device.get('name'),
            'info': device.get('info'),
        }
        [is_duplicated, target_uuid, target_item] = duplicate_cb(*duplicate_cb_args)
        if is_duplicated:
            info['target_uuid'] = target_uuid
            info['site_name'] = target_item.get('site_name')
            info['pricing'] = target_item.get('price')
            info['link'] = target_item.get('link')
            pricing_csv.append_row(info)
        else:
            product_csv.append_row(info)

    @staticmethod
    def create_product_pricing(phones, laps, tvs, target):
        """
            * Add pricing information if duplicated with master data
            * If it does not overlap with the master data, add the product page
        """
        pricing_csv = PricingManger()
        product_csv = ProductManager()

        for phone in phones:
            duplicate_cb_args = [
                phone, target, phone_label_extractor, get_phone_info_for_target]
            DeviceManger._create_product_pricing(
                phone, get_duplicate_phone_target_id, duplicate_cb_args, pricing_csv, product_csv)

        for lap in laps:
            duplicate_cb_args = [
                lap, target, lambda x: x, lambda x: {'enum': 'LAP'}]
            DeviceManger._create_product_pricing(
                lap, get_duplicate_lap_target_id, duplicate_cb_args, pricing_csv, product_csv)

        for tv in tvs:
            duplicate_cb_args = [
                tv, target, lambda x: x, lambda x: {'enum': 'TV'}]
            DeviceManger._create_product_pricing(
                tv, get_duplicate_tv_target_id, duplicate_cb_args, pricing_csv, product_csv)
        
        pricing_csv.write_to_csv()
        product_csv.write_to_csv()
