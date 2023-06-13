import contextlib
from aijson.decorate import aijson


class JsonDisposer:
    def __init__(self, path):
        self.path = path

    def dump(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f)


def formatter_factory(format="json", path=None):
    if format == "json":
        return JsonDisposer(path=path)
    else:
        raise NotImplementedError(f"{format} not supported yet!")


class LogDisposer:
    def __init__(self, data=None):
        self.data = data

    def dump(path=".model.ai.json", format="json"):
        formatter = formatter_factory(format=format, path=path)
        formatter.dump(self.data)

    def __str__(self):
        return json.dumps(self.data)


@contextlib.contextmanager
def logging_context():
    aijson.reset()
    yield LogDisposer(data=aijson.graph)
    aijson.reset()
