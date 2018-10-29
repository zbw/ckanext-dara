def string_to_list(value, context):
    if isinstance(value, basestring):
        value.split(',')
    return value
 

def list_to_string(value, context):
    print('\n\nHere\n\n')
    if isinstance(value, list):
        return ','.join(value)
    return value

