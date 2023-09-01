DS_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<resource xsi:schemaLocation="http://da-ra.de/schema/kernel-4 http://www.da-ra.de/fileadmin/media/da-ra.de/Technik/4.0/dara.xsd"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://da-ra.de/schema/kernel-4">

    <!-- this is a Collection -->
    <resourceType>Dataset</resourceType> 
    <resourceIdentifier>
        <identifier>e1e62daa-f9b5-494b-842c-d425031f24e7</identifier>
        <currentVersion>1</currentVersion>
    </resourceIdentifier> 

    <titles>
        <title>
            <titleName>Averaging Across Asset Allocation Models (replication data)</titleName>
            <language>en</language>
        </title>
    </titles>  

    <creators>  
        <creator> 
            <person>
                <firstName>Peter</firstName>
                <lastName>Schanbacher</lastName>
                <affiliation>
                    <affiliationName>
                        University of Konstanz
                    </affiliationName>
                </affiliation>
            </person>
        </creator>

    </creators>


    <dataURLs>
        <dataURL>http://edawax.de/dataset/averaging-across-asset-allocation-models</dataURL>
    </dataURLs>
    <doiProposal>10.15456/jbnst.2015176.153001</doiProposal>


    <publicationDate>
        <year>2015</year>
    </publicationDate>


    <availability>
        <availabilityType>Download</availabilityType>
    </availability>

    <resourceLanguage>eng</resourceLanguage>

    <descriptions>
        <description>
            <language>en</language> 
            <freetext>Combination of asset allocation models is rewarding if 

                (i) the applied risk function is concave and    
                (ii) there is no dominating model.   

                We show that most common risk functions are either concave or at least concave in common applications. In a comprehensive empirical study using standard asset allocation models we find that there is no constantly dominating model. The ranking of the models depends on the data set, the risk function and even changes over time. We find that a simple average of all asset allocation models can outperform each individual model. Our contribution is twofold. We present a theory why the combined model is expected to dominate most individual models. In a comprehensive empirical study we show that model combinations perform exceptionally well in asset allocation.</freetext>
                <descriptionType>Abstract</descriptionType>
            </description>
        </descriptions>


        <relations>

            <relation>
                <identifier>http://edawax.de:5000/dataset/e1e62daa-f9b5-494b-842c-d425031f24e7/resource/b2aec61a-b19e-487d-b94d-7c5eb976746b/download/dow.txt</identifier>
                <identifierType>URL</identifierType>
                <relationType>HasPart</relationType>
            </relation>

            <relation>
                <identifier>http://edawax.de:5000/dataset/e1e62daa-f9b5-494b-842c-d425031f24e7/resource/b3af3a83-328d-427d-8375-5b8de2341223/download/pension.txt</identifier>
                <identifierType>URL</identifierType>
                <relationType>HasPart</relationType>
            </relation>


            <relation>
                <identifier>http://edawax.de:5000/dataset/e1e62daa-f9b5-494b-842c-d425031f24e7/resource/2a8ce339-c0ee-40c2-a7da-85d4fdaac7b5/download/world.txt</identifier>
                <identifierType>URL</identifierType>
                <relationType>HasPart</relationType>
            </relation>

            <relation>
                <identifier>http://edawax.de:5000/dataset/e1e62daa-f9b5-494b-842c-d425031f24e7/resource/8c1642b4-715c-4f97-948d-26d7d59a688c/download/readme.pdf</identifier>
                <identifierType>URL</identifierType>
                <relationType>HasPart</relationType>
            </relation>

        </relations>
    </resource>

'''


RES_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<resource xsi:schemaLocation="http://da-ra.de/schema/kernel-4 http://www.da-ra.de/fileadmin/media/da-ra.de/Technik/4.0/dara.xsd"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://da-ra.de/schema/kernel-4">

<!-- this is a Dataset (file) -->
<resourceType>Dataset</resourceType> 
<resourceIdentifier>
    <identifier>b2aec61a-b19e-487d-b94d-7c5eb976746b</identifier>
    <currentVersion>1</currentVersion>
</resourceIdentifier> 

<titles>
    <title>
      <titleName>Dow Jones</titleName>
       <language>en</language>
    </title>
</titles>  

<creators>  
    <creator> 
    <person>
        <firstName>Peter</firstName>
        <lastName>Schanbacher</lastName>
        
        
        <affiliation>
            <affiliationName>
                University of Konstanz
            </affiliationName>
        </affiliation>
    </person>
</creator>

</creators>


<dataURLs>
    <dataURL>http://edawax.de:5000/dataset/e1e62daa-f9b5-494b-842c-d425031f24e7/resource/b2aec61a-b19e-487d-b94d-7c5eb976746b/download/dow.txt</dataURL>
</dataURLs>
<doiProposal>10.15456/jbnst.2015176.173551R</doiProposal>


<publicationDate>
    <year>2015</year>
</publicationDate>


<availability>
    <availabilityType>Download</availabilityType>
</availability>

<descriptions>
    <description>
        <language>en</language> 
        <freetext>Investments in the Dow Jones Industrial firms</freetext>
        <descriptionType>Abstract</descriptionType> 
    </description>
</descriptions>

<geographicCoverages>
    <geographicCoverage>
        <geographicCoverageControlled>AF</geographicCoverageControlled>
    </geographicCoverage>
</geographicCoverages>


<universes>
    <universe>
        <language>en</language> 
        <sampled>Dow Jones Industrial firms</sampled>
    </universe>
</universes>

<relations>

<relation>
    <identifier>10.15456/jbnst.2015176.153001</identifier>
    <identifierType>DOI</identifierType>
    <relationType>IsPartOf</relationType>
</relation>

</relations>


</resource>

'''
