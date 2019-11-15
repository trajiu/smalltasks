import re
import xml.etree.cElementTree as ET


def writeXML(item):
    ET.SubElement(data, 'field0', name='Number').text = lst_i[0]
    ET.SubElement(data, 'field1', name='IP').text = lst_i[1]
    ET.SubElement(data, 'field2', name='Adress').text = lst_i[2]   
    
    tree = ET.ElementTree(camera)
    tree.write('file.xml', encoding='UTF-8')

lst_data = []
with open('/home/dmitriy/Dropbox/test.txt', 'r') as f:
    for data_line in f.readlines():
        lst_data.append(data_line.replace('\t', ';').replace('\n', ''))

camera = ET.Element('Cameras')
for i in lst_data:
    lst_i = str(i).split(';')
    data = ET.SubElement(camera, 'data')
    ET.SubElement(data, 'field0', name='Number').text = lst_i[0]
    ET.SubElement(data, 'field1', name='IP').text = lst_i[1]
    ET.SubElement(data, 'field2', name='Adress').text = lst_i[2]   
    
    tree = ET.ElementTree(camera)
    tree.write('/home/dmitriy/Dropbox/test.xml')
