import spacy


class GetDate:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def __call__(self, text: str) -> dict:
        doc = self.nlp(text)
        result = {"DATE": [], "TIME": []}
        for entity in doc.ents:
            if entity.label_ in result:
                result[entity.label_].append(entity.text)
        return result
