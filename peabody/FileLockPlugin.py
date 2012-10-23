from peabody import LockPlugin
from lockfile import FileLock

class FileLockPlugin(LockPlugin):
    def acquire(self, timeout = 0):
        self.filelock = FileLock(self.backend)
        self.filelock.acquire(timeout)

    def release(self):
        self.filelock.release()
