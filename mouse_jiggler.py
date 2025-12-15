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
    
    def get_window_bounds(self):
        """Get the window bounds for random mouse movement"""
        try:
            # Force window to update geometry before getting dimensions
            self.root.update_idletasks()
            
            # Get canvas position on screen (absolute coordinates)
            canvas_x = self.canvas.winfo_rootx()
            canvas_y = self.canvas.winfo_rooty()
            
            # Get canvas dimensions
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            
            # If canvas dimensions are invalid (not yet rendered), use window dimensions
            if canvas_width <= 1 or canvas_height <= 1:
                canvas_x = self.root.winfo_rootx()
                canvas_y = self.root.winfo_rooty()
                canvas_width = self.root.winfo_width()
                canvas_height = self.root.winfo_height()
            
            # Ensure we have valid dimensions
            if canvas_width <= 1 or canvas_height <= 1:
                # Fallback: use default dimensions
                canvas_width = 200
                canvas_height = 200
            
            # Use margins to keep positions well within window bounds
            margin = 30
            
            # Calculate bounds for random positions
            min_x = canvas_x + margin
            max_x = canvas_x + canvas_width - margin
            min_y = canvas_y + margin
            max_y = canvas_y + canvas_height - margin
            
            # Ensure bounds are within screen limits
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            
            min_x = max(0, min(min_x, screen_width - 1))
            max_x = max(0, min(max_x, screen_width - 1))
            min_y = max(0, min(min_y, screen_height - 1))
            max_y = max(0, min(max_y, screen_height - 1))
            
            # Ensure we have valid range
            if max_x <= min_x:
                max_x = min_x + 50
            if max_y <= min_y:
                max_y = min_y + 50
            
            return (min_x, max_x, min_y, max_y)
        except Exception as e:
            print(f"Error getting window bounds: {e}")
            return None
    
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
        """Move the mouse to a random position within the window"""
        try:
            # Get window bounds
            bounds = self.get_window_bounds()
            
            if bounds is None:
                return
            
            min_x, max_x, min_y, max_y = bounds
            
            # Generate random position within window bounds
            target_x = random.randint(int(min_x), int(max_x))
            target_y = random.randint(int(min_y), int(max_y))
            
            # Double-check bounds before moving
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            target_x = max(0, min(target_x, screen_width - 1))
            target_y = max(0, min(target_y, screen_height - 1))
            
            # Move mouse to the random position
            pyautogui.moveTo(target_x, target_y, duration=0.1)
            # Click at the new position
            pyautogui.click(target_x, target_y)
            
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

