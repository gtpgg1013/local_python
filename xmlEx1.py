import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')

print('User count: ', len(lst))

for item in lst :
    print('Name: ', item.find('name').text)
    print('ID: ', item.find('id').text)
    print('X: ', item.get('x'))