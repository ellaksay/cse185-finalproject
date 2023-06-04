import re

def is_gzip(filename):
    return len(re.findall(r'.gz$', filename)) > 0
