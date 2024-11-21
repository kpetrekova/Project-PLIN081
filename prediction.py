import pandas as pd
from ludwig.api import LudwigModel


model = LudwigModel.load('model')


def predict_if_shakespeare(sentences):
    """Predict label for each sentence to determine the result if it is Shakespeare."""

    text_to_predict = pd.DataFrame(sentences, columns=['sentence'])

    predictions, _ = model.predict(dataset=text_to_predict)
    print(predictions)
    pred = predictions['label_probabilities_1'].tolist()

    labels = [float(item) for item in pred]

    result = round(sum(labels) / len(labels))

    return result
