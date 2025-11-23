class Television:
	# setting the maximum and minimum volume and channel variables
	MIN_VOLUME: int = 0
	MAX_VOLUME: int = 2
	MIN_CHANNEL: int = 0
	MAX_CHANNEL: int = 3

	# setting the initial tv state
	def __init__(self) -> None:
		self.__muted: bool = False
		self.__volume: int = Television.MIN_VOLUME
		self.__channel: int = Television.MIN_CHANNEL
		self.__power_on: bool = False

	# if the power is off this turns it on if it is off this turns it on
	def power(self) -> None:
		self.__power_on = not self.__power_on

	# this mutes and unmutes the tv
	def mute(self) -> None:
		if self.__power_on:
			self.__muted = not self.__muted

	# this ups the current channel by 1 unless it is already on the max channel
	def channel_up(self) -> None:
		if not self.__power_on:
			return
		if self.__channel < Television.MAX_CHANNEL:
			self.__channel += 1
		else:
			self.__channel = Television.MIN_CHANNEL

	# this lowers the current channel by one unless it is already on the minimum channel
	def channel_down(self) -> None:
		if not self.__power_on:
			return
		if self.__channel > Television.MIN_CHANNEL:
			self.__channel -= 1
		else:
			self.__channel = Television.MAX_CHANNEL

	# this raises the volume by one unless it is already on the max volume
	def volume_up(self) -> None:
		if not self.__power_on:
			return
		self.__muted = False
		if self.__volume < Television.MAX_VOLUME:
			self.__volume += 1

	# this lowers the volume by one unless it is already on the min volume
	def volume_down(self) -> None:
		if not self.__power_on:
			return
		if self.__volume > Television.MIN_VOLUME:
			self.__volume -= 1

	# This prints the current tv state
	def __str__(self) -> str:
		if self.__muted:
			return f'Volume = {Television.MIN_VOLUME} (muted), Channel = {self.__channel}'
		else:
			return f'Volume = {self.__volume}, Channel = {self.__channel}'
