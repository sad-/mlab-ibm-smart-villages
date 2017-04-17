import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features

def analyze(text):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='f482a680-b22f-44cb-90ec-f17f958e7efc',
        password='BLMaJkqErAkM')

    response = natural_language_understanding.analyze(
        text=text,
        features=[features.Entities(), features.Keywords(), features.Concepts(), features.Sentiment()])

    decoder = json.JSONDecoder()

    decoded_response = decoder.decode(json.dumps(response, indent=2))
    language = decoded_response["language"]
    keywords = decoded_response["keywords"]
    entities = decoded_response["entities"]
    concepts = decoded_response["concepts"]
    sentiment = decoded_response["sentiment"]
    return language, keywords, entities, concepts, sentiment

if __name__ == "__main__":
    analyze()