from flask import Flask, render_template_string
from gpiozero import LED
from time import sleep

# === GPIO pins for LEDs (simulate motors) ===
# Left Motor
LF_F = LED(17)
LF_B = LED(18)

# Right Motor
RF_F = LED(22)
RF_B = LED(23)

# Left Back Motor
LB_F = LED(24)
LB_B = LED(25)

# Right Back Motor
RB_F = LED(5)
RB_B = LED(6)

# Grouping for easy control
forward_leds = [LF_F, RF_F, LB_F, RB_F]
backward_leds = [LF_B, RF_B, LB_B, RB_B]

left_motors = [LF_F, LF_B, LB_F, LB_B]
right_motors = [RF_F, RF_B, RB_F, RB_B]

# Flask setup
app = Flask(__name__)

def stop_all():
    for led in left_motors + right_motors:
        led.off()

@app.route("/")
def index():
    # We use a comprehensive HTML/CSS string here to create a nice UI
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MedPal Controller</title>
        <style>
            :root {
                --bg-color: #1a1a2e;
                --btn-color: #16213e;
                --accent-color: #0f3460;
                --text-color: #e94560;
                --stop-color: #e74c3c;
                --go-color: #2ecc71;
            }
            body {
                background-color: var(--bg-color);
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                user-select: none; /* Prevent text selection on long press */
            }
            h1 {
                margin-bottom: 20px;
                font-weight: 300;
                letter-spacing: 2px;
                color: #fff;
            }
            
            /* D-Pad Grid Layout */
            .control-pad {
                display: grid;
                grid-template-columns: 100px 100px 100px;
                grid-template-rows: 100px 100px 100px;
                gap: 15px;
            }
            
            button {
                background: var(--btn-color);
                border: none;
                border-radius: 15px;
                color: white;
                font-size: 24px;
                cursor: pointer;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.1s, background 0.2s;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            button:active {
                transform: scale(0.95);
                box-shadow: 0 2px 3px rgba(0,0,0,0.3);
            }

            /* Positioning Buttons */
            .btn-fwd { grid-column: 2; grid-row: 1; background: var(--accent-color); font-size: 30px;}
            .btn-left { grid-column: 1; grid-row: 2; background: var(--accent-color); font-size: 30px;}
            .btn-right { grid-column: 3; grid-row: 2; background: var(--accent-color); font-size: 30px;}
            .btn-back { grid-column: 2; grid-row: 3; background: var(--accent-color); font-size: 30px;}
            
            .btn-stop { 
                grid-column: 2; 
                grid-row: 2; 
                background: var(--stop-color); 
                font-weight: bold;
                font-size: 18px;
                border: 2px solid #c0392b;
            }

            /* Status Bar */
            #status-bar {
                margin-top: 30px;
                padding: 10px 20px;
                background: #0f3460;
                border-radius: 50px;
                font-size: 14px;
                color: #bbb;
            }

        </style>
    </head>
    <body>

        <h1>MedPal Control</h1>

        <div class="control-pad">
            <button class="btn-fwd" onclick="sendCommand('/forward', 'Moving Forward')">▲</button>
            
            <button class="btn-left" onclick="sendCommand('/left', 'Turning Left')">◀</button>
            
            <button class="btn-stop" onclick="sendCommand('/stop', 'STOPPED')">STOP</button>
            
            <button class="btn-right" onclick="sendCommand('/right', 'Turning Right')">▶</button>
            
            <button class="btn-back" onclick="sendCommand('/backward', 'Moving Backward')">▼</button>
        </div>

        <div id="status-bar">Status: Ready</div>

        <script>
            function sendCommand(route, statusText) {
                // Update status text on screen
                document.getElementById('status-bar').innerText = "Status: " + statusText;
                
                // Send request to Flask
                fetch(route)
                    .then(response => {
                        if (!response.ok) {
                            console.error("Command failed");
                        }
                    })
                    .catch(error => console.error("Error:", error));
            }
        </script>
    </body>
    </html>
    """)

@app.route("/forward")
def forward():
    stop_all()
    for led in forward_leds:
        led.on()
    return "Moving Forward"

@app.route("/backward")
def backward():
    stop_all()
    for led in backward_leds:
        led.on()
    return "Moving Backward"

@app.route("/left")
def left():
    stop_all()
    # Left motors backward, right motors forward
    for led in [LF_B, LB_B]:  # left backward
        led.on()
    for led in [RF_F, RB_F]:  # right forward
        led.on()
    return "Turning Left"

@app.route("/right")
def right():
    stop_all()
    # Left motors forward, right motors backward
    for led in [LF_F, LB_F]:  # left forward
        led.on()
    for led in [RF_B, RB_B]:  # right backward
        led.on()
    return "Turning Right"

@app.route("/stop")
def stop_route():
    stop_all()
    return "Stop"

if __name__ == "__main__":
    stop_all()
    # Make sure to run with host 0.0.0.0 so you can access it from other devices
    app.run(host="0.0.0.0", port=5000, debug=False)