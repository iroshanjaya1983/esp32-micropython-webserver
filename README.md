# ESP32 MicroPython Web Server Control Node

A lightweight, standalone IoT solution that allows users to control hardware via a mobile-responsive web interface hosted directly on an ESP32. No internet or external router required.



## 🚀 Features
- **Standalone Access Point:** Acts as a WiFi hotspot (SSID: `esp32-iot`).
- **Embedded Web Server:** Serves a modern HTML/CSS UI directly from the ESP32.
- **MicroPython Powered:** Clean, readable, and efficient Python code for embedded systems.
- **Responsive UI:** Optimized for both mobile and desktop browsers.

## 🛠️ Tech Stack
- **Hardware:** ESP32 DevKit V1
- **Language:** MicroPython 1.20+
- **Protocols:** IEEE 802.11 b/g/n (AP Mode), HTTP, TCP/IP Sockets

## 🔧 Installation & Setup

1. **Flash MicroPython:** Ensure your ESP32 has the latest MicroPython firmware installed.
2. **Upload Code:** Use Thonny, Ampy, or the Pymakr extension to upload `src/main.py` to your device.
3. **Connect:** - Scan for WiFi networks on your phone.
   - Connect to **esp32-iot** (Password: `12345678`).
4. **Access UI:** Open your web browser and navigate to `http://192.168.4.1`.

## 📂 Project Structure
- `src/main.py`: The core application handling WiFi AP setup and the socket server.
- `README.md`: Project documentation.

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.