import typing as t


class Ml:

    @staticmethod
    def predict(text: str) -> t.Dict[str, t.Any]:
        # do ML magic
        task = {
            "tldr": "Blah-blah",
            "time": "8 mins"
        }
        return task
