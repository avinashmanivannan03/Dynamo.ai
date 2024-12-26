import json

def load_login_data():
    try:
        with open("data.json") as f:
            data = json.load(f)
        if not data:
            print("Error: login_data.json is empty")
            return None
        return data
    except FileNotFoundError:
        print("Error: login_data.json not found")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON in login_data.json")
        return None
