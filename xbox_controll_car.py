import RPi.GPIO as GPIO
from evdev import InputDevice, ecodes

# Configuracion de los pines GPIO
MOTOR1_FORWARD_PIN = 18
MOTOR1_BACKWARD_PIN = 23
MOTOR2_FORWARD_PIN = 22
MOTOR2_BACKWARD_PIN = 24

# Configura los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR1_FORWARD_PIN, GPIO.OUT)
GPIO.setup(MOTOR1_BACKWARD_PIN, GPIO.OUT)
GPIO.setup(MOTOR2_FORWARD_PIN, GPIO.OUT)
GPIO.setup(MOTOR2_BACKWARD_PIN, GPIO.OUT)

# Inicializa los motores apagados
GPIO.output(MOTOR1_FORWARD_PIN, GPIO.LOW)
GPIO.output(MOTOR1_BACKWARD_PIN, GPIO.LOW)
GPIO.output(MOTOR2_FORWARD_PIN, GPIO.LOW)
GPIO.output(MOTOR2_BACKWARD_PIN, GPIO.LOW)

# Funciones para controlar los motores
def motor1_forward():
    GPIO.output(MOTOR1_FORWARD_PIN, GPIO.HIGH)
    GPIO.output(MOTOR1_BACKWARD_PIN, GPIO.LOW)

def motor1_backward():
    GPIO.output(MOTOR1_FORWARD_PIN, GPIO.LOW)
    GPIO.output(MOTOR1_BACKWARD_PIN, GPIO.HIGH)

def motor2_forward():
    GPIO.output(MOTOR2_FORWARD_PIN, GPIO.HIGH)
    GPIO.output(MOTOR2_BACKWARD_PIN, GPIO.LOW)

def motor2_backward():
    GPIO.output(MOTOR2_FORWARD_PIN, GPIO.LOW)
    GPIO.output(MOTOR2_BACKWARD_PIN, GPIO.HIGH)

def stop_motors():
    GPIO.output(MOTOR1_FORWARD_PIN, GPIO.LOW)
    GPIO.output(MOTOR1_BACKWARD_PIN, GPIO.LOW)
    GPIO.output(MOTOR2_FORWARD_PIN, GPIO.LOW)
    GPIO.output(MOTOR2_BACKWARD_PIN, GPIO.LOW)

# Configura el dispositivo del control
gamepad = InputDevice('/dev/input/event4')  # Asegurate de que sea correcto
print("Control conectado. Esperando movimientos del joystick...")

# Lectura del joystick
try:
    for event in gamepad.read_loop():
        if event.type == ecodes.EV_ABS:
            if event.code == 0:  # Eje X del joystick izquierdo
                if event.value < 30000:  # Hacia la izquierda
                    print("Joystick hacia la izquierda")
                    motor1_backward()
                    motor2_forward()
                elif event.value > 36000:  # Hacia la derecha
                    print("Joystick hacia la derecha")
                    motor1_forward()
                    motor2_backward()
                else:  # Joystick en el centro
                    stop_motors()
            elif event.code == 1:  # Eje Y del joystick izquierdo
                if event.value < 30000:  # Hacia arriba
                    print("Joystick hacia arriba")
                    motor1_backward()
                    motor2_backward()
                elif event.value > 36000:  # Hacia abajo
                    print("Joystick hacia abajo")
                    motor1_forward()
                    motor2_forward()
                else:
                    print("Joystick centrado")
except KeyboardInterrupt:
    print("Saliendo...")
    stop_motors()
    GPIO.cleanup()
