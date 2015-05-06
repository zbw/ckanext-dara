from pylons import config
import ckan.plugins.toolkit as tk

#OrderedDict is not available in Python < 2.7
try:
    from collections import OrderedDict   # 2.7
except ImportError:
    from sqlalchemy.util import OrderedDict

from collections import namedtuple




#XXX this functional (in this case: immutable) approach is for now a bit
#inconsistent, since we'll mix it with mutable classes/objects. We should,
#however, return all schema objects as immutable objects
DaraField = namedtuple('DaraField', 'id level adapt widget')


#class DaraField(object):
#   """
#   """

#   def __init__(self, id, level, adapt, widget):

#       self.id = id
#       self.level = level
#       self.adapt = adapt
#       self.widget = widget


class DaraWidget(object):
    """
    """

    def __init__(self, form_type='input', name=u'', role=None, classes=[]):
        """
        """

        self.form_type = form_type
        self.name = name
        self.role = role
        self.classes = classes


class Input(DaraWidget):
    """
    """
    def __init__(self, size='', placeholder='', **kw):
        """
        """
        super(Input, self).__init__(**kw)
        self.size = size
        self.placeholder = placeholder


class Select(DaraWidget):
    """
    """

    def __init__(self, options, **kw):
        """
        """

        super(Select, self).__init__(**kw)
        self.form_type = 'select'
        self.options = options


class Text(DaraWidget):
    """
    """

    def __init__(self, placeholder='', **kw):
        """
        """
        super(Text, self).__init__(**kw)
        self.form_type = 'text'


class Date(DaraWidget):
    """
    """

    def __init__(self, **kw):
        """
        """
        super(Date, self).__init__(**kw)
        self.form_type = "date"



def __transform(fields):
    """
    """
    FieldProperties = namedtuple('FieldProperties', 'level adapt widget')
    f = map(lambda field: (field.id, FieldProperties(field.level, field.adapt, 
        field.widget.__dict__)), fields)
    
    #import pdb; pdb.set_trace()
    return OrderedDict(f)


def testfields():
    """
    for developing purposes
    """
    
    fields = (
        
        DaraField(
            'PublicationDate',
            1, 
            ('dataset', 'resource'),
            Input(
                placeholder="eg. 2011",
                name="Publication Year",
                size='small',
                classes=['dara_required']
                )
            ),

        DaraField('Availabilitycontrolled',
            1, ('dataset', 'resource'),
            Select(
                options=[
                    {'value': '1', 'text': 'Free Download'},
                    {'value': '2', 'text': 'Delivery on demand'},
                    {'value': '3', 'text': 'Onsite only'},
                    {'value': '4', 'text': 'Not available'},
                    {'value': '5', 'text': 'Unknown'},
                    ],
                name = 'Availability (controlled)',
                classes = ['dara_required']
                ),
            ),

    )
    return __transform(fields)
    

def fields():
    """
    main function that generates most of da|ra metadata fields
    """

    fields = (

        DaraField('PublicationDate',
            1, ('dataset', 'resource'),
            Input(
                placeholder="eg. 2011",
                name="Publication Year",
                size='small',
                classes=['dara_required']
                )
            ),

        DaraField('Availabilitycontrolled',
            1, ('dataset', 'resource'),
            Select(
                options=[
                    {'value': '1', 'text': 'Free Download'},
                    {'value': '2', 'text': 'Delivery on demand'},
                    {'value': '3', 'text': 'Onsite only'},
                    {'value': '4', 'text': 'Not available'},
                    {'value': '5', 'text': 'Unknown'},
                    ],
                name = 'Availability (controlled)',
                classes = ['dara_required']
                ),
            ),
        
        DaraField('Availabilityfree',
            1, ('dataset', 'resource'),

            Input(
                name = 'Availability (free)',
                size = 'medium',
                placeholder = 'eg. Die Datennutzung unterliegt \
                        schriftlichen Datenschutzvereinbarungen',
                )
            ),
    
        
        DaraField('OtherTitle',
            2, ('dataset', 'resource'),
            Input(
            placeholder = 'eg. Subtitle, alternative title',
            role = 'master',
            name = 'Other Title',
            size = 'medium',
            )
        ),

        DaraField('OtherTitleType',
            2, ('dataset', 'resource'),
            Select(
            role = 'slave',
            name = 'Type of other Title',
            options = [
                {'text': 'Alternative Title', 'value': '1'}, 
                {'text': 'Translated Title', 'value': '2'}, 
                {'text': 'Subtitle', 'value': '3'}, 
                {'text': 'Original Title', 'value': '4'}],
            )
        ),

        
        DaraField('currentVersion',
                2, ('dataset', 'resource'),
                Input(
                placeholder = 'eg. 1.1',
                name = 'Version',
                size = 'small',
                )
        ),

        DaraField('language',
                    2, ('dataset', 'resource'),

                Select(
                name = 'Language',
                options = [
                    {'text': '', 'value': ''}, 
                    {'text': 'Belarusian', 'value': 'bel'}, 
                    {'text': 'Bosnian', 'value': 'bos'}, 
                    {'text': 'Czech', 'value': 'cze'}, 
                    {'text': 'Dutch', 'value': 'dut'}, 
                    {'text': 'English', 'value': 'eng'}, 
                    {'text': 'Estonian', 'value': 'est'}, 
                    {'text': 'Finnish', 'value': 'fin'}, 
                    {'text': 'French', 'value': 'fre'}, 
                    {'text': 'German', 'value': 'ger'}, 
                    {'text': 'Greek', 'value': 'gre'}, 
                    {'text': 'Croatian', 'value': 'hrv'}, 
                    {'text': 'Hungarian', 'value': 'hun'}, 
                    {'text': 'Italian', 'value': 'ita'}, 
                    {'text': 'Latvian', 'value': 'lav'}, 
                    {'text': 'Lithuanian', 'value': 'lit'}, 
                    {'text': 'Norwegian', 'value': 'nor'}, 
                    {'text': 'Polish', 'value': 'pol'}, 
                    {'text': 'Romanian', 'value': 'rum'}, 
                    {'text': 'Russian', 'value': 'rus'}, 
                    {'text': 'Slovak', 'value': 'slo'}, 
                    {'text': 'Slovenian', 'value': 'slv'}, 
                    {'text': 'Spanish', 'value': 'spa'}, 
                    {'text': 'Serbian', 'value': 'srp'}, 
                    {'text': 'Swedish', 'value': 'swe'}, 
                    {'text': 'Ukrainian', 'value': 'ukr'}],
                )
        ),

        DaraField('AlternativeIdentifier_ID',
                2, ('dataset', 'resource'),

                Input(
                placeholder = 'eg. ISBN, Handle, DOI',
                role = 'master',
                name = 'Alternative Identifier',
                )
        ),

        DaraField('AlternativeIdentifier_Type',
                2, ('dataset', 'resource'),

                Select(
                role = 'slave',
                name = 'Type of Alternative Identifier',
                options = [
                    {'text': ''}, 
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
                )
        ),

        DaraField('geographicCoverage',
                2, ('dataset', 'resource'),

                Select(
                classes = ['todo'],
                name = 'Geographic Coverage (controlled)',
                options = [{'text': ''}],
                )
        ),

        DaraField('geographicCoverageFree',
                2, ('dataset', 'resource'),

                Input(
                placeholder = 'eg. West-Germany',
                name = 'Geographic Coverage (free)',
                size = 'medium',
                )
        ),
        
        DaraField('sampling',
                2, ('dataset', 'resource'),

                Input(
                    placeholder= 'test',
                    name='test universe',
                    size = 'medium'
                    )
                ),

        DaraField('universeSampled',
                2, ('dataset', 'resource'),

                Input(
                placeholder = 'eg. adults in Eastern and Western Germany',
                name = 'Sampled Universe',
                size = 'medium',
                )
        ),

        DaraField('Sampling',
                2, ('dataset', 'resource'),

                Text(
                placeholder = 'Describe your selection method',
                name = 'Sampling',
                )
        ),

        DaraField('CollectionDate_controlled',
                2, ('dataset', 'resource'),

                Date(
                classes = ['todo'],
                name = 'Collection Date (controlled)',
                )
        ),

        DaraField('CollectionDate_free',
                2, ('dataset', 'resource'),

                Input(
                placeholder = 'eg. Spring 1999',
                name = 'Collection Date (free)',
                size = 'medium',
                )
        ),

        DaraField('CollectionMode_controlled',
                2, ('dataset', 'resource'),

                Select(
                name = 'Collection Mode (controlled)',
                options = [
                    {'text': '', 'value': ''}, 
                    {'text': 'Interview', 'value': '1'}, 
                    {'text': 'Interview: Face-to-Face', 'value': '2'}, 
                    {'text': 'Interview: Telephone', 'value': '3'}, 
                    {'text': 'Interview: E-Mail', 'value': '4'}, 
                    {'text': 'Interview: CATI', 'value': '5'}, 
                    {'text': 'Interview: CAPI', 'value': '6'}, 
                    {'text': 'Self-completed questionnaire', 'value': '7'}, 
                    {'text': 'Self-completed questionnaire: Paper/Pencil', 'value': '8'}, 
                    {'text': 'Self-completed questionnaire: Web-based', 'value': '9'}, 
                    {'text': 'Self-completed questionnaire: CASI', 'value': '10'}, 
                    {'text': 'Self-completed questionnaire: ACASI', 'value': '11'}, 
                    {'text': 'Coding', 'value': '12'}, {'text': 'Transcription', 'value': '13'}, 
                    {'text': 'Compilation', 'value': '14'}, 
                    {'text': 'Synthesis', 'value': '15'}, 
                    {'text': 'Recording', 'value': '16'}, 
                    {'text': 'Simulation', 'value': '17'}, 
                    {'text': 'Observation', 'value': '18'}, 
                    {'text': 'Observation: Field', 'value': '19'}, 
                    {'text': 'Observation: Laboratory', 'value': '20'}, 
                    {'text': 'Observation: Participant', 'value': '21'}, 
                    {'text': 'Experiments', 'value': '22'}, 
                    {'text': 'Focus Group', 'value': '23'}, 
                    {'text': 'Other', 'value': '24'}],
                )
        ),

        DaraField('CollectionMode_free',
                2, ('dataset', 'resource'),

                Input(
                placeholder = 'eg. Interview',
                name = 'Collection Mode (free)',
                size = 'medium',
                )
        ),

        DaraField('TimeDimension_controlled',
                2, ('dataset', 'resource'),

                Select(
                name = 'Time Dimension (controlled)',
                options = [
                    {'text': '', 'value': ''}, 
                    {'text': 'Longitudinal ', 'value': '1'}, 
                    {'text': 'Longitudinal.CohortEventBased ', 'value': '2'}, 
                    {'text': 'Longitudinal.TrendRepeatedCrossSection ', 'value': '3'}, 
                    {'text': 'Longitudinal.Panel ', 'value': '4'}, 
                    {'text': 'Longitudinal.Panel.Continuous', 'value': '5'}, 
                    {'text': 'Longitudinal: Panel: Interval', 'value': '6'}, 
                    {'text': 'Time Series', 'value': '7'}, 
                    {'text': 'TimeSeries: Continuous', 'value': '8'}, 
                    {'text': 'TimeSeries: Discrete', 'value': '9'}, 
                    {'text': 'Cross-section', 'value': '10'}, 
                    {'text': 'Cross-section ad-hoc follow-up', 'value': '11'}, 
                    {'text': 'Other', 'value': '12'}],
                )
        ),

        DaraField('TimeDimension_free',
                2, ('dataset', 'resource'),

                Input(
                placeholder = 'eg. Zeitreihe',
                name = 'Time Dimension (free)',
                size = 'medium',
                )
        ),

        DaraField('Frequency',
                2, ('dataset', 'resource'),

                Input(
                    name='Frequency',
                    placeholder="eg. weekly, monthly",
                    )
        ),


        DaraField('DataCollector_name',
                2, ('dataset', 'resource'),

                Input(
                classes = ['todo'],
                placeholder = 'eg. EMNID',
                name = 'Data Collector',
                )
        ),

        DaraField('Rights',
                2, ('dataset', 'resource'),

                Input(
                placeholder = 'eg. Copyright Joe Biggs',
                name = 'Rights',
                size = 'medium',
                )
        ),

        DaraField('Note_text',
                2, ('dataset', 'resource'),

                Text(
                placeholder = 'any additional notes',
                name = 'Notes',
                )
        ),


        DaraField('currentVersion',
            2, ('resource'),

            Input(
                name="Version",
                placeholder="eg. '1' or '2.2'"
                )
            ),
                    
        DaraField('DataSet_unitType',
            2, ('resource'),    
            Input(
            name = 'Type of Units',
            placeholder='eg. persons, households, firms'
            )
        ),

        DaraField('DataSet_numberUnits',
            2, ('resource'),
            Input(
            name = 'Number of Units',
            placeholder='eg 3456',
            size = 'small',
            )
        ),

        DaraField('DataSet_numberVariables',
            2, ('resource'),
            Input(
            name= 'Number of Variables',
            placeholder= 'eg. 210',
            size = 'small',
            )
        ),

        DaraField('DataSet_dataType',
            2, ('resource'),
            Input(
            name = 'Type of Data',
            placeholder= ''
            )
        ),


        #TODO get automatically 
        DaraField('File_size',
            2, ('resource'),
            Input(
            name = 'File Size (MB)',
            size = 'small',
            classes=['todo'],
            placeholder='will be calculated automatically',
            )
        ),

        DaraField('File_fingerprint',
            2, ('resource'),
            Input(
            role = 'master',
            name = 'Data Fingerprint',
            placeholder='eg. 00994e0caa89bc6bf394c12d9a2e72e6',
            )
        ),

        DaraField('File_fingerprintMethod',
            2, ('resource'),
            Input(
            role = 'slave',
            name = 'Method Fingerprint',
            size = 'small',
            placeholder='eg. MD5'
            )
        ),

    )
    return __transform(fields)



def publication_fields():
    """
    """
    fields = (

        DaraField('Publication_Author',
                3, ('dataset', 'resource'),
                Input(
                name = 'Author of Publication',
                size = 'medium',
                )
        ),

        DaraField('Publication_Editor',
                3, ('dataset', 'resource'),
                Input(
                name = 'Editor',
                size = 'medium',
                )
        ),

        DaraField('Publication_Title',
            3, ('dataset', 'resource'),

            Input(
                name = 'Title of Publication',
                size = 'medium',
                )
        ),

        DaraField('Publication_Year',
            3, ('dataset', 'resource'),

            Input(
                name = 'Year of Publication',
                )
        ),

        DaraField('Publication_Publisher',
            3, ('dataset', 'resource'),

            Input(
                name = 'Publisher',
                size = 'medium',
                )
        ),

        DaraField('Publication_PID',
            3, ('dataset', 'resource'),

            Input(
                role = 'master',
                name = 'Persistent Identifier of Publication',
                )
        ),

        DaraField('Publication_PIDType',
                3, ('dataset', 'resource'),

                Select(
                role = 'slave',
                name = 'Type of Persistent Identifier',
                options = [
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
                    {'text': 'URN', 'value': 'URN'}],
                )
        ),

        DaraField('Publication_Place',
            3, ('dataset', 'resource'),

                Input(
                name = 'Place',
                )
        ),

        DaraField('Publication_Journal',
            3, ('dataset', 'resource'),

                Input(
                name = 'Journal',
                size = 'medium',
                )
        ),

        DaraField('Publication_Volume',
            3, ('dataset', 'resource'),

                Input(
                name = 'Volume',
                size = 'small',
                )
        ),

        DaraField('Publication_Issue',
            3, ('dataset', 'resource'),

                Input(
                name = 'Issue',
                size = 'small',
                )
        ),

        DaraField('Publication_Anthology',
            3, ('dataset', 'resource'),

                Input(
                name = 'Anthology',
                size = 'medium',
                )
        ),

        DaraField('Publication_Pages',
            3, ('dataset', 'resource'),

                Input(
                name = 'Pages',
                size = 'small',
                )
        ),

        DaraField('Publication_ISBN',
            3, ('dataset', 'resource'),

                Input(
                name = 'ISBN',
                size = 'small',
                )
        ),

        DaraField('Publication_ISSN',
            3, ('dataset', 'resource'),

                Input(
                name = 'ISSN',
                size = 'small',
                )
        ),

        DaraField('Publication_RelationType',
            3, ('dataset', 'resource'),

                Text(
                name = 'Relation Type',
                )
        ),

        DaraField('Publication_DocType',
            3, ('dataset', 'resource'),

                Select(
                name = 'Document Type',
                options = [
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
                    {'text': 'Magazine', 'value': '10'}],
                )
        ),

    
    )
    return __transform(fields)



def auto_fields(pkg):
    """
    auto generated metadata without form fields. needs pkg
    """
    
    auto = {}
    
    #XXX this needs to be adapted when we know how to submit Datasets vs.
    #Resources to dara. For now everything is a Dataset. A Collection would
    #be 1
    resource_type = '2'
        
    site_url = config.get('ckan.site_url')

    #for development
    if 'localhost' in site_url:
        site_url = "http://edawax.de"
    
    pkg_url = tk.url_for(controller='package', action='read', id=pkg['name'])
    dara_url = site_url + pkg_url
    

    auto['URL'] = dara_url
    auto['ResourceType'] = resource_type

    return auto



def hidden_fields():
    """
    hidden fields, not mutable by user
    """

    fields = (
            'DOI', 
            'DOI_Proposal', 
            'created', 
            'registered', 
            'updated',
            )
    return fields


def all_fields():
    """
    """
    dara_all = fields().copy()
    dara_all.update(publication_fields())
    return dara_all








