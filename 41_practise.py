def merge_dicts(d1={}, d2={}):

    result = d1.copy()
    result.update(d2)
    return result

print(merge_dicts({"krishna":1}, {"nirwan":2}))