"""Model trainer"""

from ludwig.api import LudwigModel
from ludwig.api import logging
import pandas as pd

config = {
    "model_type": "ecd",
    "input_features": [
        {
            "name": "sentence",
            "type": "text"
        },
        
    ], 
    "output_features": [
        {
            "name": "label",
            "type": "category",
        }
    ],
    "trainer": 
        {
            "optimizer": {
                "type": "adam",
                "learning_rate": 0.001
            },
            "epochs": 20,
            "batch_size" : 64
    
        },
    "split": 
        {
            "type": "random", 
            "probabilities": [0.6, 0.2, 0.2]  # train, validation, test
        }
    }


df = pd.read_csv("sh_dataset.csv", sep="#")

ludwig_model = LudwigModel(config, logging_level=logging.INFO)
train_stats, _, _ = ludwig_model.train(dataset=df, random_seed=42)
predictions, _ = ludwig_model.predict(dataset=df)

test_stats, predictions, output_directory = ludwig_model.evaluate(
  df,
  collect_predictions=True,
  collect_overall_stats=True
)
ludwig_model.save("./model/")







