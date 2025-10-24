#!/bin/sh

echo "Content-Type: text"

echo "ret: ${?}"

echo 1 > /sys/class/leds/led:pwr/brightness

echo "ret: ${?}"

