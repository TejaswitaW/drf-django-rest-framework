import json
# checking the data coming is valid json data or not
def is_json(data):
    try:
        p_data = json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid