#!/usr/bin/env python3
"""
Mouse Jiggler - A minimal application to keep your status active
Moves the mouse randomly within the window when you hover over it
"""

import tkinter as tk
import pyautogui
import random
import time


class MouseJiggler:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Jiggler")
        self.root.geometry("200x200")
        self.root.resizable(True, True)
        
        # State
        self.is_active = False
        self.jiggle_job = None
        
        # Colors for visual indicator
        self.inactive_color = "#D3D3D3"  # Light gray
        self.active_color = "#90EE90"    # Light green
        
        # Create canvas
        self.canvas = tk.Canvas(
            self.root, 
            bg=self.inactive_color,
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Add status text
        self.status_text = self.canvas.create_text(
            100, 100,
            text="Hover to Activate",
            font=("Arial", 12),
            fill="#333333"
        )
        
        # Bind mouse enter/leave events
        self.canvas.bind("<Enter>", self.on_mouse_enter)
        self.canvas.bind("<Leave>", self.on_mouse_leave)
        
        # Bind resize event to update text position
        self.canvas.bind("<Configure>", self.on_resize)
        
        # PyAutoGUI settings
        pyautogui.FAILSAFE = False  # Disable failsafe for this specific use case
        pyautogui.PAUSE = 0.01  # Minimal pause between commands
    
    def on_resize(self, event):
        """Update text position when window is resized"""
        width = event.width
        height = event.height
        self.canvas.coords(self.status_text, width // 2, height // 2)
    
    def on_mouse_enter(self, event):
        """Called when mouse enters the window"""
        if not self.is_active:
            self.is_active = True
            self.canvas.configure(bg=self.active_color)
            self.canvas.itemconfig(self.status_text, text="Active")
            self.start_jiggling()
    
    def on_mouse_leave(self, event):
        """Called when mouse leaves the window"""
        if self.is_active:
            self.is_active = False
            self.canvas.configure(bg=self.inactive_color)
            self.canvas.itemconfig(self.status_text, text="Hover to Activate")
            self.stop_jiggling()
    
    def start_jiggling(self):
        """Start the mouse jiggling loop"""
        if self.is_active:
            self.jiggle_mouse()
            # Schedule next jiggle with random interval (1-2 seconds)
            delay = random.randint(1000, 2000)  # milliseconds
            self.jiggle_job = self.root.after(delay, self.start_jiggling)
    
    def stop_jiggling(self):
        """Stop the mouse jiggling loop"""
        if self.jiggle_job:
            self.root.after_cancel(self.jiggle_job)
            self.jiggle_job = None
    
    def jiggle_mouse(self):
        """Move the mouse randomly within the window bounds"""
        try:
            # Get window geometry
            window_x = self.root.winfo_x()
            window_y = self.root.winfo_y()
            window_width = self.canvas.winfo_width()
            window_height = self.canvas.winfo_height()
            
            # Calculate random position within window (with some margin)
            margin = 10
            target_x = window_x + random.randint(margin, max(margin + 1, window_width - margin))
            target_y = window_y + random.randint(margin, max(margin + 1, window_height - margin))
            
            # Move mouse to random position within window
            pyautogui.moveTo(target_x, target_y, duration=0.1)
            
        except Exception as e:
            print(f"Error moving mouse: {e}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    root = tk.Tk()
    app = MouseJiggler(root)
    app.run()


if __name__ == "__main__":
    main()

