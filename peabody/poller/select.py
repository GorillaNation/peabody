class Select(peabody.poller.Poller):
    def loop():
        while self.fds:
            (reads, writes, rithmatics) = select.select(self.fds.keys(), [], [])
            for readfd in reads:
                print "got something on {0}".format(readfd)
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
                    print "fd closed, baleeeeted"
                    del self.fds[readfd]
