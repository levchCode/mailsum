import spacy
from spacy.cli import download

class GetDate:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            download('en')
            self.nlp = spacy.load("en_core_web_sm")

    def __call__(self, text: str) -> list:
        text = text.replace('!', '.').replace('?', '.').replace(';', '.').split('.')
        results = []
        for t in text:
            doc = self.nlp(t)
            result = {}
            keys = ["PERSON", "TIME", "DATE"]
            for entity in doc.ents:
                if entity.label_ in keys:
                    if entity.label_ in result:
                        result[entity.label_].append(entity.text)
                    else:
                        result[entity.label_] = [entity.text]

            if bool(result):
                results.append(result)
        return results

