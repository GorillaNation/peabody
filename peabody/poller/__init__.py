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
    
    pass

def getPoller(stdout, stderr, stdoutcallback, stderrcallback):
    # TODO: add an epoll() poller
    import peabody.poller.selectpoller
    return peabody.poller.selectpoller.SelectPoller(stdout=stdout, stderr=stderr, stdoutcallback=stdoutcallback, stderrcallback=stderrcallback)
