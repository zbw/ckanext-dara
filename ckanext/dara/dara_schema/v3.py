# -*- coding: utf-8 -*-
## to avoid reading from file

schema = """<?xml version="1.0" encoding="UTF-8"?>
<!-- da|ra Metadatenschema v3.0 - www.da-ra.de 04032014-->
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
    <!--  *0. Object Resource Type-->
    <xs:element name="resourceType">
        <xs:annotation>
            <xs:documentation>mandatory</xs:documentation>
            <xs:documentation xml:lang="de">Genereller Typ der Ressource</xs:documentation>
            <xs:documentation xml:lang="en">The general type of a resource</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:enumeration value="1">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Sammlung</xs:documentation>
                        <xs:documentation xml:lang="en">Collection</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="2">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Datensatz</xs:documentation>
                        <xs:documentation xml:lang="en">Dataset</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="3">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Text</xs:documentation>
                        <xs:documentation xml:lang="en">Text</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="4">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Video</xs:documentation>
                        <xs:documentation xml:lang="en">Video</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="5">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Bild</xs:documentation>
                        <xs:documentation xml:lang="en">Image</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="6">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Audio</xs:documentation>
                        <xs:documentation xml:lang="en">Audio</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="7">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Interaktive Resource</xs:documentation>
                        <xs:documentation xml:lang="en">Interactive Resource</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="resourceTypesFree">
        <xs:annotation>
            <xs:documentation>optional</xs:documentation>
            <xs:documentation>resourceTypesFree is a container element for 1 or 2 resourceTypeFree</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="resourceTypeFree" minOccurs="1" maxOccurs="2"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="resourceTypeFreeLanguage">
            <xs:selector xpath="resourceTypeFree/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
    <xs:element name="resourceTypeFree">
        <xs:annotation>
            <xs:documentation xml:lang="de">Beschreibung der Ressource. Format ist offen, es sollte
                aber ein einzelner, ergänzender Begriff zum Generellen Ressourcentyp sein, damit ein
                Paar gebildet werden kann (Text/Artikel; Bild/Tabelle).</xs:documentation>
            <xs:documentation xml:lang="en">A description of the resource. The format is open, but
                the preferred format is a single term of some detail so that a pair can be formed
                with the property “General Resource Type”.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"/>
                <xs:element name="typeName" minOccurs="1" maxOccurs="1">
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
            <xs:documentation>mandatory</xs:documentation>
            <xs:documentation>titles is a container element for 1 or 2 title</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="title" minOccurs="1" maxOccurs="2"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="titleLanguage">
            <xs:selector xpath="title/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
    <xs:element name="title">
        <xs:annotation>
            <xs:documentation xml:lang="de">Titel der Ressource</xs:documentation>
            <xs:documentation xml:lang="en">The title of a resource</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"/>
                <xs:element name="titleName" minOccurs="1" maxOccurs="1">
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
            <xs:documentation>optional</xs:documentation>
            <xs:documentation>otherTitles is a container element for 1 or many otherTitle</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="otherTitle" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="otherTitle">
        <xs:annotation>
            <xs:documentation xml:lang="de">Zusätzlicher Titel</xs:documentation>
            <xs:documentation xml:lang="en">Further title</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language"/>
                <xs:element minOccurs="1" maxOccurs="1" name="titleName">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="titleType">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Typ des zusätzlichen
                            Titels</xs:documentation>
                        <xs:documentation xml:lang="en">The type of the other title</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:enumeration value="1">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Alternativer
                                        Titel</xs:documentation>
                                    <xs:documentation xml:lang="en">Alternative
                                        Title</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="2">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Übersetzter
                                        Titel</xs:documentation>
                                    <xs:documentation xml:lang="en">Translated
                                        Title</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="3">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Untertitel</xs:documentation>
                                    <xs:documentation xml:lang="en">Subtitle</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="4">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Originaltitel</xs:documentation>
                                    <xs:documentation xml:lang="en">Original
                                        Title</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- *3.collective title -->
    <xs:element name="collectiveTitles">
        <xs:annotation>
            <xs:documentation>optional</xs:documentation>
            <xs:documentation>collectiveTitles is a container element for 1 or 2 collectiveTitle</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="collectiveTitle" minOccurs="1" maxOccurs="2"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="ctitleLanguage">
            <xs:selector xpath="collectiveTitle/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
    <xs:element name="collectiveTitle">
        <xs:annotation>
            <xs:documentation xml:lang="de">Titel einer Schriftenreihe, Working Paper Series
                usw.</xs:documentation>
            <xs:documentation xml:lang="en">A title of book series, working paper series,
                etc.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"/>
                <xs:element name="titleName" minOccurs="1" maxOccurs="1">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="numbering" type="xs:string">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Zählungen, die eine Periodizität zum
                            Ausdruck bringen oder die Titel nummerieren.</xs:documentation>
                        <xs:documentation xml:lang="en">Indication of the source: volume count -
                            journal number - page numbers.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- *4.creators -->
    <xs:element name="creators">
        <xs:annotation>
            <xs:documentation>mandatory</xs:documentation>
            <xs:documentation>creators is a container element for 1 or many creator</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="creator"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="creator">
        <xs:annotation>
            <xs:documentation xml:lang="de">Name einer Person und/oder einer Institution
                (Primärforscher bzw. Autoren)</xs:documentation>
            <xs:documentation xml:lang="en">The name of the principal investigator or author. May be a
                corporate/institutional or a personal name. Either 4.1 or 4.2 or
                both.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:choice>
                <xs:element ref="person" maxOccurs="1" minOccurs="1"> </xs:element>
                <xs:element maxOccurs="1" minOccurs="1" ref="institution"> </xs:element>
            </xs:choice>
        </xs:complexType>
    </xs:element>

    <!-- *4.1 person -->
    <xs:element name="person">
        <xs:annotation>
            <xs:documentation xml:lang="de">Name der Person (Vorname, zweiter Name,
                Nachname).</xs:documentation>
            <xs:documentation xml:lang="en">The name of the person (First name, Middle name, Last
                Name).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element minOccurs="1" maxOccurs="1" name="firstName">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="middleName" type="xs:string" minOccurs="0"/>
                <xs:element name="lastName">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element minOccurs="0" name="personIDs">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element maxOccurs="unbounded" name="personID">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Eindeutiger Identifier der
                                        Person. Kann von da|ra ergänzt werden, wenn nicht
                                        vorhanden.</xs:documentation>
                                    <xs:documentation xml:lang="en">Unique identifier of the person.
                                        May be supplemented by da|ra if not
                                        submitted.</xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:group ref="ID"/>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element minOccurs="0" ref="affiliation"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="affiliation">
        <xs:annotation>
            <xs:documentation xml:lang="de">Zugehörigkeit des Primärforschers oder des Autors zu
                einer Institution.</xs:documentation>
            <xs:documentation xml:lang="en">The affiliation of the person.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="2" name="affiliationName">
                    <xs:complexType>
                        <xs:all maxOccurs="1">
                            <xs:element ref="language"/>
                            <xs:element name="name" minOccurs="1" maxOccurs="1">
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                        </xs:all>
                    </xs:complexType>
                </xs:element>
                <xs:element name="affiliationIDs" minOccurs="0">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element maxOccurs="unbounded" name="affiliationID">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Eindeutiger Identifier der
                                        Affiliation gemäß verschiedenen Schemata. Kann von da|ra ergänzt werden, wenn nicht
                                        vorhanden.</xs:documentation>
                                    <xs:documentation xml:lang="en">Unique Identifier of the
                                        affiliation according to various schemes. May be
                                        supplemented by da|ra if not submitted.</xs:documentation>
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
        <xs:unique name="affiliationLanguage">
            <xs:selector xpath="affiliationName/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>

    <!-- *4.2 institution -->
    <xs:element name="institution">
        <xs:annotation>
            <xs:documentation xml:lang="de">Name einer Institution (Primärforscher oder
                Autor).</xs:documentation>
            <xs:documentation xml:lang="en">The name of the institution.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element name="institutionName" maxOccurs="2">
                    <xs:complexType>
                        <xs:all>
                            <xs:element ref="language"/>
                            <xs:element minOccurs="1" maxOccurs="1" name="name">
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                        </xs:all>
                    </xs:complexType>
                </xs:element>
                <xs:element name="institutionIDs" minOccurs="0">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element maxOccurs="unbounded" name="institutionID">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Eindeutiger Identifier der
                                        Institution gemäß verschiedenen Schemata. Kann von da|ra ergänzt werden, wenn nicht
                                        vorhanden.</xs:documentation>
                                    <xs:documentation xml:lang="en">Unique identifier of the
                                        institution according to various schemes. May be
                                        supplemented by da|ra if not submitted.</xs:documentation>
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
        <xs:unique name="institutionLanguage">
            <xs:selector xpath="institutionName/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>

    <!-- *9.doi proposal -->
    <xs:element name="doiProposal" type="doiType">
        <xs:annotation>
            <xs:documentation>optional</xs:documentation>
            <xs:documentation xml:lang="de">Vorschlag einer DOI, wenn vom Publikationsagenten kein
                automatisch generierter DOI-Name gewünscht wird.</xs:documentation>
            <xs:documentation xml:lang="en">The Publication Agent may suggest a DOI-name, if an
                automatically generated DOI name is not required.</xs:documentation>
        </xs:annotation>
    </xs:element>
    <!-- *8.url -->
    <xs:element name="dataURLs">
        <xs:annotation>
            <xs:documentation>mandatory</xs:documentation>
            <xs:documentation>dataURLs is a container element for 1 or many dataURL</xs:documentation>
            <xs:documentation xml:lang="de">URL, zu der DOI aufgelöst wird (Landing
                Page). Es können eine oder mehrere URLs angegeben werden. Der DOI-Name wird von der ersten angegeben URL aus aufgelöst (Landing page).</xs:documentation>
            <xs:documentation xml:lang="en">Each DOI name has an URL to which it resolves (Landing
                Page). It is possible to enter one or more URLs. The DOI name will be resolved from the first URL (Landing page).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element minOccurs="1" maxOccurs="unbounded" name="dataURL" type="xs:anyURI">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Bitte geben Sie eine gültige URL an, beginnend mit http:// oder https://</xs:documentation>
                        <xs:documentation xml:lang="en">Please enter a valid URL starting with http:// or https://</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="dataURL">
            <xs:selector xpath="dataURL"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>

    <!-- 11. resource language -->
    <xs:element name="resourceLanguage">
        <xs:annotation>
            <xs:documentation>optional</xs:documentation>
            <xs:documentation xml:lang="de">Sprache, in der die Ressource beim Publikationsagenten
                vorliegt. (ISO 639-2)</xs:documentation>
            <xs:documentation xml:lang="en">The language in which the resource is available at the
                Publication Agent. (ISO 639-2)</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="bel">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Weißrussisch</xs:documentation>
                        <xs:documentation xml:lang="en">Belarusian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="bos">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Bosnisch</xs:documentation>
                        <xs:documentation xml:lang="en">Bosnian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="cze">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Tschechisch</xs:documentation>
                        <xs:documentation xml:lang="en">Czech</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="dut">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Niederländisch</xs:documentation>
                        <xs:documentation xml:lang="en">Dutch; Flemish</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="eng">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Englisch</xs:documentation>
                        <xs:documentation xml:lang="en">English</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="est">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Estnisch</xs:documentation>
                        <xs:documentation xml:lang="en">Estonian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="fin">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Finnisch</xs:documentation>
                        <xs:documentation xml:lang="en">Finnish</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="fre">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Französisch</xs:documentation>
                        <xs:documentation xml:lang="en">French</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="gre">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Neugriechisch</xs:documentation>
                        <xs:documentation xml:lang="en">Greek, Modern (1453-)</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="ger">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Deutsch</xs:documentation>
                        <xs:documentation xml:lang="en">German</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="hrv">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Kroatisch</xs:documentation>
                        <xs:documentation xml:lang="en">Croatian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="hun">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Ungarisch</xs:documentation>
                        <xs:documentation xml:lang="en">Hungarian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="ita">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Italienisch</xs:documentation>
                        <xs:documentation xml:lang="en">Italian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="lav">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Lettisch</xs:documentation>
                        <xs:documentation xml:lang="en">Latvian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="lit">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Litauisch</xs:documentation>
                        <xs:documentation xml:lang="en">Lithuanian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="nor">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Norwegisch</xs:documentation>
                        <xs:documentation xml:lang="en">Norwegian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="pol">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Polnisch</xs:documentation>
                        <xs:documentation xml:lang="en">Polish</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="rum">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Rumänisch</xs:documentation>
                        <xs:documentation xml:lang="en">Romanian; Moldavian;
                            Moldovan</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="rus">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Russisch</xs:documentation>
                        <xs:documentation xml:lang="en">Russian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="slo">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Slowakisch</xs:documentation>
                        <xs:documentation xml:lang="en">Slovak</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="slv">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Slowenisch</xs:documentation>
                        <xs:documentation xml:lang="en">Slovenian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="spa">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Spanisch</xs:documentation>
                        <xs:documentation xml:lang="en">Spanish; Castilian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="srp">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Serbisch</xs:documentation>
                        <xs:documentation xml:lang="en">Serbian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="swe">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Schwedisch</xs:documentation>
                        <xs:documentation xml:lang="en">Swedish</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="ukr">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Ukrainisch</xs:documentation>
                        <xs:documentation xml:lang="en">Ukrainian</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>

    <!-- *.metadata language -->
    <xs:element name="language">
        <xs:annotation>
            <xs:documentation xml:lang="de">Sprache der Metadaten einer Ressource (Deutsch und/oder
                Englisch). </xs:documentation>
            <xs:documentation xml:lang="en">The language of the resource
                metadata (German or English).</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="de">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Deutsch</xs:documentation>
                        <xs:documentation xml:lang="en">German</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="en">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Englisch</xs:documentation>
                        <xs:documentation xml:lang="en">English</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>

    <!-- *12.publication date -->
    <xs:element name="publicationDate">
        <xs:annotation>
            <xs:documentation>mandatory</xs:documentation>
            <xs:documentation xml:lang="de">Datum der Veröffentlichung der Ressource beim
                Publikationsagenten.</xs:documentation>
            <xs:documentation xml:lang="en">The publication date of the resource submitted by the
                Publication Agent.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:choice>
                <xs:element name="date" type="xs:date"> </xs:element>
                <xs:element name="monthyear" type="xs:gYearMonth"> </xs:element>
                <xs:element name="year" type="xs:gYear"/>
            </xs:choice>
        </xs:complexType>
    </xs:element>

    <!-- 13. alternative identifier -->
    <xs:element name="alternativeIDs">
        <xs:annotation>
            <xs:documentation>alternativeIDs is a container element for 1 or many alternativeID</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="alternativeID" maxOccurs="unbounded" minOccurs="1"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="alternativeID">
        <xs:annotation>
            <xs:documentation xml:lang="de">Identifier aus dem Informationssystem des
                Publikationsagenten, aber auch andere persistenter Identifier.</xs:documentation>
            <xs:documentation xml:lang="en">An identifier other than the primary identifier of the
                registered resource. This may be an identifier from the information system of the
                Publication Agent as well as from other information systems.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="identifier">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="type">
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
            <xs:documentation xml:lang="de">Klassenbezeichnung aus einer disziplinären
                Klassifikation (z.B. Soziologie).</xs:documentation>
            <xs:documentation xml:lang="en">Subject class (e.g. Sociology).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:choice maxOccurs="1" minOccurs="1">
                <xs:element name="classificationInternal">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Klassifikation aus GESIS-Klassifikation,
                            ZA-Klassifikation und JEL (Journal of Economic Literature)
                            Klassifikation.</xs:documentation>
                        <xs:documentation xml:lang="en">Subject class from GESIS-Classification,
                            ZA-Classification and JEL (Journal of Economic Literature)
                            Classification.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:all>
                            <xs:element name="schema">
                                <xs:simpleType>
                                    <xs:restriction base="xs:string">
                                        <xs:enumeration value="GESIS">
                                            <xs:annotation>
                                                <xs:documentation xml:lang="de">Klassifikation
                                                  Sozialwissenschaften</xs:documentation>
                                                <xs:documentation xml:lang="en">GESIS Classification
                                                  Social Sciences</xs:documentation>
                                            </xs:annotation>
                                        </xs:enumeration>
                                        <xs:enumeration value="JEL">
                                            <xs:annotation>
                                                <xs:documentation xml:lang="de">JEL (Journal of
                                                  Economic Literature)
                                                  Klassifikation</xs:documentation>
                                                <xs:documentation xml:lang="en">JEL (Journal of
                                                  Economic Literature)
                                                  Classification</xs:documentation>
                                            </xs:annotation>
                                        </xs:enumeration>
                                        <xs:enumeration value="ZA">
                                            <xs:annotation>
                                                <xs:documentation xml:lang="de">ZA-Klassifikation
                                                  (GESIS Datenbestandskatalog)</xs:documentation>
                                                <xs:documentation xml:lang="en">ZA-Classification
                                                  (GESIS Data Catalogue)</xs:documentation>
                                            </xs:annotation>
                                        </xs:enumeration>
                                    </xs:restriction>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element minOccurs="1" maxOccurs="1" name="identifiers">
                                <xs:complexType>
                                    <xs:sequence maxOccurs="1">
                                        <xs:element name="identifier" maxOccurs="unbounded">
                                            <xs:simpleType>
                                                <xs:restriction base="nonemptycontentStringType"/>
                                            </xs:simpleType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                                <xs:unique name="classificationIdentifier">
                                    <xs:selector xpath="identifier"/>
                                    <xs:field xpath="."/>
                                </xs:unique>
                            </xs:element>
                        </xs:all>
                    </xs:complexType>
                </xs:element>
                <xs:element maxOccurs="1" name="classificationExternal">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Klassifikation des Publikationsagenten (bzw.
                            des Nachweisagenten).</xs:documentation>
                        <xs:documentation xml:lang="en">Subject class from the classification system
                                                    of the Publication Agent (or of the Data Reference
                                                    Agent).</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:all>
                            <xs:element ref="language"/>
                            <xs:element name="schema">
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element minOccurs="1" maxOccurs="1" name="terms">
                                <xs:complexType>
                                    <xs:sequence maxOccurs="1">
                                        <xs:element name="term" maxOccurs="unbounded">
                                            <xs:simpleType>
                                                <xs:restriction base="nonemptycontentStringType"/>
                                            </xs:simpleType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                                <xs:unique name="classificationTerm">
                                    <xs:selector xpath="term"/>
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
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="classification" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <!-- 15. keywords controlled -->
    <xs:element name="controlledKeyword">
        <xs:annotation>
            <xs:documentation xml:lang="de">Schlagwörter aus Thesauri oder kontrollierten
                Schlagwortlisten, die den Inhalt der Ressource näher beschreiben.</xs:documentation>
            <xs:documentation xml:lang="en">Controlled keywords (Thesauri or controlled vocabulary
                lists) that describe the content of the resource in detail.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element name="schema">
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="TheSozWiss">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Thesaurus
                                        Sozialwissenschaften</xs:documentation>
                                    <xs:documentation xml:lang="en">Thesaurus for the Social
                                        Sciences</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="STW">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Standard-Thesaurus
                                        Wirtschaft</xs:documentation>
                                    <xs:documentation xml:lang="en">STW Thesaurus for
                                        Economics</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
                <xs:element minOccurs="1" maxOccurs="1" name="identifiers">
                    <xs:complexType>
                        <xs:sequence maxOccurs="unbounded">
                            <xs:element name="identifier" maxOccurs="unbounded">
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                    <xs:unique name="controlledKeywordIdentifier">
                        <xs:selector xpath="identifier"/>
                        <xs:field xpath="."/>
                    </xs:unique>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="controlledKeywords">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="controlledKeyword" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <!-- 16. keywords free-->
    <xs:element name="freeKeyword">
        <xs:annotation>
            <xs:documentation xml:lang="de">Freie Schlagwörter, die den Inhalt der Ressource näher
                beschreiben.</xs:documentation>
            <xs:documentation xml:lang="en">Free keywords describing the content of the
                resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" maxOccurs="1"/>
                <xs:element name="keywords">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element maxOccurs="unbounded" name="keyword">
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
            <xs:documentation>freeKeywords is a container element for 1 or many freeKeyword</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="freeKeyword" maxOccurs="2" minOccurs="1"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="freeKeywordsLanguage">
            <xs:selector xpath="freeKeyword/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>

    <!-- 17. description -->
    <xs:element name="descriptions">
        <xs:annotation>
            <xs:documentation>descriptions is a container element for 1 or many description</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="description"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="description">
        <xs:annotation>
            <xs:documentation xml:lang="de">Inhaltliche Beschreibung der Ressource. Wenn Sie in
                diesem Freitextfeld einen formatierten Text eingeben möchten, sind zur Verwendung
                folgende HTML Tags zugelassen: für Absätze: <![CDATA[<p>]]> ; für nummerierte
                Listen: <![CDATA[<ol>]]> ; für Aufzählungslisten (unsortierte Liste):
                <![CDATA[<ul>]]> ; für Listeneintrag innerhalb einer Liste: <![CDATA[<li>]]>; für
                logische Auszeichnungen im Text (um einen Text hervorzuheben): <![CDATA[<strong>]]>
                ; für einen Zeilenumbruch: <![CDATA[<br>]]>. Da wir XHTML-Standard-konform arbeiten,
                sind alle Tags zu schließen <![CDATA[<p>Text</p>]]>). </xs:documentation>
            <xs:documentation xml:lang="en">Description of the resource content. For formatting of
                the text the following HTML Tags are allowed: for paragraphs: <![CDATA[<p>]]> ; for
                numbered lists: <![CDATA[<ol>]]> ; for enumeration lists (unordered lists):
                <![CDATA[<ul>]]> ; for a list entry within a list: <![CDATA[<li>]]>; for logical
                markup in the text (to highlight the text): <![CDATA[<strong>]]> ; for line wrap:
                <![CDATA[<br>]]>. According to XHTML-Standard, all tags are to close.
                <![CDATA[<p>Text</p>]]>).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="language"/>
                <xs:element name="freetext" type="richtext"/>
                <xs:element name="type">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Typ der Beschreibung.</xs:documentation>
                        <xs:documentation xml:lang="en">The type of the
                            description.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:enumeration value="1">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Zusammenfassung</xs:documentation>
                                    <xs:documentation xml:lang="en">Abstract</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="2">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Information zur
                                        Schriftenreihe</xs:documentation>
                                    <xs:documentation xml:lang="en">Series
                                        Information</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="3">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Inhaltsverzeichnis</xs:documentation>
                                    <xs:documentation xml:lang="en">Table of
                                        Contents</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="4">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Methoden</xs:documentation>
                                    <xs:documentation xml:lang="en">Methods</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="5">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Sonstiges</xs:documentation>
                                    <xs:documentation xml:lang="en">Other</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 18. geographic coverage controlled/free-->
    <xs:element name="geographicCoverages">
        <xs:annotation>
            <xs:documentation>geographicCoverages is a container element for 1 or many geographicCoverage</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="geographicCoverage"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="geographicCoverage">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="language"/>
                <!-- 18.1 geographic coverage controlled-->
                <xs:element name="geographicCoverageControlled" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Geografische Einheit des jeweiligen
                            Untersuchungsgebiets. ISO 3166 1, 2 und 3 ist ein international anerkannter Standard.</xs:documentation>
                        <xs:documentation xml:lang="en">Spatial region or named place where the data
                            was gathered or about which the data is focused. ISO 3166 (Parts 1, 2
                            and 3) is commonly accepted International Standard.</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <!-- 18.2 geographic coverage free-->
                <xs:element name="freetext" minOccurs="0" type="xs:string">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Geografische Einheit des jeweiligen
                            Untersuchungsgebiets. Möglichkeit, geografische Einheiten frei zu
                            vergeben, wenn im kontrollierten Vokabular diese nicht vorhanden sind;
                            z. B. Westberlin; gleichzeitig Vergabe des kontrollierten
                            Oberbegriffs.</xs:documentation>
                        <xs:documentation xml:lang="en">Geographic units on which the resource
                            focuses. The option to indicate certain units, in case they cannot be
                            found in the controlled vocabulary list.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <!-- 18.3 geographic location point-->
                <xs:element minOccurs="0" name="geoLocationPoint" type="point">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Geographische Koordinaten. Angaben zu Länge
                            und Breite, getrennt durch ein Leerzeichen, z.B. 31.233000 -67.302000.</xs:documentation>
                        <xs:documentation xml:lang="en">A point location in space. A point contains
                            a single latitude-longitude pair, separated by whitespace. e.g.
                            31.233000 -67.302000</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <!-- 18.4 geographic location box-->
                <xs:element minOccurs="0" name="geoLocationBox" type="box">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Geographische Ausdehnung. Eine Box enthält
                            zwei getrennte Paarangaben zu Breite und Länge. Die Paare sind durch ein Leerzeichen getrennt. Die ersten Paarangaben
                            beziehen sich auf die niedrigere Ecke, die zweiten auf die obere Ecke,
                            z. B. 41.090000 -71.032000 42.893000 -68.211000</xs:documentation>
                        <xs:documentation xml:lang="en">The spatial limits of a place. A box
                            contains two white space separated latitude-longitude pairs, with each
                            pair separated by whitespace. The first pair is the lower corner
                            (normally south west), the second is the upper corner (normally north
                            east), e.g. 41.090000 -71.032000 42.893000 -68.211000</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 19. sampled universe -->
    <xs:element name="universes">
        <xs:annotation>
            <xs:documentation>universes is a container element for 1 or 2 universe</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="2" ref="universe"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="sampledLanguage">
            <xs:selector xpath="universe/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
    <xs:element name="universe">
        <xs:annotation>
            <xs:documentation xml:lang="de">Beschreibung der statistischen Einheiten, die der
                Auswahl zugrunde liegen. Wenn Sie in diesem Freitextfeld einen formatierten Text
                eingeben möchten, sind zur Verwendung folgende HTML Tags zugelassen: für Absätze:
                <![CDATA[<p>]]> ; für nummerierte Listen: <![CDATA[<ol>]]> ; für Aufzählungslisten
                (unsortierte Liste): <![CDATA[<ul>]]> ; für Listeneintrag innerhalb einer Liste:
                <![CDATA[<li>]]>; für logische Auszeichnungen im Text (um einen Text hervorzuheben):
                <![CDATA[<strong>]]> ; für einen Zeilenumbruch: <![CDATA[<br>]]>. Da wir
                XHTML-Standard-konform arbeiten, sind alle Tags zu schließen (auch
                <![CDATA[<p>Text</p>]]>). </xs:documentation>
            <xs:documentation xml:lang="en"> Elementary units about which inferences are to be drawn
                and to which analytic results refer. For formatting of the text the following HTML
                Tags are allowed: for paragraphs: <![CDATA[<p>]]> ; for numbered lists:
                <![CDATA[<ol>]]> ; for enumeration lists (unordered lists): <![CDATA[<ul>]]> ; for a
                list entry within a list: <![CDATA[<li>]]>; for logical makeups in the text (to
                highlight the text): <![CDATA[<strong>]]> ; for line wraps: <![CDATA[<br>]]>.
                According to XHTML-Standard, all tags are to close. (also <![CDATA[<p>Text</p>]]>).
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="language"/>
                <xs:element name="sampled" type="richtext"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 20. sampling -->
    <xs:element name="samplings">
        <xs:annotation>
            <xs:documentation>samplings is a container element for 1 or 2 sampling</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="2" ref="sampling"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="samplingLanguage">
            <xs:selector xpath="sampling/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
    <xs:element name="sampling">
        <xs:annotation>
            <xs:documentation xml:lang="de">Die Stichprobentechnik, benutzt für die Auswahl der Umfrageteilnehmer, welche die Bevölkerung repräsentieren.</xs:documentation>
            <xs:documentation xml:lang="en">The type of sample and sample design used to select the
                survey respondents to represent the population.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" maxOccurs="1"/>
                <xs:element maxOccurs="1" name="method" type="richtext">
                    <xs:annotation>
                        <xs:documentation xml:lang="en">For formatting of the text the following
                            HTML Tags are allowed: for paragraphs: <![CDATA[<p>]]> ; for numbered
                            lists: <![CDATA[<ol>]]> ; for enumeration lists (unordered lists):
                            <![CDATA[<ul>]]> ; for a list entry within a list: <![CDATA[<li>]]>; for
                            logical makeups in the text (to highlight the text):
                            <![CDATA[<strong>]]> ; for line wraps: <![CDATA[<br>]]>. According to
                            XHTML-Standard, all tags are to close. (also
                            <![CDATA[<p>Text</p>]]>).</xs:documentation>
                        <xs:documentation xml:lang="de">Wenn Sie in diesem Freitextfeld einen
                            formatierten Text eingeben möchten, sind zur Verwendung folgende HTML
                            Tags zugelassen: für Absätze: <![CDATA[<p>]]> ; für nummerierte Listen:
                            <![CDATA[<ol>]]> ; für Aufzählungslisten (unsortierte Liste):
                            <![CDATA[<ul>]]> ; für Listeneintrag innerhalb einer Liste:
                            <![CDATA[<li>]]>; für logische Auszeichnungen im Text (um einen Text
                            hervorzuheben): <![CDATA[<strong>]]> ; für einen Zeilenumbruch:
                            <![CDATA[<br>]]>. Da wir XHTML-Standard-konform arbeiten, sind alle Tags
                            zu schließen (auch <![CDATA[<p>Text</p>]]>). </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- 21. temporal coverage formal/free->start-end Date -->
    <xs:element name="temporalCoverage">
        <xs:annotation>
            <xs:documentation xml:lang="de">Zeitraum, den die Daten inhaltlich abbilden (bei Umfragen: Feldzeit der Datenerhebung).
                </xs:documentation>
            <xs:documentation xml:lang="en">The time period to which the data refer (in case of surveys the time period of field work).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"/>
                <!-- 21.2 temporal coverage free -->
                <xs:element minOccurs="0" maxOccurs="1" name="temporalCoverageFree" type="xs:string">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Möglichkeit, einen Zeitraum anzugeben, wenn
                            dieser nicht im Kalendermodus angegeben werden kann oder als Ergänzung zu 21.1.</xs:documentation>
                        <xs:documentation xml:lang="en">Provides the possibility to indicate the
                            temporal coverage, if the calendar mode cannot be applied or as a
                            supplement to 21.1.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <!-- 21.1 temporal coverage formal -->
                <xs:element name="temporalCoverageFormal" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Zeitraum, auf den sich die
                            Datenerhebung/Beobachtungen/Aktivitäten bzw. Sammlungen inhaltlich
                            beziehen.</xs:documentation>
                        <xs:documentation xml:lang="en">Temporal coverage refers to a time period
                            during which the data was collected or observations made or to a time
                            period that an activity or collection is linked to intellectually or
                            thematically.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="startDate">
                                <xs:complexType>
                                    <xs:choice>
                                        <xs:element name="date" type="xs:date"> </xs:element>
                                        <xs:element name="monthyear" type="xs:gYearMonth"> </xs:element>
                                        <xs:element name="year" type="xs:gYear"/>
                                    </xs:choice>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="endDate" minOccurs="0">
                                <xs:complexType>
                                    <xs:choice>
                                        <xs:element name="date" type="xs:date"> </xs:element>
                                        <xs:element name="monthyear" type="xs:gYearMonth"> </xs:element>
                                        <xs:element name="year" type="xs:gYear"/>
                                    </xs:choice>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="temporalCoverages">
        <xs:annotation>
            <xs:documentation>temporalCoverages is a container element for 1 or many temporalCoverage</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1">
                <xs:element maxOccurs="unbounded" ref="temporalCoverage"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 22. time dimension controlled/free-->
    <xs:element name="timeDimension">
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"/>
                <xs:element name="timeDimensionControlled" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Zeitliche Ausdehnung der Datenerhebung
                            (da|ra kontrollierte Liste)</xs:documentation>
                        <xs:documentation xml:lang="en">Describes the time dimension of the data
                            collection (da|ra controlled list).</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:enumeration value="1">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Längsschnitt</xs:documentation>
                                    <xs:documentation xml:lang="en">Longitudinal</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="2">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Längsschnitt
                                        Kohorte/Eventbasierte</xs:documentation>
                                    <xs:documentation xml:lang="en">Longitudinal:
                                        CohortEventBased</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="3">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Längsschnitttrend/Wiederholter
                                        Querschnitt</xs:documentation>
                                    <xs:documentation xml:lang="en">Longitudinal:
                                        TrendRepeatedCrossSection</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="4">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Längsschnittpanel</xs:documentation>
                                    <xs:documentation xml:lang="en">Longitudinal:
                                        Panel</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="5">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Kontinuierlicher
                                        Längsschnittpanel</xs:documentation>
                                    <xs:documentation xml:lang="en">Longitudinal:
                                        Panel.Continuous</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="6">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Längsschnitt: Panel:
                                        Intervall</xs:documentation>
                                    <xs:documentation xml:lang="en">Longitudinal: Panel:
                                        Interval</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="7">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Zeitreihe</xs:documentation>
                                    <xs:documentation xml:lang="en">Time Series</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="8">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">kontinuierliche
                                        Zeitreihe</xs:documentation>
                                    <xs:documentation xml:lang="en">Time Series:
                                        Continuous</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="9">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">diskrete
                                        Zeitreihe</xs:documentation>
                                    <xs:documentation xml:lang="en">Time Series:
                                        Discrete</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="10">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Querschnitt</xs:documentation>
                                    <xs:documentation xml:lang="en">Cross-section</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="11">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Querschnitts-Ad-hoc-Follow-up</xs:documentation>
                                    <xs:documentation xml:lang="en">Cross-section ad-hoc
                                        follow-up</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="12">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">andere</xs:documentation>
                                    <xs:documentation xml:lang="en">Other</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
                <xs:element maxOccurs="1" name="timeDimensionFree" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Möglichkeit, die zeitliche Dimension zu
                            beschreiben, wenn in der kontrollierten Liste keine passenden Begriffe
                            gefunden werden.</xs:documentation>
                        <xs:documentation xml:lang="en">Provides the possibility to describe the
                            time dimension if there are no equivalent terms in the controlled
                            vocabulary.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="frequency" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Häufigkeit der
                            Datenerhebung.</xs:documentation>
                        <xs:documentation xml:lang="en">The time frequency at which data is
                            collected at regular intervals.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="timeDimensions">
        <xs:annotation>
            <xs:documentation>timeDimensions is a container element for 1 or many timeDimension</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="timeDimension" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 23. contributor -->
    <xs:element name="contributors">
        <xs:annotation>
            <xs:documentation>contributors is a container element for 1 or many contributor</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" minOccurs="1" ref="contributor"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="contributor">
        <xs:complexType>
            <xs:choice>
                <xs:element name="person">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Name der Person, die für Datensammlung, Management, Vertrieb verantwortlich ist oder die in einer oder anderer
                            Weise zur Entstehung der Resource beigetragen hat.</xs:documentation>
                        <xs:documentation xml:lang="en">The name of the person responsible for
                            collecting, managing, distributing, or otherwise contributing to the
                            development of the resource.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element minOccurs="1" maxOccurs="1" name="firstName">
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element name="middleName" type="xs:string" minOccurs="0"/>
                            <xs:element name="lastName">
                                <xs:simpleType>
                                    <xs:restriction base="nonemptycontentStringType"/>
                                </xs:simpleType>
                            </xs:element>
                            <xs:element ref="contributorType"/>
                            <xs:element minOccurs="0" name="personIDs">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element maxOccurs="unbounded" name="personID">
                                            <xs:complexType>
                                                <xs:group ref="ID"/>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                            <xs:element minOccurs="0" ref="affiliation"/>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element name="institution">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Name der Institution, die für Datensammlung, Management, Vertrieb verantwortlich ist oder die in einer oder
                            anderer Weise zur Entstehung der Resource beigetragen
                            hat.</xs:documentation>
                        <xs:documentation xml:lang="en">The name of the institution responsible for
                            collecting, managing, distributing, or otherwise contributing to the
                            development of the resource.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence maxOccurs="1" minOccurs="1">
                            <xs:element name="institutionName" maxOccurs="2">
                                <xs:complexType>
                                    <xs:all>
                                        <xs:element ref="language"/>
                                        <xs:element minOccurs="1" maxOccurs="1" name="name">
                                            <xs:simpleType>
                                                <xs:restriction base="nonemptycontentStringType"/>
                                            </xs:simpleType>
                                        </xs:element>
                                    </xs:all>
                                </xs:complexType>
                            </xs:element>
                            <xs:element ref="contributorType"/>
                            <xs:element name="institutionIDs" minOccurs="0">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element maxOccurs="unbounded" name="institutionID">
                                            <xs:complexType>
                                                <xs:group ref="ID"/>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                    <xs:unique name="contributorInstitutionLanguage">
                        <xs:selector xpath="institutionName/language"/>
                        <xs:field xpath="."/>
                    </xs:unique>
                </xs:element>
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <xs:element name="contributorType">
        <xs:annotation>
            <xs:documentation xml:lang="de">Typ des Contributors</xs:documentation>
            <xs:documentation xml:lang="en">Contributor Type</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:enumeration value="1">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Kontaktperson</xs:documentation>
                        <xs:documentation xml:lang="en">ContactPerson</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="2">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Datenerhebung</xs:documentation>
                        <xs:documentation xml:lang="en">DataCollector</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="3">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Datenmanager</xs:documentation>
                        <xs:documentation xml:lang="en">DataManager</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="4">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Vertrieb</xs:documentation>
                        <xs:documentation xml:lang="en">Distributor</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="5">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Herausgeber</xs:documentation>
                        <xs:documentation xml:lang="en">Editor</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="6">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Geldgeber</xs:documentation>
                        <xs:documentation xml:lang="en">Funder</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="7">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Anbieter</xs:documentation>
                        <xs:documentation xml:lang="en">HostingInstitution</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="8">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Produzent</xs:documentation>
                        <xs:documentation xml:lang="en">Producer</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="9">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Projektleiter</xs:documentation>
                        <xs:documentation xml:lang="en">ProjectLeader</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="10">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Projektmanager</xs:documentation>
                        <xs:documentation xml:lang="en">ProjectManager</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="11">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Projektmitarbeiter</xs:documentation>
                        <xs:documentation xml:lang="en">ProjectMember</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="12">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Registrierungsagentur</xs:documentation>
                        <xs:documentation xml:lang="en">RegistrationAgency</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="13">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Registrierungsbehörde</xs:documentation>
                        <xs:documentation xml:lang="en">RegistrationAuthority</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="14">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">VerbundenePerson</xs:documentation>
                        <xs:documentation xml:lang="en">RelatedPerson</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="15">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Forscher</xs:documentation>
                        <xs:documentation xml:lang="en">Researcher</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="16">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Forschungsgruppe</xs:documentation>
                        <xs:documentation xml:lang="en">ResearchGroup</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="17">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Rechtsinhaber</xs:documentation>
                        <xs:documentation xml:lang="en">RightsHolder</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="18">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Sponsor</xs:documentation>
                        <xs:documentation xml:lang="en">Sponsor</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="19">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Administrator</xs:documentation>
                        <xs:documentation xml:lang="en">Supervisor</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="20">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Leiter des Arbeitspakets</xs:documentation>
                        <xs:documentation xml:lang="en">WorkPackageLeader</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="21">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Sonstiges</xs:documentation>
                        <xs:documentation xml:lang="en">Other</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>

    <!-- 24. collection mode controlled-->
    <xs:element name="collectionModeControlled">
        <xs:annotation>
            <xs:documentation xml:lang="de">Typ des Erhebungsverfahrens</xs:documentation>
            <xs:documentation xml:lang="en">The method used to collect the data</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:enumeration value="1">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Interview</xs:documentation>
                        <xs:documentation xml:lang="en">Interview</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="2">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Interview: persönliches</xs:documentation>
                        <xs:documentation xml:lang="en">Interview: Face-to-face</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="3">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Interview: Telefon</xs:documentation>
                        <xs:documentation xml:lang="en">Interview: Telephone</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="4">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Interview: E-Mail</xs:documentation>
                        <xs:documentation xml:lang="en">Interview: E-mail</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="5">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Interview: CATI</xs:documentation>
                        <xs:documentation xml:lang="en">Interview: CATI</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="6">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Interview: CAPI</xs:documentation>
                        <xs:documentation xml:lang="en">Interview: CAPI</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="7">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Selbst ausgefüllter
                            Fragebogen</xs:documentation>
                        <xs:documentation xml:lang="en">Self-completed
                            questionnaire</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="8">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Selbst ausgefüllter Fragebogen:
                            Papier/Bleistift</xs:documentation>
                        <xs:documentation xml:lang="en">Self-completed questionnaire:
                            Paper/pencil</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="9">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Selbst ausgefüllter Fragebogen:
                            Web-basiert</xs:documentation>
                        <xs:documentation xml:lang="en">Self-completed questionnaire:
                            Web-based</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="10">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Selbst ausgefüllter Fragebogen:
                            CASI</xs:documentation>
                        <xs:documentation xml:lang="en">Self-completed questionnaire:
                            CASI</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="11">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Selbst ausgefüllter Fragebogen:
                            ACASI</xs:documentation>
                        <xs:documentation xml:lang="en">Self-completed questionnaire:
                            ACASI</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="12">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Verschlüsselung</xs:documentation>
                        <xs:documentation xml:lang="en">Coding</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="13">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Transkription</xs:documentation>
                        <xs:documentation xml:lang="en">Transcription</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="14">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Zusammenstellung</xs:documentation>
                        <xs:documentation xml:lang="en">Compilation</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="15">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Synthese</xs:documentation>
                        <xs:documentation xml:lang="en">Synthesis</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="16">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">(Ton-) Aufnahme</xs:documentation>
                        <xs:documentation xml:lang="en">Recording</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="17">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Simulation</xs:documentation>
                        <xs:documentation xml:lang="en">Simulation</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="18">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Beobachtung</xs:documentation>
                        <xs:documentation xml:lang="en">Observation</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="19">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Beobachtung: Feld</xs:documentation>
                        <xs:documentation xml:lang="en">Observation: Field</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="20">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Beobachtung: Labor</xs:documentation>
                        <xs:documentation xml:lang="en">Observation: Laboratory</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="21">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Beobachtung: Teilnehmer</xs:documentation>
                        <xs:documentation xml:lang="en">Observation: Participant</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="22">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Experimente</xs:documentation>
                        <xs:documentation xml:lang="en">Experiments</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="23">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Fokus-Gruppe</xs:documentation>
                        <xs:documentation xml:lang="en">Focus Group</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="24">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Andere</xs:documentation>
                        <xs:documentation xml:lang="en">Other</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <!-- 25. collection mode free -->
    <xs:element name="collectionModeFree">
        <xs:annotation>
            <xs:documentation xml:lang="de">Möglichkeit, das Erhebungsverfahren zu beschreiben, wenn
                in der kontrollierten Liste keine passenden Begriffe gefunden werden. Wenn Sie in
                diesem Freitextfeld einen formatierten Text eingeben möchten, sind zur Verwendung
                folgende HTML Tags zugelassen: für Absätze: <![CDATA[<p>]]> ; für nummerierte
                Listen: <![CDATA[<ol>]]> ; für Aufzählungslisten (unsortierte Liste):
                <![CDATA[<ul>]]> ; für Listeneintrag innerhalb einer Liste: <![CDATA[<li>]]>; für
                logische Auszeichnungen im Text (um einen Text hervorzuheben): <![CDATA[<strong>]]>
                ; für einen Zeilenumbruch: <![CDATA[<br>]]>. Da wir XHTML-Standard-konform arbeiten,
                sind alle Tags zu schließen (auch <![CDATA[<p>Text</p>]]>). </xs:documentation>
            <xs:documentation xml:lang="en">Possibility to describe the collection mode if there are
                no appropriate terms in the controlled vocabulary. For formatting of the text the
                following HTML Tags are allowed: for paragraphs: <![CDATA[<p>]]> ; for numbered
                lists: <![CDATA[<ol>]]> ; for enumeration lists (unordered lists): <![CDATA[<ul>]]>
                ; for a list entry within a list: <![CDATA[<li>]]>; for logical makeups in the text
                (to highlight the text): <![CDATA[<strong>]]> ; for line wraps: <![CDATA[<br>]]>.
                According to XHTML-Standard, all tags are to close. (also
                <![CDATA[<p>Text</p>]]>).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"/>
                <xs:element minOccurs="1" maxOccurs="1" name="modeFree" type="richtext"/>
            </xs:all>
        </xs:complexType>
    </xs:element>
    <xs:element name="collectionModesFree">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="collectionModeFree" maxOccurs="2" minOccurs="1"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="collectionModeLanguage">
            <xs:selector xpath="collectionModeFree/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>

    <!-- 26. dataset-->
    <xs:element name="dataSet">
        <xs:annotation>
            <xs:documentation xml:lang="de">Gesamtheit aller Daten.</xs:documentation>
            <xs:documentation xml:lang="en">Entirety of all data.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element ref="language"/>
                <xs:choice>
                    <xs:group ref="withUnits"/>
                    <xs:group ref="withoutUnits"/>
                </xs:choice>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="dataSets">
        <xs:annotation>
            <xs:documentation>optional</xs:documentation>
            <xs:documentation>dataSets is a container element for 1 or many dataSet</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="dataSet" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 26.5-26.9 file:technical description of the data -->
    <xs:element name="file">
        <xs:annotation>
            <xs:documentation xml:lang="de">Format des Datensatzes, Größe der Datendatei; Prüfsumme,
                die die Authentizität der Datei belegt; Datei, auf den sich der jeweilige
                Fingerprint bezieht; technisches Verfahren, mit dem der Fingerprint gebildet wurde. </xs:documentation>
            <xs:documentation xml:lang="en">The format of the data file, size information; the
                checksum which confirms the authenticity of the file; the name of the file to which
                the respective fingerprint refers; technical procedure generating data
                fingerprint.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <!--<xs:element name="name" type="xs:string"/>-->
                <xs:element minOccurs="0" maxOccurs="1" name="name">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="format" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="size" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="fingerprint" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="fingerprintMethod" type="xs:string"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="files">
        <xs:annotation>
            <xs:documentation>files is a container element for 1 or many file</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="file" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 27. notes -->
    <xs:element name="notes">
        <xs:annotation>
            <xs:documentation>notes is a container element for 1 or 2 note</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="note" minOccurs="1" maxOccurs="2"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="noteLanguage">
            <xs:selector xpath="note/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
    <xs:element name="note">
        <xs:annotation>
            <xs:documentation xml:lang="de">Hinweise auf weitere relevante Informationen bezogen auf
                die registrierte Ressource.</xs:documentation>
            <xs:documentation xml:lang="en">References to further relevant information on the
                resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" maxOccurs="1"/>
                <xs:element maxOccurs="1" name="text" type="xs:string"/>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- *28/29 availability controlled/free-->
    <xs:element name="availability">
        <xs:annotation>
            <xs:documentation>mandatory</xs:documentation>
            <xs:documentation>availability is a container element for availabilityControlled and 0 or 2 availabilityFree</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="1" ref="availabilityControlled"/>
                <xs:element maxOccurs="2" ref="availabilityFree" minOccurs="0"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="availabilityLanguage">
            <xs:selector xpath="availabilityFree/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
    <xs:element name="availabilityControlled">
        <xs:annotation>
            <xs:documentation xml:lang="de">Verfügbarkeit der Ressource.</xs:documentation>
            <xs:documentation xml:lang="en">Conditions governing the access to the resource.</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:enumeration value="1">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Download</xs:documentation>
                        <xs:documentation xml:lang="en">Download</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="2">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">lieferbar</xs:documentation>
                        <xs:documentation xml:lang="en">Delivery</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="3">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Vor-Ort-Nutzung</xs:documentation>
                        <xs:documentation xml:lang="en">Onsite</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="4">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">nicht verfügbar</xs:documentation>
                        <xs:documentation xml:lang="en">Not Available</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="5">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">unbekannt</xs:documentation>
                        <xs:documentation xml:lang="en">Unknown</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="availabilityFree">
        <xs:annotation>
            <xs:documentation xml:lang="de">Zusätzliche Angaben zur
                Verfügbarkeit.</xs:documentation>
            <xs:documentation xml:lang="en">Additional specification of
                availability.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:all minOccurs="1">
                <xs:element ref="language"/>
                <xs:element name="availabilityText" type="xs:string"/>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- 30.rights -->
    <xs:element name="rights">
        <xs:annotation>
            <xs:documentation>rights is a container element for 1 or 2 right</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="2" ref="right"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="rightLanguage">
            <xs:selector xpath="right/language"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
    <xs:element name="right">
        <xs:annotation>
            <xs:documentation xml:lang="de">Informationen zu den mit der Ressource verknüpften
                Rechten.</xs:documentation>
            <xs:documentation xml:lang="en">Any rights information for the
                resource.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" maxOccurs="1"/>
                <xs:element maxOccurs="1" name="rightsText">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- 31.relation -->
    <xs:element name="relation">
        <xs:annotation>
            <xs:documentation xml:lang="de">Identifier der verwandten Ressource(n).</xs:documentation>
            <xs:documentation xml:lang="en">Identifier of related resources.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="1" name="identifier">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="identifierType">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Typ des weiteren Persistent
                            Identifiers</xs:documentation>
                        <xs:documentation xml:lang="en">The type of the related
                            identifier</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="ARK"/>
                            <xs:enumeration value="DOI"/>
                            <xs:enumeration value="EAN13"/>
                            <xs:enumeration value="EISSN"/>
                            <xs:enumeration value="Handle"/>
                            <xs:enumeration value="ISBN"/>
                            <xs:enumeration value="ISSN"/>
                            <xs:enumeration value="ISTC"/>
                            <xs:enumeration value="LISSN"/>
                            <xs:enumeration value="LSID"/>
                            <xs:enumeration value="PURL"/>
                            <xs:enumeration value="UPC"/>
                            <xs:enumeration value="URL"/>
                            <xs:enumeration value="URN"/>
                            <xs:enumeration value="PMID"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="relationType">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Beschreibung des Verhältnisses zwischen der
                            Ressource registriert, und der verwandten Ressource(n).
                        </xs:documentation>
                        <xs:documentation xml:lang="en">The relationship of the resource being
                            registered and the related resource.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:enumeration value="1">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Wird zitiert von</xs:documentation>
                                    <xs:documentation xml:lang="en">IsCitedBy</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="2">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Zitiert</xs:documentation>
                                    <xs:documentation xml:lang="en">Cites</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="3">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Ist Ergänzung zu</xs:documentation>
                                    <xs:documentation xml:lang="en">IsSupplementTo</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="4">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Wird ergänzt durch</xs:documentation>
                                    <xs:documentation xml:lang="en">IsSupplementedBy</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="5">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Wird fortgesetzt von</xs:documentation>
                                    <xs:documentation xml:lang="en">IsContinuedBy</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="6">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Setzt fort</xs:documentation>
                                    <xs:documentation xml:lang="en">Continues</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="7">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Ist neue Version von</xs:documentation>
                                    <xs:documentation xml:lang="en">IsNewVersionOf</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="8">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Ist vorherige Version von</xs:documentation>
                                    <xs:documentation xml:lang="en">IsPreviousVersionOf</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="9">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Ist Teil von</xs:documentation>
                                    <xs:documentation xml:lang="en">IsPartOf</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="10">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Enthält Teil von</xs:documentation>
                                    <xs:documentation xml:lang="en">HasPart</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="11">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Wird referenziert von</xs:documentation>
                                    <xs:documentation xml:lang="en">IsReferencedBy</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="12">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Verweist auf / Referenziert</xs:documentation>
                                    <xs:documentation xml:lang="en">References</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="13">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Wird dokumentiert von</xs:documentation>
                                    <xs:documentation xml:lang="en">IsDocumentedBy</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="14">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Dokumentiert</xs:documentation>
                                    <xs:documentation xml:lang="en">Documents</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="15">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Erstellt von</xs:documentation>
                                    <xs:documentation xml:lang="en">isCompiledBy</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="16">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">erstellt</xs:documentation>
                                    <xs:documentation xml:lang="en">Compiles</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="17">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Ist Variante von</xs:documentation>
                                    <xs:documentation xml:lang="en">IsVariantFormOf</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="18">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Ist Original von</xs:documentation>
                                    <xs:documentation xml:lang="en">IsOriginalFormOf</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="19">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Hat Metadaten</xs:documentation>
                                    <xs:documentation xml:lang="en">HasMetadata</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="20">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Ist Metadaten für</xs:documentation>
                                    <xs:documentation xml:lang="en">IsMetadataFor</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="21">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Ist identisch zu</xs:documentation>
                                    <xs:documentation xml:lang="en">IsIdenticalTo</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>

                </xs:element>
                <xs:element minOccurs="0" name="relatedMetadataSchema">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element minOccurs="0" name="schemaType">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="schemaURI" type="xs:anyURI" minOccurs="0"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="relations">
        <xs:annotation>
            <xs:documentation>relations is a container element for 1 or many relation</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="relation" minOccurs="1" maxOccurs="unbounded"> </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 32.publications -->
    <xs:element name="publications">
        <xs:annotation>
            <xs:documentation>publications is a container element for 1 or many publication</xs:documentation>
            <xs:documentation xml:lang="de">Wissenschaftliche Veröffentlichungen, die sich
                inhaltlich auf die registrierten Ressource(n) beziehen. </xs:documentation>
            <xs:documentation xml:lang="en">The scientific publication(s) relating to the registered
                resource in terms of content.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence minOccurs="1" maxOccurs="1">
                <xs:element maxOccurs="unbounded" ref="publication"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="publication">
        <xs:complexType>
            <xs:choice maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="1" ref="unstructuredPublication" minOccurs="1"/>
                <xs:element ref="structuredPublication" maxOccurs="1" minOccurs="1"/>
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <!-- 32.1. structured-->
    <xs:element name="structuredPublication">
        <xs:annotation>
            <xs:documentation xml:lang="de">Strukturierte Erfassung wissenschaftlicher
                Veröffentlichungen, die sich inhaltlich auf die registrierte Ressource beziehen. </xs:documentation>
            <xs:documentation xml:lang="en">Structured recording of the scientific publications
                relating to the registered resource in terms of content.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element name="doctype" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Typ der Veröffentlichung</xs:documentation>
                        <xs:documentation xml:lang="en">The type of the publication</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:enumeration value="1">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Arbeitspapier</xs:documentation>
                                    <xs:documentation xml:lang="en">Working Paper</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="2">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Aufsatz</xs:documentation>
                                    <xs:documentation xml:lang="en">Article</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="3">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Bericht</xs:documentation>
                                    <xs:documentation xml:lang="en">Report</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="4">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Buch/Monographie</xs:documentation>
                                    <xs:documentation xml:lang="en">Book/Monograph</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="5">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Handschrift</xs:documentation>
                                    <xs:documentation xml:lang="en">Manuscript</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="6">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Nachschlagewerk</xs:documentation>
                                    <xs:documentation xml:lang="en">Reference book</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="7">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Rezension</xs:documentation>
                                    <xs:documentation xml:lang="en">Review</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="8">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Schriftenreihe</xs:documentation>
                                    <xs:documentation xml:lang="en">Series</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="9">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Zeitschrift</xs:documentation>
                                    <xs:documentation xml:lang="en">Journal</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="10">
                                <xs:annotation>
                                    <xs:documentation xml:lang="de">Zeitung</xs:documentation>
                                    <xs:documentation xml:lang="en">Newspaper</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
                <xs:element ref="authorsEditors" maxOccurs="1"/>
                <xs:element maxOccurs="1" name="title">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="year" type="xs:gYear"/>
                <xs:element minOccurs="0" maxOccurs="1" name="publisher" type="xs:string"/>
                <xs:element minOccurs="0" name="places" type="xs:string">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Erscheinungsort(e) der Publikation;</xs:documentation>
                        <xs:documentation xml:lang="en">Publication place</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element minOccurs="0" maxOccurs="1" name="journal" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="volume" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="issue" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="anthology" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="pages" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="isbn" type="xs:string"/>
                <xs:element ref="ISSNs" minOccurs="0" maxOccurs="1"/>
                <xs:element minOccurs="0" maxOccurs="1" name="sowiportID" type="xs:string"/>
                <xs:element ref="PIDs" minOccurs="0"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="authorsEditors">
        <xs:annotation>
            <xs:documentation>authorsEditors is a container element for 1 or many authorEditor</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="authorEditor"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="authorEditor">
        <xs:annotation>
            <xs:documentation xml:lang="de">Name des Autors oder Herausgebers der
                Publikation.</xs:documentation>
            <xs:documentation xml:lang="en">The name of the author or of the
                editor.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:choice>
                <xs:element ref="author" maxOccurs="1" minOccurs="1"/>
                <xs:element maxOccurs="1" minOccurs="1" ref="editor"/>
            </xs:choice>
        </xs:complexType>
    </xs:element>
    <xs:element name="author">
        <xs:annotation>
            <xs:documentation xml:lang="de">Name, Vorname.</xs:documentation>
            <xs:documentation xml:lang="en">Surname, first name.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element minOccurs="1" maxOccurs="1" name="firstName">
                    <xs:annotation>
                        <xs:documentation/>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="middleName" type="xs:string" minOccurs="0"/>
                <xs:element name="lastName">
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
            <xs:documentation xml:lang="de">Name einer Institution oder Person.</xs:documentation>
            <xs:documentation xml:lang="en">The name of a person or an institution.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element minOccurs="1" maxOccurs="1" name="name">
                    <xs:annotation>
                        <xs:documentation/>
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
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" minOccurs="1" name="ISSN">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Internationale Standardnummer für fortlaufende Sammelwerke </xs:documentation>
                        <xs:documentation xml:lang="en">International Standard Serial Number</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>



    <xs:element name="PID">
        <xs:annotation>
            <xs:documentation xml:lang="de">Weitere Persistent Identifier der
                Veröffentlichung/Publikation.</xs:documentation>
            <xs:documentation xml:lang="en">Further Persistent Identifiers related to the
                publication.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="ID">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element ref="pidType"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PIDs">
        <xs:complexType>
            <xs:sequence maxOccurs="unbounded" minOccurs="1">
                <xs:element ref="PID"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <!-- pid type -->
    <xs:element name="pidType">
        <xs:annotation>
            <xs:documentation xml:lang="de">Typ der weiteren Persistent
                Identifier.</xs:documentation>
            <xs:documentation xml:lang="en">The type of the further Persistent
                Identifier.</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="ARK"/>
                <xs:enumeration value="DOI"/>
                <xs:enumeration value="EAN13"/>
                <xs:enumeration value="EISSN"/>
                <xs:enumeration value="Handle"/>
                <xs:enumeration value="ISBN"/>
                <xs:enumeration value="ISSN"/>
                <xs:enumeration value="ISTC"/>
                <xs:enumeration value="LISSN"/>
                <xs:enumeration value="LSID"/>
                <xs:enumeration value="PURL"/>
                <xs:enumeration value="UPC"/>
                <xs:enumeration value="URL"/>
                <xs:enumeration value="URN"/>
                <xs:enumeration value="PMID"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>

    <!-- 32.2. unstructured-->
    <xs:element name="unstructuredPublication">
        <xs:annotation>
            <xs:documentation xml:lang="de">Unstrukturierte Angaben zu wissenschaftlichen
                Veröffentlichungen, die sich inhaltlich auf die registrierte Ressource beziehen.
                Wenn Sie in diesem Freitextfeld einen formatierten Text eingeben möchten, sind zur
                Verwendung folgende HTML Tags zugelassen: für Absätze: <![CDATA[<p>]]> ; für
                nummerierte Listen: <![CDATA[<ol>]]> ; für Aufzählungslisten (unsortierte Liste):
                <![CDATA[<ul>]]> ; für Listeneintrag innerhalb einer Liste: <![CDATA[<li>]]>; für
                logische Auszeichnungen im Text (um einen Text hervorzuheben): <![CDATA[<strong>]]>
                ; für einen Zeilenumbruch: <![CDATA[<br>]]>. Da wir XHTML-Standard-konform arbeiten,
                sind alle Tags zu schließen (auch <![CDATA[<p>Text</p>]]>). </xs:documentation>
            <xs:documentation xml:lang="en">Unstructured bibliographic information relating to the
                registered resource in terms of content. For formatting of the text the following
                HTML Tags are allowed: for paragraphs: <![CDATA[<p>]]> ; for numbered lists:
                <![CDATA[<ol>]]> ; for enumeration lists (unordered lists): <![CDATA[<ul>]]> ; for a
                list entry within a list: <![CDATA[<li>]]>; for logical makeups in the text (to
                highlight the text): <![CDATA[<strong>]]> ; for line wraps: <![CDATA[<br>]]>.
                According to XHTML-Standard, all tags are to close. (also
                <![CDATA[<p>Text</p>]]>).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="1" name="freetext" type="richtext"/>
                <xs:element ref="PIDs" minOccurs="0"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>




    <!-- *34.resource identifier /current version-->
    <xs:element name="resourceIdentifier">
        <xs:annotation>
            <xs:documentation xml:lang="de">Für dieses Element gibt es drei Möglichkeiten: 1.
                resourceIdentifier und currentVersion sind nicht angegeben, dann werden beide vom
                System generiert und ein neuer Datensatz wird gespeichert. 2. resourceIdentifier
                wird angegeben, aber kein currentVersion, dann wird currentversion vom System
                generiert und ein neuer Datensatz wird gespeichert. 3. resourceIdentifier und
                currentVersion werden angegeben, dann wird geprüft, ob einen Datensatz im System
                existiert und falls ja wird er aktualisiert, falls nein wird ein neuer Datensatz
                angelegt. </xs:documentation>
            <xs:documentation xml:lang="en">There are three options for this element: 1.
                resourceIdentifier and currentVersion are not indicated, in this case both are
                generated by the system and a new dataset is recorded. 2. resourceIdentifier is
                indicated, but not a currentVersion, in this case a currentVersion is generated by
                the system and a new dataset is recorded. 3. resourceIdentifier and currentVersion
                are indicated, in this case the system checks whether the imported dataset already
                exists. If it is, the dataset is updated, if not, a new dataset is recorded.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="identifier">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element minOccurs="0" name="currentVersion">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 38. glplace -->
    <xs:element name="glPlace">
        <xs:annotation>
            <xs:documentation xml:lang="de">Erscheinungsort</xs:documentation>
            <xs:documentation xml:lang="en">Place of publication</xs:documentation>
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
                <xs:element minOccurs="0" ref="resourceTypesFree"/>
                <xs:element ref="resourceIdentifier" minOccurs="0"/>
                <xs:element ref="titles" minOccurs="1" maxOccurs="1"/>
                <xs:element minOccurs="0" ref="otherTitles"/>
                <xs:element minOccurs="0" ref="collectiveTitles"/>
                <xs:element ref="creators" minOccurs="1" maxOccurs="1"/>
                <xs:element ref="dataURLs" minOccurs="1" maxOccurs="1"/>
                <xs:element ref="doiProposal" minOccurs="0" maxOccurs="1"/>
                <xs:element ref="publicationDate" minOccurs="1" maxOccurs="1"/>
                <xs:element minOccurs="0" ref="glPlace"/>
                <xs:element ref="availability"/>
                <xs:element minOccurs="0" ref="rights"/>
                <xs:element ref="resourceLanguage" minOccurs="0" maxOccurs="1"/>
                <xs:element minOccurs="0" ref="alternativeIDs"/>
                <xs:element minOccurs="0" ref="classifications"/>
                <xs:element minOccurs="0" ref="controlledKeywords"/>
                <xs:element minOccurs="0" ref="freeKeywords"/>
                <xs:element minOccurs="0" ref="descriptions"/>
                <xs:element minOccurs="0" ref="geographicCoverages"/>
                <xs:element ref="universes" minOccurs="0"/>
                <xs:element minOccurs="0" ref="samplings"/>
                <xs:element minOccurs="0" ref="temporalCoverages"/>
                <xs:element minOccurs="0" ref="timeDimensions"/>
                <xs:element minOccurs="0" ref="contributors"/>
                <xs:element minOccurs="0" ref="collectionModesFree"/>
                <xs:element minOccurs="0" ref="collectionModeControlled"/>
                <xs:element minOccurs="0" ref="dataSets"/>
                <xs:element minOccurs="0" ref="notes"/>
                <xs:element minOccurs="0" ref="relations"/>
                <xs:element minOccurs="0" ref="publications"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- ID group(identifier/schema/schemaURI) -->
    <xs:group name="ID">
        <xs:sequence>
            <xs:element name="identifier">
                <xs:annotation>
                    <xs:documentation xml:lang="de">Identifier des Creators oder der Affiliation des
                        Creators (Person) oder der internen Klassifikation oder der kontrollierten
                        Schlagwörtern oder des Contributors.</xs:documentation>
                    <xs:documentation xml:lang="en">Identifier of Creators or Affiliation (Person)
                        or of internal Classification or controlled Keywords or of
                        Contributor.</xs:documentation>
                </xs:annotation>
                <xs:simpleType>
                    <xs:restriction base="nonemptycontentStringType"/>
                </xs:simpleType>
            </xs:element>
            <xs:element name="identifierSchema">
                <xs:annotation>
                    <xs:documentation xml:lang="de">Name des verwendeten Vokabulars
                        (Verzeichnisses), aus dem der Identifier (des Creators oder der Affiliation
                        des Creators [Person] oder der internen Klassifikation oder der
                        kontrollierten Schlagwörtern oder des Contributors)
                        stammt.</xs:documentation>
                    <xs:documentation xml:lang="en">The name of the identifier scheme (of Creators
                        or Affiliation [Person] or of internal Classification or controlled Keywords or
                        of Contributor).</xs:documentation>
                </xs:annotation>
                <xs:simpleType>
                    <xs:restriction base="nonemptycontentStringType"/>
                </xs:simpleType>
            </xs:element>
            <xs:element name="schemaURI" type="xs:anyURI">
                <xs:annotation>
                    <xs:documentation xml:lang="de">URI des Normdatensatzes (des Creators oder der
                        Affiliation des Creators [Person] oder der internen Klassifikation oder der
                        kontrollierten Schlagwörtern oder des Contributors).</xs:documentation>
                    <xs:documentation xml:lang="en">The URI of the name identifier scheme (of
                        Creators or Affiliation [Person] or internal Classification or controlled
                        Keywords or of Contributor).</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:group>

    <!-- unitType and NumberOfUnits-->
    <xs:group name="withUnits">
        <xs:sequence>
            <!-- 26.1 type of units-->
            <xs:element name="unitType">
                <xs:annotation>
                    <xs:documentation xml:lang="de">Typ der Einheiten, zu denen die Resource
                        Aussagen trifft. Pflicht, wenn 26.2 ausgefüllt ist.</xs:documentation>
                    <xs:documentation xml:lang="en">Describes the entity being analysed or observed
                        in the resource. Required if 26.2 is used.</xs:documentation>
                </xs:annotation>
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:enumeration value="1">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Individuum</xs:documentation>
                                <xs:documentation xml:lang="en">Individual</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="2">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Organisation</xs:documentation>
                                <xs:documentation xml:lang="en">Organization</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="3">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Familie</xs:documentation>
                                <xs:documentation xml:lang="en">Family</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="4">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Familie, im selben Haushalt</xs:documentation>
                                <xs:documentation xml:lang="en">Family: Household family</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="5">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Haushalt</xs:documentation>
                                <xs:documentation xml:lang="en">Household</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="6">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Wohneinheit</xs:documentation>
                                <xs:documentation xml:lang="en">Housing Unit</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="7">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Ereignis/ Prozess</xs:documentation>
                                <xs:documentation xml:lang="en">Event/Process</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="8">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Geographische Einheit</xs:documentation>
                                <xs:documentation xml:lang="en">Geographic Unit</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="9">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Zeiteinheit</xs:documentation>
                                <xs:documentation xml:lang="en">Time Unit</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="10">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Texteinheit</xs:documentation>
                                <xs:documentation xml:lang="en">Text Unit</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="11">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Gruppe</xs:documentation>
                                <xs:documentation xml:lang="en">Group</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="12">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Objekt</xs:documentation>
                                <xs:documentation xml:lang="en">Object</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                        <xs:enumeration value="13">
                            <xs:annotation>
                                <xs:documentation xml:lang="de">Sonstiges</xs:documentation>
                                <xs:documentation xml:lang="en">Other</xs:documentation>
                            </xs:annotation>
                        </xs:enumeration>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <!-- 26.2 number of units-->
            <xs:element name="numberUnits" type="xs:int">
                <xs:annotation>
                    <xs:documentation xml:lang="de">Anzahl der in der Resource untersuchten oder
                        beobachteten Einheiten. Pflicht, wenn 26.1 ausgefüllt
                        ist.</xs:documentation>
                    <xs:documentation xml:lang="en">The number of units being analysed or observed
                        in the resource. Required if 26.1 is used.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element minOccurs="0" maxOccurs="1" name="numberVariables" type="xs:int"/>
            <xs:element minOccurs="0" maxOccurs="1" name="dataType" type="xs:string"/>
            <xs:element minOccurs="0" ref="files"/>

        </xs:sequence>
    </xs:group>
    <!-- without unitType and NumberOfUnits-->
    <xs:group name="withoutUnits">
        <xs:sequence>

            <xs:element minOccurs="0" maxOccurs="1" name="numberVariables" type="xs:int"/>
            <xs:element minOccurs="0" maxOccurs="1" name="dataType" type="xs:string"/>
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
    <!-- geo loc point -->
    <xs:simpleType name="point">
        <xs:restriction base="listOfDoubles">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <!-- geo loc box -->
    <xs:simpleType name="box">
        <xs:restriction base="listOfDoubles">

            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="listOfDoubles">
        <xs:list itemType="xs:double"/>
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
</xs:schema>
"""

