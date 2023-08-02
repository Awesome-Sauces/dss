# DSS v0.3 (Dataset Standard)

** THIS DSS STANDARD IS IN BETA AND STILL IN DEVELOPMENT, PLEASE DO NOT USE THIS STANDARD **

## Overview:
The DSS v0.3 (Dataset Standard) is a comprehensive format designed for storing data in JSON. It builds upon the previous versions by adding several new sections that provide more detailed instructions for handling the dataset, preprocessing the data, and building machine learning models.

## JSON Structure:
- The DSS v0.3 introduces several new sections to the JSON structure:

- split_info: This section provides recommendations for splitting the dataset into training, validation, and test sets.

- preprocessing: This section documents any preprocessing steps that need to be applied to the data before it's used for model training.

- feature_engineering: This section provides suggestions for generating new features from the existing ones.

- baseline_model: This section provides the performance of a simple "baseline" model on the dataset.

- versioning: This section provides information about different versions of the dataset.

## Example:
```json
{
  "metadata": {
    ...
  },
  "features": [
    ...
  ],
  "targets": [
    ...
  ],
  "data": [
    ...
  ],
  "model_info": [
    ...
  ],
  "split_info": {
    "train_ratio": 0.8,
    "validation_ratio": 0.1,
    "test_ratio": 0.1
  },
  "preprocessing": [
    {
      "step": "Impute missing values",
      "details": "Use the median value for numeric features and the most frequent value for categorical features."
    },
    {
      "step": "Scale numeric features",
      "details": "Use StandardScaler to scale numeric features to have zero mean and unit variance."
    }
  ],
  "feature_engineering": [
    {
      "new_feature": "interaction_term",
      "details": "Create a new feature by multiplying 'feature1' and 'feature2'."
    }
  ],
  "baseline_model": {
    "model": "Dummy Classifier",
    "performance": {
      "accuracy": 0.6
    }
  },
  "versioning": [
    {
      "version": "1.0",
      "date": "2023-08-01",
      "changes": "Initial version."
    },
    {
      "version": "1.1",
      "date": "2023-09-01",
      "changes": "Added new samples."
    }
  ]
}
```

## Usage with dss.py Library:
- Here's a sample Python code snippet showing how to use the dss.py library to create, modify, import, and export datasets in the DSS v0.3 format.

## Import the Library and Create a Dataset Instance
```python
from dss import Dataset

# Create a new instance of the Dataset class
ds = Dataset()
```
## Add Metadata, Features, and Targets
```python
# Add metadata
ds.add_metadata("Iris Dataset", "A famous dataset for classification tasks.", "1.0", "2023-08-01")

# Add features
ds.add_feature("sepal_length", "numeric", "Length of the sepal in centimeters", "cm")
ds.add_feature("sepal_width", "numeric", "Width of the sepal in centimeters", "cm")

# Add target
ds.add_target("species", "categorical", "The species of the iris flower")
```
## Add Data Records
```python
# Add data (usually obtained from a pandas DataFrame or other data source)
data = [
    {"sepal_length": 5.1, "sepal_width": 3.5, "species": "setosa"},
    {"sepal_length": 4.9, "sepal_width": 3.0, "species": "setosa"},
    # ...
]
ds.add_data(data)
```
## Add Model Info, Split Info, Preprocessing Steps, and More
```python
# Add model info
ds.add_model_info("Random Forest", "Handles categorical features well.", {"n_estimators": 100})

# Add split info
ds.add_split_info(0.7, 0.15, 0.15)

# Add preprocessing step
ds.add_preprocessing_step("Impute missing values", "Use median for numeric features and mode for categorical features.")
```
## Export the Dataset to a JSON File
```python
# Export the dataset to a DSS v0.3 JSON file
ds.to_json("iris_dataset.dss.json")
```
## Import a Dataset from a JSON File
```python
# Import a dataset from a DSS v0.3 JSON file
ds.from_json("iris_dataset.dss.json")
```
Note: This is a basic usage example. Depending on your specific needs and the complexity of your dataset, you may need to use other methods provided by the Dataset class or even modify the class itself.

## Usage Guidelines:
The usage guidelines remain the same as in DSS v0.2, with the additional recommendation to consult the new sections for detailed instructions on handling the dataset, preprocessing the data, and building machine learning models.
The DSS v0.3 (Dataset Standard) continues to foster data accessibility, reusability, and reproducibility within the AI community, with comprehensive features to facilitate the entire machine learning process from data preprocessing to model building.
