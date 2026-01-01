from pathlib import Path
from typing import Dict, Any

import numpy as np

from timeeval import TimeEval, DatasetManager, Algorithm, TrainingType, InputDimensionality
from timeeval.adapters import FunctionAdapter
from timeeval.algorithms import subsequence_if,copod
from timeeval.params import FixedParameters

# Load dataset metadata
dm = DatasetManager(Path("skabdata"), create_if_missing=False)

# Select datasets and algorithms
datasets = dm.select()
datasets = datasets[-1:]
# Add algorithms to evaluate...
algorithms = [
    copod(),
]
timeeval = TimeEval(dm, datasets, algorithms)

# execute evaluation
timeeval.run()
# retrieve results
print(timeeval.get_results())
