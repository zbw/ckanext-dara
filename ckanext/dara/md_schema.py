#HB 2013-06-17

from ckanext.dara.ordered_dict import OrderedDict



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
    'CollectionDate_controlled' :
        {'name': "Collection Date (controlled)"},
    'CollectionDate_free': 
        {'name': 'Temporal Coverage (free)'},
    'CollectionMode_controlled': 
        {'name': 'Collection Mode (controlled)'},
    'CollectionMode_free': 
        {'name': 'Collection Mode (free)'},
    'DataCollector_name': 
        {'name': 'Data Collector'},
    'Note_text': 
        {'name': 'Notes'},
    'OtherTitle': 
        {'name': 'Other Title'},
    'OtherTitleType' :
        {'name' : 'Type of other Title'},
    'Rights': 
        {'name': 'Rights'},
    'SelectionMethod': 
        {'name': 'Sampling'},
    'TimeDimension_controlled' :
        {'name': 'Time Dimension (controlled)'},
    'TimeDimension_free': 
        {'name': 'Time Dimension (free)'},
    'Universe_areaControlled' :
        {'name' : 'Geographic Coverage (controlled)'},
    'Universe_areaFree': 
        {'name': 'Geographic Coverage (free)'},
    'Universe_sampled': 
        {'name': 'Sampled Universe'},
    'currentVersion': 
        {'name': 'Version'},
    'language': 
        {'name': 'Language'},
    'DescriptionType' : 
        {'name' : 'Type of Description'},
    }


def level_3():
    """
    """
    fields = [
            ('DataSet_dataType', 
                {'name': 'Type of Units', 
                'form_type': 'input',
                }
            ),
            ('DataSet_numberUnits', {
                'name': 'Number of Units',
                'form_type': 'input',
                'size': 'small',
                }
            ),
            ('DataSet_numberVariables', {
                'name': 'Number of Variables',
                'form_type': 'input',
                'size': 'small',
                }
            ),
            ('DataSet_dataType', {
                'name': 'Type of Data',
                'form_type': 'input',
                }
            ),
            

            #XXX all File_ fields are problematic since we do allow more than one
            #datafile in each data set, so this fields should probably better
            #go into resource metadata fields (which we do not provide at the
            #moment)
            
            ('File_format', {
                'name': 'File Format',
                'form_type' : 'small',
                }
            ),
            ('File_size', {
                'name': 'Size',
                'form_type': 'input',
                'size': 'small',
                }
            ),
            ('File_fingerprint', {
                'name': 'Data Fingerprint',
                'form_type': 'input',
                'role': 'master'
                }
            ),
            ('File_fingerprintMethod', {
                'name': 'Method Fingerprint',
                'form_type': 'input',
                'size': 'small',
                'role': 'slave'
                }
            ),
            
        ]


    schema = OrderedDict(fields)
    return schema



def publication_fields():
    """
    testing
    """
    
    fields = [
            ('Author', {'name': 'Author of Publication',
                'form_type': 'input', 'size' : 'medium'}),

            ('Editor', {'name': 'Editor',
                'form_type': 'input', 'size' : 'medium'}),

                        
            ('Title',
                {'name': 'Title of Publication',
                'form_type': 'input', 'size' : 'medium'}),
            
            ('Year',
                {'name': 'Year of Publication',
                'form_type': 'input'}),
            
            ('Publisher',
                {'name': 'Publisher',
                'form_type': 'input', 'size' : 'medium'}),

            ('PID',
                {'name': 'Persistent Identifier of Publication',
                    'form_type': 'input', 'role' : 'master' }),

            ('PIDType',
                {'name': 'Type of Persistent Identifier',
                'form_type': 'select',
                'role' : 'slave',
                'master' : 'PID',
                'options': [
                    {'text': '', 'value': ''},
                    {'text': 'DOI', 'value': 'DOI'}, 
                    {'text': 'ARK', 'value': 'ARK'}, 
                    {'text': 'EAN13', 'value': 'EAN13'}, 
                    {'text': 'EISSN', 'value': 'EISSN'}, 
                    {'text': 'Handle', 'value': 'Handle'}, 
                    {'text': 'ISBN', 'value': 'ISBN'}, 
                    {'text': 'ISSN', 'value': 'ISSN'}, 
                    {'text': 'ISTC', 'value': 'ISTC'}, 
                    {'text': 'LISSN', 'value': 'LISSN'}, 
                    {'text': 'LSID', 'value': 'LSID'}, 
                    {'text': 'PURL', 'value': 'PURL'}, 
                    {'text': 'UPC', 'value': 'UPC'}, 
                    {'text': 'URL', 'value': 'URL'}, 
                    {'text': 'URN', 'value': 'URN'}
                    ],
            }),

            ('Place',
                {'name': 'Place',
                'form_type': 'input'}),

            ('Journal',
                {'name': 'Journal',
                    'form_type': 'input', 'size' : 'medium'}),

            ('Volume',
                {'name': 'Volume',
                    'form_type': 'input', 'size': 'small'}),

            ('Issue',
                {'name': 'Issue',
                    'form_type': 'input', 'size': 'small'}),

            ('Anthology',
                {'name': 'Anthology',
                        'form_type': 'input', 'size': 'medium'}),
            
            ('Pages',
                {'name': 'Pages',
                        'form_type': 'input', 'size': 'small'}),
            
            ('ISBN',
                {'name': 'ISBN',
                'form_type': 'input', 'size': 'small'}),
            
            ('ISSN',
                {'name': 'ISSN', 'form_type': 'input', 'size': 'small'}),
            
            ('RelationType',
                {'name': 'Relation Type', 'form_type': 'text'}),

            ]



    #import pdb; pdb.set_trace()

    schema = OrderedDict(fields)
    return schema


#TODO: publications not in here yet; level_3 probably not working since we
#rebuild it with OrderedDict
def dara_all_levels():
    dara_all = LEVEL_1.copy()
    dara_all.update(LEVEL_2)
    dara_all.update(LEVEL_3)
    return dara_all



#for legacy code
PUBLICATION = publication_fields()
LEVEL_3 = level_3()
