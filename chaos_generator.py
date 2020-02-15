from time import sleep
from random import random

import pika

from rate import Rate


def main():
    # RabbitMQ stuff
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='PushRateToPostgresQueue', durable=True)

    print("[I] - Chaos Rates generator starting...")
    # generate and publish rates
    while True:
        rate = Rate.generate_random_rate()
        body = rate.serialize()
        channel.basic_publish(exchange='RateExchange',
                              routing_key='RatesData',
                              body=body)
        print(f"[x] Published rate: {body}")
        sleep(random())


if __name__ == "__main__":
    main()
