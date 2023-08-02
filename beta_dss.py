import json

class Dataset:
    def __init__(self):
        self.dataset = {
            "metadata": {},
            "features": [],
            "targets": [],
            "data": [],
            "model_info": [],
            "split_info": {},
            "preprocessing": [],
            "feature_engineering": [],
            "baseline_model": {},
            "versioning": []
        }

    def from_json(self, file_path):
        with open(file_path, 'r') as f:
            self.dataset = json.load(f)

    def to_json(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.dataset, f, indent=4)

    def add_metadata(self, name, description, version, created_at):
        self.dataset["metadata"] = {
            "name": name,
            "description": description,
            "version": version,
            "created_at": created_at
        }

    def add_feature(self, name, data_type, description="", units="", time_index=False, missing_values="",
                    transformations=""):
        self.dataset["features"].append({
            "name": name,
            "data_type": data_type,
            "description": description,
            "units": units,
            "time_index": time_index,
            "missing_values": missing_values,
            "transformations": transformations
        })

    def add_target(self, name, data_type, description=""):
        self.dataset["targets"].append({
            "name": name,
            "data_type": data_type,
            "description": description
        })

    def add_data(self, data):
        self.dataset["data"] = data

    def add_model_info(self, model, reason, hyperparameters):
        self.dataset["model_info"].append({
            "model": model,
            "reason": reason,
            "hyperparameters": hyperparameters
        })

    def add_split_info(self, train_ratio, validation_ratio, test_ratio):
        self.dataset["split_info"] = {
            "train_ratio": train_ratio,
            "validation_ratio": validation_ratio,
            "test_ratio": test_ratio
        }

    def add_preprocessing_step(self, step, details):
        self.dataset["preprocessing"].append({
            "step": step,
            "details": details
        })

    def add_feature_engineering(self, new_feature, details):
        self.dataset["feature_engineering"].append({
            "new_feature": new_feature,
            "details": details
        })

    def add_baseline_model(self, model, performance):
        self.dataset["baseline_model"] = {
            "model": model,
            "performance": performance
        }

    def add_version(self, version, date, changes):
        self.dataset["versioning"].append({
            "version": version,
            "date": date,
            "changes": changes
        })

    def to_dataframe(self):
        # Convert each data entry to a pandas Series and collect them in a list
        data_series = [pd.Series(entry) for entry in self.dataset['data']]

        # Concatenate all series into a DataFrame
        df = pd.concat(data_series, axis=1).T  # transpose (T) because concat works column-wise

        # Convert the feature data types
        for feature in self.dataset['features']:
            if feature['data_type'] == 'numeric':
                df[feature['name']] = pd.to_numeric(df[feature['name']], errors='coerce')

        return df
