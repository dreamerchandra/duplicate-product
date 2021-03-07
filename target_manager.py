import copy

from csv_helper import read as read_csv


class TargetManger(object):
    csv = read_csv('./data/target.csv')

    @staticmethod
    def update_uuid(row_index, uuid):
        TargetManger.csv[row_index]['uuid'] = uuid

    @staticmethod
    def _get_by_id(uuid):
        for item in TargetManger.csv:
            if item.get('uuid') == uuid:
                return item

    @staticmethod 
    def get_by_id(uuid):
        item = TargetManger._get_by_id(uuid)
        item = copy.deepcopy(item)
        if (item.get('uuid')):
            del item['uuid']
        if (item.get('duplicate')):
            del item['duplicate']
        return item

    @staticmethod
    def mark_duplicate(uuid):
        item = TargetManger._get_by_id(uuid)
        item['duplicate'] = True
    
    @staticmethod
    def get_non_duplicate():
        items = []
        for item in TargetManger.csv:
            if not item.get('duplicate'):
                items.append(item)
        return items

    @staticmethod
    def update_uuid_to_target_manager(target):
        index = 0
        for item in target:
            TargetManger.update_uuid(index, item.get('uuid'))
            index += 1
