from unidecode import unidecode

class StringHelper(object):
    """Bu sinif metinsel ifadelerin manipulasyonu icin kullanilir"""
    def remove_diacritics(self, text, isLower):
        result = unidecode(text)
        if isLower == 'True':
            return str.lower(result)
        else:
            return result