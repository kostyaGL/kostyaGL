from django.db import models
import subprocess


class Node(models.Model):
    STATE_CHOICES = (
        (0, 'alive'),
        (1, 'dead'),
        (2, 'undefined')
    )

    hostname = models.CharField(max_length=30)
    ip = models.GenericIPAddressField(default='0.0.0.0')
    state = models.SmallIntegerField(choices=STATE_CHOICES, default=2)

    def verbose_state(self):
        return dict(self.STATE_CHOICES).get(self.state)

    def ping(self, ping_method):
        try:
            result = subprocess.Popen(["ping", "-n", "1", "-w", "200", getattr(self, ping_method)], stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
            self.state = result
            self.save()
        except:
            pass

    def __str__(self):
        return "%s %s" % (self.hostname, self.ip)
