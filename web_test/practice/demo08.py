import sys
from lxml import etree
from

xml_tree = etree.parse("xmlToHtmlTest.xml")
xsl_tree = etree.parse("xmlToHtmlTest.xsl")

xml_file_content = etree.tostring(xml_tree,encoding='UTF-8',method='xml')
xsl_file_content = etree.tostring(xsl_tree,encoding='UTF-8',method='html')

xsl_dom = etree.XML(xsl_file_content)
xml_dom = etree.XML(xml_file_content)

transform = etree.XSLT(xsl_dom)
html_result = transform(xml_dom)

print(html_result)

str_html = str(html_result)

with open('xmlToHtmlTest.html','w+') as f:
    f.write(str_html)
    f.close()
