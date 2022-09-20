import re

emails = """
    skeepertech@gmail.com
    gugod254@gmail.com
    https://github.com
    123Gigthub.com
    skeeper.www@yahoo.com
    """
    
pattern = re.compile(r'[a-zA-Z0-9\.]+(@?:?/?/?)([a-zA-Z])+(.com)+')
matches = pattern.finditer(emails)

for match in matches:
    print(match.group(1,2,3))