import json


class FileHandler:
    @staticmethod
    def load_json(filepath):
        try:
            with open(filepath, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {filepath} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {filepath}.")
            return None

    @staticmethod
    def save_json(filepath, data):
        try:
            with open(filepath, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving file: {e}")
