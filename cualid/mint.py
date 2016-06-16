import uuid


def hamming(s1, s2):
    count_diff = 0
    for i1, i2 in zip(s1, s2):
        if i1 != i2:
            count_diff += 1
    return count_diff


def at_least_distance(query, existing, d=3):
    for e in existing:
        if hamming(query, e) < d:
            return False
    return True


def create_ids(n, id_length,
               min_distance=3,
               failure_threshold=0.99,
               existing_ids=None):
    if existing_ids is not None:
        hrids = existing_ids
    else:
        hrids = []
    uuids = []
    initial_hrid_len = len(hrids)
    failures = 0
    trys = 1
    while len(hrids) - initial_hrid_len < n and failures/trys < failure_threshold:
        trys += 1
        uuid_ = uuid.uuid4()
        hrid = uuid_.hex[-id_length:]
        if at_least_distance(hrid, hrids, d=min_distance):
            uuids.append(uuid_)
            hrids.append(hrid)
            yield (uuid_, hrid)
        else:
            failures += 1
