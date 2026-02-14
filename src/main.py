import network
import socket
import machine

# 1. Hardware Setup
led = machine.Pin(2, machine.Pin.OUT)
led_state = "OFF"

# 2. Access Point Configuration
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='esp32-iot', password='12345678')

print('AP Active. IP Address:', ap.ifconfig()[0])

# 3. HTML UI (Lightweight UI/UX)
def web_page():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: Arial; text-align: center; background-color: #f4f4f9; color: #333; }}
            .container {{ marginTop: 50px; padding: 20px; }}
            .card {{ background: white; padding: 30px; border-radius: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display: inline-block; }}
            .btn {{ display: inline-block; padding: 15px 40px; font-size: 18px; cursor: pointer; text-decoration: none; border-radius: 10px; margin: 10px; border: none; transition: 0.3s; }}
            .on {{ background-color: #4CAF50; color: white; }}
            .off {{ background-color: #f44336; color: white; }}
            .status {{ font-weight: bold; color: {"#4CAF50" if led_state == "ON" else "#f44336"}; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <h1>ESP32 Control</h1>
                <p>LED Status: <span class="status">{led_state}</span></p>
                <a href="/?led=on"><button class="btn on">TURN ON</button></a>
                <a href="/?led=off"><button class="btn off">TURN OFF</button></a>
            </div>
        </div>
    </body>
    </html>
    """
    return html

# 4. Web Server Logic
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode('utf-8')
    
    # Handle LED logic
    if "/?led=on" in request:
        led.value(1)
        led_state = "ON"
    elif "/?led=off" in request:
        led.value(0)
        led_state = "OFF"
    
    # Send response
    response = web_page()
    conn.send('HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n')
    conn.sendall(response)
    conn.close()
