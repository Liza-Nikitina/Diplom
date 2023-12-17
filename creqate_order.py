import configuration
import data
import requests


def create_order(body):
    return requests.post(configuration.BASIC_URL + configuration.CREATE_ORDER_PATH,
                         json=body)


def get_order_track():
    track = create_order(data.create_order_body).json()
    return track["track"]


def get_order_info():
    return requests.get(configuration.BASIC_URL + configuration.GET_ORDER_PATH + str(get_order_track()))

