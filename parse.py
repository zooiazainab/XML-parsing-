import xml.etree.ElementTree as ET
mytree=ET.parse('compiler.xml')
myroot=mytree.getroot()
print(myroot)
for element in myroot.findall("book"):
    print('________________________________')
    print(element.tag, element.attrib)
    for child in element:
        print(child.tag , ' => ', child.text)    
