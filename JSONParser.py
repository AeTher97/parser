import json


class JSONParser:
    @staticmethod
    def ParseJSON(JsonToParse):
        JSON = json.loads(JsonToParse)

        JSONArray = []
        for key in JSON:
            JSONArray.append(JSON[key])
        return JSONArray



