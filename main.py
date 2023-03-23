def on_received_value_deprecated(name, value):
    global timerCounter
    motobit.enable(MotorPower.ON)
    led.toggle(2, 4)
    led.toggle(2, 4)
    if name == "right":
        timerCounter = 0
        led.toggle(0, 0)
        led.toggle(0, 0)
        if value >= 65:
            motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 50)
            led.plot(0, 0)
            led.unplot(4, 0)
        elif value >= 35:
            motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 50)
    elif name == "left":
        timerCounter = 0
        led.toggle(0, 0)
        led.toggle(0, 0)
        if value >= 65:
            motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)
            led.plot(0, 0)
            led.unplot(4, 0)
        elif value >= 35:
            motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 50)
radio.on_received_value_deprecated(on_received_value_deprecated)

timerCounter = 0
timerCounter = 0
basic.show_leds("""
    . . . . .
        . . . . .
        . . # . .
        . . . . .
        # . . . .
""")
radio.set_group(1)
basic.show_string("1 j ")
# heartbeat

def on_forever():
    global timerCounter
    motobit.enable(MotorPower.ON)
    led.plot(2, 2)
    led.unplot(2, 2)
    timerCounter += 1
basic.forever(on_forever)
