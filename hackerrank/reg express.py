# Post Code
import re

s = '127832'
print(bool(re.match(r'^[1-9][\d]{5}$', s) and len(re.findall(r'(\d)(?=.\1)', s)) < 2))
