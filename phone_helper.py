import re

from helper import get_subsequent_int


def get_storage_from_title(title):
    index = title.find('gb/') + len('gb/')
    return get_subsequent_int(title, index)


def get_storage_from_entity(phone):
    desc = str(phone)
    index = desc.find('storage') + len('storage')
    return get_subsequent_int(desc, index)


def get_storage(phone):
    index = str(phone).find('storage')
    if index > -1:
        storage = get_storage_from_entity(phone)
    else:
        storage = get_storage_from_title(
            phone.get('name') or phone.get('title'))
    return storage


def get_ram_from_entity(phone):
    desc = str(phone)
    index = desc.find('memory_capacity') + len('memory_capacity')
    return get_subsequent_int(desc, index)


def get_ram_from_title(phone):
    # TODO: add logic
    return 0


def get_ram(phone):
    index = str(phone).find('memory_capacity')
    if index > -1:
        ram = get_ram_from_entity(phone)
    else:
        ram = get_ram_from_title(phone)
    return ram


def label_from_tittle(tittle):
    if(not isinstance(tittle, str)):
        return
    return re.split('(([1-9]\d*|0)(gb))', tittle.lower())[0].lower().strip()


def update_phone_info(phones):
    # create_csv('./out/temp.csv', phone)
    for phone in phones:
        storage = get_storage(phone)
        ram = get_ram(phone)
        label = label_from_tittle(phone.get('name') or phone.get('title'))
        phone['info'] = {
            'storage': storage,
            'ram': ram,
            'label': label,
            'enum': 'PHONE',
        }


def get_phone_info_for_target(phone):
    label = label_from_tittle(phone.get('name') or phone.get('title'))
    ram = get_subsequent_int(phone.get('RAM'), 0)
    storage = get_subsequent_int(phone.get('Storage'), 0)
    return {
        'storage': storage,
        'ram': ram,
        'label': label,
        'enum': 'PHONE',
    }
