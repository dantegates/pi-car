from .gpio import Channel


class _Machinery:
    def __init__(self, channel, *args, **kwargs):


class Car:
    forward = _Machinery(11)

    def drive(self, direction):
        if direction == 'forward':
            self._drive_forward()

    def _drive_forward(self):
        self.channel.output(1)