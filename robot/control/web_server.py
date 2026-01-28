from flask import Flask, render_template, jsonify
import robot_logic as rl
import os

# --- Automatically set paths to your web folder ---
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../web")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# --- Helper function to get LED status for web dashboard ---
def get_led_status():
    return {
        "LF_F": rl.LF_F.is_lit,
        "LF_B": rl.LF_B.is_lit,
        "RF_F": rl.RF_F.is_lit,
        "RF_B": rl.RF_B.is_lit,
        "LB_F": rl.LB_F.is_lit,
        "LB_B": rl.LB_B.is_lit,
        "RB_F": rl.RB_F.is_lit,
        "RB_B": rl.RB_B.is_lit,
    }

# --- Flask routes ---
@app.route("/")
def index():
    return render_template("index.html")  # Flask will now look in web/templates

@app.route("/forward")
def forward():
    rl.move_forward()
    return jsonify(get_led_status())

@app.route("/backward")
def backward():
    rl.move_backward()
    return jsonify(get_led_status())

@app.route("/left")
def left():
    rl.turn_left()
    return jsonify(get_led_status())

@app.route("/right")
def right():
    rl.turn_right()
    return jsonify(get_led_status())

@app.route("/stop")
def stop_route():
    rl.stop_all()
    return jsonify(get_led_status())

# --- Main ---
if __name__ == "__main__":
    rl.stop_all()
    print("MedPal server running... open http://<Pi_IP>:5000")
    app.run(host="0.0.0.0", port=5000)
