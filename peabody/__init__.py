class Plugin(object):
    pass

class LockPlugin(Plugin):
    def __init__(self, backend, options = {}):
        self.backend = backend
        self.options = options

    def acquire(self, timeout = 0):
        raise NotImplementedError("This method was not implemented by the subclass")

    def release(self):
        raise NotImplementedError("This method was not implemented by the subclass")

class LockAlreadyLockedException(Exception):
    pass

class LockTimeoutException(Exception):
    pass
