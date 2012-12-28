import redis
import json
from peabody.output import Output
import redis
import socket
from datetime import datetime
import uuid

class LogstashRedis(Output):
    def __init__(self, options):
        #super(Output, self).__init__(options)
        self.redis = redis.StrictRedis(host="jupiter.home.kitchen.io", port=6379, db=0)

        self.obj = {
            '@fields': {
                    'peabody_job_id': uuid.uuid4().hex,
            },
            '@type':'peabody',
            '@source_host':socket.getfqdn(),
            '@source_path':'peabody_script_thing',
        }

        self.obj['@source'] = "file://{0}/{1}".format(self.obj["@source_host"], self.obj["@source_path"])

        self.redis_key = 'logstash'
        
    def stdout(self, line):
        self.obj["@timestamp"] = datetime.utcnow().isoformat('T') + 'Z'
        self.obj["@message"] = line
        self.obj["@fields"]["peabody_output"] = "stdout"
        self.redis.rpush(self.redis_key, json.dumps(self.obj))

    def stderr(self, line):
        self.obj["@timestamp"] = datetime.utcnow().isoformat('T') + 'Z'
        self.obj["@message"] = line
        self.obj["@fields"]["peabody_output"] = "stderr"
        self.redis.rpush(self.redis_key, json.dumps(self.obj))
