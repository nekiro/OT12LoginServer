from login_server import LoginServer
from tornado.ioloop import IOLoop
import tornado.web
import json
import models

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, login_server: LoginServer) -> None:
        self.login_server = login_server

    def post(self: "MainHandler") -> None:
        try:
            request = json.loads(self.request.body)
            type = request.get("type")
            if type is None:
                return

            if type == "login":
                email = request.get("email")
                if email is None:
                    return

                password = request.get("password")
                if password is None:
                    return

                token = request.get("token")
                if token is None:
                    token = ""

                self.login_server.process_login(email, password, token, self)
            elif type == "boostedcreature":
                print("requesting boosted creature")
            elif type == "cacheinfo":
                print("requesting cache info")
            elif type == "eventschedule":
                print("requesting events schedule")
        except Exception as err:
            print(err)

def main():
    login_server = LoginServer()
    if not login_server.start():
        print("There was a problem with connecting to database.")
        exit()

    app = tornado.web.Application(
        [
            (r"/login", MainHandler, dict(login_server=login_server)),
            (r"/login.php", MainHandler, dict(login_server=login_server))
        ]
    )

    conf = models.config.get("server", None)
    if not conf:
        print("Invalid server configuration config.yml")
        exit()

    try:
        app.listen(conf.get("port", 80))
    except Exception as err:
        print(err)
        exit()

    print("Started listening at {}:{}".format(conf.get("host", "127.0.0.1"), conf.get("port", 80)))

    try:
        IOLoop.instance().start()
    except KeyboardInterrupt:
        IOLoop.instance().stop()

if __name__ == '__main__':
    main()