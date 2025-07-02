from tkinter import *
import time

from tkinter import Tk, Label

def smile_widget(parent):
    window = Toplevel(parent)
    window.overrideredirect(True)  # No window borders
    # window.attributes("-topmost", True)  # Always on top
    window.configure(bg='black')  # Background color
    window.wm_attributes('-transparentcolor', 'black')  # Makes black transparent

# Create the smile

    smile = Label(window, text= "^_^", font=('Courier New', 40), fg="#D3D3D3", bg='black')
    smile.pack()

    smile_width = 160  # Rough guess (adjust if needed) was 160 n below was 70
    smile_height = 70

    window.geometry(f"+{700}+{250}") #640, 150 work well for 24h time

    
def clock_widget(parent):
    window = Toplevel(parent)
    window.overrideredirect(True)  # No window borders
    # window.attributes("-topmost", True)  # Always on top
    window.configure(bg='black')  # Background color
    window.wm_attributes('-transparentcolor', 'black')  # Makes black transparent

    # Create the clock label
    clock = Label(window, font=('Courier New', 60), fg="#D3D3D3", bg='black')
    clock.pack()

    # Function to update time every minute
    def update_time():
        current_time = time.strftime("%I:%M <%p>") #can change this to make look better
        clock.config(text=current_time)
        window.after(60000, update_time)

    update_time()

# ------------------------
# Position window safely
# ------------------------
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

# Estimate clock width and height
    clock_width = 160  # Rough guess (adjust if needed) was 160 n below was 70
    clock_height = 70

# Choose margin from edge
    margin_x = 10
    margin_y = 10

# Final position
    x = screen_width - clock_width - margin_x
    y = margin_y

# Apply new position
    window.geometry(f"+{550}+{150}") #640, 150 work well for 24h time

    window.mainloop()
    



root = Tk()
root.geometry("250x250")  # Just to see something in the main window

# Button to open the clock widget
Button(root, text="Open Clock Widget", command= lambda: clock_widget(root)).pack(pady=20)
Button(root, text="Open smile Widget", command= lambda: smile_widget(root)).pack(pady=20)
Button(root, text="Close this window", command=root.withdraw).pack(pady=20)

root.mainloop()




