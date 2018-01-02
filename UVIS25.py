#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""UVIS25: Digital UV index sensor: 0 - 15 UV index output range."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["STMicroelectronics"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from UVIS25_constants import *

# name:        UVIS25
# description: Digital UV index sensor: 0 - 15 UV index output range.
# manuf:       STMicroelectronics
# version:     0.1
# url:         http://www.st.com/resource/en/datasheet/uvis25.pdf
# date:        2018-01-02


# Derive from this class and implement read and write
class UVIS25_Base:
	"""Digital UV index sensor: 0 - 15 UV index output range."""
	# Register WHO_AM_I
	# Device who am I 
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register CTRL_REG1
	# Control register 1 
	
	def setCTRL_REG1(self, val):
		"""Set register CTRL_REG1"""
		self.write(REG.CTRL_REG1, val, 8)
	
	def getCTRL_REG1(self):
		"""Get register CTRL_REG1"""
		return self.read(REG.CTRL_REG1, 8)
	
	# Bits reserved_0
	# These bits must be set to ‘0’ to ensure proper operation of the device 
	# Bits BDU
	# Block data update. 
	# Bits ODR
	# Enable continuous reading at 1 Hz. 
	#           ODR bit enables the continuous reading of the UV index at 1 Hz.. When ODR is set to ‘0’ the
	#           device enables the one-shot mode. When ‘ONESHOT’ bit in 9.3: CTRL_REG2 (21h) is set
	#           to ‘1’, a new UV index value is acquired. 
	#           If ODR bit and 'ONESHOT’ bit in 9.3: CTRL_REG2 (21h) are set to '0', the device is in
	#           power down mode. If ODR bit is set to '1', ‘ONESHOT’ bit in 9.3: CTRL_REG2 (21h) must
	#           be '0'. 
	
	# Register CTRL_REG2
	# Control register 2 
	
	def setCTRL_REG2(self, val):
		"""Set register CTRL_REG2"""
		self.write(REG.CTRL_REG2, val, 8)
	
	def getCTRL_REG2(self):
		"""Get register CTRL_REG2"""
		return self.read(REG.CTRL_REG2, 8)
	
	# Bits BOOT
	# Reboot memory content. 
	#           The bit is self-cleared when the BOOT is completed.
	#           BOOT bit is used to refresh the content of the internal registers stored in the Flash memory
	#           block. At the device power-up, the content of the Flash memory block is transferred to the
	#           internal registers related to trimming functions to permit a good behavior of the device itself.
	#           If for any reason, the content of the trimming registers is modified, it is sufficient to use this
	#           bit to restore the correct values. When BOOT bit is set to ‘1’ the content of the internal Flash
	#           is copied into the corresponding internal registers and is used to calibrate the device. These
	#           values are factory trimmed, and they are different for every device. They permit good
	#           behavior of the device and generally they should not be changed. At the end of the boot
	#           process, the BOOT bit is set again to ‘0’ by hardware. BOOT bit takes effect after one ODR
	#           clock cycle. 
	
	# Bits reserved_0
	# These bits must be set to ‘0’ to ensure proper operation of the device 
	# Bits I2C_DS
	# Disable I2C interface. 
	# Bits SIM
	# SPI Serial Interface Mode Selection. 
	# Bits reserved_1
	# These bits must be set to ‘0’ to ensure proper operation of the device 
	# Bits ONE_SHOT
	# One shot enable. 
	# Register CTRL_REG3
	# Interrupt control
	#       The device features one fully-programmable interrupt source (INT) that can be configured to
	#       trigger different events.
	#       The device may also be configured to generate, a Data Ready signal (DRDY) which
	#       indicates when a new measured UV index is available, thus simplifying data synchronization
	#       in digital systems or to optimize the system power consumption. 
	
	
	def setCTRL_REG3(self, val):
		"""Set register CTRL_REG3"""
		self.write(REG.CTRL_REG3, val, 8)
	
	def getCTRL_REG3(self):
		"""Get register CTRL_REG3"""
		return self.read(REG.CTRL_REG3, 8)
	
	# Bits INT_H_L
	# Interrupt active high, low. 
	# Bits PP_OD
	# Push-pull/open drain selection on interrupt pads. 
	# Bits reserved_0
	# These bits must be set to ‘0’ to ensure proper operation of the device 
	# Bits INT_S
	# Data signal on INT_DRDY pin control bits. 
	# Register INT_CFG
	# Interrupt configuration 
	
	def setINT_CFG(self, val):
		"""Set register INT_CFG"""
		self.write(REG.INT_CFG, val, 8)
	
	def getINT_CFG(self):
		"""Get register INT_CFG"""
		return self.read(REG.INT_CFG, 8)
	
	# Bits reserved_0
	# These bits must be set to ‘0’ to ensure proper operation of the device 
	# Bits DIFF_EN
	# Interrupt generation enable. 
	# Bits LIR
	# Latch interrupt request to the INT_SOURCE (24h) register. 
	# Bits UVLE
	# Enable interrupt generation on differential UV low event. 
	# Bits UVHE
	# Enable interrupt generation on differential UV high event. 
	# Register INT_SOURCE
	# Interrupt source configuration 
	
	def setINT_SOURCE(self, val):
		"""Set register INT_SOURCE"""
		self.write(REG.INT_SOURCE, val, 8)
	
	def getINT_SOURCE(self):
		"""Get register INT_SOURCE"""
		return self.read(REG.INT_SOURCE, 8)
	
	# Bits unused_0
	# Bits IA
	# Interrupt active. 
	# Bits UVL
	# Differential UV low. 
	# Bits UVH
	# Differential UV high. 
	# Register THS_UV
	# Threshold register 
	
	def setTHS_UV(self, val):
		"""Set register THS_UV"""
		self.write(REG.THS_UV, val, 8)
	
	def getTHS_UV(self):
		"""Get register THS_UV"""
		return self.read(REG.THS_UV, 8)
	
	# Bits THS_UV
	# This register contains the differential UV Interrupt threshold value for the 
	#            interrupt generation. 
	
	# Register reserved_0
	# do not use 
	
	def setreserved_0(self, val):
		"""Set register reserved_0"""
		self.write(REG.reserved_0, val, 8)
	
	def getreserved_0(self):
		"""Get register reserved_0"""
		return self.read(REG.reserved_0, 8)
	
	# Bits reserved_0
	# Register STATUS_REG
	# Status register 
	
	def setSTATUS_REG(self, val):
		"""Set register STATUS_REG"""
		self.write(REG.STATUS_REG, val, 8)
	
	def getSTATUS_REG(self):
		"""Get register STATUS_REG"""
		return self.read(REG.STATUS_REG, 8)
	
	# Bits reserved_0
	# These bits must be set to ‘0’ to ensure proper operation of the device 
	# Bits UV_DA
	# UV data available. 
	#           UV_DA is set to 1 whenever a new UVI sample is available. UV_DA is cleared
	#           when the UV_OUT_REG (28h) is read.
	#         
	
	# Register UV_OUT_REG
	# UV index output register 
	
	def setUV_OUT_REG(self, val):
		"""Set register UV_OUT_REG"""
		self.write(REG.UV_OUT_REG, val, 8)
	
	def getUV_OUT_REG(self):
		"""Get register UV_OUT_REG"""
		return self.read(REG.UV_OUT_REG, 8)
	
	# Bits OUT
	# UVI data output value. 
