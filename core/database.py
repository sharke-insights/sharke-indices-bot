import json
import logging

logger = logger = logging.getLogger(__name__)


class Database:
    """
    Define Database as a Singleton class to retrieve data
    """

    _instance = None

    def __new__(cls, filepath):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.filepath = filepath

        return cls._instance

    def data(self):

        data = {}
        try:
            with open(self.filepath, "r") as fp:
                data = json.loads(fp.read())
        except FileNotFoundError:
            logger.warning("File %s does not exist" % self.filepath)

        return data

    def save(self, data):
        curr_data = self.data()

        try:
            if data not in curr_data['chat_ids']:
                curr_data['chat_ids'].append(data)
        except KeyError:
            curr_data = {"chat_ids": [data]}

        with open(self.filepath, "w") as fp:
            json.dump(curr_data, fp)
