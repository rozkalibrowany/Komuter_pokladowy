MAX_RPM_VALUE = 6000
CAN_COMMAND = 'stdbuf -o0 candump can0'
TEST_COMMAND = 'python can_simulation.py'
ANGLE_RANGE = 245
MAX_TEMPERATURE_VALUE = 255

ERR = {
    0 : 'Identification error',
    1 : 'Over voltage',
    2 : 'Low voltage',
    3 : 'RESERVED',
    4 : 'Motor provide speed feedback',
    5 : 'Internal volts fault',
    6 : 'Over temperature',
    7 : 'Throttle error at power-up',
    8 : 'RESERVED',
    9 : 'Internal reset',
    10 : 'Hall throttle open',
    11 : 'Angle sensor open',
    12 : 'RESERVED',
    13 : 'RESERVED',
    14 : 'Motor over temperature',
    15 : 'Hall Galvanometer sensor error',
}

