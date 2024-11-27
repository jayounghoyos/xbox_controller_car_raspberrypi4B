# Raspberrypi 4 Car With XBOX_controller

This is a project to drive a raspberrypi car with a xbox controller. you can drive it with other controllers but you will need to to use the library evtest and try all the inputs for your controller.

![driving_the_car_GIF](imgs/controller.gif)
![close_case](imgs/close.jpeg)
![open_case](imgs/open.jpeg)

# Librearies to install 

#### RPi.GPIO is installed for deafault in the raspverry but you can check
```bash
pip install RPi.GPIO

```
#### evdev input devices

```bash
pip install evdev
```
or use this one
```bash
sudo apt-get install evtest
```

### All commands
```bash
pip install RPi.GPIO
pip install evdev
sudo apt-get install evtest
```

To try and see the controller inputs use this:
```bash
sudo evtest
```