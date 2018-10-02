# Hendrik Bunke
# ZBW - Leibniz Information Centre for Economics

from collections import namedtuple
from datetime import datetime

# TODO: make field selection/config runtime-editable (instead of commenting
# them out)


# Widgets are designed as subclasses of DaraWidget
class DaraWidget(object):
    """
    base class for all dara form widgets
    """
    def __init__(self, form_type='input', name=u'', role=None, classes=[],
            info=u''):
        self.form_type = form_type
        self.name = name
        self.role = role
        self.classes = classes
        self.info = info


class Input(DaraWidget):
    """
    DaraWidget for input fields
    """
    def __init__(self, size='', placeholder='', **kw):
        super(Input, self).__init__(**kw)
        self.size = size
        self.placeholder = placeholder


class Select(DaraWidget):
    """
    DaraWidget for select fields
    """
    def __init__(self, options, **kw):
        super(Select, self).__init__(**kw)
        self.form_type = 'select'
        self.options = options


class Text(DaraWidget):
    """
    DaraWidget for textfields
    """
    def __init__(self, placeholder='', **kw):
        super(Text, self).__init__(**kw)
        self.form_type = 'text'


class Date(DaraWidget):
    """
    DaraWidget for date fields
    """
    def __init__(self, **kw):
        super(Date, self).__init__(**kw)
        self.form_type = "date"


class Number(DaraWidget):
    """
    DaraWidget for numeric fields
    """
    def __init__(self, placeholder='', size='', mi='', ma='', **kw):
        super(Number,self).__init__(**kw)
        self.size = size
        self.placeholder = placeholder
        self.form_type="number"
        self.min = mi
        self.max = ma




def fields():
    """
    main function that returns most of da|ra metadata fields
    """

    DaraField = namedtuple('DaraField', 'id adapt validators widget')

    fields = (

        DaraField('PublicationDate',
            ('dataset', 'data', 'text', 'code'), ('not_empty',),
            Number(
                placeholder="eg. 2011",
                name="Publication Year",
                size='small',
                mi = 1000,
                ma = datetime.now().year,
                classes=['dara_required'],
                info=u"""Please provide the publication year of your
                    article."""
                )
        ),

        DaraField('Availabilitycontrolled',
            ('data'), ('ignore_missing',), # no not_empty here since we have 1 as default in dara xml anyways
            Select(
                options=[
                    {'value': 'Download', 'text': 'Free Download'},
                    {'value': 'Delivery', 'text': 'Delivery on demand'},
                    {'value': 'OnSite', 'text': 'Onsite only'},
                    {'value': 'NotAvailable', 'text': 'Not available'},
                    {'value': 'Unknown', 'text': 'Unknown'},
                ],
                name='Availability',
                classes=['dara_required'],
                info=u"""By default the availability is 'Free Download'. Please change it to 'Onsite Only,' if you've provided a link or DOI to a dataset that you cannot upload for legal reasons (see 'URL' field above).""",

            ),
        ),


      # DaraField('Availabilityfree',
      #     ('dataset'), ('ignore_missing',),

      #     Input(
      #         name = 'Availability (free)',
      #         size = 'medium',
      #         placeholder = 'eg. Die Datennutzung unterliegt schriftlichen Datenschutzvereinbarungen',
      #         )
      #     ),


       #DaraField('OtherTitle',
       #    ('dataset', 'data', 'text', 'code'), ('ignore_missing',),
       #    Input(
       #    placeholder = 'eg. Subtitle, alternative title',
       #    role = 'master',
       #    name = 'Other Title',
       #    size = 'medium',
       #    )
       #),

       #DaraField('OtherTitleType',
       #    ('dataset', 'data', 'text', 'code'), ('ignore_missing',),
       #    Select(
       #    role = 'slave',
       #    name = 'Type of other Title',
       #    options = [
       #        {'text': 'Alternative Title', 'value': '1'},
       #        {'text': 'Translated Title', 'value': '2'},
       #        {'text': 'Subtitle', 'value': '3'},
       #        {'text': 'Original Title', 'value': '4'}],
       #    )
       #),


        DaraField('currentVersion',
                ('dataset', 'data', 'code'), ('not_empty',),
                Input(
                placeholder = 'eg. 1.1',
                name = 'Version',
                size = 'small',
                classes= ['dara_required'],
                info=u"""The default version number is 1. This should only be changed in the case of minor revisions (eg. 1.1) or major revisions (eg. 2) to your submitted data."""
                )
        ),

        # language is ALWAYS supposed to be "English"
       #DaraField('language',
       #            ('dataset', 'data', 'text', 'code'), ('ignore_missing',),
       #        Select(
       #        name = 'Language',
       #        options = [
       #            {'text': 'English', 'value': 'eng'},
       #            {'text': 'Belarusian', 'value': 'bel'},
       #            {'text': 'Bosnian', 'value': 'bos'},
       #            {'text': 'Czech', 'value': 'cze'},
       #            {'text': 'Dutch', 'value': 'dut'},
       #            {'text': 'Estonian', 'value': 'est'},
       #            {'text': 'Finnish', 'value': 'fin'},
       #            {'text': 'French', 'value': 'fre'},
       #            {'text': 'German', 'value': 'ger'},
       #            {'text': 'Greek', 'value': 'gre'},
       #            {'text': 'Croatian', 'value': 'hrv'},
       #            {'text': 'Hungarian', 'value': 'hun'},
       #            {'text': 'Italian', 'value': 'ita'},
       #            {'text': 'Latvian', 'value': 'lav'},
       #            {'text': 'Lithuanian', 'value': 'lit'},
       #            {'text': 'Norwegian', 'value': 'nor'},
       #            {'text': 'Polish', 'value': 'pol'},
       #            {'text': 'Romanian', 'value': 'rum'},
       #            {'text': 'Russian', 'value': 'rus'},
       #            {'text': 'Slovak', 'value': 'slo'},
       #            {'text': 'Slovenian', 'value': 'slv'},
       #            {'text': 'Spanish', 'value': 'spa'},
       #            {'text': 'Serbian', 'value': 'srp'},
       #            {'text': 'Swedish', 'value': 'swe'},
       #            {'text': 'Ukrainian', 'value': 'ukr'}],
       #        )
       #),

        #XXX deselected
       #DaraField('AlternativeIdentifier_ID',
       #     ('dataset', 'data', 'text', 'code'), ('ignore_missing',),

       #        Input(
       #        placeholder = 'eg. ISBN, Handle, DOI',
       #        role = 'master',
       #        name = 'Alternative Identifier',
       #        )
       #),
       #DaraField('AlternativeIdentifier_Type',
       #         ('dataset', 'data', 'text', 'code'), ('ignore_missing',),

       #        Select(
       #        role = 'slave',
       #        name = 'Type of Alternative Identifier',
       #        options = [
       #            {'text': ''},
       #            {'text': 'DOI', 'value': 'DOI'},
       #            {'text': 'ARK', 'value': 'ARK'},
       #            {'text': 'EAN13', 'value': 'EAN13'},
       #            {'text': 'EISSN', 'value': 'EISSN'},
       #            {'text': 'Handle', 'value': 'Handle'},
       #            {'text': 'ISBN', 'value': 'ISBN'},
       #            {'text': 'ISSN', 'value': 'ISSN'},
       #            {'text': 'ISTC', 'value': 'ISTC'},
       #            {'text': 'LISSN', 'value': 'LISSN'},
       #            {'text': 'LSID', 'value': 'LSID'},
       #            {'text': 'PURL', 'value': 'PURL'},
       #            {'text': 'UPC', 'value': 'UPC'},
       #            {'text': 'URL', 'value': 'URL'},
       #            {'text': 'URN', 'value': 'URN'}],
       #        )
       #),


        #TODO erstmal raus wegen fehlendem Vokabular
       #DaraField('geographicCoverage',
       #         ('dataset', 'data'), ('ignore_missing',),

       #        Select(
       #        classes = ['todo'],
       #        name = 'Geographic Coverage (controlled)',
       #        options = [{'text': ''}],
       #        )
       #),


        DaraField('geographicCoverageFree',
                 ('data',), ('ignore_missing', 'dara'),
                Input(
                placeholder = 'eg. West-Germany',
                name = 'Geographic Coverage (free)',
                size = 'medium',
                info=u"""Please detail which geographic areas are acovered by your dataset.""",

                )
        ),


        DaraField('universeSampled',
                ('data',), ('ignore_missing',),
                Input(
                placeholder = 'eg. adults in Eastern and Western Germany',
                name = 'Sampled Universe',
                size = 'medium',
                info=u"""Please specify the sample on which your dataset relies
                (e.g. GDP of all states within the Eurozone, Companies in
                China, foreign students in Canada,...).""",
                )
        ),


       #DaraField('Sampling',
       #        ('dataset', 'data', 'text', 'code'), ('ignore_missing',)

       #        Text(
       #        placeholder = 'Describe your selection method',
       #        name = 'Sampling',
       #        )
       #),


        #TODO
       #DaraField('temporalCoverageFormal',
       #        ('data',), ('ignore_missing',)
       #        Date(
       #            classes= ['todo'],
       #            name = "Temporal Coverage (controlled)",
       #            )
       #),

        DaraField('temporalCoverageFree',
                ('data',), ('ignore_missing',),

                Input(
                    placeholder="",
                    name="Temporal Coverage (free)",
                    size='medium',
                    info=u"""Please state which time period is covered by your
                    dataset. This can be a single year (e.g. 1990) or a time
                    period (e.g. 2004-2008).""",
                    )
        ),

        #TODO erstmal raus wegen; JS Date Widget finden
       #DaraField('CollectionDate_controlled',
       #        ('dataset', 'data', 'text', 'code'), ('ignore_missing',),


       #        Date(
       #        classes = ['todo'],
       #        name = 'Collection Date (controlled)',
       #        )
       #),

       #XXX obsolete
       #DaraField('CollectionDate_free',
       #        ('dataset', 'data', 'text', 'code'), ('ignore_missing',),

       #        Input(
       #        placeholder = 'eg. Spring 1999',
       #        name = 'Collection Date (free)',
       #        size = 'medium',
       #        )
       #),


       #XXX Collection Mode not selected
       #DaraField('CollectionMode_controlled',
       #        ('dataset', 'data', 'text', 'code'), ('ignore_missing',),

       #        Select(
       #        name = 'Collection Mode (controlled)',
       #        options = [
       #            {'text': '', 'value': ''},
       #            {'text': 'Interview', 'value': '1'},
       #            {'text': 'Interview: Face-to-Face', 'value': '2'},
       #            {'text': 'Interview: Telephone', 'value': '3'},
       #            {'text': 'Interview: E-Mail', 'value': '4'},
       #            {'text': 'Interview: CATI', 'value': '5'},
       #            {'text': 'Interview: CAPI', 'value': '6'},
       #            {'text': 'Self-completed questionnaire', 'value': '7'},
       #            {'text': 'Self-completed questionnaire: Paper/Pencil', 'value': '8'},
       #            {'text': 'Self-completed questionnaire: Web-based', 'value': '9'},
       #            {'text': 'Self-completed questionnaire: CASI', 'value': '10'},
       #            {'text': 'Self-completed questionnaire: ACASI', 'value': '11'},
       #            {'text': 'Coding', 'value': '12'}, {'text': 'Transcription', 'value': '13'},
       #            {'text': 'Compilation', 'value': '14'},
       #            {'text': 'Synthesis', 'value': '15'},
       #            {'text': 'Recording', 'value': '16'},
       #            {'text': 'Simulation', 'value': '17'},
       #            {'text': 'Observation', 'value': '18'},
       #            {'text': 'Observation: Field', 'value': '19'},
       #            {'text': 'Observation: Laboratory', 'value': '20'},
       #            {'text': 'Observation: Participant', 'value': '21'},
       #            {'text': 'Experiments', 'value': '22'},
       #            {'text': 'Focus Group', 'value': '23'},
       #            {'text': 'Other', 'value': '24'}],
       #        )
       #),

       #DaraField('CollectionMode_free',
       #        ('dataset', 'data', 'text', 'code'), ('ignore_missing',),

       #        Input(
       #        placeholder = 'eg. Interview',
       #        name = 'Collection Mode (free)',
       #        size = 'medium',
       #        )
       #),

        #XXX timedimension fields not selected
       #DaraField('TimeDimension_controlled',
       #        ('dataset', 'data', 'text', 'code'), ('ignore_missing',),

       #        Select(
       #        name = 'Time Dimension (controlled)',
       #        options = [
       #            {'text': '', 'value': ''},
       #            {'text': 'Longitudinal ', 'value': '1'},
       #            {'text': 'Longitudinal.CohortEventBased ', 'value': '2'},
       #            {'text': 'Longitudinal.TrendRepeatedCrossSection ', 'value': '3'},
       #            {'text': 'Longitudinal.Panel ', 'value': '4'},
       #            {'text': 'Longitudinal.Panel.Continuous', 'value': '5'},
       #            {'text': 'Longitudinal: Panel: Interval', 'value': '6'},
       #            {'text': 'Time Series', 'value': '7'},
       #            {'text': 'TimeSeries: Continuous', 'value': '8'},
       #            {'text': 'TimeSeries: Discrete', 'value': '9'},
       #            {'text': 'Cross-section', 'value': '10'},
       #            {'text': 'Cross-section ad-hoc follow-up', 'value': '11'},
       #            {'text': 'Other', 'value': '12'}],
       #        )
       #),

       #DaraField('TimeDimension_free',
       #        ('dataset', 'data', 'text', 'code'), ('ignore_missing',),

       #        Input(
       #        placeholder = 'eg. Zeitreihe',
       #        name = 'Time Dimension (free)',
       #        size = 'medium',
       #        )
       #),

      # DaraField('Frequency',
      #         ('dataset', 'data', 'text', 'code'),

      #         Input(
      #             name='Frequency',
      #             placeholder="eg. weekly, monthly",
      #             )
      # ),


        #XXX taken out
      # DaraField('Rights',
      #         ('dataset'), ('ignore_missing',),

      #         Input(
      #         placeholder = 'eg. Copyright Joe Biggs',
      #         name = 'Rights',
      #         size = 'medium',
      #         )
      # ),




        DaraField('numberUnits',
           ('data',), ('ignore_missing',),
            Number(
            name = 'Number of Units',
            placeholder='eg 3456',
            size = 'small',
            role='master',
            mi=1,
            info=u"""Please specify the number of units of your dataset. Such
            units can be persons, households, organisations, states,
            regions... please provide a whole number (e.g.43).""",
            )
        ),

        DaraField('unitType',
            ('data',), ('ignore_missing',),
            Select(
            name = 'Type of Units',
            role = 'slave',
            options = [
                {'text': '', 'value': ''},
                {'text': 'Individual', 'value': 'Individual'},
                {'text': 'Organization', 'value': 'Organization'},
                {'text': 'Family', 'value': 'Family'},
                {'text': 'Family: Household family', 'value':
                    'Family.HouseholdFamily'},
                {'text': 'Household', 'value': 'Household'},
                {'text': 'Housing Unit', 'value': 'HousingUnit'},
                {'text': 'Event/Process', 'value': 'EventOrProcess'},
                {'text': 'Geographic Unit', 'value': 'GeographicUnit'},
                {'text': 'Time Unit', 'value': 'TimeUnit'},
                {'text': 'Text Unit', 'value': 'TextUnit'},
                {'text': 'Group', 'value': 'Group'},
                {'text': 'Object', 'value': 'Object'},
                {'text': 'Other', 'value': 'Other'}
                ],
            classes = ['dara_required'],
            info=u"""You can choose the appropriate type of unit from a
            (controlled) list (e.g. Household, Organisation,...). This is
            mandatory if you give a value in 'Number of Units."""
            )
        ),


        DaraField('numberVariables',
            ('data',),  ('ignore_missing',),

            Number(
            name= 'Number of Variables',
            placeholder= 'eg. 210',
            size = 'small',
            mi=1,
            info=u"""Please name the number of variables of the dataset (e.g.
            12).""",
            )
        ),

        DaraField('dataType',
            ('data',), ('ignore_missing',),

            Input(
            name = 'Type of Data',
            placeholder= '',
            info=u""" In this field we kindly ask you to provide some
            information on the type of data. For instance, it can be a
            longitudinal study, a cross-sectional study, experimental data, or
            something other.""",
            )
        ),

        # technical file data; format is retrieved from CKAN
        # XXX done by h.fileinfo()
       #DaraField('file_size',
       #    ('data', 'text', 'code'), ('ignore_missing',),

       #    Input(
       #    name = 'File Size (MB)',
       #    size = 'small',
       #    classes=['todo'],
       #    placeholder='will be calculated automatically',
       #    )
       #),

      #DaraField('file_fingerprint',
      #     ('data', 'text', 'code'),  ('ignore_missing',),

      #     Input(
      #     role = 'master',
      #     name = 'Data Fingerprint',
      #     placeholder='eg. 00994e0caa89bc6bf394c12d9a2e72e6',
      #     )
      # ),

      # DaraField('file_fingerprintMethod',
      #     ('data', 'text', 'code'),  ('ignore_missing',),

      #     Input(
      #     role = 'slave',
      #     name = 'Method Fingerprint',
      #     size = 'small',
      #     placeholder='eg. MD5'
      #     )
      # ),

        DaraField('note',
                ('data', 'code'), ('ignore_missing',),
                Text(
                placeholder = 'any additional notes',
                name = 'Additional Notes',
                info=u"""Please provide any additional remarks regarding your dataset
                (free text field).""",
                )
        ),

        DaraField('jda_submission_id',
            ('dataset',), ('ignore_missing',),
            Input(
                placeholder="eg. 2016-12346",
               name="Article Submission ID",
                info=u"If you have been given a submission ID for your article add it here. This helps the publishing journal to connect the dataset with the article.",
            ),
        ),

        DaraField('jels',
                ('dataset',), ('ignore_missing', 'jel_convert',),
                Select(
                    name="JELs",
                    info="Put as many JELs as you like here",
                    classes=["select.jels"],
                    options=jels_to_options(),
                   # size="medium",
                ),

        ),



###### publication fields start here, not separated anymore #############


      # DaraField('Publication_Author',
      #         ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),

      #         Input(
      #         name = 'Author of Publication',
      #         size = 'medium',
      #         )
      # ),

      # DaraField('Publication_Editor',
      #         ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),

      #         Input(
      #         name = 'Editor',
      #         size = 'medium',
      #         )
      # ),

      # DaraField('Publication_Title',
      #     ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),


      #     Input(
      #         name = 'Title of Publication',
      #         size = 'medium',
      #         )
      # ),

      # DaraField('Publication_Year',
      #     ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),


      #     Input(
      #         name = 'Year of Publication',
      #         )
      # ),

      # DaraField('Publication_Publisher',
      #     ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),


      #     Input(
      #         name = 'Publisher',
      #         size = 'medium',
      #         )
      # ),

        # XXX out as long we have edawax_url. we need a mechanism for transferring
        # the old url value to this field
        DaraField('Publication_PID',
            ('publication',), ('ignore_missing',),
            Input(
                role = 'master',
                name = 'Identifier',
                placeholder = 'DOI, URL, or other identifier',
                size = 'medium',
                classes = [],
                info=u"""Please enter the article's http-address or DOI. If using a DOI, please start with the suffix: 10.XXXX ('dx.doi.org' is not required).""",
                )
        ),

        DaraField('Publication_PIDType',
                ('publication',), ('ignore_missing',),
                Select(
                role='slave',
                name='Type of Identifier',
                options=pid_types(),
                classes=['dara_required'],
                info=u"""Select the type of the above given identifier. This is
                mandatory."""
                )
        ),

      # DaraField('Publication_Place',
      #     ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),


      #         Input(
      #         name = 'Place',
      #         )
      # ),

      # DaraField('Publication_Journal',
      #     ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),


      #         Input(
      #         name = 'Journal',
      #         size = 'medium',
      #         )
      # ),

        DaraField('Publication_Volume',
            ('publication',), ('ignore_missing',),

                Number(
                name = 'Volume',
                size = 'small',
                classes = [],
                info=u"""Enter the volume of the journal in which the article
                is published."""
                )
        ),

        DaraField('Publication_Issue',
            ('publication',), ('ignore_missing', 'normalize_issue_string'),
                Input(
                name = 'Issue',
                size = 'small',
                classes = [],
                info=u"""Enter the issue of the journal in which the article is
                published.""",

                )
        ),

      # DaraField('Publication_Anthology',
      #     ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),


      #         Input(
      #         name = 'Anthology',
      #         size = 'medium',
      #         )
      # ),

     #  DaraField('Publication_Pages',
     #      ('publication',), ('ignore_missing',),


     #          Input(
     #          name = 'Pages',
     #          size = 'small',
     #          classes = ['dara_required'],
     #          )
     #  ),

        DaraField('Publication_StartPage',
            ('publication',), ('ignore_missing',),
                Number(
                name='Start Page',
                size='small',
                classes = [],
                info=u"""Please enter the start page of the article as given in the journal. If
                the journal is not printed, please simply enter 1, or give the
                number as it appears in the PDF file."""
                )
        ),

        DaraField('Publication_EndPage',
            ('publication',), ('ignore_missing',),
                Number(
                name = 'End Page',
                size = 'small',
                classes = [],
                info=u"""Please enter the end page of the article as given in the journal. If
                the journal is not printed, please simply enter the
                number as it appears in the PDF file"""
                )
        ),




      # DaraField('Publication_ISBN',
      #     ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),


      #         Input(
      #         name = 'ISBN',
      #         size = 'small',
      #         )
      # ),

      # DaraField('Publication_ISSN',
      #     ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),


      #         Input(
      #         name = 'ISSN',
      #         size = 'small',
      #         )
      # ),

      # DaraField('Publication_RelationType',
      #     ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),


      #         Text(
      #         name = 'Relation Type',
      #         )
      # ),

      # DaraField('Publication_DocType',
      #     ('dataset', 'data', 'text', 'code', 'publication'), ('ignore_missing',),


      #         Select(
      #         name = 'Document Type',
      #         options = [
      #             {'text': '', 'value': ''},
      #             {'text': 'Working Paper', 'value': '1'},
      #             {'text': 'Article', 'value': '2'},
      #             {'text': 'Report', 'value': '3'},
      #             {'text': 'Book/Monograph', 'value': '4'},
      #             {'text': 'Manuscript', 'value': '5'},
      #             {'text': 'Reference Book', 'value': '6'},
      #             {'text': 'Review', 'value': '7'},
      #             {'text': 'Series', 'value': '8'},
      #             {'text': 'Journal', 'value': '9'},
      #             {'text': 'Magazine', 'value': '10'}],
      #         )
      # ),

    )

    return fields


def author_fields():

    AuthorField = namedtuple('AuthorField', 'id widget')
    fields = (


        AuthorField('lastname',
            Input(
                placeholder = '',
                name = 'Last Name',
                size = 'medium',
                classes = ['econws', 'dara_required'],
                info=u"""Please specify the last name of the author.
                Choose the name from the list, if available. Middle names should be included in the field 'First Name'""",
                )
            ),


        AuthorField('firstname',
            Input(
                placeholder = '',
                name = 'First Name',
                size = 'medium',
                classes = [],
                info=u"""Please specify the first name of author. In case of a
                middle name, please also add it here.""",
                ),
            ),


        AuthorField('affil',
            Input(
                placeholder = 'Your institution',
                name = 'Affiliation',
                size = 'medium',
                classes=['econws_affil'],
                info=u"""Please state the affiliation you are working for
                respectively the affiliation you already have mentioned in your
                paper.""",
                ),
            ),

        AuthorField('url',
            Input(
                placeholder = 'http://www...',
                name = 'Professional URL',
                classes = [],
                info=u"""Enter your personal or institutional homepate. Start with 'http'""",
                ),
            ),


        AuthorField('authorID',
            Input(
                name = 'Personal ID',
                placeholder = 'ORCID, Scopus, GND or Web of Science ID',
                size = '',
                classes = [],
                role = 'master',
                info=u"""Enter any personal ID you have (eg. ORCID, WOS, RePEc). If you choose your last name from a list, this will be filled in automatically.""",
                ),
        ),

        AuthorField('authorID_Type',
                Select(
                name = 'ID Type',
                options = [
                    {'text': '', 'value': ''},
                    {'text': 'GND', 'value': 'GND'},
                    {'text': 'ORCID', 'value': 'ORCID'},
                    {'text': 'Scopus', 'value': 'Scopus'},
                    {'text': 'RePEc', 'value': 'Repec'},
                    {'text': 'Web of Science', 'value': 'WoS'}
                ],
                role = 'slave',
                classes = ['dara_required'],
                info=u"""Select the type of the above given Personal ID.
                This is mandatory if you've entered an ID.""",
                ),
        ),


        )

    return fields


def hidden_fields():
    """
    hidden fields, not mutable by user
    """
    HiddenField = namedtuple('HiddenField', 'id validators')

    fields = (
                HiddenField('DOI', ('ignore_missing',)),
#                HiddenField('DOI_Proposal', ('ignore_missing',)),
                HiddenField('DOI_Test', ('ignore_missing',)),
                HiddenField('created', ('ignore_missing',)),
                HiddenField('registered', ('ignore_missing',)),
                HiddenField('updated', ('ignore_missing',)),
                HiddenField('registered_test', ('ignore_missing',)),
                HiddenField('updated_test', ('ignore_missing',)),
                HiddenField('type', ('ignore_missing',)),

                # TODO this really should be in ckanext.edawax, but we had trouble
                # with two IDatasetForm implements
                HiddenField('edawax_review', ('ignore_missing',)),
             )
    return fields


def single_fields():

    SingleField = namedtuple('SingleField', 'id validators')

    fields = (
            SingleField('authors', ('ignore_missing', 'authors',)),
            )

    return fields


def pid_types():
    """ return dictionary with key,values of PID types """
    types = ['', 'DOI', 'ARK', 'EAN13', 'EISSN', 'Handle', 'ISBN', 'ISSN',
            'ISTC', 'LISSN', 'LSID', 'PURL', 'UPC', 'URL', 'URN']
    return map(lambda k: {'text': k, 'value': k}, types)


def jels_to_options():

    jels = ['A', 'A1', 'A2', 'A3', 'A10', 'A11', 'A12', 'A13', 'A14', 'A19',
                'A20', 'A21', 'A22', 'A23', 'A29', 'A30', 'A31', 'A32', 'A39', 'B',
                'B0', 'B00', 'B1', 'B2', 'B3', 'B4', 'B5', 'B10', 'B11', 'B12',
                'B13', 'B14', 'B15', 'B16', 'B19', 'B20', 'B21', 'B22', 'B23',
                'B24', 'B25', 'B29', 'B30', 'B31', 'B32', 'B40', 'B41', 'B49',
                'B50', 'B51', 'B52', 'B53', 'B54', 'B59', 'C', 'C0', 'C00', 'C01',
                'C1', 'C02', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10',
                'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19',
                'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C29', 'C30',
                'C31', 'C32', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42',
                'C43', 'C44', 'C45', 'C46', 'C49', 'C50', 'C51', 'C52', 'C53',
                'C54', 'C55', 'C56', 'C57', 'C58', 'C59', 'C60', 'C61', 'C62',
                'C63', 'C65', 'C67', 'C68', 'C69', 'C70', 'C71', 'C72', 'C73',
                'C78', 'C79', 'C80', 'C81', 'C82', 'C83', 'C87', 'C88', 'C89',
                'C90', 'C91', 'C92', 'C93', 'C99', 'D', 'D0', 'D00', 'D01', 'D1',
                'D02', 'D2', 'D03', 'D04', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
                'D10', 'D11', 'D12', 'D13', 'D14', 'D18', 'D19', 'D20', 'D21',
                'D22', 'D23', 'D24', 'D29', 'D30', 'D31', 'D33', 'D39', 'D40',
                'D41', 'D42', 'D43', 'D44', 'D45', 'D46', 'D49', 'D50', 'D51',
                'D52', 'D53', 'D57', 'D58', 'D59', 'D60', 'D61', 'D62', 'D63',
                'D64', 'D69', 'D70', 'D71', 'D72', 'D73', 'D74', 'D78', 'D79',
                'D80', 'D81', 'D82', 'D83', 'D84', 'D85', 'D86', 'D87', 'D89',
                'D90', 'D91', 'D92', 'D99', 'E', 'E0', 'E00', 'E01', 'E1', 'E02',
                'E2', 'E3', 'E4', 'E5', 'E6', 'E10', 'E11', 'E12', 'E13', 'E14', 'E17',
                'E19', 'E20', 'E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27',
                'E29', 'E30', 'E31', 'E32', 'E37', 'E39', 'E40', 'E41', 'E42',
                'E43', 'E44', 'E47', 'E49', 'E50', 'E51', 'E52', 'E58', 'E59',
                'E60', 'E61', 'E62', 'E63', 'E64', 'E65', 'E66', 'E69', 'F', 'F0',
                'F00', 'F01', 'F1', 'F02', 'F2', 'F3', 'F4', 'F5', 'F6', 'F10',
                'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19',
                'F20', 'F21', 'F22', 'F23', 'F24', 'F29', 'F30', 'F31', 'F32',
                'F33', 'F34', 'F35', 'F36', 'F37', 'F38', 'F39', 'F40', 'F41', 'F42',
                'F43', 'F44', 'F45', 'F47', 'F49', 'F50', 'F51', 'F52', 'F53', 'F54',
                'F55', 'F59', 'F60', 'F61', 'F62', 'F63', 'F64', 'F65', 'F66',
                'F68', 'F69', 'G', 'G0', 'G00', 'G01', 'G02', 'G1', 'G2', 'G3', 'G10',
                'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19',
                'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31',
                'G32', 'G33', 'G34', 'G35', 'G38', 'G39', 'H', 'H0', 'H00', 'H1',
                'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H10', 'H11', 'H12', 'H19',
                'H20', 'H21', 'H22', 'H23', 'H24', 'H25', 'H26', 'H27', 'H28',
                'H29', 'H30', 'H31', 'H32', 'H39', 'H40', 'H41', 'H42', 'H43',
                'H44', 'H49', 'H50', 'H51', 'H52', 'H53', 'H54', 'H55', 'H56',
                'H57', 'H59', 'H60', 'H61', 'H62', 'H63', 'H68', 'H69', 'H70',
                'H71', 'H72', 'H73', 'H74', 'H75', 'H76', 'H77', 'H79', 'H80',
                'H81', 'H82', 'H83', 'H87', 'H89', 'I', 'I0', 'I00', 'I1', 'I2',
                'I3', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I18', 'I19', 'I20', 'I21', 'I22',
                'I23', 'I24', 'I25', 'I26', 'I27', 'I28', 'I29', 'I30', 'I31', 'I32', 'I38', 'I39', 'J', 'J0',
                'J00', 'J01', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J08',
                'J8', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17',
                'J18', 'J19', 'J20', 'J21', 'J22', 'J23', 'J24', 'J25', 'J26', 'J28',
                'J29', 'J30', 'J31', 'J32', 'J33', 'J38', 'J39', 'J40', 'J41',
                'J42', 'J43', 'J44', 'J45', 'J48', 'J49', 'J50', 'J51', 'J52', 'J53',
                'J54', 'J58', 'J59', 'J60', 'J61', 'J62', 'J63', 'J64', 'J65', 'J68',
                'J69', 'J70', 'J71', 'J78', 'J79', 'J80', 'J81', 'J82', 'J83', 'J88',
                'J89', 'K', 'K0', 'K00', 'K1', 'K2', 'K3', 'K4', 'K10', 'K11', 'K12',
                'K13', 'K14', 'K19', 'K20', 'K21', 'K22', 'K23', 'K24', 'K29', 'K30', 'K31',
                'K32', 'K33', 'K34', 'K35', 'K36', 'K39', 'K40', 'K41', 'K42', 'K49', 'L',
                'L0', 'L00', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10',
                'L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L17', 'L19', 'L20', 'L21',
                'L22', 'L23', 'L24', 'L25', 'L26', 'L29', 'L30', 'L31', 'L32', 'L33',
                'L38', 'L39', 'L40', 'L41', 'L42', 'L43', 'L44', 'L49', 'L50', 'L51',
                'L52', 'L53', 'L59', 'L60', 'L61', 'L62', 'L63', 'L64', 'L65', 'L66',
                'L67', 'L68', 'L69', 'L70', 'L71', 'L72', 'L73', 'L74', 'L78', 'L79',
                'L80', 'L81', 'L82', 'L83', 'L84', 'L85', 'L86', 'L87', 'L88', 'L89',
                'L90', 'L91', 'L92', 'L93', 'L94', 'L95', 'L96', 'L97', 'L98', 'L99', 'M',
                'M0', 'M00', 'M1', 'M2', 'M3', 'M4', 'M5', 'M10', 'M11', 'M12', 'M13',
                'M14', 'M19', 'M20', 'M21', 'M29', 'M30', 'M31', 'M37', 'M39', 'M40',
                'M41', 'M42', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55',
                'M59', 'N', 'N0', 'N00', 'N01', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7',
                'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N20',
                'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N30', 'N31', 'N32',
                'N33', 'N34', 'N35', 'N36', 'N37', 'N40', 'N41', 'N42', 'N43', 'N44',
                'N45', 'N46', 'N47', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56',
                'N57', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N70',
                'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N80', 'N81', 'N82',
                'N83', 'N84', 'N85', 'N86', 'N87', 'N90', 'N91', 'N92', 'N93', 'N94',
                'N95', 'N96', 'N97', 'O', 'O1', 'O2', 'O3', 'O4', 'O5', 'O10', 'O11',
                'O12', 'O13', 'O14', 'O15', 'O16', 'O17', 'O18', 'O19', 'O20', 'O21',
                'O22', 'O23', 'O24', 'O25', 'O29', 'O30', 'O31', 'O32', 'O33', 'O34',
                'O38', 'O39', 'O40', 'O41', 'O42', 'O43', 'O44', 'O47', 'O49', 'O50', 'O51',
                'O52', 'O53', 'O54', 'O55', 'O56', 'O57', 'P', 'P0', 'P00', 'P1', 'P2',
                'P3', 'P4', 'P5', 'P10', 'P11', 'P12', 'P13', 'P14', 'P16', 'P17', 'P19',
                'P20', 'P21', 'P22', 'P23', 'P24', 'P25', 'P26', 'P27', 'P28', 'P29',
                'P30', 'P31', 'P32', 'P33', 'P34', 'P35', 'P36', 'P37', 'P39', 'P40',
                'P41', 'P42', 'P43', 'P44', 'P45', 'P46', 'P47', 'P48', 'P49', 'P50',
                'P51', 'P52', 'P59', 'Q', 'Q0', 'Q00', 'Q01', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5',
                'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19',
                'Q20', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25', 'Q26', 'Q27', 'Q28', 'Q29',
                'Q30', 'Q31', 'Q32', 'Q33', 'Q34', 'Q38', 'Q39', 'Q40', 'Q41', 'Q42',
                'Q43', 'Q48', 'Q49', 'Q50', 'Q51', 'Q52', 'Q53', 'Q54', 'Q55', 'Q56',
                'Q57', 'Q58', 'Q59', 'R', 'R0', 'R00', 'R1', 'R2', 'R3', 'R4', 'R5', 'R10',
                'R11', 'R12', 'R13', 'R14', 'R15', 'R19', 'R20', 'R21', 'R22', 'R23',
                'R29', 'R30', 'R31', 'R32', 'R33', 'R34', 'R38', 'R39', 'R40', 'R41',
                'R42', 'R48', 'R49', 'R50', 'R51', 'R52', 'R53', 'R58', 'R59', 'Y', 'Y1',
                'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y8', 'Y9', 'Y10', 'Y20', 'Y30', 'Y40',
                'Y50', 'Y60', 'Y80', 'Y90', 'Z', 'Z0', 'Z00', 'Z1', 'Z10', 'Z11', 'Z12',
                'Z13', 'Z19', 'Z33']

    dic = lambda jel: {'text': jel, 'value': jel}
    return map(dic, jels)

