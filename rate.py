import random
import json
from datetime import datetime

from faker import Faker
from pytz import utc

RATE_SOURCES = ['Reuters', 'Bloomberg']


class Rate:
    fake = Faker()

    def __init__(self, index, value, source, source_timestamp):
        self.index = index
        self.value = value
        self.source = source
        self.source_timestamp = source_timestamp

    def __repr__(self):
        return "{cls}(index={index}, value={value}, source={source}, source_timestamp={source_timestamp})".format(
            cls=self.__class__.__name__,
            index=self.index,
            value=self.value,
            source=self.source,
            source_timestamp=self.source_timestamp
        )

    def serialize(self):
        return json.dumps({
            "index": self.index,
            "value": self.value,
            "source": self.source,
            "source_timestamp": self.source_timestamp
        }, default=str)

    @classmethod
    def deserialize(cls, o):
        data = json.loads(o)
        # string to datetime conversion
        data["source_timestamp"] = datetime.fromisoformat(data["source_timestamp"])
        return cls(**data)

    @classmethod
    def generate_random_rate(cls):
        index = random.randint(1, 100)
        value = random.random()
        source = random.choice(RATE_SOURCES)
        source_timestamp = cls.fake.date_time_between(
            start_date='-5y',
            end_date='now',
            tzinfo=utc
        )

        return cls(
            index=index,
            value=value,
            source=source,
            source_timestamp=source_timestamp
        )
