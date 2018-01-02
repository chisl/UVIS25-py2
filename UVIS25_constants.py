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

class REG:
	WHO_AM_I = 15
	CTRL_REG1 = 32
	CTRL_REG2 = 33
	CTRL_REG3 = 34
	INT_CFG = 35
	INT_SOURCE = 36
	THS_UV = 37
	reserved_0 = 38
	STATUS_REG = 39
	UV_OUT_REG = 40
