import os
from pathlib import Path
import json

class TranslationManager:
    language = 'en'
    translations = {}

    def __init__(self):
        lang_folder = "language"
        files = os.listdir(lang_folder)
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(lang_folder, file)
                lang_name = str(Path(file).with_suffix(""))
                try:
                    # Open and  the JSON file
                    with open(file_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)
                        self.translations[lang_name] = data
                except Exception as e:
                    print(f"Error reading {file}: {e}")

    def set_language(self, language):
        self.language = language

    def translate(self, input, mapping=None):
        dictionary = self.translations.get(self.language, None)
        if dictionary is None: # Fallback to 'en'
            dictionary = self.translations.get('en', None)
        if dictionary is None: # Not even 'en'?? Give up.
            return input
        
        res = dictionary.get(input, input) # Use translation of 'input', or just use the original string
        try:
            if mapping is not None:
                res = res.format_map(mapping)
        except Exception as e:
            print(f"Error in translation mapping. {e}")
        return res

