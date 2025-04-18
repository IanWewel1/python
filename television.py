class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3


    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = self.min_volume
        self.temp = self.volume
        self.channel = self.min_channel

    def power(self):
        self.status = not self.status

    def mute(self):
        if self.status:
            if not self.muted:
                self.temp = self.volume
                self.muted = True
            else:
                self.muted = False
                self.volume = self.temp

    def channel_up(self):
        if self.status == True:
            if self.channel < self.max_channel:
                self.channel += 1
            else:
                self.channel = self.min_channel

    def channel_down(self):
        if self.status == True:
            if self.channel > self.min_channel:
                self.channel -= 1
            else:
                self.channel = self.max_channel

    def volume_up(self):
        if self.status:
            if self.muted:
                if self.temp < self.max_volume:
                    self.temp += 1
                self.volume = self.temp
                self.muted = False
            elif self.volume < self.max_volume:
                self.volume += 1

    def volume_down(self):
        if self.status:
            if self.muted:
                if self.temp > self.min_volume:
                    self.temp -= 1
                self.volume = self.temp
                self.muted = False
            elif self.volume > self.min_volume:
                self.volume -= 1

    def __str__(self):
        display_volume = 0 if self.muted else self.volume
        return (f'Power - {self.status}, Channel - {self.channel}, Volume - {display_volume}')



