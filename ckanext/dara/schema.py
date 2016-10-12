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
                info=u"""Please provide us with the publication year of your
                    article. If you do not know the year, yet, please choose the
                    actual year. Please note: This is a mandatory field."""
                )
        ),

        DaraField('Availabilitycontrolled',
            ('data'), ('ignore_missing',), # no not_empty here since we have 1 as default in dara xml anyways
            Select(
                options=[
                    {'value': '1', 'text': 'Free Download'},
                    {'value': '2', 'text': 'Delivery on demand'},
                    {'value': '3', 'text': 'Onsite only'},
                    {'value': '4', 'text': 'Not available'},
                    {'value': '5', 'text': 'Unknown'},
                ],
                name='Availability',
                classes=['dara_required'],
                info=u"""By default the availability is 'Free Download'. You
                should only change this value in cases when you are not
                able/not allowed to upload the dataset used for your
                calculations AND when you would like to provide a link to the
                dataset, instead. Please note: This is a mandatory field.""",

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
                info=u"""The default version number is 1. You should only
                change the version number if you submit a revised version of
                your supplementary data. In this case please choose an
                appropriate new version number (e.g. 1.1 for minor revisions or
                2 for major revisions)."""
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
                info=u"""Please state, which geographical areas are covered by
                your dataset. This is a free text field, therefore you are free
                to mention the region(s) that fit most (e.g. North-America;
                Eurozone, Germany, EU-Member States,...)""",

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
                {'text': 'Individual', 'value': '1'},
                {'text': 'Organization', 'value' : '2'},
                {'text': 'Family', 'value': '3'},
                {'text': 'Family: Household family', 'value': '4'},
                {'text': 'Household', 'value': '5'},
                {'text': 'Housing Unit', 'value': '6'},
                {'text': 'Event/Process', 'value': '7'},
                {'text': 'Geographic Unit', 'value': '8'},
                {'text': 'Time Unit', 'value': '9'},
                {'text': 'Text Unit', 'value': '10'},
                {'text': 'Group', 'value': '11'},
                {'text': 'Object', 'value': '12'},
                {'text': 'Other', 'value': '13'}
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
        #TODO get automatically
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
                info=u""" Here you can state additional remarks, if needed
                (free text field).""",
                )
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
                info=u"""Enter an identifier for the article. This should be an
                URL, DOI, or Handle""",
                )
        ),

        DaraField('Publication_PIDType',
                ('publication',), ('ignore_missing',),
                Select(
                role = 'slave',
                name = 'Type of Identifier',
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
                classes = ['dara_required'],
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
                info=u"""Please specify the last name of author.
                You will get autosuggests as soon you've typed the first
                letters. In case of a
                middle name, please add the middle name to the field 'first
                name'. This is a mandatory field.""",
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
                info=u"""Please state the affiliation you are working for
                respectively the affiliation you already have mentioned in your
                paper.""",
                ),
            ),

        AuthorField('url',
            Input(
                placeholder = 'Personal URL of Author',
                name = 'URL',
                classes = [],
                info=u"""In this field, you can state your personal or
                institutional website. Thereby, other users and visitors of
                your data submission are enabled to directly inform themselves
                about you and your fields of research.""",
                ),
            ),


        AuthorField('authorID',
            Input(
                name = 'Personal ID',
                placeholder = 'ORCID, Scopus, GND or Web of Science ID',
                size = '',
                classes = [],
                role = 'master',
                info=u"""If available please enter your personal ID. In case of
                ORCID the system will then try to get all other data
                automatically from the ORCID API. Please note that if you give
                a value here you must give the type of the ID also.""",
                ),
        ),

        AuthorField('authorID_Type',
                Select(
                name = 'Type',
                options = [
                    {'text': '', 'value': ''},
                    {'text': 'ORCID', 'value': 'ORCID'},
                    {'text': 'GND', 'value': 'GND'},
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

        AuthorField('authorID_URI',
                Input(
                    name='Personal ID URI',
                    classes = ['hidden_author_field'],
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
