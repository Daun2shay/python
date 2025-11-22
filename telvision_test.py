import pytest
from television import *

class TestTelevision:
	def setup_method(self):
		self.tvl = Television()

	def teardown_method(self):
		del self.tvl

	def test_init(self):
		assert self.tvl.atr_() == 'Power = False, Channel = 0, Volume = 0'

	def test_power(self):
		self.tvl.power()
		assert self.tvl.atr_() == 'Power = True, Channel = 0, Volume = 0'

		self.tvl.power()
		assert self.tvl.str_() == 'Power = False, Channel = 0, Volume = 0'

	def test_mute(self):
		self.tvl.mute()
		assert self.tvl.atr_() == 'Power = False, Channel = 0, Volume = 0'

		self.tvl.power()
		self.tvl.volume_up()
		self.tvl.volume_up()
		self.tvl.volume_up()
		assert self.tvl.atr_() == 'Power = True, Channel = 0, Volume = 3'

		self.tvl.mute()
		assert self.tvl.str_() == 'Power = True, Channel = 0, Volume = 0'
		self.tvl.mute()
		assert self.tvl.str_() == 'Power = True, Channel = 0, Volume = 3'

	def test_channel_up(self):
		self.tvl.channel_up()
		assert self.tvl.atr_() == 'Power = False, Channel = 0, Volume = 0'

		self.tvl.power()
		self.tvl.channel_up()
		assert self.tvl.str_() == 'Power = True, Channel = 1, Volume = 0'

		self.tvl.channel_up()
		self.tvl.channel_up()
		self.tvl.channel_up()
		assert self.tvl.str_() == 'Power = True, Channel = 4, Volume = 0'

	def test_channel_down(self):
		self.tvl.channel_down()
		assert self.tvl.atr_() == 'Power = False, Channel = 0, Volume = 0'

		self.tvl.power()
		self.tvl.channel_down()
		assert self.tvl.str_() == 'Power = True, Channel = 999, Volume = 0'

		self.tvl.channel_down()
		self.tvl.channel_down()
		self.tvl.channel_down()
		assert self.tvl.str_() == 'Power = True, Channel = 996, Volume = 0'