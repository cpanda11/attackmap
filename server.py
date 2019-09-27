import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('norse.html')


class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []

    def open(self):
        print("new connection")
        self.write_message("The server says: 'Hello'. Connection was accepted.")
        WSHandler.clients.append(self)

    def on_message(self, message):
        print('received:', message)
        self.write_to_clients(message)

    def on_close(self):
        print('connection closed...')
        WSHandler.clients.remove(self)

    def write_to_clients(self, msg):
        print("Writing to clients")
        for client in self.clients:
            client.write_message(msg)


application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "."}),
])

if __name__ == "__main__":
    application.listen(9090, address='192.168.2.6')
    tornado.ioloop.IOLoop.instance().start()
