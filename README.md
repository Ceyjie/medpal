//////////////////////////////////////////////////////////////////////////////////////////
# MedPal

AI-assisted medical + mobile robot platform (Raspberry Pi 5 & Google Coral USB)

## Structure
- `robot/` - motor control, simulation, hardware wiring
- `ai/` - local AI models, emergency logic
- `web/` - web control interface
- `docker/` - Docker setup for robot + AI
- `docs/` - architecture, wiring diagrams, notes

///////////////////////////////////////////////////////////////////////////////////////////
update control!
# MedPal Robot Controller

MedPal is a 4-wheel robot controlled via a web interface.  
It uses LEDs to simulate motor movements and can later be connected to real motors.

## Features
- Web dashboard to move robot: Forward / Backward / Left / Right / Stop
- Live LED indicators on the web page for each motor
- Easy to extend for real motor control

## Setup

1. Install required Python packages:

```bash
sudo apt update
sudo apt install python3-flask python3-gpiozero -y
///////////////////////////////////////////////////////////////////////////////////////////////
