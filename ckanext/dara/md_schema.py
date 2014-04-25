#HB 2013-06-17

from ckanext.dara.ordered_dict import OrderedDict

#XXX This is only a first rough schema implementation. I'd like better
#abstraction level, objects... We also still have presentation classes here




## Level 1 just contains fields that are not in standard CKAN fields. Title,
# Author are not in here.


LEVEL_1 = {
        'PublicationDate' : 
            {'name' : 'Publication Date'},
        
        'Availabilitycontrolled' : 
            {'name' : 'Availability (controlled)'},
        
        #actually this is Level 2, but we put it for usability reasons in level1
        'Availabilityfree':
            {'name': 'Availability (free)'}, 
        }



def level_2():
    """
    """

    fields = [

            ('OtherTitle', 
                {'form_type': 'input', 
                'name': 'Other Title',
                'role' : 'master',
                'size': 'medium',
                'placeholder': u'eg. Subtitle, alternative title',
            }), 


            ('OtherTitleType', 
                {'form_type': 'select', 
                'name': 'Type of other Title',
                'role': 'slave',
                'options' : [
                    {'value': '1', 'text' :'Alternative Title'}, 
                    {'value': '2', 'text' : 'Translated Title'}, 
                    {'value': '3', 'text' :'Subtitle'},
                    {'value' : '4', 'text' : 'Original Title'},]
            }), 
            
            ('currentVersion', 
                {'form_type': 'input', 
                'name': 'Version',
                'size': 'small',
                'placeholder': 'eg. 1.1',
            }), 

            ('language', 
                {'form_type': 'select', 
                'name': 'Language',
                'options' : [
                    {'value' : '', 'text' : ''},
                    {'value' : 'bel', 'text' : 'Belarusian'},
                    {'value' : 'bos', 'text' : 'Bosnian'},
                    {'value' : 'cze', 'text' : 'Czech'},
                    {'value' : 'dut', 'text' : 'Dutch'},
                    {'value' : 'eng', 'text' : 'English'},
                    {'value' : 'est', 'text' : 'Estonian'},
                    {'value' : 'fin', 'text' : 'Finnish'},
                    {'value' : 'fre', 'text' : 'French'},
                    {'value' : 'ger', 'text' : 'German'},
                    {'value' : 'gre', 'text' : 'Greek'},
                    {'value' : 'hrv', 'text' : 'Croatian'},
                    {'value' : 'hun', 'text' : 'Hungarian'},
                    {'value' : 'ita', 'text' : 'Italian'},
                    {'value' : 'lav', 'text' : 'Latvian'},
                    {'value' : 'lit', 'text' : 'Lithuanian'},
                    {'value' : 'nor', 'text' : 'Norwegian'},
                    {'value' : 'pol', 'text' : 'Polish'},
                    {'value' : 'rum', 'text' : 'Romanian'},
                    {'value' : 'rus', 'text' : 'Russian'},
                    {'value' : 'slo', 'text' : 'Slovak'},
                    {'value' : 'slv', 'text' : 'Slovenian'},
                    {'value' : 'spa', 'text' : 'Spanish'},
                    {'value' : 'srp', 'text' : 'Serbian'},
                    {'value' : 'swe', 'text' : 'Swedish'},
                    {'value' : 'ukr', 'text' : 'Ukrainian'},
                ]
            }), 
            
            
            ('AlternativeIdentifier_ID', 
                {'form_type': 'input', 
                'name': 'Alternative Identifier',
                'role': 'master',
                'placeholder': u'eg. ISBN, Handle, DOI',
            }),


            
            ('AlternativeIdentifier_Type', 
                {'form_type': 'select', 
                'name': 'Type of Alternative Identifier',
                'role': 'slave',
                'master': 'AlternativeIdentifier_ID',
                'options': [
                    {'text' : ''},
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
                    {'text': 'URN', 'value': 'URN'}],
                
            }),


            ('Universe_areaControlled', {'form_type': 'select', 
                'name': 'Geographic Coverage (controlled)',
                'form_type': 'select',
                'options': [
                    {'text' : ''},
                    ],
                'classes': ['todo']
                }),
            
            ('Universe_areaFree', {'form_type': 'input', 
                'name': 'Geographic Coverage (free)',
                'size': 'medium',
                'placeholder': u'eg. West-Germany',

            }),


            ('Universe_sampled', 
                {'form_type': 'input', 
                'name': 'Sampled Universe',
                'size': 'medium',
                'placeholder': u'eg. adults in Eastern and Western Germany', 

            }), 


            ('SelectionMethod', {'form_type': 'text', 
                'name': 'Sampling',
                'placeholder': u'Describe your selection method',
            }), 

            #XXX needs better date widget/selection    
            ('CollectionDate_controlled', 
                {'form_type': 'date', 
                'name': 'Collection Date (controlled)',
                'classes': ['todo']
            }), 

            ('CollectionDate_free', 
                {'form_type': 'input', 
                'name': 'Collection Date (free)',
                'size': 'medium',
                'placeholder': u'eg. Spring 1999', 

                }), 

            ('CollectionMode_controlled', 
                {'form_type': 'select', 
                'name': 'Collection Mode (controlled)',
                'options': [
                    {'value': '', 'text': ''},
                    {'value': '1', 'text': 'Interview'},
                    {'value': '2', 'text': 'Interview: Face-to-Face'},
                    {'value': '3', 'text': 'Interview: Telephone'},
                    {'value': '4', 'text': 'Interview: E-Mail'},
                    {'value': '5', 'text': 'Interview: CATI'},
                    {'value': '6', 'text': 'Interview: CAPI'},
                    {'value': '7', 'text': 'Self-completed questionnaire'},
                    {'value': '8', 'text': 'Self-completed questionnaire: Paper/Pencil'},
                    {'value': '9', 'text': 'Self-completed questionnaire: Web-based'},
                    {'value': '10', 'text': 'Self-completed questionnaire: CASI'},
                    {'value': '11', 'text': 'Self-completed questionnaire: ACASI'},
                    {'value': '12', 'text': 'Coding'},
                    {'value': '13', 'text': 'Transcription'},
                    {'value': '14', 'text': 'Compilation'},
                    {'value': '15', 'text': 'Synthesis'},
                    {'value': '16', 'text': 'Recording'},
                    {'value': '17', 'text': 'Simulation'},
                    {'value': '18', 'text': 'Observation'},
                    {'value': '19', 'text': 'Observation: Field'},
                    {'value': '20', 'text': 'Observation: Laboratory'},
                    {'value': '21', 'text': 'Observation: Participant'},
                    {'value': '22', 'text': 'Experiments'},
                    {'value': '23', 'text': 'Focus Group'},
                    {'value': '24', 'text': 'Other'},
                ],
                
            }), 
            
            
            ('CollectionMode_free', 
                {'form_type': 'input', 
                'name': 'Collection Mode (free)',
                'size': 'medium',
                'placeholder': u'eg. Interview',
            }), 

                
            ('TimeDimension_controlled', 
                {'form_type': 'select', 
                'name': 'Time Dimension (controlled)',
                'options': [
                    {'value': '', 'text': ''},
                    {'value': '1', 'text':'Longitudinal '}, 
                    {'value': '2', 'text': 'Longitudinal.CohortEventBased '}, 
                    {'value': '3', 'text':'Longitudinal.TrendRepeatedCrossSection '},
                    {'value': '4', 'text': 'Longitudinal.Panel '},
                    {'value': '5', 'text': 'Longitudinal.Panel.Continuous'},
                    {'value': '6', 'text': 'Longitudinal: Panel: Interval'},
                    {'value': '7', 'text': 'Time Series'},
                    {'value': '8', 'text': 'TimeSeries: Continuous'},
                    {'value': '9', 'text': 'TimeSeries: Discrete'},
                    {'value': '10', 'text': 'Cross-section'},
                    {'value': '11', 'text': 'Cross-section ad-hoc follow-up'},
                    {'value': '12', 'text': 'Other'}],
                }), 
            
            ('TimeDimension_free', 
                {'form_type': 'input', 
                'name': 'Time Dimension (free)',
                'size': 'medium',
                'placeholder': u'eg. Zeitreihe',
            }), 


            #TODO DataCollector has several attributes
            ('DataCollector_name', 
                    {'form_type': 'input', 
                    'name': 'Data Collector',
                    'classes': ['todo'], 
                    'placeholder': u'eg. EMNID', 
             }),

            ('Rights', 
                    {'form_type': 'input', 'name': 'Rights',
                     'size': 'medium',
                    'placeholder': u'eg. Copyright Joe Biggs',
            }), 
            
                       
            ('Note_text', 
                {'form_type': 'text', 'name': 'Notes',
                    'placeholder': u'any additional notes',
            })
                    
                        
        ]


    schema = OrderedDict(fields)
    return schema




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
            
            ('DocType',
                {'name': 'Document Type', 'form_type': 'select',
                    'options': [
                        {'text': '', 'value': ''}, 
                        {'text': 'Working Paper', 'value': '1'}, 
                        {'text': 'Article', 'value': '2'}, 
                        {'text': 'Report', 'value': '3'}, 
                        {'text': 'Book/Monograph', 'value': '4'}, 
                        {'text': 'Manuscript', 'value': '5'}, 
                        {'text': 'Reference Book', 'value': '6'}, 
                        {'text': 'Review', 'value': '7'}, 
                        {'text': 'Series', 'value': '8'}, 
                        {'text': 'Journal', 'value': '9'}, 
                        {'text': 'Magazine', 'value': '10'}
                    ],
                    
                })

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
LEVEL_2 = level_2()
LEVEL_3 = level_3()
