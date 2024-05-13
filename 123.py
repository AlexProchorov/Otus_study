import re

str = '3 тов  pf 200.99'
pat = r'\d+.\d'
match = re.search(pat,str)

print(match.group())