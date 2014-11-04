# -*- coding: utf-8 -*-


## to avoid reading from file

schema = """<?xml version="1.0" encoding="UTF-8"?>
<!-- da|ra Metadatenschema v2.2.1 - www.da-ra.de -->
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
    <!--  *0. Object Resource Type-->
    <xs:element name="resourceType">
        <xs:annotation>
            <xs:documentation xml:lang="de">Genereller Typ der Ressource:  
                2: Datensatz 
                3: Graue Literatur
           </xs:documentation>
            <xs:documentation xml:lang="en">The general type of a resource:  
                2: Dataset
                3: Grey Literature
            </xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="1"/>
                <xs:maxInclusive value="11"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>

    <!-- *1.title -->
    <xs:element name="titles">
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
            <xs:documentation xml:lang="de">Titel des digitalen Objekts.</xs:documentation>
            <xs:documentation xml:lang="en">Title of the digital object.</xs:documentation>
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
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="otherTitle" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="otherTitle">
        <xs:annotation>
            <xs:documentation xml:lang="de">Zusätzliche Titel.</xs:documentation>
            <xs:documentation xml:lang="en">Further titles.</xs:documentation>
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
                        <xs:documentation xml:lang="de">Typ des zusätzlichen Titels: 
1: Alternativer Titel
2: Übersetzter Titel
3: Untertitel
4: Originaltitel
                        </xs:documentation>
                        <xs:documentation xml:lang="en">The type of other titles:
1: Alternative Title 
2: Translated Title 
3: Subtitle 
4: Original Title
                        </xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:minInclusive value="1"/>
                            <xs:maxInclusive value="4"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- *3.collective title -->
    <xs:element name="collectiveTitles">
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
            <xs:documentation xml:lang="de">Titel einer Schriftenreihe, Working Paper Series usw.</xs:documentation>
            <xs:documentation xml:lang="en">Title of book series,working paper series, etc.</xs:documentation>
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
                        <xs:documentation xml:lang="de">Zählungen, die eine Periodizität zum Ausdruck bringen oder die Titel nummerieren.</xs:documentation>
                        <xs:documentation xml:lang="en">Indication of the source: volume count - journal number - page numbers.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- *4.principal investigators -->
    <xs:element name="principalInvestigators">
        <xs:complexType mixed="false">
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="principalInvestigator"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="principalInvestigator">
        <xs:annotation>
            <xs:documentation xml:lang="de">Name einer Person und/oder einer Institution (Primärforscher).
                </xs:documentation>
            <xs:documentation xml:lang="en">Name(s) of principal investigator(s). May be a corporate/institutional or a personal name.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:choice>
                <xs:element ref="person" maxOccurs="1" minOccurs="1"> </xs:element>
                <xs:element maxOccurs="1" minOccurs="1" ref="institution"> </xs:element>
            </xs:choice>
        </xs:complexType>
    </xs:element>

    <!-- *4.1 person(for data collectors too) -->
    <xs:element name="person">
        <xs:annotation>
            <xs:documentation xml:lang="de">Name einer Person, die die Studie durchgeführt (Primärforscher) oder die die Daten erhoben hat (Datenerhebung).</xs:documentation>
            <xs:documentation xml:lang="en">The name of the principal investigator or the data collector.</xs:documentation>
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
            <xs:documentation xml:lang="de">Zugehörigkeit einer Person, die die Studie durchgeführt (Primärforscher) oder die die Daten erhoben hat (Datenerhebung) zu einer Institution.</xs:documentation>
            <xs:documentation xml:lang="en">The affiliation of the principal investigator or the data collector.</xs:documentation>
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

    <!-- *4.2 institution (for data collectors too) -->
    <xs:element name="institution">
        <xs:annotation>
            <xs:documentation xml:lang="de">Name einer Institution, die die Studie durchgeführt (Primärforscher) oder die die Daten erhoben hat (Datenerhebung).</xs:documentation>
            <xs:documentation xml:lang="en">The institutional name of the principal investigator or of the data collector.</xs:documentation>
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
            <xs:documentation xml:lang="de">Vorschlag einer DOI, wenn vom Publikationsagenten kein automatisch generierter DOI-Name gewünscht wird.</xs:documentation>
            <xs:documentation xml:lang="en">The Publication Agent may suggest a DOI-name, if an automatically generated DOI name is not required.</xs:documentation>
        </xs:annotation>
    </xs:element>
    <!-- *8.url -->
    <xs:element name="dataURLs">
        <xs:annotation>
            <xs:documentation xml:lang="de">URL, zu der DOI aufgelöst wird (Landing Page).Falls mehrere angegeben wird die DOI mit dem ersten Element in der Liste registriert.</xs:documentation>
            <xs:documentation xml:lang="en">Each DOI name has an URL to which it resolves.Where several DOIs are indicated, the first DOI will be registered.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element minOccurs="1" maxOccurs="unbounded" name="dataURL" type="xs:anyURI"/>
            </xs:sequence>
        </xs:complexType>
        <xs:unique name="dataURL">
            <xs:selector xpath="dataURL"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>

    <!-- 11. study language -->
    <xs:element name="studyLanguage">
        <xs:annotation>
            <xs:documentation xml:lang="de">Sprache, in der die Studie beim Publikationsagenten vorliegt.</xs:documentation>
            <xs:documentation xml:lang="en">The language in which the study is available at the Publication Agent.</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:pattern
                    value="bel|bos|cze|dut|eng|est|fin|fre|ger|hrv|hun|ita|lav|lit|nor|pol|rum|rus|slo|slv|spa|srp|swe|ukr"
                />
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <!-- *.metadata language -->
    <xs:element name="language">
        <xs:annotation>
            <xs:documentation xml:lang="de">Sprache der Metadaten einer Studie (Deutsch und/oder Englisch). </xs:documentation>
            <xs:documentation xml:lang="en">The language of the study metadata.</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:pattern value="de|en"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>

    <!-- *12.publication date -->
    <xs:element name="publicationDate">
        <xs:annotation>
            <xs:documentation xml:lang="de">Datum der Veröffentlichung des Datensatzes/Studie beim Publikationsagenten.</xs:documentation>
            <xs:documentation xml:lang="en">The publication date of the study by the Publication Agent.</xs:documentation>
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
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="alternativeID" maxOccurs="unbounded" minOccurs="1"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="alternativeID">
        <xs:annotation>
            <xs:documentation xml:lang="de">Identifier aus dem Informationssystem des Publikationsagenten, aber  auch andere persistenter  Identifier (z.B. Handle aus Dataverse).</xs:documentation>
            <xs:documentation xml:lang="en">An identifier other than the primary identifier of the registered study. This may be an identifier from the information system of the Publication Agent as well as from other information systems.</xs:documentation>
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
            <xs:documentation xml:lang="de">Klassenbezeichnung aus einer disziplinären Klassifikation (z.B. Soziologie).</xs:documentation>
            <xs:documentation xml:lang="en">Subject class (e.g. Sociology).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:choice maxOccurs="1" minOccurs="1">
                <xs:element name="classificationInternal">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Klassifikation aus GESIS-Klassifikation, ZA-Klassifikation und JEL.</xs:documentation>
                        <xs:documentation xml:lang="en">Subject class from GESIS-Classification, ZA-Classification and JEL (Journal of Economic Literature)-Classification.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:all>
                            <xs:element name="schema">
                                <xs:simpleType>
                                    <xs:restriction base="xs:string">
                                        <xs:pattern value="GESIS|JEL|ZA"/>
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
                        <xs:documentation xml:lang="de">Klassifikation des Publikationsagenten (bzw. des Nachweisagenten).</xs:documentation>
                        <xs:documentation xml:lang="en">Subject class (e.g. Sociology) from the classification system of the Publishing Agent.</xs:documentation>
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
            <xs:documentation xml:lang="de">Schlagwörter aus Thesauri oder kontrollierten Schlagwortlisten, die den Inhalt der Studie näher beschreiben. da|ra bietet zur Unterstützung derzeit zwei Thesauri an. Thesauri und Schlagwortlisten der Publikationsagenten werden im Feld Schlagwörter (frei) angegeben.</xs:documentation>
            <xs:documentation xml:lang="en">Controlled keywords (Thesauri or controlled vocabulary lists), that describe the study in detail in terms of content. Support is given in the form of two Thesauri. Keywords of the Publication Agent are to indicate in the field Keywords free.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element name="schema">
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:pattern value="TheSozWiss|STW"/>
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
            <xs:documentation xml:lang="de">Freie Schlagwörter, die den Inhalt der Studie näher beschreiben. Thesauri, die von den Publikationagenten verwendet werden, können in diesem Feld eingetragen werden.</xs:documentation>
            <xs:documentation xml:lang="en">Free keywords that describe the study in detail in terms of content. Keywords of the Publication Agent are to indicate here.</xs:documentation>
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
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="description"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="description">
        <xs:annotation>
            <xs:documentation xml:lang="de">Inhaltliche Beschreibung der Studie.
Wenn Sie in diesem Freitextfeld einen formatierten Text eingeben möchten, sind zur Verwendung folgende HTML Tags zugelassen: 
            für Absätze: <![CDATA[<p>]]> ; für nummerierte Listen: <![CDATA[<ol>]]> ; für Aufzählungslisten (unsortierte Liste): <![CDATA[<ul>]]> ; 
            für Listeneintrag innerhalb einer Liste: <![CDATA[<li>]]>; für logische Auszeichnungen im Text (um einen Text hervorzuheben): <![CDATA[<strong>]]> ; 
            für einen Zeilenumbruch: <![CDATA[<br>]]>. Da wir XHTML-Standard-konform arbeiten, sind alle Tags zu schließen (also <![CDATA[<p>Text</p>]]>).
            </xs:documentation>
            <xs:documentation xml:lang="en">Description of the study content.
For formatting of the text the following HTML Tags are allowed: for paragraphs: <![CDATA[<p>]]> ; for numbered lists: <![CDATA[<ol>]]> ; 
            for enumeration lists (unordered lists): <![CDATA[<ul>]]> ; for a list entry within a list: <![CDATA[<li>]]>; 
            for logical makeup in the text (to highlight the text): <![CDATA[<strong>]]> ; 
            for line wrap: <![CDATA[<br>]]>. According to XHTML-Standard, all tags are to close. (also <![CDATA[<p>Text</p>]]>).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="language"/>
                <xs:element name="freetext" type="richtext"/>
                <xs:element name="type">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Typ der Beschreibung:
1: Zusammenfassung
2: Information zur Schriftenreihe
3: Inhaltsverzeichnis
4: Sonstiges
                        </xs:documentation>
                        <xs:documentation xml:lang="en">The type of the description:
1: Abstract
2: Series Information
3: Table of Contents
4: Other
                        </xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:minInclusive value="1"/>
                            <xs:maxInclusive value="4"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 18. geographic coverage controlled/free-->
    <xs:element name="geographicCoverages">
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="geographicCoverage"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="geographicCoverage">
        <xs:annotation>
            <xs:documentation xml:lang="de">Geografische Einheit, die der Auswahl zugrunde liegt.</xs:documentation>
            <xs:documentation xml:lang="en">Geographic units on which the study focuses.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="language"/>
                <xs:element name="geographicCoverageControlled" minOccurs="0">
                    <xs:simpleType>
                        <xs:restriction base="nonemptycontentStringType"/>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="freetext" minOccurs="0" type="xs:string"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 19. sampled universe -->
    <xs:element name="universes">
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
            <xs:documentation xml:lang="de">Beschreibung der statistischen Einheiten, die der Auswahl zugrunde liegen.
        Wenn Sie in diesem Freitextfeld einen formatierten Text eingeben möchten, sind zur Verwendung folgende HTML Tags zugelassen: 
        für Absätze: <![CDATA[<p>]]> ; für nummerierte Listen: <![CDATA[<ol>]]> ; für Aufzählungslisten (unsortierte Liste): <![CDATA[<ul>]]> ; 
        für Listeneintrag innerhalb einer Liste: <![CDATA[<li>]]>; für logische Auszeichnungen im Text (um einen Text hervorzuheben): <![CDATA[<strong>]]> ; 
        für einen Zeilenumbruch: <![CDATA[<br>]]>. Da wir XHTML-Standard-konform arbeiten, sind alle Tags zu schließen (also <![CDATA[<p>Text</p>]]>).
        </xs:documentation>
            <xs:documentation xml:lang="en"> Elements that are the object of the study and to which any analytic results refer.
 For formatting of the text the following HTML Tags are allowed: for paragraphs: <![CDATA[<p>]]> ; for numbered lists: <![CDATA[<ol>]]> ; 
        for enumeration lists (unordered lists): <![CDATA[<ul>]]> ; for a list entry within a list: <![CDATA[<li>]]>; 
        for logical makeups in the text (to highlight the text): <![CDATA[<strong>]]> ; for line wraps: <![CDATA[<br>]]>. 
        According to XHTML-Standard, all tags are to close. (also <![CDATA[<p>Text</p>]]>). </xs:documentation>
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
            <xs:documentation xml:lang="de">Benutztes Auswahlverfahren.</xs:documentation>
            <xs:documentation xml:lang="en">The type of sample and sample design used to select the survey respondents to represent the population.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" maxOccurs="1"/>
                <xs:element maxOccurs="1" name="method" type="richtext">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Wenn Sie in diesem Freitextfeld einen formatierten Text eingeben möchten, sind zur Verwendung folgende HTML Tags zugelassen: 
                            für Absätze: <![CDATA[<p>]]> ; für nummerierte Listen: <![CDATA[<ol>]]> ; für Aufzählungslisten (unsortierte Liste): <![CDATA[<ul>]]> ; 
                            für Listeneintrag innerhalb einer Liste: <![CDATA[<li>]]>; für logische Auszeichnungen im Text (um einen Text hervorzuheben): <![CDATA[<strong>]]> ;
                            für einen Zeilenumbruch: <![CDATA[<br>]]>. Da wir XHTML-Standard-konform arbeiten, sind alle Tags zu schließen (also <![CDATA[<p>Text</p>]]>).
                           </xs:documentation>
                        <xs:documentation xml:lang="en">For formatting of the text the following HTML Tags are allowed: for paragraphs: <![CDATA[<p>]]> ; 
                            for numbered lists: <![CDATA[<ol>]]> ; for enumeration lists (unordered lists): <![CDATA[<ul>]]> ; 
                            for a list entry within a list: <![CDATA[<li>]]>; for logical makeups in the text (to highlight the text): <![CDATA[<strong>]]> ; 
                            for line wraps: <![CDATA[<br>]]>. According to XHTML-Standard, all tags are to close. (also <![CDATA[<p>Text</p>]]>).</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- 21. temporal coverage formal/free->start-end Date) -->
    <xs:element name="temporalCoverage">
        <xs:annotation>
            <xs:documentation xml:lang="de">Zeitraum, den die Daten inhaltlich abbilden (bei Umfragen: Feldzeit der Datenerhebung). 
                </xs:documentation>
            <xs:documentation xml:lang="en">The time period to which the data refer (in case of surveys the time period of field work).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"/>
                <xs:element minOccurs="0" maxOccurs="1" name="temporalCoverageFree" type="xs:string"
                    > </xs:element>
                <xs:element name="temporalCoverageFormal" minOccurs="0" maxOccurs="1">
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
                        <xs:documentation xml:lang="de">Zeitliche Ausdehnung der Datenerhebung:
1: Längsschnitt
2: Längsschnitt Kohorte/Eventbasierte
3: Längsschnitttrend/Wiederholter Querschnitt
4: Längsschnittpanel
5: Kontinuierlicher Längsschnittpanel
6: Längsschnitt: Panel: Intervall
7: Zeitreihe
8: kontinuierliche Zeitreihe
9: diskrete Zeitreihe
10: Querschnitt
11: Querschnitts-Ad-hoc-Follow-up
12: andere                        </xs:documentation>
                        <xs:documentation xml:lang="en"> Describes the time dimension of the data collection: 
1: Longitudinal
2: Longitudinal: CohortEventBased
3: Longitudinal: TrendRepeatedCrossSection 
4: Longitudinal: Panel 
5: Longitudinal: Panel.Continuous 
6: Longitudinal: Panel: Interval 
7: Time Series 
8: Time Series: Continuous 
9: Time Series: Discrete 
10: Cross-section 
11: Cross-section ad-hoc follow-up 
12: Other                         </xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:minInclusive value="1"/>
                            <xs:maxInclusive value="12"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
                <xs:element maxOccurs="1" name="timeDimensionFree" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Möglichkeit, die zeitliche Dimension zu beschreiben, wenn in der kontrollierten Liste keine passenden Begriffe gefunden werden.
</xs:documentation>
                        <xs:documentation xml:lang="en">Provides the possibility to indicate the temporal coverage, if the calendar mode cannot be applied.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="frequency" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Häufigkeit der Datenerhebung.</xs:documentation>
                        <xs:documentation xml:lang="en">The time frequency at which data is collected at regular intervals.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="timeDimensions">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="timeDimension" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 23. data collector -->
    <xs:element name="dataCollectors">
        <xs:complexType>
            <xs:sequence>
                <xs:element maxOccurs="unbounded" minOccurs="1" ref="dataCollector"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="dataCollector">
        <xs:complexType>
            <xs:choice>
                <xs:element ref="person">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Name der Person, die die Daten erhoben hat.</xs:documentation>
                        <xs:documentation xml:lang="en">The name of a person responsible for data collection.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="institution">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Name der Institution, die die Daten erhoben hat</xs:documentation>
                        <xs:documentation xml:lang="en">The name of an institution responsible for data collection.</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:choice>
        </xs:complexType>
    </xs:element>


    <!-- 24. collection mode controlled-->
    <xs:element name="collectionModeControlled">
        <xs:annotation>
            <xs:documentation xml:lang="de">Typ des Erhebungsverfahrens:
1: Interview)
2: Interview: persönliches
3: Interview: Telefon
4: Interview: E-Mail
5: Interview: CATI
6: Interview: CAPI
7: Selbst ausgefüllter Fragebogen
8: Selbst ausgefüllter Fragebogen: Papier/Bleistift
9: Selbst ausgefüllter Fragebogen: Web-basiert
10: Selbst ausgefüllter Fragebogen: CASI
11: Selbst ausgefüllter Fragebogen: ACASI
12: Verschlüsselun
13: Transkription
14: Zusammenstellung
15: Synthese
16: (Ton-) Aufnahme
17: Simulation 
18: Beobachtung
19: Beobachtung: Feld
20: Beobachtung: Labor
21: Beobachtung: Teilnehmer
22: Experimente
23: Fokus-Gruppe
24: Andere            </xs:documentation>
            <xs:documentation xml:lang="en">The method used to collect data:
1: Interview 
2: Interview: Face-to-face 
3: Interview: Telephone
4: Interview: E-mail 
5: Interview: CATI 
6: Interview: CAPI
7: Self-completed questionnaire 
8: Self-completed questionnaire: Paper/pencil 
9: Self-completed questionnaire: Web-based 
10: Self-completed questionnaire: CASI 
11: Self-completed questionnaire: ACASI 
12: Coding
13: Transcription 
14: Compilation 
15: Synthesis
16: Recording
17: Simulation
18: Observation 
19: Observation: Field 
20: Observation: Laboratory 
21: Observation: Participant
22: Experiments 
23: Focus Group
24: Other          </xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="1"/>
                <xs:maxInclusive value="24"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <!-- 25. collection mode free -->
    <xs:element name="collectionModeFree">
        <xs:annotation>
            <xs:documentation xml:lang="de">Möglichkeit, das Erhebungsverfahren zu beschreiben, wenn in der kontrollierten Liste keine passenden Begriffe gefunden werden.
                    
        Wenn Sie in diesem Freitextfeld einen formatierten Text eingeben möchten, sind zur Verwendung folgende HTML Tags zugelassen: 
        für Absätze: <![CDATA[<p>]]> ; für nummerierte Listen: <![CDATA[<ol>]]> ; für Aufzählungslisten (unsortierte Liste): <![CDATA[<ul>]]> ; 
        für Listeneintrag innerhalb einer Liste: <![CDATA[<li>]]>; für logische Auszeichnungen im Text (um einen Text hervorzuheben): <![CDATA[<strong>]]> ; 
        für einen Zeilenumbruch: <![CDATA[<br>]]>. Da wir XHTML-Standard-konform arbeiten, sind alle Tags zu schließen (also <![CDATA[<p>Text</p>]]>).
       </xs:documentation>
            <xs:documentation xml:lang="en">Provides the possibility to describe the collection mode if there are no appropriate terms in controlled vocabulary. 
 For formatting of the text the following HTML Tags are allowed: for paragraphs: <![CDATA[<p>]]> ; 
        for numbered lists: <![CDATA[<ol>]]> ; for enumeration lists (unordered lists): <![CDATA[<ul>]]> ; 
        for a list entry within a list: <![CDATA[<li>]]>; for logical makeups in the text (to highlight the text): <![CDATA[<strong>]]> ; 
        for line wraps: <![CDATA[<br>]]>. According to XHTML-Standard, all tags are to close. (also <![CDATA[<p>Text</p>]]>).</xs:documentation>
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
            <xs:documentation xml:lang="de">Gesamtheit aller Daten.
			</xs:documentation>
            <xs:documentation xml:lang="en">Entirety of all data.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element ref="language"/>
                <xs:element name="unitType" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Typ der Einheiten, zu denen der/die  Datensatz/Studie Aussagen trifft; 
                            The type of units of analyses or observation that the study describes.
1: Individual (Individuum)
2: Organization (Organisation)
3: Family (Familie)
4: Family: Household family (Familie, im selben Haushalt)
5: Household (Haushalt)
6: Housing Unit (Wohneinheit)
7: Event/Process (Ereignis/ Prozess)
8: Geographic Unit (Geographische Einheit)
9: Time Unit (Zeiteinheit)
10: Text Unit (Texteinheit)
11: Group (Gruppe)
12: Object (Objekt)
13: Other (Sonstiges)                     </xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:minInclusive value="1"/>
                            <xs:maxInclusive value="13"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
                <xs:element maxOccurs="1" name="numberUnits" type="xs:int"/>
                <xs:element minOccurs="0" maxOccurs="1" name="numberVariables" type="xs:int"/>
                <xs:element minOccurs="0" maxOccurs="1" name="dataType" type="xs:string"/>
                <xs:element minOccurs="0" ref="files"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="dataSets">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="dataSet" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 27. file:technical description of the data -->
    <xs:element name="file">
        <xs:annotation>
            <xs:documentation xml:lang="de">Technische Beschreibung der Daten: Format des Datensatzes, Größe des beschriebenen Objekts; Prüfsumme, die die Authentizität der Datei belegt; Datei, auf den sich der jeweilige Fingerprint bezieht; technisches Verfahren, mit dem der Fingerprint  gebildet wurde.
			</xs:documentation>
            <xs:documentation xml:lang="en">Technical description of the data: format of the data file, size information; the checksum which confirms the authenticity of the file; the name of the file to which the respective fingerprint refers ; technical procedure generating data fingerprint.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element name="name" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="format" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="size" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="fingerprint" type="xs:string"/>
                <xs:element minOccurs="0" maxOccurs="1" name="fingerprintMethod" type="xs:string"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="files">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="file" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 28. notes -->
    <xs:element name="notes">
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
            <xs:documentation xml:lang="de">Hinweise auf weitere relevante Informationen.</xs:documentation>
            <xs:documentation xml:lang="en">References to further relevant information on a study.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" maxOccurs="1"/>
                <xs:element maxOccurs="1" name="text" type="xs:string"/>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- *29/30 availability controlled/free-->
    <xs:element name="availability">
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
            <xs:documentation xml:lang="de">Möglichkeiten/Bedingungen des Datenzugangs.
1: Download
2: lieferbar
3: Vor-Ort-Nutzung
4: nicht verfügbar
5: unbekannt</xs:documentation>
            <xs:documentation xml:lang="en">Conditions governing the access to primary data.
1: Download 
2: Delivery 
3: Onsite
4: Not Available
5: Unknown</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="1"/>
                <xs:maxInclusive value="5"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
    <xs:element name="availabilityFree">
        <xs:annotation>
            <xs:documentation xml:lang="de">Zusätzliche Angaben zur Verfügbarkeit.</xs:documentation>
            <xs:documentation xml:lang="en">Additional specification of data availability.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:all minOccurs="1">
                <xs:element ref="language"/>
                <xs:element name="availabilityText" type="xs:string"/>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- 31.rights -->
    <xs:element name="rights">
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
            <xs:documentation xml:lang="de">Informationen zu den mit der Ressource verknüpften Rechten.</xs:documentation>
            <xs:documentation xml:lang="en">Any rights information on the study.</xs:documentation>
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

    <!-- 32.relation -->
    <xs:element name="relation">
        <xs:annotation>
            <xs:documentation xml:lang="de">Persistent Identifier der verwandten Resoourcen.</xs:documentation>
            <xs:documentation xml:lang="en">Persistent Identifiers of related resources.</xs:documentation>
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
                        <xs:documentation xml:lang="de">Typ der weiteren Persistent Identifier</xs:documentation>
                        <xs:documentation xml:lang="en">The type of the related identifiers</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:pattern
                                value="ARK|DOI|EAN13|EISSN|Handle|ISBN|ISSN|ISTC|LISSN|LSID|PURL|UPC|URL|URN"
                            />
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="relationType">
                    <xs:annotation>
                        <xs:documentation xml:lang="de">Beziehung der Studie zu verwandten Ressourcen:
1: Wird zitiert von
2: Zitiert
3: Ist Ergänzung zu
4: Wird ergänzt durch
5: Wird fortgesetzt von
6: Setzt fort
7: Ist neue Version von
8: Ist vorherige Version von
9: Ist Teil von
10: Enthält Teil von
11: Wird referenziert von
12: Verweist auf / Referenziert
13: Wird dokumentiert von
14: Dokumentiert
15: Erstellt von
16: erstellt
17: Ist Variante von
18: Ist Original von</xs:documentation>
                        <xs:documentation xml:lang="en">The relation of the study to the related resources:
1: IsCitedBy 
2: Cites 
3: IsSupplementTo 
4: IsSupplementedBy 
5: IsContinuedBy 
6: Continues
7: IsNewVersionOf 
8: IsPreviousVersionOf 
9: IsPartOf
10: HasPart 
11: IsReferencedBy
12: References 
13: IsDocumentedBy
14: Documents 
15: isCompiledBy
16: Compiles
17: IsVariantFormOf
18: IsOriginalFormOf </xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:minInclusive value="1"/>
                            <xs:maxInclusive value="18"/>
                        </xs:restriction>
                    </xs:simpleType>

                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="relations">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="relation" minOccurs="1" maxOccurs="unbounded"> </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <!-- 33.publications -->
    <xs:element name="publications">
        <xs:annotation>
            <xs:documentation xml:lang="de">Wissenschaftliche Veröffentlichungen, die sich inhaltlich auf den registrierten Datensatz beziehen.
               </xs:documentation>
            <xs:documentation xml:lang="en">The scientific publications relating to the registered study in terms of content.</xs:documentation>
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
    <!-- 33.1. structured-->
    <xs:element name="structuredPublication">
        <xs:annotation>
            <xs:documentation xml:lang="de">Strukturierte wissenschaftliche Veröffentlichungen, die sich inhaltlich auf die registrierte Studie beziehen.
                </xs:documentation>
            <xs:documentation xml:lang="en">Structured recording of the scientific publications relating to the registered study in terms of content.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element name="doctype" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Typ der Veröffentlichung
						    1: Working Paper (Arbeitspapier)
                            2: Article (Aufsatz)
                            3: Report (Bericht)
                            4: Book/Monograph (Buch/Monographie)
                            5: Manuscript (Handschrift)
                            6: Reference book (Nachschlagewerk)
                            7: Review (Rezension)
                            8: Series (Schriftenreihe)
                            9: Journal (Zeitschrift)
                            10: Magazine (Zeitung)
                        </xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:minInclusive value="1"/>
                            <xs:maxInclusive value="10"/>
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
                        <xs:documentation>Erscheinungsort(e) der Publikation; Publication place</xs:documentation>
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
            <xs:documentation/>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:sequence>
                <xs:element maxOccurs="unbounded" ref="authorEditor"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="authorEditor">
        <xs:annotation>
            <xs:documentation xml:lang="de">Name eines Autors oder Herausgebers für eine Publikation.</xs:documentation>
            <xs:documentation xml:lang="en">The name of an author or of an editor.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:choice>
                <xs:element ref="author" maxOccurs="1" minOccurs="1"> </xs:element>
                <xs:element maxOccurs="1" minOccurs="1" ref="editor"> </xs:element>
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
                        <xs:documentation>International Standard Serial Number</xs:documentation>
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
            <xs:documentation xml:lang="de">Weitere Persistent Identifier der Veröffentlichung/Publikation.</xs:documentation>
            <xs:documentation xml:lang="en">Further Persistent Identifiers related to the publication.</xs:documentation>
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
            <xs:documentation xml:lang="de">Typ der weiteren Persistent Identifier.</xs:documentation>
            <xs:documentation xml:lang="en">The type of a further Persistent Identifier.</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:pattern
                    value="ARK|DOI|EAN13|EISSN|Handle|ISBN|ISSN|ISTC|LISSN|LSID|PURL|UPC|URL|URN"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>

    <!-- 33.2. unstructured-->
    <xs:element name="unstructuredPublication">
        <xs:annotation>
            <xs:documentation xml:lang="de">Unstrukturierte Angaben zu  wissenschaftlichen Veröffentlichungen, die sich inhaltlich auf die registrierte Studie beziehen.
                  
        Wenn Sie in diesem Freitextfeld einen formatierten Text eingeben möchten, sind zur Verwendung folgende HTML Tags zugelassen: 
        für Absätze: <![CDATA[<p>]]> ; für nummerierte Listen: <![CDATA[<ol>]]> ; für Aufzählungslisten (unsortierte Liste): <![CDATA[<ul>]]> ; 
        für Listeneintrag innerhalb einer Liste: <![CDATA[<li>]]>; für logische Auszeichnungen im Text (um einen Text hervorzuheben): <![CDATA[<strong>]]> ; 
        für einen Zeilenumbruch: <![CDATA[<br>]]>. Da wir XHTML-Standard-konform arbeiten, sind alle Tags zu schließen (also <![CDATA[<p>Text</p>]]>).
       </xs:documentation>
            <xs:documentation xml:lang="en">Unstructured recording of publications relating to the registered study in terms of content.
 For formatting of the text the following HTML Tags are allowed: for paragraphs: <![CDATA[<p>]]> ; 
        for numbered lists: <![CDATA[<ol>]]> ; for enumeration lists (unordered lists): <![CDATA[<ul>]]> ; 
        for a list entry within a list: <![CDATA[<li>]]>; for logical makeups in the text (to highlight the text): <![CDATA[<strong>]]> ; 
        for line wraps: <![CDATA[<br>]]>. According to XHTML-Standard, all tags are to close. (also <![CDATA[<p>Text</p>]]>).</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence maxOccurs="1" minOccurs="1">
                <xs:element maxOccurs="1" name="freetext" type="richtext"/>
                <xs:element ref="PIDs" minOccurs="0"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>




    <!-- *34.study identifier /current version-->
    <xs:element name="studyIdentifier">
        <xs:annotation>
            <xs:documentation xml:lang="de">Für dieses Element gibt es drei Möglichkeiten:
1. studyIdentifier und currentVersion sind nicht angegeben, dann werden beide vom System generiert und ein neuer Datensatz wird gespeichert.
2. studyIdentifier wird angegeben, aber kein currentVersion, dann wird currentversion vom System generiert und ein neuer Datensatz wird gespeichert.
3. studyIdentifier und currentVersion werden angegeben, dann wird geprüft, ob einen Datensatz im System existiert und falls ja wird er aktualisiert, falls nein wird ein neuer Datensatz angelegt.
            </xs:documentation>
            <xs:documentation xml:lang="en">There are three options for this element:
1. studyIdentifier and currentVersion are not indicated, in this case both are generated by the system and a new dataset is recorded.
2. studyIdentifier is indicated, but not a currentVersion, in this case a currentVersion is generated by the system and a new dataset is recorded.
3. studyIdentifier and currentVersion are indicated, in this case the system checks whether the imported dataset already exists. If it is, the dataset is updated, if not, a new dataset is recorded.   
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

    <!-- 38. gleditor -->
    <xs:element name="glEditors">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="glEditor" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="glEditor">
        <xs:annotation>
            <xs:documentation xml:lang="de">Name des Herausgebers (Institution oder Person).</xs:documentation>
            <xs:documentation xml:lang="en">The name of a person or an institution.</xs:documentation>
        </xs:annotation>
        <xs:complexType mixed="false">
            <xs:all maxOccurs="1" minOccurs="1">
                <xs:element ref="language" minOccurs="1" maxOccurs="1"/>
                <xs:element name="name" minOccurs="1" maxOccurs="1">
                    <xs:complexType>
                        <xs:simpleContent>
                            <xs:extension base="xs:string"/>
                        </xs:simpleContent>
                    </xs:complexType>
                </xs:element>
            </xs:all>
        </xs:complexType>
    </xs:element>

    <!-- 39. glplace -->

    <!-- study -->
    <xs:element name="glPlace">
        <xs:annotation>
            <xs:documentation xml:lang="de">Erscheinungsort Grauer Literatur.</xs:documentation>
            <xs:documentation xml:lang="en">Publication place of grey literature.</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string"/>
        </xs:simpleType>
    </xs:element>
    <xs:element name="study">
        <xs:complexType>
            <xs:sequence minOccurs="1">
                <xs:element ref="resourceType"/>
                <xs:element ref="studyIdentifier" minOccurs="0"/>
                <xs:element ref="titles" minOccurs="1" maxOccurs="1"/>
                <xs:element minOccurs="0" ref="otherTitles"/>
                <xs:element minOccurs="0" ref="collectiveTitles"/>
                <xs:element ref="principalInvestigators" minOccurs="1" maxOccurs="1"/>
                <xs:element ref="dataURLs" minOccurs="1" maxOccurs="1"/>
                <xs:element ref="doiProposal" minOccurs="0" maxOccurs="1"/>
                <xs:element ref="publicationDate" minOccurs="1" maxOccurs="1"/>
                <xs:element minOccurs="0" ref="glEditors"/>
                <xs:element minOccurs="0" ref="glPlace"/>
                <xs:element ref="availability"/>
                <xs:element minOccurs="0" ref="rights"/>
                <xs:element ref="studyLanguage" minOccurs="0" maxOccurs="1"/>
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
                <xs:element minOccurs="0" ref="dataCollectors"/>
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
                <xs:simpleType>
                    <xs:restriction base="nonemptycontentStringType"/>
                </xs:simpleType>
            </xs:element>
            <xs:element name="identifierSchema">
                <xs:simpleType>
                    <xs:restriction base="nonemptycontentStringType"/>
                </xs:simpleType>
            </xs:element>
            <xs:element name="schemaURI" type="xs:anyURI"/>
        </xs:sequence>
    </xs:group>

    <!-- defines value for mandatory fields -->
    <xs:simpleType name="nonemptycontentStringType">
        <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
        </xs:restriction>
    </xs:simpleType>

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

