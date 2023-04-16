import json
import time
import requests


class complex_encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, stream):
            return obj.__dict__
        if isinstance(obj, loki_request):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class loki_handler:
    def __init__(self, url, labels, labelKeys=None):
        if labelKeys is None:
            labelKeys = {}
        self.url = url
        self.request = loki_request()
        self.steam = stream(labels)
        self.request.addVSteam(self.steam)
        self.labelKeys = labelKeys

    def write(self, message):
        record = message.record

        self.steam.addLabel("level", record["level"].name)

        simplified = {
            "message": record["message"],
            "timestamp": record["time"].timestamp(),
            "process": record["process"].id,
            "thread": record["thread"].id,
            "function": record["function"],
            "module": record["module"],
            "name": record["name"],
        }

        for key, value in record["extra"].items():
            simplified[key] = value

        if record["level"].name == "ERROR":
            simplified["file"] = record.get("file").name
            simplified["path"] = record.get("file").path
            simplified["line"] = record.get("line")

        for key, val in simplified.items():
            if key in self.labelKeys:
                self.steam.addLabel(key, val)

        self.steam.setValue(json.dumps(simplified))

        headers = {"Content-type": "application/json"}

        requests.post(self.url, data=self.request.serialize(), headers=headers)
        

class stream(object):
    def __init__(self, labels=None, enableBuffer=False):
        if labels is None:
            labels = {}
        self.stream = labels
        self.values = []

        if enableBuffer == False:
            self.values.append("")

    def addLabel(self, key, value):
        self.stream[key] = value

    def appendValue(self, value):
        self.values.append([str(time.time_ns()), value])

    def setValue(self, value):
        self.values[0] = [str(time.time_ns()), value]

    def serialize(self):
        return json.dumps(self, cls=complex_encoder)


class loki_request:
    def __init__(
        self,
    ):
        self.streams = []

    def addVSteam(self, steam):
        self.streams.append(steam)

    def serialize(self):
        return json.dumps(self, cls=complex_encoder)
