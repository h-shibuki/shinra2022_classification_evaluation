import json


class DataUtils:
    class JsonL:
        def load(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                data = []
                for line in f:
                    try:
                        data.append(json.loads(line))
                    except json.decoder.JSONDecodeError:
                        continue
                return data
