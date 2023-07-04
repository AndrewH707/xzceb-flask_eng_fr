from deep_translator import MyMemoryTranslator 

def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source='en', target='fr').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    englishText = MyMemoryTranslator(source='fr', target='en').translate(frenchText)
    return englishText
