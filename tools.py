from datetime import datetime
from itertools import groupby


def group_by_uid(elements):
    groups = {}
    for uid, group in groupby(elements, lambda x: x["uid"]):
        groups[uid] = list(group)
    return groups


def find_object(start_date, objects):
    res=[]
    for obj in objects:
        if obj.start is not None:
            obj_date = datetime.strptime(obj.start, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m')
            if obj_date == start_date:
                res.append(obj)
    return res


def bytes_to_gb(bytes):
    gb = bytes / (1024 ** 3)
    return gb


def convert_data_from_db (data,acc):
    base=4294967295
    if acc==0:
        return round(bytes_to_gb(data),2)
    else:
        return round(bytes_to_gb(acc*base+data),2)

