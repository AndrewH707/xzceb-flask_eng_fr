"""Module providing Translation"""

from deep_translator import MyMemoryTranslator


def englishToFrench(english_text):
    """function to translate from english to french"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text


def frenchToEnglish(french_text):
    """function to translate from french to english"""
    #write the code here
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
