import redis
import json
import peabody.output
import redis
import socket
from datetime import datetime
import uuid
from urlparse import urlparse
import re

class LogstashRedis(peabody.output.Output):
    def __init__(self, options):
        super(LogstashRedis, self).__init__(options)
        redis_url = urlparse(options.logstash_redis_url)
        self.redis = redis.StrictRedis(host=redis_url.hostname, port=redis_url.port, db=re.sub(r'^/', '', redis_url.path))

        self.obj = {
            '@fields': {
                'peabody': {
                    "run_id": options.cronjob_run_id,
                    "child_pid": options.child_pid,
                }
            },
            '@type':'peabody',
            '@source_host': options.logstash_source_host,
            '@source_path': options.logstash_source_file,
            '@source': "file://{0}/{1}".format(options.logstash_source_host, options.logstash_source_file),
        }

        if options.cronjob_name:
            self.obj["@fields"]["peabody"]["cronjob"] = options.cronjob_name

        self.redis_key = options.logstash_redis_key
        
    def stdout(self, line):
        self.obj["@fields"]["peabody"]["output"] = "stdout"
        self.output(line)

    def stderr(self, line):
        self.obj["@fields"]["peabody"]["output"] = "stderr"
        self.output(line)

    def output(self, line):
        self.obj["@timestamp"] = datetime.utcnow().isoformat('T') + 'Z'
        self.obj["@message"] = line
        self.redis.rpush(self.redis_key, json.dumps(self.obj))

