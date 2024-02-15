from pprint import pprint

fale_name = 'fale.txt'
fale = open(fale_name, mode='r')
fale_content = fale.read()
fale.close()
pprint(fale_content)
