def count_duplicate(str1, str2):
    token1 = str1.split()
    token2 = str2.split()
    if str1 == str2:
        return 100
    count = 0
    for token in token2:
        if token in token1:
            count += 1
    # percent = mark*100/length(total)
    return count*100/len(token1)


def info_matcher(info1, info2):
    drop_keys = ['label', 'title', 'name']
    for key in info1:
        if (key in drop_keys):
            continue
        value1 = str(info1.get(key)).lower()
        value2 = str(info2.get(key)).lower()
        if value1 != value2:
            return False
    return True


def get_duplicate_phone_target_id(phone, target, title_extractor, get_info):
    title1 = phone.get('title') or phone.get('name')
    info1 = phone.get('info')
    label1 = title_extractor(title1)
    for item in target:
        title2 = item.get('title')
        info2 = get_info(item)
        label2 = title_extractor(title2)
        score = count_duplicate(label1, label2)
        if score > 50 and info_matcher(info1, info2):
            return [True, item.get('uuid'), item]
    return [False, None, None]


def get_duplicate_lap_target_id(lap, target, title_extractor, get_info):
    title1 = lap.get('title') or lap.get('name')
    info1 = lap.get('info')
    label1 = title_extractor(title1)
    for item in target:
        title2 = item.get('title')
        info2 = get_info(item)
        label2 = title_extractor(title2)
        score = count_duplicate(label1, label2)
        if score > 50 and info_matcher(info1, info2):
            return [True, item.get('uuid'), item]
    return [False, None, None]


def get_duplicate_tv_target_id(tv, target, title_extractor, get_info):
    title1 = tv.get('title') or tv.get('name')
    info1 = tv.get('info')
    label1 = title_extractor(title1)
    for item in target:
        title2 = item.get('title')
        info2 = get_info(item)
        label2 = title_extractor(title2)
        score = count_duplicate(label1, label2)
        if score > 50 and info_matcher(info1, info2):
            return [True, item.get('uuid'), item]
    return [False, None, None]
