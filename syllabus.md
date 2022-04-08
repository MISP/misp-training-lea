# Syllabus overview

|Module 3|Information sharing and modeling introduction|
|:---|:---|
|What is covered|Introduction sessions describing the various information sharing and modelling techniques via MISP followed by a practical lab session||
|Requirements|- MISP Introduction (from eLearning materials)|
|Responsible partner|CIRCL|
|**Contents**|- Module 3.1 (e.101) Practical Information Sharing between Law Enforcement and CSIRT communities using MISP<br />-Module 3.2 (e.205) Mapping investigation and cases in MISP<br />-Module 3.3 (e.206) From evidences to actionable information|

|Module 3.1|Practical Information Sharing between Law Enforcement and CSIRT communities using MISP|
|:---|:---|
|What is covered|- Objectives<br />- Description of the 2-day session and setup<br />- MISP introduction (refresh from mandatory eLearning materials)<br />- Law-enforcement usage of MISP<br />- Benefit of using MISP||
|Requirements|- MISP Introduction (from eLearning materials)|
|Total Duration|105minutes|
|Responsible partner|CIRCL|
|Course reference|e.101|

|Module 3.2|Mapping investigation and cases in MISP|
|:---|:---|
|What is covered|- Structure evidences<br /> - Contextualise information<br />- Prepare information for sharing<br />||
|Requirements|- MISP Introduction (from eLearning materials)|
|Total Duration|90minutes|
|Responsible partner|CIRCL|
|Course reference|e.205|

|Module 3.3|From evidences to actionable information|
|:---|:---|
|What is covered|- How evidences (from logs, network captures to disk acquired) can be useful for defense?<br />- How to structure non-technical information?||
|Requirements|- MISP Introduction (from eLearning materials)|
|Total Duration|75minutes|
|Responsible partner|CIRCL|
|Course reference|e.206|

|Module 4|Labs I - Modeling, Interpreting and Sharing “Hacking Evidence”|
|:---|:---|
|What is covered|**Finding Hacking evidence:**<br />- Structure the logs and encode it in MISP<br />&nbsp;&nbsp;- Include the original log file as an attachment<br />&nbsp;&nbsp;- Share resource addresses to find the encoded data back in the original file<br />- Correlation with pre-encoded/exported event from AIL<br />&nbsp;&nbsp;- Fake bitcoin address found in the student’s materials -> Trainers show the a full event they crafted containing as much feature as MISP can offer: Yara rules, timeline, contextualisation, …|
|Requirements|- MISP Introduction (from eLearning materials)<br />- Module 3|
|Total Duration|90+minutes|
|Responsible partner|CIRCL|
|Course reference|e.302|

### Day 4

|Module 5|Supplementary tools for information sharing|
|:---|:---|
|What is covered|Information enrichment, gathering as well as community management and information distribution handling||
|Requirements|- MISP Introduction (from eLearning materials)<br />- Module 3|
|Responsible partner|CIRCL|
|**Contents**|- Module 5.1 (e.102) Data mining Tor, social networks, OSINT with AIL Project<br />- Module 5.2 (e.103) Managing information sharing communities - cerebrate introduction|
|What is covered|- Objectives<br />- Description of the 2-day session and se<br />-Module 3.2 (e.205) Mapping investigation and cases in MISP |

|Module 5.1|Data mining Tor, social networks, OSINT with AIL Project|
|:---|:---|
|What is covered|- Overview of the open source project AIL<br />- Demo and usage of AIL including Tor crawling<br />- Finding evidences from AIL and produce MISP event reports<br />- Law-enforcement usage of AIL<br />||
|Requirements|- MISP Introduction (from eLearning materials)|
|Total Duration|105minutes|
|Responsible partner|CIRCL|
|Course reference|e.102|

|Module 5.2|Managing information sharing communities - Cerebrate introduction|
|:---|:---|
|What is covered|- Directory and Budapest convention<br />- Managing sharing groups<br />- Searching for information||
|Requirements|- MISP Introduction (from eLearning materials)|
|Total Duration|60minutes|
|Responsible partner|CIRCL|
|Course reference|e.103|

|Module 6|CSIRTs network, notification and sharing scenarios|
|:---|:---|
|What is covered|- An introduction into how the [CSIRTs network](https://www.enisa.europa.eu/topics/csirts-in-europe/csirts-network) handles notification and information sharing in general<br />- Challenges of collaboration between accredited CSIRTs and LEAs||
|Requirements||
|Total Duration|30minutes|
|Responsible partner|CIRCL|
|Course reference|e.104|

|Module 7|Labs II: Encoding information and sharing it|
|:---|:---|
|What is covered|**Extract an Executable from PCAP & Investigating a compromised Linux Host:**<br />- PCAP is coming from a Linux machine<br />Analysing PCAP<br />- extracting evidences<br />- Pre-encode the event (manual and JSON import in UI)<br />- Encode the executable and describe what it does<br />- Connected graph, [hashlookup](https://www.circl.lu/services/hashlookup/) example<br />- From correlations between the provided events and the ones encoded by the students, find more information and correlation about their events||
|Requirements|- MISP Introduction (from eLearning materials)|
|Total Duration|75minutes|
|Responsible partner|CIRCL|
|Course reference|e.303|

|Module 8|Labs III - Encoding information and sharing - HTTP and DNS Data to Isolate Threat Actor|
|:---|:---|
|What is covered|**HTTP and DNS Data to Isolate Threat Actor:**<br />- Target: PCAP about Log4J exfiltration over DNS<br />- Describe and encode the exfiltration process, data and target in MISP<br />- Manual and automatic import with PyMISP<br />- Play with distribution and correctly set it for each data point<br />- **[Advanced exercise]** Second stage malware exfiltrating TXT record custom base64 encoded where information is contained in the padding||
|Requirements|- MISP Introduction (from eLearning materials)|
|Total Duration|90+minutes|
|Responsible partner|CIRCL|
|Course reference|e.304|
