from lxml import etree
from lxml import html
import re
from bs4 import BeautifulSoup

__author__ = 'rabbi'

s = '<tr style="color:Black;background-color:White;"> <td align="center" style="width:3%;"> <span align="left" id="GridView1_ctl02_l1">1</span></td><td align="left" style="width:28%;" valign="top"> <table cellpadding="2" width="100%"> <tr> <td align="left" valign="top" width="30%"> <b>Proposal No </b> </td> <td width="5%"> : </td> <td align="left" valign="top" width="65%"> <span align="left" id="GridView1_ctl02_std">IA/GJ/MIN/2037/2011</span> </td> </tr> <tr> <td align="left" valign="top"> <b>File No </b> </td> <td width="5%"> : </td> <td align="left" valign="top"> <span align="left" id="GridView1_ctl02_fn">J -11015/366/2006-IA.II(M)</span> </td> </tr> <tr> <td align="left" valign="top"> <b>Proposal Name </b> </td> <td width="5%"> : </td> <td align="left" valign="top"> <span align="left" id="GridView1_ctl02_Label2" style="display:inline-block;width:100%;">Naniber Limestone Mining Project</span> </td> </tr> </table> </td><td align="left" style="width:15%;" valign="top"> <table cellpadding="2" width="100%"> <tr> <td align="left" valign="top" width="30%"> <b>State </b> </td> <td width="10%"> : </td> <td align="left" valign="top" width="60%"> <span align="left" id="GridView1_ctl02_stdname">Gujarat</span> </td> </tr> <tr> <td align="left" valign="top"> <b>District </b> </td> <td width="10%"> : </td> <td align="left" valign="top"> <span align="left" id="GridView1_ctl02_lbldis">Ahmedabad</span> </td> </tr> <tr> <td align="left" valign="top"> <b>Village </b> </td> <td width="10%"> : </td> <td align="left" valign="top"> <span align="left" id="GridView1_ctl02_lblvill">Naniber</span> </td> </tr> </table> </td><td align="center" style="width:23%;" valign="top"> <span align="left" id="GridView1_ctl02_datehtml"><table cellpadding="2" width="100%"><tr><td align="left" valign="top" width="62%"><b>Date of TOR Granted </b></td><td width="8%">:</td><td align="left" valign="top" width="30%"> 23 Oct 2007</td></tr><tr><td align="left" valign="top" width="62%"><b>Date of Receipt for EC </b></td><td width="8%">:</td><td align="left" valign="top" width="30%"> </td></tr><tr><td align="left" valign="top" width="62%"><b>Date of EC Granted </b></td><td width="8%">:</td><td align="left" valign="top" width="30%"> 11 Jun 2011</td></tr></table></span></td><td align="left" style="width:7%;"> <span align="left" id="GridView1_ctl02_dst">Mining Projects</span> </td><td align="left" style="width:10%;"> <span align="left" id="GridView1_ctl02_uag">M/s ABG Cement Limited</span></td><td align="left" style="width:10%;"> <span align="left" id="GridView1_ctl02_uag1"></span></td><td align="left" style="width:15%;white-space:nowrap;" valign="top"> <span align="left" id="GridView1_ctl02_attfile"><div style="float: left; width: 200px; padding: 5px;"><span style="padding: 0 5px 0;float:left;height:40px"><a href="Auth/openletter.aspx?TOR=684" target="_blank" title="TOR Letter"><img border="0" src="images/tor.png" width="35px"/></a></span><span style="padding: 0 5px 0;float:left;height:40px"><a href="Auth/openletter.aspx?EC=2290" target="_blank" title="EC Letter"><img border="0" src="images/ec.png" width="35px"/></a></span></div></span> </td> </tr>'
soup = BeautifulSoup(s)
# print soup.findChild('td')
# tr = soup.find('tr')

# t = etree.fromstring(s)
# rows = t.xpath("//td")
# for row in rows:
#     print row
#
i = 0
# for c in tr.find_all('td'):

tr = html.fromstring(s)
tds = tr.xpath('./td')
print tds[1].text_content()
for td in tds:
    print td.text_content()

for c in soup.find_all('td'):
    print c
    i += 1

    # tree = html.fromstring(s)
    # print tree.xpath('//td')