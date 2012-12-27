import select
from peabody.poller import Poller

class SelectPoller(Poller):
    def loop(self):
        while self.fds:
            foo = self.fds.keys()
            (reads, writes, rithmatics) = select.select(self.fds.keys(), [], [])
            for readfd in reads:
                buf = self.fds[readfd]["fd"].read(8192)
                self.fds[readfd]["buf"] += buf
                while True:
                    (line, partition, leftover) = self.fds[readfd]["buf"].partition("\n")
                    if partition:
                        # callback goes here
                        self.fds[readfd]["callback"](line)
                        self.fds[readfd]["buf"] = leftover
                    else:
                        break
                if not buf:
                    del self.fds[readfd]
