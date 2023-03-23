def on_received_value(name, value):
    global timerCounter
    motobit.enable(MotorPower.ON)
    if name == "right":
        timerCounter = 0
        if value > 65:
            motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, value)
            showSpeed(4, value)
        elif value < 35:
            motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, value)
            showSpeed(4, value)
        elif value < 65 and value > 35:
            motobit.enable(MotorPower.OFF)
    elif name == "left":
        timerCounter = 0
        if value > 65:
            motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)
        elif value < 35:
            motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 50)
        elif value < 65 and value > 35:
            motobit.enable(MotorPower.OFF)
        timerCounter = 0
radio.on_received_value(on_received_value)

def showSpeed(ledColumn: number, motorSpeed: number):
    led.plot(ledColumn, Math.map(motorSpeed, 0, 100, 0, 4))
timerCounter = 0
radio.set_group(1)
motobit.enable(MotorPower.ON)
timerCounter = 0
ledRow3 = 0
basic.show_leds("""
    # . . . #
        . . . . .
        . . # . .
        . . . . .
        # . . . #
""")
basic.show_string("hello")
# heartbeat

def on_forever():
    global timerCounter
    timerCounter += 1
    if timerCounter > 5:
        motobit.enable(MotorPower.OFF)
basic.forever(on_forever)


def displayMotorSpeed(ledColumn2: number, motorSpeed: number):
    global ledRow3
    ledRow3 = pins.map(motorSpeed, -100, 200, 4, 0)
    for index62 in range(5):
        if index62 < ledRow3:
            led.unplot(ledColumn2, index62)
        else:
            led.plot(ledColumn2, index62)