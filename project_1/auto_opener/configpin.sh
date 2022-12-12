#!/bin/bash
# --------------------------------------------------------------------------
# Opener Pin Configuration
# --------------------------------------------------------------------------
# Copyright 2022 Brandon Peoples
# 
# ... License ... 
# 
# --------------------------------------------------------------------------
# Configure pins for <Opener>
# --------------------------------------------------------------------------
#Button
config-pin P2_02 gpio

#servo1
config-pin P2_04 gpio
config-pin P2_06 gpio
config-pin P2_08 gpio
config-pin P2_10 gpio

#servo2
config-pin P2_01 gpio
config-pin P2_03 gpio
config-pin P2_05 gpio
config-pin P2_07 gpio

#ultrasound sensor
config-pin P1_02 gpio
config-pin P1_04 gpio

#lcd screen
config-pin P1_26 gpio
config-pin P1_28 gpio
config-pin P1_30 gpio
config-pin P1_10 spio
config-pin P1_12 spio
config-pin P1_08 spio
config-pin P1_14 sys
config-pin P1_16 sys
