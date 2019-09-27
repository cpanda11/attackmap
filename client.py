import tornado.websocket
import time
from tornado import gen
import tornado.ioloop


@gen.coroutine
def test_ws():
    client = yield tornado.websocket.websocket_connect("ws://192.168.2.6:9090/ws")
    message = "{\"latitude\":\"50.78\",\"longitude\":\"119.97\",\"countrycode\":\"CN\",\"country\":\"CN\"," \
              "\"city\":\"Changzhou\",\"org\":\"Chinanet Jiangsu Province Network\",\"latitude2\":\"40.48\"," \
              "\"longitude2\":\"-112.01\",\"countrycode2\":\"US\",\"country2\":\"US\",\"city2\":\"Riverton\"," \
              "\"type\":\"ipviking.honey\",\"md5\":\"61.160.224.129\",\"dport\":\"8080\",\"svc\":\"8080\"," \
              "\"zerg\":\"\"}"
    client.write_message(message)
    msg = yield client.read_message()
    print("msg is %s" % msg)
    client.close()


if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().run_sync(test_ws)
