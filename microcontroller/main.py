from m5stack import *
from m5ui import *
from uiflow import *
import machine
import time

setScreenColor(0xffffff)  # White background

adc0 = machine.ADC(34)
adc0.width(machine.ADC.WIDTH_9BIT)      # 9-bit resolution (0–511)
adc0.atten(machine.ADC.ATTN_11DB)       # Voltage range 0–3.3V

# UI text fields
label_status = M5TextBox(20, 60, "Waiting for sound...", lcd.FONT_DejaVu24, 0x000000, rotate=0)
label_level = M5TextBox(20, 120, "Mic Level: 0", lcd.FONT_DejaVu18, 0x000000, rotate=0)

while True:
    mic_level = adc0.read()
    
    print("Mic level:", mic_level)
    label_level.setText("Mic Level: {}".format(mic_level))  # Show numeric level

    if mic_level > 100:
        label_status.setText("🎙️ Sound detected!")
    else:
        label_status.setText("...")

    wait(0.1)
