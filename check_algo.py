
from timeeval import Algorithm, TrainingType, InputDimensionality
from timeeval.algorithms import lstm_ad

print(f"Algorithm: {lstm_ad().name}")
print(f"Training Type: {lstm_ad().training_type}")
print(f"Input Dimensionality: {lstm_ad().input_dimensionality}")
