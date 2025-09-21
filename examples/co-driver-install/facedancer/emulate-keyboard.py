#!/usr/bin/env python3
#
# Simulate a keyboard.
#
""" Simulate keyboard with specific VID/PID. """

import asyncio
import logging

from facedancer import main
from facedancer.devices.keyboard     import USBKeyboardDevice
from facedancer.classes.hid.keyboard import KeyboardModifiers

device = USBKeyboardDevice()
device.manufacturer_string = "manufacturer"
device.product_string = "product"
device.serial_number_string = "1234"

# # Razer
# device.vendor_id = 0x1532
# device.product_id = 0x0084
# SteelSeries
device.vendor_id = 0x1038
device.product_id= 0x1610
# # Magic Control Technology
# device.vendor_id = 0x0711
# device.product_id = 0x5511
# # Logitech
# device.vendor_id = 0x046d
# device.product_id = 0xc547


async def type_letters():
    await asyncio.sleep(2)

    logging.info("Emulating keyboard.")

    # logging.info("Beginning message typing...")
    # await device.type_string("hello\n")
    # logging.info("Typing complete. Idly handling USB requests.")


main(device, type_letters())
