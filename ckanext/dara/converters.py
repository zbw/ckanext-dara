def string_to_list(value, context):
    if isinstance(value, str):
        value.split(',')
    return value


def list_to_string(value, context):
    if isinstance(value, list):
        return ','.join(value)
    return value

