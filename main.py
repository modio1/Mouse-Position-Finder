import tkinter as tk
from tkinter import ttk
import keyboard as key
import pyautogui as pag
import time
import threading
import subprocess

class MouseTrackerApp:
    def __init__(self, master):
        self.master = master
        master.geometry("500x250")
        master.title("Modio's Multi-Tool")

        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Mouse Location Tab
        self.create_mouse_location_tab()

        # Autoclicker Tab
        self.create_autoclicker_tab()

        # Action Tab
        self.create_action_tab()

        # Update Tab
        self.create_update_tab()

        # GitHub Label
        self.github_label = tk.Label(master, text="GitHub: https://github.com/modio1", fg="blue", cursor="hand2")
        self.github_label.pack(side=tk.BOTTOM, pady=5)
        self.github_label.bind("<Button-1>", lambda e: self.open_github_link())

        # Variable to track mouse location search state
        self.searching = False
        self.saved_position = None
        self.saved_color = None
        self.stop_trig_bot_flag = False
        self.trig_bot_thread = None
        self.autoclicking = False
        self.autoclick_thread = None

    def create_mouse_location_tab(self):
        mouse_location_frame = ttk.Frame(self.notebook)
        self.notebook.add(mouse_location_frame, text="Mouse Location")

        self.position_label = tk.Label(master=mouse_location_frame, text="", bg="white")
        self.position_label.grid(row=0, column=0, padx=10)

        self.color_label = tk.Label(master=mouse_location_frame, text="", bg="white")
        self.color_label.grid(row=0, column=1, padx=10)

        self.find_btn = tk.Button(master=mouse_location_frame, text="Find Mouse Location", command=self.toggle_search)
        self.find_btn.grid(row=1, column=0, columnspan=2, pady=10)

    def create_autoclicker_tab(self):
        autoclicker_frame = ttk.Frame(self.notebook)
        self.notebook.add(autoclicker_frame, text="Autoclicker")

        self.start_autoclick_btn = tk.Button(master=autoclicker_frame, text="Start Autoclicker", command=self.start_autoclick)
        self.start_autoclick_btn.grid(row=0, column=0, pady=10)

        self.stop_autoclick_btn = tk.Button(master=autoclicker_frame, text="Stop Autoclicker", command=self.stop_autoclick, state=tk.DISABLED)
        self.stop_autoclick_btn.grid(row=0, column=1, pady=10)

    def create_action_tab(self):
        action_frame = ttk.Frame(self.notebook)
        self.notebook.add(action_frame, text="Action")

        self.start_trig_btn = tk.Button(master=action_frame, text="Start Trig Bot", command=self.start_trig_bot)
        self.start_trig_btn.grid(row=0, column=0, pady=10)

        self.stop_trig_btn = tk.Button(master=action_frame, text="Stop Trig Bot", command=self.stop_trig_bot, state=tk.DISABLED)
        self.stop_trig_btn.grid(row=0, column=1, pady=10)

    def create_update_tab(self):
        update_frame = ttk.Frame(self.notebook)
        self.notebook.add(update_frame, text="Update")

        self.update_btn = tk.Button(master=update_frame, text="Under Construction", command=self.update_from_github)
        self.update_btn.grid(row=0, column=0, pady=10)

    def toggle_search(self):
        self.searching = not self.searching
        if self.searching:
            threading.Thread(target=self.find_location_async).start()

    def find_location_async(self):
        try:
            while self.searching:
                x, y, color = self.get_mouse_info()
                self.update_labels(x, y, color)
                self.saved_position = (x, y)
                self.saved_color = color
                time.sleep(0.1)
        except Exception as e:
            print(f"Error: {e}")

    def get_mouse_info(self):
        position = pag.position()
        x, y = position
        color = self.get_pixel_color(x, y)
        return x, y, color

    def get_pixel_color(self, x, y):
        screenshot = pag.screenshot()
        pixel_color = screenshot.getpixel((x, y))
        return pixel_color

    def update_labels(self, x, y, color):
        color_string = "#{:02X}{:02X}{:02X}".format(*color)
        self.position_label.config(text=f"Position: {x}, {y}")
        self.color_label.config(text=f"Color: {color}", bg=color_string)

# sets the hotkey for the auto-clicker, feel free to change it.
    def autoclick(self):
        while self.autoclicking:
            if key.is_pressed("r"):
                pag.click()
                time.sleep(.01)

    def start_autoclick(self):
        self.autoclicking = True
        self.autoclick_thread = threading.Thread(target=self.autoclick)
        self.autoclick_thread.start()
        self.autoclick_thread1 = threading.Thread(target=self.autoclick)
        self.autoclick_thread1.start()
        self.autoclick_thread2 = threading.Thread(target=self.autoclick)
        self.autoclick_thread2.start()
        self.autoclick_thread3 = threading.Thread(target=self.autoclick)
        self.autoclick_thread3.start()
        self.start_autoclick_btn.config(state=tk.DISABLED)
        self.stop_autoclick_btn.config(state=tk.NORMAL)

    def stop_autoclick(self):
        self.autoclicking = False
        if self.autoclick_thread and self.autoclick_thread.is_alive() and self.autoclick_thread1 and self.autoclick_thread2 and self.autoclick_thread3:
            self.autoclick_thread.join()

        self.start_autoclick_btn.config(state=tk.NORMAL)
        self.stop_autoclick_btn.config(state=tk.DISABLED)

    def start_trig_bot(self):
        self.trig_bot_thread = threading.Thread(target=self.run_trig_bot)
        self.trig_bot_thread.start()
        self.start_trig_btn.config(state=tk.DISABLED)
        self.stop_trig_btn.config(state=tk.NORMAL)

    def stop_trig_bot(self):
        self.stop_trig_bot_flag = True
        self.start_trig_btn.config(state=tk.NORMAL)
        self.stop_trig_btn.config(state=tk.DISABLED)

    def run_trig_bot(self):
        self.stop_trig_bot_flag = False
        while not key.is_pressed("space") and not self.stop_trig_bot_flag:
            if self.saved_position is not None and self.saved_color is not None:
                x, y = self.saved_position
                color_at_saved_position = self.get_pixel_color(x, y)

                if color_at_saved_position == self.saved_color:
                    # Placeholder code; replace with your logic for trig_bot
                    print(f"Performing trig_bot action at position {x}, {y} with color {self.saved_color}")
                    pag.click(x, y)

            time.sleep(0.1)

        # Reset the state after trig_bot thread finishes
        self.start_trig_btn.config(state=tk.NORMAL)
        self.stop_trig_btn.config(state=tk.DISABLED)
        self.trig_bot_thread = None

    def update_from_github(self):
        try:
            # Use the 'git' command to fetch the latest changes
            subprocess.run(["git", "pull"])

            # Display a message or take additional update steps if needed
            print("Update successful. Please restart the application.")
        except Exception as e:
            print(f"Error during update: {e}")

    def open_github_link(self):
        import webbrowser
        webbrowser.open("https://github.com/modio1")

if __name__ == "__main__":
    app = tk.Tk()
    mouse_tracker_app = MouseTrackerApp(app)
    app.mainloop()

