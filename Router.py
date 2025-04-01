# router.py
class Router:
    def __init__(self):
        self.routes = {}
        self.methods = {}

    def setpath(self, client, path, methods=["GET"]):
        def wrapper(func):
            self.routes[path] = func
            self.methods[path] = methods
            return func
        return wrapper

    def get_route(self, path):
        return self.routes.get(path, None)

    def get_methods(self, path):
        return self.methods.get(path, ["GET"])
