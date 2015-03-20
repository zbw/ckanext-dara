# -*- coding: utf-8 -*-


xml = """<?xml version="1.0" encoding="UTF-8"?>

<study xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="dara_v2.2.1_05092012.xsd">

  <resourceType>2</resourceType>
  
  <titles>
    <title>
      <titleName>Is a &#34;Firm&#34; a Firm? A Stackelberg Experiment</titleName>
      <language>en</language>
    </title>
  </titles>
  
  <principalInvestigators>  <!--XXX this <creators> in 3.0-->
      <principalInvestigator> <!-- creator in 3.0 -->
        <person>
          <firstName>Andreas</firstName>
          <lastName>Hildenbrand</lastName>
        </person>
      </principalInvestigator>
  </principalInvestigators>

  <dataURLs>
    <dataURL>http://localhost:5000/dataset/is-a-firm-a-firm-a-stackelberg-experiment</dataURL>
  </dataURLs>

  <doiProposal>10.2345/economics.2kAR1w89Bj</doiProposal>

  <publicationDate>
      <year>2012</year>
  </publicationDate>

  <availability>
      <availabilityControlled>1</availabilityControlled>
  </availability>






<!-- control -
<auto> {&#39;URL&#39;: u&#39;http://localhost:5000/dataset/is-a-firm-a-firm-a-stackelberg-experiment&#39;, &#39;ResourceType&#39;: &#39;2&#39;} </auto>
<inhalt>{u&#39;dara_Universe_sampled&#39;: u&#39;&#39;, u&#39;dara_AlternativeIdentifier_ID&#39;: u&#39;10-23443&#39;, u&#39;dara_Publication_Issue&#39;: u&#39;&#39;, u&#39;dara_PublicationDate&#39;: u&#39;2012&#39;, u&#39;dara_Note_text&#39;: u&#39;this is a test dataset&#39;, u&#39;dara_TimeDimension_free&#39;: u&#39;&#39;, u&#39;dara_Availabilitycontrolled&#39;: u&#39;1&#39;, u&#39;dara_OtherTitle&#39;: u&#39;ein ganz anderer titel&#39;, u&#39;dara_Universe_areaFree&#39;: u&#39;&#39;, u&#39;dara_CollectionDate_controlled&#39;: u&#39;2014-04-22&#39;, u&#39;dara_Availabilityfree&#39;: u&#39;&#39;, u&#39;dara_Publication_Editor&#39;: u&#39;Carola Schirmer&#39;, u&#39;dara_OtherTitleType&#39;: u&#39;1&#39;, u&#39;dara_Rights&#39;: u&#39;&#39;, u&#39;dara_AlternativeIdentifier_Type&#39;: u&#39;ISBN&#39;, u&#39;dara_Publication_Author&#39;: u&#39;Hinnerk Bunke&#39;, u&#39;dara_Publication_Journal&#39;: u&#39;AuS&#39;, u&#39;dara_Frequency&#39;: u&#39;&#39;, u&#39;dara_CollectionDate_free&#39;: u&#39;Winter 2001&#39;, u&#39;dara_language&#39;: u&#39;eng&#39;, u&#39;dara_SelectionMethod&#39;: u&#39;bla bladf if then&#39;, u&#39;dara_Publication_Place&#39;: u&#39;Bremen&#39;, u&#39;dara_Publication_Volume&#39;: u&#39;&#39;, u&#39;dara_Publication_PIDType&#39;: u&#39;DOI&#39;, u&#39;dara_Publication_Year&#39;: u&#39;2014&#39;, u&#39;dara_Publication_DocType&#39;: u&#39;2&#39;, u&#39;dara_CollectionMode_free&#39;: u&#39;&#39;, u&#39;dara_currentVersion&#39;: u&#39;&#39;, u&#39;dara_TimeDimension_controlled&#39;: u&#39;7&#39;, u&#39;edawax_article_url&#39;: u&#39;http://www.economics-ejournal.org/economics/journalarticles/2013-20&#39;, u&#39;dara_Publication_Pages&#39;: u&#39;&#39;, u&#39;dara_Publication_Publisher&#39;: u&#39;FriesenEdition&#39;, u&#39;dara_Universe_areaControlled&#39;: u&#39;&#39;, u&#39;dara_Publication_PID&#39;: u&#39;10.4567/eda.3456&#39;, u&#39;dara_Publication_Title&#39;: u&#39;Ein toller Edawax Test&#39;, u&#39;dara_Publication_RelationType&#39;: u&#39;test *relation*&#39;, u&#39;dara_Publication_ISSN&#39;: u&#39;&#39;, u&#39;dara_Publication_Anthology&#39;: u&#39;&#39;, u&#39;dara_author_2&#39;: u&#39;Hinnerk Bunke&#39;, u&#39;dara_CollectionMode_controlled&#39;: u&#39;8&#39;, u&#39;dara_Publication_ISBN&#39;: u&#39;&#39;, u&#39;dara_DataCollector_name&#39;: u&#39;&#39;}</inhalt>
<pkg> &lt;Package id=e11185fc-f1de-4350-a89e-54e81de8e35c name=is-a-firm-a-firm-a-stackelberg-experiment title=Is a &#34;Firm&#34; a Firm? A Stackelberg Experiment version=None url=None author=Andreas Hildenbrand  author_email=None maintainer=None maintainer_email=None notes=Dataset for http://www.economics-ejournal.org/economics/journalarticles/2013-20

Industrial organization is mainly concerned with the behavior of large firms, especially when it comes to oligopoly theory. Experimental industrial organization therefore faces a problem: How can firms be brought into the laboratory? The main approach relies on framing: Call individuals “firms”! This experimental approach is not in line with modern industrial organization, according to which a firm’s market behavior is also determined by its organizational structure. In this paper, a Stackelberg experiment is considered in order to answer the question whether framing individual decision making as organizational decision making or implementing an organizational structure is more effective in generating profitmaximizing behavior. Firms are either represented by individuals or by teams. Teams are organized according to Alchian and Demsetz’s (1972) contractual view of the firm. I find that teams’ quantity choices are more in line with the assumption of profit maximization than individuals’ choices. Compared to individuals, teams appear to be less inequality averse. license_id=None type=dataset owner_org=2465675b-888d-41a4-b49a-ef15bc3f0e9e creator_user_id=bef0487f-3f67-4eb0-99dc-3b6276797a93 metadata_modified=2014-10-21 11:40:55.581639 private=False state=active revision_id=435ed361-2941-42bf-9574-048af36e005f&gt; </pkg>
-->

</study>
"""
