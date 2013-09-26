#HB 2013-06-17
#


## Level 1 just contains fields that are not in standard CKAN fields. Title,
# Author are not in here.

LEVEL_1 = {
        'PublicationDate' : 
            {'name' : 'Publication Date'},
        'Availabilitycontrolled' : 
            {'name' : 'Availability (controlled)'},
        }

LEVEL_2 = {
    'AlternativeIdentifier_ID': 
        {'name': 'Alternative Identifier'},
    'AlternativeIdentifier_Type': 
        {'name': 'Type of Alternative Identifier'},
    'Availabilityfree': 
        {'name': 'Availability (free)'},
    'CollectionDate_free': 
        {'name': 'Temporal Coverage (free)'},
    'CollectionMode_free': 
        {'name': 'Collection Mode (free)'},
    'DataCollector_name': 
        {'name': 'Data Collector'},
    'Note_text': 
        {'name': 'Notes'},
    'OtherTitle': 
        {'name': 'Other Titles'},
    'Rights': 
        {'name': 'Rights'},
    'SelectionMethod': 
        {'name': 'Sampling'},
    'TimeDimension_free': 
        {'name': 'Time Dimension (free)'},
    'Universe_area': 
        {'name': 'Geographic Coverage'},
    'Universe_sampled': 
        {'name': 'Sampled Universe'},
    'currentVersion': 
        {'name': 'Version'},
    'language': 
        {'name': 'Language'}
    }

LEVEL_3 = {
    
    'Author_name' :
        {'name' : 'Author of Publication'},
    'Publication_title':
        {'name':'Title of Pubication'},
    'Publication_Year':
        {'name': 'Year of Publication'},
    'Publication_PID':
        {'name': 'Persistent Identifier of Publication'},
    'Publication_PIDType':
        {'name': 'Type of Persistent Identifier'}

}


def dara_all_levels():
    dara_all = LEVEL_1.copy()
    dara_all.update(LEVEL_2)
    dara_all.update(LEVEL_3)
    return dara_all