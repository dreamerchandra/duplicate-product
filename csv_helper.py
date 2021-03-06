import uuid
from csv import DictReader, DictWriter

from helper import mkdir


def write_to_csv(row, file, dir=''):
    if (not row):
        return
    keys = list(row[0].keys())
    if dir:
        mkdir(dir)
    path = dir+'/'+file
    with open(path, "w") as outfile:
        write = DictWriter(outfile, keys)
        write.writeheader()
        write.writerows(row)


def read(path):
    with open(path) as f:
        reader = DictReader(f)
        return list(reader)


def normalize_csv(data):
    for entity in data:
        for key in entity:
            value = entity[key]
            if(isinstance(value, str)):
                entity[key] = value.lower().strip()
            elif (isinstance(value, list)):
                to_str = []
                for i in value:
                    if(isinstance(i, str)):
                        to_str.append(i.lower().strip())
                    else:
                        to_str.append(i)
                entity[key] = to_str
            else:
                entity[key] = value
        entity['info'] = {}
        entity['type'] = None
        if (not entity.get('uuid')):
            entity['uuid'] = str(uuid.uuid4())
    return data
