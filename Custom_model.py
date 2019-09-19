

import pickle

filename = 'model_v1.pk'
#classifier = joblib.load('./classifier/model.pkl')
classifier = pickle.load(open(filename, 'rb'))


def post_predictions(query):
    predictions = []
    for item in query:
        text = item['text']
        category = classifier.predict([text])[0]
        predictions.append({"category": category, "text": text})
    return predictions
	
def post_predictions1(query):
    predictions = []
    for item in query:
        text = item['text']
        category = classifier.predict([text])[0]
        predictions.append({"category": category, "text": text})
    return predictions

