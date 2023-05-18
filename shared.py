import re
from unidecode import unidecode

COLUMN_NAME_REGEX= '[^a-zA-Z0-9\;]'
TRIM_END_REGEX = '[_]+$'

def trim_column_names(col):
    col = unidecode(col)   
    col = re.sub(COLUMN_NAME_REGEX, '_', col).upper().strip()
    col = re.sub('[__]+', '_', col)
    col =  re.sub(TRIM_END_REGEX, '', col)
    return col