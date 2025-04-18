class Television:
    """
    Creates global variables to use in the rest of the code
    """
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3


    def __init__(self) -> None:
        """
        Method initializes private variables for power, muting, volume, and channel
        """
        self.status = False
        self.muted = False
        self.volume = self.min_volume
        self.temp = self.volume
        self.channel = self.min_channel

    def power(self) -> None:
        """
        Method turns on and off the television
        """
        self.status = not self.status

    def mute(self) -> None:
        """
        Method mutes the television but shows the volume as zero while keeping the actual volume
        """
        if self.status:
            if not self.muted:
                self.temp = self.volume
                self.muted = True
            else:
                self.muted = False
                self.volume = self.temp

    def channel_up(self) -> None:
        """
        Method increases channel by one until it reaches max, then it goes down to minimum
        """
        if self.status:
            if self.channel < self.max_channel:
                self.channel += 1
            else:
                self.channel = self.min_channel

    def channel_down(self) -> None:
        """
        Method decreases channel by one until it reaches min, then it goes up to the maximum
        """
        if self.status:
            if self.channel > self.min_channel:
                self.channel -= 1
            else:
                self.channel = self.max_channel

    def volume_up(self) -> None:
        """
        Method increases volume by one, when it reaches max it stops increasing
        """
        if self.status:
            if self.muted:
                if self.temp < self.max_volume:
                    self.temp += 1
                self.volume = self.temp
                self.muted = False
            elif self.volume < self.max_volume:
                self.volume += 1

    def volume_down(self) -> None:
        """
        Method decreases volume by one, when it reaches min it stops decreasing
        """
        if self.status:
            if self.muted:
                if self.temp > self.min_volume:
                    self.temp -= 1
                self.volume = self.temp
                self.muted = False
            elif self.volume > self.min_volume:
                self.volume -= 1

    def __str__(self) -> str:
        display_volume = 0 if self.muted else self.volume
        return (f'Power - {self.status}, Channel - {self.channel}, Volume - {display_volume}')



