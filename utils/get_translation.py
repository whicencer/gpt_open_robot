from config import translations

def get_translation(key: str, language: str = "en") -> str:
  if language not in translations:
    language = "en"
  return translations[language][key]