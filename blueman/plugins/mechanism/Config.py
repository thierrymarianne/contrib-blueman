# Copyright (C) 2009 Valmantas Paliksa <walmis at balticum-tv dot lt>
#
# Licensed under the GNU General Public License Version 3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 

from blueman.plugins.MechanismPlugin import MechanismPlugin
import os

class Config(MechanismPlugin):
	def on_load(self):
		self.add_dbus_method(self.SetBluezConfig, in_signature="ssss", out_signature="", sender_keyword="caller")

	def SetBluezConfig(self, file, section, key, value, caller):
		self.confirm_authorization(caller, "org.blueman.bluez.config")
		
		c = BluezConfig(file)
		c.set(section, key, value)
		c.write()