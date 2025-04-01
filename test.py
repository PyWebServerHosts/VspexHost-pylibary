# example_usage.py
from vspexhost import VSPEXHOST

# Create an instance of the VSPEXHOST application
app = VSPEXHOST(host='localhost', port=8081)

@app.router.setpath(client=None, path='/')
def home():
    return "<h1>Welcome to VSPEXHOST!</h1>"

@app.router.setpath(client=None, path='/about')
def about():
    return "<h1>About VSPEXHOST</h1><p>This is a simple Python web server.</p>"


# Start the server and GUI
app.initialize_gui()
app.log_action("Messages", "Server is starting...")

# Start the server in a separate thread
import threading
threading.Thread(target=app.start, daemon=True).start()

# Run the GUI
app.run_gui()
