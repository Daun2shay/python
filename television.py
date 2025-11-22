class Television:
	MIN_VOLUME = 0
	MAX_VOLUME = 100
	MIN_CHANNEL = 1
	MAX_CHANNEL = 999

	def __init__(self):
		self.muted = False
		self.volume = Television.MIN_VOLUME
		self.channel = Television.MIN_CHANNEL
		self.power_on = False

	def power(self):
		self.power_on = not self.power_on

	def mute(self):
		if self.power_on:
			self.muted = not self.muted

	def channel_up(self):
		if not self.power_on:
			return
		if self.channel < Television.MAX_CHANNEL:
			self.channel += 1
		else:
			self.channel = Television.MIN_CHANNEL

	def channel_down(self):
		if not self.power_on:
			return
		if self.channel > Television.MIN_CHANNEL:
			self.channel -= 1
		else:
			self.channel = Television.MAX_CHANNEL

	def volume_up(self):
		if not self.power_on:
			return
		self.muted = False
		if self.volume < Television.MAX_VOLUME:
			self.volume += 1

	def volume_down(self):
		if not self.power_on:
			return
		if self.volume > Television.MIN_VOLUME:
			self.volume -= 1

	def __str__(self):
		if self.muted:
			return f'Volume = {Television.MIN_VOLUME} (muted), Channel = {self.channel}'
		else:
			return f'Volume = {self.volume}, Channel = {self.channel}'