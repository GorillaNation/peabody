class Poller(object):
    def __init__(self, stdout, stderr, stdoutcallback, stderrcallback):
        self.fds = {
            stderr.fileno(): {
                "buf": "",
                "fd": stderr,
                "callback": stderrcallback,
            },
            stdout.fileno(): {
                "buf": "",
                "fd": stdout,
                "callback": stdoutcallback,
            }
        }

    # do the loop and make the callbacks
    # override this in subclasses
    def loop():
        pass

# logics to figure out the best poller to use. falls back to select() poller
def getPoller(stdout, stderr, stdoutcallback, stderrcallback):
    # TODO: add an epoll() poller
    import peabody.poller.selectpoller
    return peabody.poller.selectpoller.SelectPoller(stdout=stdout, stderr=stderr, stdoutcallback=stdoutcallback, stderrcallback=stderrcallback)
