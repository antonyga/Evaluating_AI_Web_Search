import tkinter as tk
from pynput import mouse
import time
import threading

class SimpleTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Timer")
        
        self.is_listening = False
        self.start_time = None
        self.listener = None
        self.click_count = 0
        
        self.label = tk.Label(root, text="Click 'Get Ready' to start", font=('Arial', 14))
        self.label.pack(pady=20)
        
        self.ready_btn = tk.Button(root, text="Get Ready", command=self.prepare_timer)
        self.ready_btn.pack(pady=10)
        
        self.quit_btn = tk.Button(root, text="Quit", command=root.quit)
        self.quit_btn.pack(pady=10)

    def prepare_timer(self):
        self.ready_btn.config(state=tk.DISABLED)
        self.label.config(text="Click anywhere to start timing...")
        self.click_count = 0
        self.start_listener()

    def start_listener(self):
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.click_count += 1
            
            if self.click_count == 1:
                self.start_time = time.time()
                self.label.config(text="Timing... Click again to stop!")
                self.root.attributes('-topmost', True)  # Bring window to front
                self.root.attributes('-topmost', False)  # Allow other windows to stay on top
                
            elif self.click_count == 2:
                elapsed = time.time() - self.start_time
                self.label.config(text=f"Time elapsed: {elapsed:.2f} seconds")
                self.ready_btn.config(state=tk.NORMAL)
                self.listener.stop()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    timer = SimpleTimer(root)
    timer.run()