from gpiozero import LED

# GPIO pins for LEDs (simulate motors)
LF_F = LED(17)
LF_B = LED(18)
RF_F = LED(22)
RF_B = LED(23)
LB_F = LED(24)
LB_B = LED(25)
RB_F = LED(5)
RB_B = LED(6)

# Group LEDs for easy control
forward_leds = [LF_F, RF_F, LB_F, RB_F]
backward_leds = [LF_B, RF_B, LB_B, RB_B]
left_motors = [LF_F, LF_B, LB_F, LB_B]
right_motors = [RF_F, RF_B, RB_F, RB_B]

# ===== Movement Functions =====
def stop_all():
    for led in left_motors + right_motors:
        led.off()

def move_forward():
    stop_all()
    for led in forward_leds:
        led.on()

def move_backward():
    stop_all()
    for led in backward_leds:
        led.on()

def turn_left():
    stop_all()
    for led in [LF_B, LB_B]:  # left backward
        led.on()
    for led in [RF_F, RB_F]:  # right forward
        led.on()

def turn_right():
    stop_all()
    for led in [LF_F, LB_F]:  # left forward
        led.on()
    for led in [RF_B, RB_B]:  # right backward
        led.on()
