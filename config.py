import tensorflow as tf
from ultralytics import YOLO
from gpiozero import DistanceSensor, Servo
from gpiozero.pins.pigpio import PiGPIOFactory

#change this to your own pin
echo_pin = 24
trigger_pin = 23
servo_pin = 12
#change this to your own parking id
idparkir = 2
#change this to your own api url
api = "http://localhost:5000/"

factory = PiGPIOFactory()
ultrasonic = DistanceSensor(echo=echo_pin, trigger=trigger_pin)
servo = Servo(servo_pin, pin_factory=factory)
modelyolo = YOLO("models/best.onnx")
model = tf.keras.models.load_model("models/charplatevechile_recognition.keras")
class_names = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
temp_directory = "temp"