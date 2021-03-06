import phone_helper as PhoneHelper
from csv_helper import normalize_csv
from csv_helper import read as read_csv
from csv_helper import write_to_csv
from device_manager import DeviceManger


def split_devices(data):
    lap_list = []
    phone_list = []
    tv_list = []
    for entity in data:
        name = entity.get('name') or entity.get('title')
        tv = DeviceManger.is_tv(name)
        lap = DeviceManger.is_lap(name)
        if tv:
            tv_list.append(entity)
        elif lap:
            lap_list.append(entity)
        else:
            phone_list.append(entity)

    return phone_list, lap_list, tv_list


def main():
    master = read_csv("./data/master.csv")
    master = normalize_csv(master)
    [phone, lap, tv] = split_devices(master)
    PhoneHelper.update_phone_info(phone)
    DeviceManger.update_info(lap, 'LAP')
    DeviceManger.update_info(tv, 'TV')
    target = read_csv("./data/target.csv")
    target = normalize_csv(target)
    write_to_csv(target, 'target.csv', './out')
    DeviceManger.create_product_pricing(phone, lap, tv, target)


if __name__ == '__main__':
    main()
    
