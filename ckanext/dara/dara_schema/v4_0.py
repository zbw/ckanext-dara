# -*- coding: utf-8 -*-
import logging
from ckan.common import config
log = logging.getLogger(__name__)

def replace_includes(schema):
    home = config.get('ckan.site_url')
    #url_prefix="http://www.da-ra.de/fileadmin/media/da-ra.de/Technik/4.0/include/"
    # Test
    if home == 'http://134.245.93.94':
        url_prefix = 'file:///home/edawax/src/ckanext-dara/ckanext/dara/dara_schema/import/'
    # Dev - Need to start from within the folder for dara
    elif home == 'http://127.0.0.1:5000':
        url_prefix = '/home/ckan/Python/src/ckanext-dara/ckanext/dara/dara_schema/import/'
    # Production
    else:
        url_prefix = 'file:///home/edawax/ckanenv/plugins/ckanext-dara/ckanext/dara/dara_schema/import/'
    return schema.replace('include/', url_prefix)



dara_schema = """<?xml version="1.0" encoding="UTF-8"?>
<!-- da|ra Metadatenschema v4.0 - www.da-ra.de 12.10.2017 -->
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="http://da-ra.de/schema/kernel-4"
    targetNamespace="http://da-ra.de/schema/kernel-4" xmlns:dara="http://da-ra.de/schema/kernel-4"
    elementFormDefault="qualified" xml:lang="EN">
    <!-- include fields -->
    <!-- include/dara-resourceType-v4.xsd -->
    <xs:include schemaLocation="include/dara-resourceType-v4.xsd">
        <xs:annotation>
            <xs:documentation>A predefined term to provide information about the type of resource being registered.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-otherTitleType-v4.xsd">
        <xs:annotation>
            <xs:documentation>Predefined terms to provide information about different types of additional titles or names of the registered resource to differentiate between the different title types.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-contributorType-v4.xsd">
        <xs:annotation>
            <xs:documentation>A classification of the role of the person to describe which specific task he/she holds to contribute to the registered resource.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-availabilityType-v4.xsd">
        <xs:annotation>
            <xs:documentation>Predefined terms to provide information about different types of the availability conditions of the registered resource.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-relationType-v4.xsd">
        <xs:annotation>
            <xs:documentation>Predefined terms to provide information about different types of relations between the resource being registered and a related resource, e.g. the registered resources is a new version ofthe related resource.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-pidType-v4.xsd">
        <xs:annotation>
            <xs:documentation>Predefined terms to provide information about different types of Persistent Identifiers of the unstructured information of the publication.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-descriptionType-v4.xsd">
        <xs:annotation>
            <xs:documentation>The type of the additional information about the registered resource.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-identifierSchemaType-v4.xsd">
        <xs:annotation>
            <xs:documentation>The name of the schema used to differentiate between different ID types that identify the container element; e.g. the person, the institution or the organization.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-timeDimensionType-v4.xsd">
        <xs:annotation>
            <xs:documentation>Predefined terms to provide information about different types of time dimensions, e.g. if the survey examines a population on more than one occasion (longitudinal), if the study draws different samples from the same general population at different times (trend), etc.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-collectionModeType-v4.xsd">
        <xs:annotation>
            <xs:documentation>Predefined terms to provide information about different types of methods that are used to collect information from a sample in a survey. </xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-documentType-v4.xsd">
        <xs:annotation>
            <xs:documentation>The type of publication that has been made available to the public.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-unitType-v4.xsd">
        <xs:annotation>
            <xs:documentation>Describes the entity being analysed or observed in the resource.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-rightsCCType-v4.xsd">
        <xs:annotation>
            <xs:documentation>Predefined terms to provide information about different types of copyright-licences known as Creative Commons licenses to allow creators to communicate which rights they reserve for the registered resource.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-languageCodes-v4.xsd">
        <xs:annotation>
            <xs:documentation>The language of the metadata information. It applies to the according piece of information where it is specified. The value is a language code for the natural language and must conform to the ISO code 639-1.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-resourceLanguageCodes-v4.xsd">
        <xs:annotation>
            <xs:documentation>A primary language of the registered resource itself, using ISO 3-letter codes (639-3) as the enumerated possible values.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-internalClassificationSchemaType-v4.xsd">
        <xs:annotation>
            <xs:documentation>The name of the internal schema used to differentiate between classification systems describing the topical coverage of the registered resource.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-controlledKeywordSchemaType-v4.xsd">
        <xs:annotation>
            <xs:documentation>The name of the internal schema used to differentiate between keywords to describe the topical coverage.</xs:documentation>
        </xs:annotation>
    </xs:include>
    <xs:include schemaLocation="include/dara-geoCodes-v4.xsd">
        <xs:annotation>
            <xs:documentation>Predefined terms to provide information about different types of locations or spatial regions covered by the data collection. Information about the Geographic Coverage has been standardized according to ISO3166-1, ISO3166-2 and ISO3166-3.</xs:documentation>
        </xs:annotation>
    </xs:include>

    <!--  *0. Object Resource Type-->
    <xs:element name="resourceType" type="resourceType">
        <xs:annotation>
            <xs:documentation xml:lang="en">Predefined terms to provide information about the type
                of resource being registered to differentiate between registered
                resources.</xs:documentation>
        </xs:annotation>
    </xs:element>
    <xs:element name="resourceTypesFree">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide language-dependent
                information about the types of resources being registered.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="resourceTypeFree" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element for one specific language-dependent name of the resource type.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="resourceTypeFreeLanguage">
            <xs:selector xpath="dara:resourceTypeFree"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <xs:element name="resourceTypeFree">
        <xs:complexType mixed="false">
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>The language of the metadata information. It applies to the according piece of information where it is specified. The value is a language code for the natural language and must conform to the ISO code 639-1.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="typeName" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>A free-text field to describe the type of resource more in detail in addition to the selected code of the general resource type.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- *1.title -->
    <xs:element name="titles">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide language-dependent infor-mation about the main titles of the registered resource. </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="title" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element for one specific language-dependent title.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="titleLanguage">
            <xs:selector xpath="dara:title"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <xs:element name="title">
        <xs:complexType mixed="false">
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"> </xs:element>
                <xs:element name="titleName" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>A name or title of the registered resource. The title is a distinguishing name or a descriptive or general heading of the registered resource.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- 2.other titles-->
    <xs:element name="otherTitles">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide language-dependent information about titles other than the main title for the registered resource. </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="otherTitle" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element for a language-dependent title other than the main title.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="otherTitle">
        <xs:complexType mixed="false">
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language"> </xs:element>
                <xs:element minOccurs="1" maxOccurs="1" name="titleName">
                    <xs:annotation>
                        <xs:documentation>An additional or another title or name of the registered resource.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="titleType" type="titleType">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">Predefined terms to provide information about different types of additional titles or names of the registered resource to differentiate between different title types.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- *3.collective title -->
    <xs:element name="collectiveTitles">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide language-dependent information about collective titles of the registered resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="collectiveTitle" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element for one specific language-dependent collective title.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="ctitleLanguage">
            <xs:selector xpath="dara:collectiveTitle"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <xs:element name="collectiveTitle">
        <xs:annotation>
            <xs:documentation xml:lang="en"/>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"> </xs:element>
                <xs:element name="titleName" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>A A title of a book series, working paper series or similar.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="numbering" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">A number to refer to the order of things or to count/number them.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- *4.creators -->
    <xs:element name="creators">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about a person, e.g. researchers involved in producing the registered resource or an institution responsible for the substan-tive and/or intellectual content of the registered re-source.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="creator">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about a person, an affiliation or an institution.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="creator">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about a person (with an affiliation) or an institution.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:choice>
                <xs:element ref="person" maxOccurs="1" minOccurs="1"> </xs:element>
                <xs:element name="institution">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about an organization or institution involved in producing the registered resource.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence maxOccurs="1" minOccurs="1">
                            <xs:element name="institutionName" maxOccurs="1" minOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>A name of the organization or institution involved in producing the data or responsible for the registered resource.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element name="institutionIDs" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>Container element to provide information about a unique identifier of the organization or institution and the name of the schema identifier to disambiguate institutions or organizations.</xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element maxOccurs="unbounded" name="institutionID">
                                            <xs:annotation>
                                                <xs:documentation>Container element to provide information about an institution’s unique identifier.</xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:group ref="ID"/>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:choice>
        </xs:complexType>
    </xs:element>

    <!-- *4.1 person -->
    <xs:element name="person">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about a person.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element minOccurs="1" maxOccurs="1" name="firstName">
                    <xs:annotation>
                        <xs:documentation>The first name of a person.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="middleName" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>The middle name of a person.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="lastName">
                    <xs:annotation>
                        <xs:documentation>The last name of a person.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element minOccurs="0" name="personIDs">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about a unique identifier of the person and the name of the schema identifier to disambiguate individuals of similar names.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element maxOccurs="unbounded" name="personID">
                                <xs:annotation>
                                    <xs:documentation>Container element to provide information about a person’s unique identifier.</xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:group ref="ID"/>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element minOccurs="0" ref="affiliation">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about the organizational or institutional connection of a person. The affiliation should reflect the person´s current and/or primary employment.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="affiliation">
        <xs:complexType mixed="false">
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element minOccurs="1" maxOccurs="1" name="affiliationName">
                    <xs:annotation>
                        <xs:documentation>The name of the organization or institution a person is affiliated to.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="affiliationIDs" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about a unique identifier of the organization or institution a person is affiliated to in order to disambiguate affiliations of similar names. </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element maxOccurs="unbounded" name="affiliationID">
                                <xs:annotation>
                                    <xs:documentation>Container element for an individual unique identifier and the related identifier schema of the affiliation.</xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:group ref="ID"/>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- *new field. publisher -->
    <xs:element name="publisher">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about a person, an affiliation and/or an institution responsible for the publication of the registered resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:choice>
                <xs:element ref="person" maxOccurs="1" minOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about a person.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="institution">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">Container element to provide information about an organ-ization or institution involved in publishing the registered resource.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence maxOccurs="1" minOccurs="1">
                            <xs:element name="institutionName" minOccurs="1" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>A name of the organization or institution involved in publishing the registered resource.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element name="institutionIDs" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>Container element to provide information about a unique identifier of the organization or institution and the name of the schema identifier to disambiguate institutions or organizations.</xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element maxOccurs="unbounded" name="institutionID">
                                            <xs:annotation>
                                                <xs:documentation>Container element to provide information about an institution’s unique identifier.</xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:group ref="ID"/>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:choice>
        </xs:complexType>
    </xs:element>

    <!-- *9.doi proposal -->
    <xs:element name="doiProposal" type="doiType">
        <xs:annotation>
            <xs:documentation xml:lang="en">A persistent interoperable identifier (=DOI) a publication agent suggests for identification purposes of the registered resource.</xs:documentation>
        </xs:annotation>
    </xs:element>

    <!-- *8.url -->
    <xs:element name="dataURLs">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about the URL or URN (a reference to a web resource that specifies its location) linking to the registered resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element minOccurs="1" maxOccurs="unbounded" name="dataURL" type="xs:anyURI">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">An URL or URN (a reference to a web resource that specifies its location) linking to the registered resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="dataURL">
            <xs:selector xpath="dara:dataURL"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>

    <!-- 11. resource language -->
    <xs:element name="resourceLanguage" type="resourceLanguage">
        <xs:annotation>
            <xs:documentation xml:lang="en">A primary language of the registered resource itself, using ISO 3-letter codes (639-3) as the enumerated possible values.</xs:documentation>
        </xs:annotation>
    </xs:element>

    <!-- *.metadata language -->
    <xs:element name="language" type="metadataLanguage">
        <!-- TODO documentation-->
        <xs:annotation>
            <xs:documentation>The language of the metadata information. It applies to the according piece of information where it is specified.</xs:documentation>
        </xs:annotation>
    </xs:element>

    <!-- *12.publication date -->
    <xs:element name="publicationDate">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about the date the registered resource was published or is going to be published.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:choice>
                <xs:element name="date" type="yyyy-mm-dd">
                    <xs:annotation>
                        <xs:documentation>The publication day, month and/or year of the registered resource submitted by the publication agent.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="monthyear" type="xs:gYearMonth"> </xs:element>
                <xs:element name="year" type="xs:gYear"> </xs:element>
            </xs:choice>
        </xs:complexType>
    </xs:element>

    <!-- 13. alternative identifier -->
    <xs:element name="alternativeIDs">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about identifiers other than the primary identifier applied to the resource being registered.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="alternativeID" maxOccurs="unbounded" minOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Container element of a specific identifier other than the primary identifier applied to the resource being registered.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="alternativeID">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="identifier">
                    <xs:annotation>
                        <xs:documentation>The value of a formally registered unique identifier other than the primary identifier of the registered resource. This may be an identifier from the infor-mation system of the publication agent as well as from other information systems.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="type">
                    <xs:annotation>
                        <xs:documentation>A free-text field to describe the name of the schema used to differentiate between different ID types that identify the alternative unique identifier of the registered resource.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 14. classification -->
    <xs:element name="classification">
        <xs:annotation>
            <xs:documentation xml:lang="en"/>
        </xs:annotation>
        <xs:complexType>
            <xs:choice maxOccurs="1" minOccurs="1">
                <xs:element name="classificationInternal">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">Container element for the internal classification system provided by da|ra (Classifications: Journal of Economic Literature (JEL), ZA, GESIS).</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:all>
                            <xs:element name="classificationSchemaType" type="classificationSchemaType">
                                <xs:annotation>
                                    <xs:documentation>The name of the internal schema used to differentiate between classification systems describing the topical coverage of the registered resource.</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element minOccurs="1" maxOccurs="1" name="identifiers">
                                <xs:annotation>
                                    <xs:documentation>Container element to provide information about the unique identifier of the internal schema.</xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence maxOccurs="1">
                                        <xs:element name="identifier" maxOccurs="unbounded">
                                            <xs:annotation>
                                                <xs:documentation>The value of formally registered unique identifier of the internal schema to disambiguate classification systems.</xs:documentation>
                                            </xs:annotation>
                                            <xs:simpleType>
                                                <xs:restriction base="nonemptycontentStringType"/>
                                            </xs:simpleType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                                <xs:unique name="classificationIdentifier">
                                    <xs:selector xpath="dara:identifier"/>
                                    <xs:field xpath="."/>
                                </xs:unique>
                            </xs:element>
                        </xs:all>
                    </xs:complexType>
                </xs:element>
                <!-- classificationExternal-->
                <xs:element maxOccurs="1" name="classificationExternal">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">Container element to provide language-dependent information about a classification system provided by the publication agent.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:all>
                            <xs:element ref="language"/>
                            <xs:element name="classificationSchema" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>The name of the external schema used to differentiate between classification systems a publication agent provides to describe the topical coverage.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element minOccurs="1" maxOccurs="1" name="terms">
                                <xs:annotation>
                                    <xs:documentation>Container element to provide information about the subject class.</xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence maxOccurs="1">
                                        <xs:element name="term" maxOccurs="unbounded">
                                            <xs:annotation>
                                                <xs:documentation>The subject class from the external classification system a publication agent uses to describe the topical coverage.</xs:documentation>
                                            </xs:annotation>
                                            <xs:simpleType>
                                                <xs:restriction base="nonemptycontentStringType"/>
                                            </xs:simpleType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                                <xs:unique name="classificationTerm">
                                    <xs:selector xpath="dara:term"/>
                                    <xs:field xpath="."/>
                                </xs:unique>
                            </xs:element>
                        </xs:all>
                    </xs:complexType>
                </xs:element>
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <xs:element name="classifications">
        <xs:annotation>
            <xs:documentation>Container element to provide information about a multi-disciplinary or discipline-specific system for hierarchically classifications. At the same time, classifications branch out into the special knowledge areas out of a few main compartments.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="classification" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element for inter-nal and external classifications.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 15. keywords controlled -->
    <xs:element name="controlledKeyword">
        <xs:annotation>
            <xs:documentation xml:lang="en"/>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element name="keywordSchemaType" type="keywordSchemaType">
                    <xs:annotation>
                        <xs:documentation>The name of the internal schema used to differentiate between keywords to describe the topical coverage.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="1" maxOccurs="1" name="identifiers">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information unique identifier of the internal schema.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence maxOccurs="unbounded">
                            <xs:element name="identifier" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>The value of formally registered unique identifier of the internal schema to disambiguate keywords.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                    <xs:unique name="controlledKeywordIdentifier">
                        <xs:selector xpath="dara:identifier"/>
                        <xs:field xpath="."/>
                    </xs:unique>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="controlledKeywords">
        <xs:annotation>
            <xs:documentation>Container element to provide information about a classification of the terminology to classify or index the registered resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="controlledKeyword" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element for controlled keywords.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 16. keywords free-->
    <xs:element name="freeKeyword">
        <xs:complexType>
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" maxOccurs="1"> </xs:element>
                <xs:element name="keywordSchema" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>The name of the schema related to the free keyword. </xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="keywords">
                    <xs:annotation>
                        <xs:documentation>Container element for the keywords. </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element maxOccurs="unbounded" name="keyword">
                                <xs:annotation>
                                    <xs:documentation>A textual description or terminology to describe the content of the registered resource.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>
    <xs:element name="freeKeywords">
        <xs:annotation>
            <xs:documentation>Container element to provide language-dependent information about the content of the registered resource if the controlled list of classifications cannot provide enough information.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="freeKeyword" maxOccurs="unbounded" minOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Container element for one specific language-dependent free keyword of the external schema used to differentiate between keywords to describe the topical coverage.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="freeKeywordsLanguage">
            <xs:selector xpath="dara:freeKeyword"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>

    <!-- 17. description -->
    <xs:element name="descriptions">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide language-dependent information, statements or passages that give additional details about someone or something.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="description">
                    <xs:annotation>
                        <xs:documentation>Container element for language-dependent descriptions.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="description">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="language"> </xs:element>
                <xs:element name="freetext" type="richtext">
                    <xs:annotation>
                        <xs:documentation>All additional information about the registered resource that does not fit in any of the other categories. May be used for technical information.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="descriptionType" type="descriptionType">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">Predefined terms to provide information about different types of descriptions used to describe the registered resource. </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 18. geographic coverage controlled/free-->
    <xs:element name="geographicCoverages">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide geographical information of the data collection including a controlled vocabulary, a language-attribute, a free-text-field, a location point, a location box and a location polygon.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="geographicCoverage">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about the geographic coverage of the registered resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="geographicCoverage">
        <xs:complexType>
            <xs:choice>
                <!-- 18.1 geographic coverage controlled-->
                <xs:sequence>
                    <xs:element name="geographicCoverageControlled" type="geographicCoverageControlled" minOccurs="1">
                        <xs:annotation>
                            <xs:documentation>Predefined terms to provide geographical information to differentiate between different locations the survey was conducted.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="geographicCoveragesFree" minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>Container element to provide language-dependent information about the geographic coverage.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="geoLocationPoint" minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>Container element of a geographic point defined by a latitude and longitude in degrees, representing a geographic area in which the survey was conducted.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="geoLocationBox" minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>Container element of a geoLocationBox with an east longitude value (xmax), a west longitude value (xmin), a north latitude value (ymax) and a south latitude value (ymin) expressed as a decimal between the values of -180 and 180 degrees.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="geoLocationPolygon" minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>Container element to provide information about a drawn polygon area, defined by a set of points and lines connecting the points in a closed chain.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>

                <xs:sequence>
                    <xs:element ref="geographicCoveragesFree"/>
                    <xs:element ref="geoLocationPoint" minOccurs="0"/>
                    <xs:element ref="geoLocationBox" minOccurs="0"/>
                    <xs:element ref="geoLocationPolygon" minOccurs="0"/>
                </xs:sequence>
                <xs:sequence>
                    <xs:element ref="geoLocationPoint"/>
                    <xs:element ref="geoLocationBox" minOccurs="0"/>
                    <xs:element ref="geoLocationPolygon" minOccurs="0"/>
                </xs:sequence>
                <xs:sequence>
                    <xs:element ref="geoLocationBox"/>
                    <xs:element ref="geoLocationPolygon" minOccurs="0"/>

                </xs:sequence>
                <xs:sequence>
                    <xs:element ref="geoLocationPolygon"/>
                </xs:sequence>
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <!-- 18.2 geographic coverage free-->
    <xs:element name="geographicCoveragesFree">
        <xs:annotation>
            <xs:documentation/>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="geographicCoverageFree" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element for a language-dependent freetext field to provide geographical information.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element ref="language"/>
                            <xs:element name="freetext">
                                <xs:annotation>
                                    <xs:documentation>An additional free-text field to describe the locations or spatial regions covered by the data collection in case it cannot be found in the controlled vocabulary list.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="geographicCoverageLanguage">
            <xs:selector xpath="dara:geographicCoverageFree"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <!-- 18.3 geographic location point-->
    <xs:element name="geoLocationPoint">
        <xs:annotation>
            <xs:documentation xml:lang="en">A geographic point defined by a latitude and longitude in degrees, representing a geographic area in which the survey was conducted.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="pointLongitude">
                    <xs:annotation>
                        <xs:documentation>A geographic point defined by longitude in degrees.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="pointLatitude">
                    <xs:annotation>
                        <xs:documentation>A geographic point defined by latitude in degrees.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <!-- 18.4 geographic location box-->
    <xs:element name="geoLocationBox">
        <xs:annotation>
            <xs:documentation xml:lang="en">A geoLocationBox is a spatial limit specified with an east longitude value (xmax), a west longitude value (xmin), a north latitude (ymax) and a south latitude value (ymin) expressed as a decimal between the values of -180 and 180 degrees.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:all>
                <xs:element name="westBoundLongitude" minOccurs="1">
                    <xs:annotation>
                        <xs:documentation>A spatial limit specified with a west longitude value (xmin) and expressed as a decimal between the values of -180 and 180 degrees.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="eastBoundLongitude">
                    <xs:annotation>
                        <xs:documentation>A spatial limit specified with an east longitude value (xmax) and expressed as a decimal between the values of -180 and 180 degrees.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="southBoundLatitude">
                    <xs:annotation>
                        <xs:documentation>A spatial limit specified with a south latitude value (ymin) and expressed as a decimal between the values of -180 and 180 degrees.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="northBoundLatitude">
                    <xs:annotation>
                        <xs:documentation>A spatial limit specified with a north latitude value (ymax) and expressed as a decimal between the values of -180 and 180 degrees.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>
    <!-- 18.? geographic location polygon-->
    <xs:element name="geoLocationPolygon">
        <xs:annotation>
            <xs:documentation>A drawn polygon area, defined by a set of points and lines connecting the points in a closed chain.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" minOccurs="4" name="polygonPoint">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about a drawn polygon area, defined by a set of points and lines connecting the points in a closed chain.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="pointLongitude">
                                <xs:annotation>
                                    <xs:documentation>The longitudinal point of a polygon.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element name="pointLatitude">
                                <xs:annotation>
                                    <xs:documentation>The latitudinal point of a polygon.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 19. sampled universe -->
    <xs:element name="universes">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide language-dependent information about statistical entities about which inferences are to be drawn and to which analytic results refer.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="unbounded" ref="universe">
                    <xs:annotation>
                        <xs:documentation>Container element for one specific language-dependent description about the universe to which analytic results refer.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="sampledLanguage">
            <xs:selector xpath="dara:universe"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <xs:element name="universe">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="language"/>
                <xs:element name="sampled" type="richtext">
                    <xs:annotation>
                        <xs:documentation>Description of the statistical entities of the survey.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 20. sampling -->
    <xs:element name="samplings">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide language-dependent information about the sample and sample design used to select the survey respondents to represent the population.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="unbounded" ref="sampling">
                    <xs:annotation>
                        <xs:documentation>Container element for one specific language-dependent sampling method.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="samplingLanguage">
            <xs:selector xpath="dara:sampling"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <xs:element name="sampling">
        <xs:complexType>
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" maxOccurs="1"/>
                <xs:element maxOccurs="1" name="method" type="richtext">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">The type of sample and sample design used to select the respondents to represent the population.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- 21. temporal coverage formal/free->start-end Date -->
    <xs:element name="temporalCoverage">
        <xs:complexType>
            <xs:choice maxOccurs="1" minOccurs="1">
                <!-- 21.1 temporal coverage formal -->
                <xs:sequence>
                    <xs:element name="temporalCoverageFormal" maxOccurs="1">
                        <xs:annotation>
                            <xs:documentation xml:lang="en">Container element to provide information about the structured temporal time frame of the data collection.</xs:documentation>
                        </xs:annotation>
                        <xs:complexType>
                            <xs:sequence>
                                <xs:element name="startDate">
                                    <xs:annotation>
                                        <xs:documentation>Container element that provides information about the start date of the data collection.</xs:documentation>
                                    </xs:annotation>
                                    <xs:complexType>
                                        <xs:choice>
                                            <xs:element name="date" type="yyyy-mm-dd">
                                                <xs:annotation>
                                                  <xs:documentation>The date a survey started.</xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element name="monthyear" type="xs:gYearMonth"> </xs:element>
                                            <xs:element name="year" type="xs:gYear"/>
                                        </xs:choice>
                                    </xs:complexType>
                                </xs:element>
                                <xs:element name="endDate" minOccurs="0">
                                    <xs:annotation>
                                        <xs:documentation>Container element that provides information about the end date of the survey.</xs:documentation>
                                    </xs:annotation>
                                    <xs:complexType>
                                        <xs:choice>
                                            <xs:element name="date" type="yyyy-mm-dd">
                                                <xs:annotation>
                                                  <xs:documentation>The date a survey ended.</xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element name="monthyear" type="xs:gYearMonth"> </xs:element>
                                            <xs:element name="year" type="xs:gYear"/>
                                        </xs:choice>
                                    </xs:complexType>
                                </xs:element>
                            </xs:sequence>
                        </xs:complexType>
                    </xs:element>
                    <xs:element minOccurs="0" ref="temporalCoveragesFree">
                        <xs:annotation>
                            <xs:documentation>Container element to provide language-dependent information about the temporal coverage.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>
                <xs:sequence>
                    <xs:element ref="temporalCoveragesFree"/>
                </xs:sequence>
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <!-- 21.2 temporal coverage free -->
    <xs:element name="temporalCoveragesFree">
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" minOccurs="1" name="temporalCoverageFree">
                    <xs:annotation>
                        <xs:documentation>Container element for language-dependent information about the temporal coverage.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element ref="language" minOccurs="1" maxOccurs="1"/>
                            <xs:element maxOccurs="1" name="freetext">
                                <xs:annotation>
                                    <xs:documentation xml:lang="en">Provides the possibility to indicate the temporal coverage, if the calendar mode cannot be applied or as a supplement to 24.1.1.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="temporalCoverageLanguage">
            <xs:selector xpath="dara:temporalCoverageFree"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <xs:element name="temporalCoverages">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about the time frame of the data collection.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1">
                <xs:element maxOccurs="unbounded" ref="temporalCoverage">
                    <xs:annotation>
                        <xs:documentation>Container element to provide structured or unstructured information about the time frame of the data collection.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 22. time dimension controlled/free-->
    <xs:element name="timeDimensionsFree">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="timeDimensionFree" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element for lan-guage-dependent information about the time dimension of the survey.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element ref="language"/>
                            <xs:element name="freetext" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>An additional free-text field to describe the time dimensions of the survey.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="tdLanguage">
            <xs:selector xpath="dara:timeDimensionFree"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <!-- 22. time dimension frequency-->
    <xs:element name="frequencies">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="frequency" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element for specific language-dependent information about the frequency a survey was conducted.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element ref="language"/>
                            <xs:element name="freetext" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation xml:lang="en">The regular time intervals at which data is collected, for example monthly, yearly, weekly, etc.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="tdfLanguage">
            <xs:selector xpath="dara:frequency"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <xs:element name="timeDimension">
        <xs:complexType>
            <xs:choice maxOccurs="1" minOccurs="1">
                <xs:sequence>
                    <xs:element name="timeDimensionType" type="timeDimensionType">
                        <xs:annotation>
                            <xs:documentation>Predefined terms to provide time-specific information of the survey to differentiate between time dimensions.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="timeDimensionsFree" minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>Container element to provide additional language-dependent information about the time dimension of the survey.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element minOccurs="0" ref="frequencies">
                        <xs:annotation>
                            <xs:documentation>Container element to provide language-dependent information about the frequency a survey was conducted.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>
                <xs:sequence>
                    <xs:element ref="timeDimensionsFree"/>
                    <xs:element ref="frequencies" minOccurs="0"> </xs:element>
                </xs:sequence>
                <xs:sequence>
                    <xs:element ref="frequencies"> </xs:element>
                </xs:sequence>
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <xs:element name="timeDimensions">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to classify or describe surveys according to the time of data collection.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="timeDimension" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about time-specific information of the survey.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 23. contributor -->
    <xs:element name="contributors">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about a person or an institution responsible for collecting, managing, distributing, or otherwise contributing to the development of the registered resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" minOccurs="1" ref="contributor">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about a person or an institution contributing to the registered resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="contributor">
        <xs:complexType>
            <xs:choice>
                <xs:element name="person">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">Container element to provide information about a person responsible for collecting, managing, distributing, or otherwise contributing to the development of the registered resource.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element minOccurs="1" maxOccurs="1" name="firstName">
                                <xs:annotation>
                                    <xs:documentation>The first name of the person.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element name="middleName" type="xs:string" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>The middle name of the person.</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="lastName">
                                <xs:annotation>
                                    <xs:documentation>The last name of the person.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element name="contributorType" type="contributorType">
                                <xs:annotation>
                                    <xs:documentation>Predefined terms to provide information about different types of roles persons hold to contribute to the registered resource.</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element minOccurs="0" name="personIDs">
                                <xs:annotation>
                                    <xs:documentation>Container element to provide information about a unique identifier of the person and the name of the schema identifier to disambiguate individuals of similar names.</xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element maxOccurs="unbounded" name="personID">
                                            <xs:annotation>
                                                <xs:documentation>Container element to provide information about a person’s unique identifier.</xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:group ref="ID"/>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                            <xs:element minOccurs="0" ref="affiliation">
                                <xs:annotation>
                                    <xs:documentation>Container element to provide information about the organizational or institutional connection of a person. The affiliation should reflect the person´s current and/or primary employment.</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element name="institution">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">Container element to provide information about an organization or institution involved in producing the registered resource.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence maxOccurs="1" minOccurs="1">
                            <xs:element name="institutionName" minOccurs="1" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>A name of the organization or institution involved in producing the data or responsible for the registered resource.</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element name="contributorType" type="contributorType">
                                <xs:annotation>
                                    <xs:documentation>Predefined terms to provide information about different types of roles institutions hold to contribute to the registered resource.</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="institutionIDs" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>Container element to provide information about a unique identifier of the organization or institution and the name of the schema identifier to disambiguate institutions or organizations.</xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element maxOccurs="unbounded" name="institutionID">
                                            <xs:annotation>
                                                <xs:documentation>Container element to provide information about an institution’s unique identifier.</xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:group ref="ID"/>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:choice>
        </xs:complexType>
    </xs:element>

    <!-- new field: funding reference -->
    <xs:element name="fundingReferences">
        <xs:annotation>
            <xs:documentation>Container element to provide information about a person or institution that provides financial support (funding) for the resource being registered.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="fundingReference">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about financial support (funding) for the resource being registered.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="fundingReference">
        <xs:complexType>
            <xs:sequence>
                <xs:choice>
                    <xs:element name="person">
                        <xs:annotation>
                            <xs:documentation xml:lang="en">Container element to provide information about a person (funding provider).</xs:documentation>
                        </xs:annotation>
                        <xs:complexType>
                            <xs:sequence>
                                <xs:element minOccurs="1" maxOccurs="1" name="firstName">
                                    <xs:annotation>
                                        <xs:documentation>The first name of the person.</xs:documentation>
                                    </xs:annotation>
                                    <xs:simpleType>
                                        <xs:restriction base="nonemptycontentStringType"/>
                                    </xs:simpleType>
                                </xs:element>
                                <xs:element name="middleName" type="xs:string" minOccurs="0">
                                    <xs:annotation>
                                        <xs:documentation>The middle name of the person.</xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                                <xs:element name="lastName">
                                    <xs:annotation>
                                        <xs:documentation>The last name of the person.</xs:documentation>
                                    </xs:annotation>
                                    <xs:simpleType>
                                        <xs:restriction base="nonemptycontentStringType"/>
                                    </xs:simpleType>
                                </xs:element>
                                <xs:element minOccurs="0" name="personIDs">
                                    <xs:annotation>
                                        <xs:documentation>Container element to provide information about a unique identifier of the person and the name of the schema identifier to disambiguate individuals of similar names.</xs:documentation>
                                    </xs:annotation>
                                    <xs:complexType>
                                        <xs:sequence>
                                            <xs:element maxOccurs="unbounded" name="personID">
                                                <xs:annotation>
                                                  <xs:documentation>Container element to provide information about a person’s unique identifier.</xs:documentation>
                                                </xs:annotation>
                                                <xs:complexType>
                                                  <xs:group ref="funderID"/>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:sequence>
                                    </xs:complexType>
                                </xs:element>
                                <xs:element minOccurs="0" ref="affiliation">
                                    <xs:annotation>
                                        <xs:documentation>Container element to provide information about the or-ganizational or institutional connection of a person. The affiliation should reflect the person´s current and/or primary employment.</xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                                <xs:element minOccurs="0" name="award">
                                    <xs:annotation>
                                        <xs:documentation>Container element to provide information about the award.</xs:documentation>
                                    </xs:annotation>
                                    <xs:complexType>
                                        <xs:sequence>
                                            <xs:element name="awardNumber" minOccurs="0">
                                                <xs:annotation>
                                                  <xs:documentation>The identification code of the grant or sponsored award assigned by a funder.</xs:documentation>
                                                </xs:annotation>
                                                <xs:simpleType>
                                                  <xs:restriction base="nonemptycontentStringType"/>
                                                </xs:simpleType>
                                            </xs:element>
                                            <xs:element name="awardURI" minOccurs="0"
                                                type="xs:anyURI">
                                                <xs:annotation>
                                                  <xs:documentation>The uri is leading to a page provided by the funder for more information about the award.</xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element name="awardTitle" maxOccurs="1"
                                                minOccurs="0">
                                                <xs:annotation>
                                                  <xs:documentation>Container element to provide one specific language-dependent name or title of the award.</xs:documentation>
                                                </xs:annotation>
                                                <xs:complexType>
                                                  <xs:all>
                                                  <xs:element ref="language"/>
                                                  <xs:element minOccurs="1" maxOccurs="1"
                                                  name="title">
                                                  <xs:annotation>
                                                  <xs:documentation>The human readable title of the award.</xs:documentation>
                                                  </xs:annotation>
                                                  <xs:simpleType>
                                                  <xs:restriction base="nonemptycontentStringType"/>
                                                  </xs:simpleType>
                                                  </xs:element>
                                                  </xs:all>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:sequence>
                                    </xs:complexType>
                                </xs:element>
                            </xs:sequence>
                        </xs:complexType>
                    </xs:element>
                    <xs:element name="institution">
                        <xs:annotation>
                            <xs:documentation xml:lang="en">Container element to provide information about an organization or institution involved in funding the registered resource.</xs:documentation>
                        </xs:annotation>
                        <xs:complexType>
                            <xs:sequence maxOccurs="1" minOccurs="1">
                                <xs:element name="institutionName" minOccurs="1" maxOccurs="1">
                                    <xs:annotation>
                                        <xs:documentation>A name of the organization or institution involved in funding the registered resource.</xs:documentation>
                                    </xs:annotation>
                                    <xs:simpleType>
                                        <xs:restriction base="nonemptycontentStringType"/>
                                    </xs:simpleType>
                                </xs:element>
                                <xs:element name="institutionIDs" minOccurs="0">
                                    <xs:annotation>
                                        <xs:documentation>Container element to provide information about a unique identifier of the organization or institution and the name of the schema identifier to disambiguate institutions or organizations.</xs:documentation>
                                    </xs:annotation>
                                    <xs:complexType>
                                        <xs:sequence>
                                            <xs:element maxOccurs="unbounded" name="institutionID">
                                                <xs:annotation>
                                                  <xs:documentation>Container element to provide information about an institution’s unique identifier.</xs:documentation>
                                                </xs:annotation>
                                                <xs:complexType>
                                                  <xs:group ref="funderID"/>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:sequence>
                                    </xs:complexType>
                                </xs:element>
                                <xs:element minOccurs="0" name="award">
                                    <xs:annotation>
                                        <xs:documentation>Container element to provide information about the award.</xs:documentation>
                                    </xs:annotation>
                                    <xs:complexType>
                                        <xs:sequence>
                                            <xs:element name="awardNumber" minOccurs="0">
                                                <xs:annotation>
                                                  <xs:documentation>The identification code of the grant or sponsored award assigned by a funder.</xs:documentation>
                                                </xs:annotation>
                                                <xs:simpleType>
                                                  <xs:restriction base="nonemptycontentStringType"/>
                                                </xs:simpleType>
                                            </xs:element>
                                            <xs:element name="awardURI" minOccurs="0"
                                                type="xs:anyURI">
                                                <xs:annotation>
                                                  <xs:documentation>The URI is leading to a page provided by the funder for more information about the award.</xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element name="awardTitle" maxOccurs="1"
                                                minOccurs="0">
                                                <xs:annotation>
                                                  <xs:documentation>Container element to provide one specific language-dependent name or title of the award.</xs:documentation>
                                                </xs:annotation>
                                                <xs:complexType>
                                                  <xs:all>
                                                  <xs:element ref="language"/>
                                                  <xs:element minOccurs="1" maxOccurs="1"
                                                  name="title">
                                                  <xs:annotation>
                                                  <xs:documentation>The human readable title of the award.</xs:documentation>
                                                  </xs:annotation>
                                                  <xs:simpleType>
                                                  <xs:restriction base="nonemptycontentStringType"/>
                                                  </xs:simpleType>
                                                  </xs:element>
                                                  </xs:all>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:sequence>
                                    </xs:complexType>
                                </xs:element>
                            </xs:sequence>
                        </xs:complexType>
                        <xs:unique name="fundingReferenceInstitutionLanguage">
                            <xs:selector xpath="dara:institutionName"/>
                            <xs:field xpath="dara:language"/>
                        </xs:unique>
                    </xs:element>
                </xs:choice>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 24. collection mode controlled-->
    <xs:element name="collectionModeType" type="collectionModeType">
        <xs:annotation>
            <xs:documentation xml:lang="en">Predefined terms to provide information about different types of methods that are used to collect information from a sample in a survey. </xs:documentation>
        </xs:annotation>
    </xs:element>
    <!-- 25. collection mode free -->
    <xs:element name="collectionModeFree">
        <xs:complexType>
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"/>
                <xs:element minOccurs="1" maxOccurs="1" name="freetext" type="richtext">
                    <xs:annotation>
                        <xs:documentation>An additional free-text field to describe the methods that are used to collect information from a sample in a survey.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>
    <xs:element name="collectionModesFree">
        <xs:annotation>
            <xs:documentation>Container element to provide information about the mode of data collection used to collect information from a sample in a survey.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="collectionModeFree" maxOccurs="unbounded" minOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Container element for language-dependent descriptions about the mode of data collection.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="collectionModeLanguage">
            <xs:selector xpath="dara:collectionModeFree"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <!-- collection modes -->
    <xs:element name="collectionModes">
        <xs:annotation>
            <xs:documentation>Container element to provide information about the mode of data collection used to collect information from a sample in a survey.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" name="collectionMode">
                    <xs:annotation>
                        <xs:documentation>Container element to provide structured or unstructured information about the mode of data collection used to collect information from a sample in a survey.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:choice>
                            <xs:sequence>
                                <xs:element ref="collectionModeType">
                                    <xs:annotation>
                                        <xs:documentation>Predefined terms to provide information about different types of methods that are used to collect information from a sample in a survey.</xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                                <xs:element ref="collectionModesFree" minOccurs="0">
                                    <xs:annotation>
                                        <xs:documentation>Container element to provide language-dependent information in order to classify or describe methods that are used to collect information from a sample in a survey.</xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                            </xs:sequence>
                            <xs:sequence>
                                <xs:element ref="collectionModesFree"/>
                            </xs:sequence>
                        </xs:choice>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>


    <!-- 26. dataset-->
    <xs:element name="dataSet">
        <xs:complexType>
            <xs:choice>
                <xs:group ref="withUnits"/>
                <xs:group ref="withoutUnits"/>
            </xs:choice>
        </xs:complexType>
    </xs:element>

    <xs:element name="dataSets">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about the data set, which is a collection of data, where every column of the statistical data matrix represents a particular variable, and each row corresponds to a given member of the data set in question.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="dataSet" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about a specific data set.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- dataset dataType -->
    <xs:element name="dataType">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="language"/>
                <xs:element maxOccurs="1" name="freetext">
                    <xs:annotation>
                        <xs:documentation>This metadata describes the kind of data that a publication agent registers.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="dataTypes">
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" minOccurs="1" ref="dataType">
                    <xs:annotation>
                        <xs:documentation>Container element for language-dependent information about the data type being registered.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="dataTypeLanguage">
            <xs:selector xpath="dara:dataType"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>

    <!-- 26.5-26.9 file:technical description of the data -->
    <xs:element name="file">
        <xs:complexType>
            <xs:choice maxOccurs="1" minOccurs="1">
                <!--<xs:element name="name" type="xs:string"/>-->
                <xs:sequence>
                    <xs:element maxOccurs="1" name="name">
                        <xs:annotation>
                            <xs:documentation>The name of the data file.</xs:documentation>
                        </xs:annotation>
                        <xs:simpleType>
                            <xs:restriction base="nonemptycontentStringType"/>
                        </xs:simpleType>
                    </xs:element>
                    <xs:element minOccurs="0" maxOccurs="1" ref="format">
                        <xs:annotation>
                            <xs:documentation>A textual desciption of the technical format of the data file.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element minOccurs="0" maxOccurs="1" ref="size">
                        <xs:annotation>
                            <xs:documentation>The size of a data file or resource.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element minOccurs="0" maxOccurs="1" ref="fingerprint">
                        <xs:annotation>
                            <xs:documentation>Checksum which confirms the authenticity of the data or data file by assignung a hash value (digital fingerprint).</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element minOccurs="0" maxOccurs="1" ref="fingerprintMethod">
                        <xs:annotation>
                            <xs:documentation>The technical procedure generating data fingerprint.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>
                <xs:sequence>
                    <xs:element maxOccurs="1" ref="format"> </xs:element>
                    <xs:element minOccurs="0" maxOccurs="1" ref="size"/>
                    <xs:element minOccurs="0" maxOccurs="1" ref="fingerprint"/>
                    <xs:element minOccurs="0" maxOccurs="1" ref="fingerprintMethod"/>
                </xs:sequence>
                <xs:sequence>
                    <xs:element maxOccurs="1" ref="size"/>
                    <xs:element minOccurs="0" maxOccurs="1" ref="fingerprint"/>
                    <xs:element minOccurs="0" maxOccurs="1" ref="fingerprintMethod"/>
                </xs:sequence>
                <xs:sequence>
                    <xs:element maxOccurs="1" ref="fingerprint"/>
                    <xs:element minOccurs="0" maxOccurs="1" ref="fingerprintMethod"/>
                </xs:sequence>
                <xs:sequence>
                    <xs:element maxOccurs="1" ref="fingerprintMethod"/>
                </xs:sequence>
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <!-- file attributes -->
    <xs:element name="format">
        <xs:annotation>
            <xs:documentation>A textual description of the technical format of the data file.</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="nonemptycontentStringType"/>
        </xs:simpleType>
    </xs:element>
    <xs:element name="size">
        <xs:annotation>
            <xs:documentation>The size of a data file or resource.</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="nonemptycontentStringType"/>
        </xs:simpleType>
    </xs:element>
    <xs:element name="fingerprint">
        <xs:annotation>
            <xs:documentation>Checksum which confirms the authenticity of the data or data file by assigning a hash value (digital fingerprint).</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="nonemptycontentStringType"/>
        </xs:simpleType>
    </xs:element>
    <xs:element name="fingerprintMethod">
        <xs:annotation>
            <xs:documentation>The technical procedure generating data fingerprint.</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="nonemptycontentStringType"/>
        </xs:simpleType>
    </xs:element>
    <!-- file attributes -->
    <xs:element name="files">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide specific information of the data file such as name, format, size and fingerprint of the file.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="file" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element to provide specific information of the data file such as name, format, size, and fingerprint of the file.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 27. notes -->
    <xs:element name="notes">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide language-dependent remarks or other information about the registered resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="note" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element for one specific language-dependent further remark about the registered resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="noteLanguage">
            <xs:selector xpath="dara:note"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <xs:element name="note">
        <xs:complexType>
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" maxOccurs="1"/>
                <xs:element maxOccurs="1" name="text" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Textual description of further information or remarks about the registered resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- *28/29 availability controlled/free-->
    <xs:element name="availability">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to classify or describe availability conditions of the registered resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="1" ref="availabilityType">
                    <xs:annotation>
                        <xs:documentation>Predefined terms to provide information about different types of availability conditions of the registered resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element maxOccurs="unbounded" ref="availabilityFree" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Container element for one specific language-dependent availability specification of the registered resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" name="embargoDate" type="yyyy-mm-dd">
                    <xs:annotation>
                        <xs:documentation>Information about the end date of access restrictions in case an embargo period has been in effect.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="availabilityLanguage">
            <xs:selector xpath="dara:availabilityFree"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <xs:element name="availabilityType" type="availabilityType">
        <xs:annotation>
            <xs:documentation xml:lang="en">Predefined terms to provide information about different types of the availability conditions of the registered resource.</xs:documentation>
        </xs:annotation>
    </xs:element>
    <xs:element name="availabilityFree">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about availability specifications of the registered resource wrapping a free-text field and a language-subproperty.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:all minOccurs="1">
                <xs:element ref="language">
                    <xs:annotation>
                        <xs:documentation>The language of the metadata information. It applies to the according piece of information where it is specified.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="freetext" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>An additional free-text field to describe the availability specifications of the registered resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- 30.rights -->
    <xs:element name="rights">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about legal principles or fundamental normative rules about what is allowed of people or owed to people in regards to the registered resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:choice>
                <xs:sequence>
                    <xs:element name="licenseType" type="licenseType">
                        <xs:annotation>
                            <xs:documentation>Predefined terms to provide information about different types of creative commons licenses to allow creators to maintain copyrights on their works and clarify what others can do with content licensed with one of those licenses.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element maxOccurs="unbounded" ref="right" minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>Container element for one specific language-dependent legal text about the registered resource.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>
                <xs:sequence>
                    <xs:element maxOccurs="unbounded" ref="right">
                        <xs:annotation>
                            <xs:documentation>Container element for one specific language-dependent legal text about the registered resource.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>
            </xs:choice>
        </xs:complexType>
        <xs:unique name="rightLanguage">
            <xs:selector xpath="dara:right"/>
            <xs:field xpath="dara:language"/>
        </xs:unique>
    </xs:element>
    <xs:element name="right">
        <xs:complexType mixed="false">
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element ref="language" maxOccurs="1"/>
                <xs:element minOccurs="1" name="freetext">
                    <xs:annotation>
                        <xs:documentation>A free-text field to describe if and how others might use or download the registered resource.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 31.relation -->
    <xs:element name="relation">
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="1" name="identifier">
                    <xs:annotation>
                        <xs:documentation>The value of a formally registered unique identifier of the related resource to disambiguate resources.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="identifierType" type="pidType">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">Predefined terms to provide information about different types of unique identifiers for the related resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="relationType" type="relationType">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">Predefined terms to provide information about different types of relations between the resource being registered and a related resource, e.g. the registered resources is a new version ofthe related resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" name="relatedMetadataSchema">
                    <xs:annotation>
                        <xs:documentation>The name of the metadata schema of the related resource, e.g. DDI-C. A schema is list of core metadata properties chosen for an accurate and consistent identification of a resource.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element minOccurs="0" name="schemaType">
                    <xs:annotation>
                        <xs:documentation>Terms to provide information about different types of schemas used for the metadata of the related resource, e.g. XSD.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="schemaURI" type="xs:anyURI" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>A metadata schema is identi-fied by a Uniform Resource Identifier (URI). A URI is a compact sequence of characters that identifies an abstract or physical resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="relations">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about resources that are related to the regis-tered resource such as the type of the identifier, the relation or information about the schema (metadata, type, URI).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="relation" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about resources that are related to the registered resource.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 32.publications -->
    <xs:element name="publications">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about an article, a document, etc. that has been made available to the public.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence minOccurs="1" maxOccurs="1">
                <xs:element maxOccurs="unbounded" ref="publication">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about a structured or/and unstructured information about a publication.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="publication">
        <xs:complexType>
            <xs:choice maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="1" ref="unstructuredPublication" minOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Container element to provide unstructured information about an article, a document or another resource that has been made available to the public.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="structuredPublication" maxOccurs="1" minOccurs="1"/>
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <!-- 32.1. structured-->
    <xs:element name="structuredPublication">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide structured information about an article, a document or another resource, that has been made available to the public.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element name="documentType" type="documentType" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">The type of publication that has been made available to the public to differentiate between document types.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="authorsEditors" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about a person, who wrote and originated (author) and/or edited and modified (editor) the publication.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element maxOccurs="1" name="title">
                    <xs:annotation>
                        <xs:documentation>The title or name of the publication.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="year" type="xs:gYear">
                    <xs:annotation>
                        <xs:documentation>The year on which the publication has been or is planned to be published.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="publisher" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" name="places" type="xs:string">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">The place of publication is the name of the city where the publisher is located.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="journal" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>The name of a academic or scholarly  periodical publication intended to further the progress of science, usually by reporting new research.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="volume" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>The volume number refers to the number of years a journal has been in publication.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="issue" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>The issue number refers to the number of individual publications during the year.  </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="anthology" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>A book or other collection of selected writings by various authors, usually in the same literary form, of the same period, or on the same subject.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="pages" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>The number of pages within the publication.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="isbn" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>The International Standard Book Number (ISBN) is a unique numeric commercial book identifier. There are two formats: a 10‐digit ISBN format and a 13‐digit ISBN.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="ISSNs" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Container element for the International Standard Serial Number (ISSN).
</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="PIDs" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about the Per-sistent Identifier (PID) that has been generated to uniquely and permanently identify the structured publication.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="authorsEditors">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about a person, who wrote and originated (author) or edited and modifies (editor) the publication.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="authorEditor">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about an author and/or an editor of a publication.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="authorEditor">
        <xs:complexType mixed="false">
            <xs:choice>
                <xs:element ref="author" maxOccurs="1" minOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about an author.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element maxOccurs="1" minOccurs="1" ref="editor"/>
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <xs:element name="author">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about an author.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element minOccurs="1" maxOccurs="1" name="firstName">
                    <xs:annotation>
                        <xs:documentation>The first name of the person.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="middleName" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>The middle name of the person.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="lastName">
                    <xs:annotation>
                        <xs:documentation>The last name of the person.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="authors">
        <xs:complexType>
            <xs:sequence maxOccurs="unbounded" minOccurs="1">
                <xs:element ref="author"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="editor">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide information about an editor.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element minOccurs="1" maxOccurs="1" name="name">
                    <xs:annotation>
                        <xs:documentation>The full name of the editor.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="editors">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="editor" maxOccurs="unbounded" minOccurs="1"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="ISSNs">
        <xs:annotation>
            <xs:documentation>The International Standard Serial Number (ISSN) is an 8-digit code used to identify newspapers, journals, magazines and periodicals of all kinds and on all media–print and electronic. </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" minOccurs="1" name="ISSN">
                    <xs:annotation>
                        <xs:documentation>The International Standard Serial Number (ISSN) is a unique 8-digit code used to identify a print or electronic periodical publication.
</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="PID">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="ID">
                    <xs:annotation>
                        <xs:documentation>The value of a formally registered unique and persistent identifier of the structured information of publication. </xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element ref="pidType">
                    <xs:annotation>
                        <xs:documentation>Predefined terms to provide information about different types of Persistent Identifiers of the unstructured information of the publication to differentiate between identifier types.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PIDs">
        <xs:complexType>
            <xs:sequence maxOccurs="unbounded" minOccurs="1">
                <xs:element ref="PID">
                    <xs:annotation>
                        <xs:documentation>Container element for the value of a formally registered unique and persistent identifier of the unstructured information of publication.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <!-- pid type -->
    <xs:element name="pidType" type="pidType">
        <xs:annotation>
            <xs:documentation xml:lang="en">Predefined terms to provide information about different types of Persistent Identifiers of the structured information of the publication.</xs:documentation>
        </xs:annotation>
    </xs:element>

    <!-- 32.2. unstructured-->
    <xs:element name="unstructuredPublication">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element to provide unstructured information about an article, a document or another resource, that has been made available to the public.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="1" name="freetext" type="richtext">
                    <xs:annotation>
                        <xs:documentation>Unstructured bibliographic information related to the publication.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="PIDs" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Container element to provide information about Persistent Identifiers (PIDs) that have been generated to uniquely and permanently identify unstructured publications.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- *34.resource identifier /current version-->
    <xs:element name="resourceIdentifier">
        <xs:annotation>
            <xs:documentation xml:lang="en">Container element for a resource identifier, which includes a unique identifier and a version number to identify the resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="identifier">
                    <xs:annotation>
                        <xs:documentation>The value of a formally registered unique internal identifier provided by the publication agent to disambiguate resources.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element minOccurs="0" name="currentVersion">
                    <xs:annotation>
                        <xs:documentation>A version number, which is a unique sequence of numbers, can be provided for the registered resource as a reference to what changes have been made between versions.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 38. glplace -->
    <xs:element name="publicationPlace">
        <xs:annotation>
            <xs:documentation xml:lang="en">The geographic location, where the resource is/was published, produced and/or distributed.</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string"/>
        </xs:simpleType>
    </xs:element>

    <!-- resource -->
    <xs:element name="resource">
        <xs:complexType>
            <xs:sequence minOccurs="1">
                <xs:element ref="resourceType"/>
                <xs:element ref="resourceTypesFree" minOccurs="0"/>
                <xs:element ref="resourceIdentifier" minOccurs="0"/>
                <xs:element ref="titles" minOccurs="1" maxOccurs="1"/>
                <xs:element ref="otherTitles" minOccurs="0"/>
                <xs:element ref="collectiveTitles" minOccurs="0"/>
                <xs:element ref="creators" minOccurs="1" maxOccurs="1"/>
                <xs:element ref="dataURLs" minOccurs="1" maxOccurs="1"/>
                <xs:element ref="doiProposal" minOccurs="0" maxOccurs="1"/>
                <xs:element ref="publicationDate" minOccurs="1" maxOccurs="1"/>
                <xs:element ref="publicationPlace" minOccurs="0"/>
                <xs:element minOccurs="0" ref="publisher"/>
                <xs:element ref="availability"/>
                <xs:element ref="rights" minOccurs="0"/>
                <xs:element ref="resourceLanguage" minOccurs="0" maxOccurs="1"/>
                <xs:element ref="alternativeIDs" minOccurs="0"/>
                <xs:element ref="classifications" minOccurs="0"/>
                <xs:element ref="controlledKeywords" minOccurs="0"/>
                <xs:element ref="freeKeywords" minOccurs="0"/>
                <xs:element ref="descriptions" minOccurs="0"/>
                <xs:element ref="geographicCoverages" minOccurs="0"/>
                <xs:element ref="universes" minOccurs="0"/>
                <xs:element ref="samplings" minOccurs="0"/>
                <xs:element ref="temporalCoverages" minOccurs="0"/>
                <xs:element ref="timeDimensions" minOccurs="0"/>
                <xs:element ref="contributors" minOccurs="0"/>
                <xs:element ref="fundingReferences" minOccurs="0"/>
                <xs:element ref="collectionModes" minOccurs="0"/>
                <xs:element ref="dataSets" minOccurs="0"/>
                <xs:element ref="notes" minOccurs="0"/>
                <xs:element ref="relations" minOccurs="0"/>
                <xs:element ref="publications" minOccurs="0"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- ID group(identifier/schema/schemaURI) -->
    <xs:group name="ID">
        <xs:sequence>
            <xs:element name="identifierURI" type="xs:anyURI">
                <xs:annotation>
                    <xs:documentation xml:lang="en">The value of a formally registered unique identifier.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="identifierSchema">
                <xs:annotation>
                    <xs:documentation xml:lang="en">The name of the schema the identifier is related to.</xs:documentation>
                </xs:annotation>
                <xs:simpleType>
                    <xs:restriction base="nonemptycontentStringType"/>
                </xs:simpleType>
            </xs:element>
        </xs:sequence>
    </xs:group>

    <!-- IDFunder - fundingReference) -->
    <xs:group name="funderID">
        <xs:sequence>
            <xs:element name="identifierURI" type="xs:anyURI">
                <xs:annotation>
                    <xs:documentation xml:lang="en">The value of a formally registered unique identifier.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="identifierSchemaType" type="identifierSchemaType">
                <xs:annotation>
                    <xs:documentation xml:lang="en">The name of the schema the identifier is related to.</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:group>
    <!-- unitType and NumberOfUnits-->
    <xs:group name="withUnits">
        <xs:sequence>
            <!-- 26.1 type of units-->
            <xs:element name="unitType" type="unitType">
                <xs:annotation>
                    <xs:documentation xml:lang="en">Describes the entity being analyzed or observed in the resource.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <!-- 26.2 number of units-->
            <xs:element name="numberUnits" type="xs:int">
                <xs:annotation>
                    <xs:documentation xml:lang="en">The number of units being analyzed or observed in the resource.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element minOccurs="0" maxOccurs="1" name="numberVariables" type="xs:int">
                <xs:annotation>
                    <xs:documentation>This metadata describes the number of variables within a registered dataset.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element minOccurs="0" ref="dataTypes">
                <xs:annotation>
                    <xs:documentation>Container element to provide language-dependent information about the types of data.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element minOccurs="0" ref="files">
                <xs:annotation>
                    <xs:documentation>Container element to provide specific information of the data file.</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:group>
    <!-- without unitType and NumberOfUnits-->
    <xs:group name="withoutUnits">
        <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="1" name="numberVariables" type="xs:int"/>
            <xs:element minOccurs="0" ref="dataTypes"/>
            <xs:element minOccurs="0" ref="files"/>
        </xs:sequence>
    </xs:group>

    <!-- defines value for mandatory fields -->
    <xs:simpleType name="nonemptycontentStringType">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:whiteSpace value="collapse"/>
        </xs:restriction>
    </xs:simpleType>
    <!-- doi type -->
    <xs:simpleType name="doiType">
        <xs:restriction base="xs:token">
            <xs:pattern value="[1][0][/.].*"/>
        </xs:restriction>
    </xs:simpleType>
    <!-- richtext -->
    <xs:complexType name="richtext" mixed="true">
        <xs:sequence maxOccurs="unbounded" minOccurs="0">
            <xs:element type="richtext" minOccurs="0" name="p" maxOccurs="unbounded"/>
            <xs:element minOccurs="0" name="br" maxOccurs="unbounded">
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:length value="0"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element type="richtext" minOccurs="0" name="strong" maxOccurs="unbounded"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="ol">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="li" type="richtext" maxOccurs="unbounded"/>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="ul">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="li" type="richtext" maxOccurs="unbounded"/>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="yyyy-mm-dd">
        <xs:annotation>
            <xs:documentation>Calendar dates are represented yyyy-mm-dd format, following ISO 8601. This is a W3C XML Schema date type, but without the optional timezone data.</xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:date">
            <xs:pattern value="[^:Z]*"/>
        </xs:restriction>
    </xs:simpleType>
</xs:schema>
"""


schema = replace_includes(dara_schema)

