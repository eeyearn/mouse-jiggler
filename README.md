# Mouse Jiggler

A minimal macOS application that keeps your status active on Microsoft Teams (or other communication apps) by automatically moving your mouse when you hover over it.

## Features

- **Hover-to-activate**: Simply hover your mouse over the window to start jiggling
- **Auto-stop**: Moves your mouse away from the app and it automatically stops
- **Visual indicator**: Window changes color to show when it's active
  - Gray = Inactive
  - Green = Active (jiggling)
- **Random movement**: Mouse moves randomly within the window every 1-2 seconds
- **Adjustable size**: Resize the window to your preference
- **Minimal design**: Clean, simple interface

## Installation

1. Make sure you have Python 3 installed on your system

2. Create a virtual environment:

   **On macOS/Linux:**
   ```bash
   python3 -m venv venv
   ```

   **On Windows:**
   ```bash
   python -m venv venv
   ```
   
   Or use the Python launcher:
   ```bash
   py -m venv venv
   ```

3. Activate the virtual environment:

   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

   **On Windows (PowerShell):**
   ```powershell
   venv\Scripts\Activate.ps1
   ```

   **On Windows (Command Prompt):**
   ```cmd
   venv\Scripts\activate.bat
   ```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

**Note:** You'll need to activate the virtual environment (step 3) each time you open a new terminal session before running the application.

**Windows Troubleshooting:** If you get an error that Python was not found, try:
- Using `python` instead of `python3`
- Using `py` (Python launcher) instead
- Installing Python from [python.org](https://www.python.org/downloads/) and make sure to check "Add Python to PATH" during installation
- Disabling Windows App execution aliases: Settings > Apps > Advanced app settings > App execution aliases, then turn off Python aliases

## Usage

### Running from Terminal

Run the application:

```bash
python mouse_jiggler.py
```

Or make it executable and run directly:

```bash
chmod +x mouse_jiggler.py
./mouse_jiggler.py
```

### Creating a Desktop Shortcut (Windows)

To run the app without opening a terminal:

1. **Double-click `run_mouse_jiggler.vbs`** - This will run the app without showing a console window

2. **Create a desktop shortcut** (optional, for easier access):
   - Right-click on `run_mouse_jiggler.vbs` in File Explorer
   - Select "Create shortcut"
   - Drag the shortcut to your desktop
   - Right-click the shortcut → Properties → Change Icon (optional) to customize it

3. **Alternative: Use the batch file directly**:
   - Double-click `run_mouse_jiggler.bat` - This will show a brief console window before the app starts

### How to Use

1. Launch the application - a small window will appear
2. Position the window somewhere convenient on your screen
3. Hover your mouse over the window to activate it (turns green)
4. The mouse will automatically move randomly within the window
5. Move your mouse away from the window to stop it (turns gray)

## Requirements

- Python 3.6 or higher
- macOS, Windows, or Linux
- PyAutoGUI library

## Notes

- The window does not stay on top, so you can work normally with other applications
- Resize the window to make it larger or smaller as needed
- The mouse movements are contained within the window boundaries
- Movement intervals are randomized between 1-2 seconds for natural behavior

## Troubleshooting

**macOS:** If PyAutoGUI doesn't work, you may need to grant Accessibility permissions:

1. Go to System Settings > Privacy & Security > Accessibility
2. Add Terminal or Python to the allowed applications
3. Restart the application

**Windows:** If you encounter permission errors with PyAutoGUI, you may need to run the application as administrator or grant appropriate permissions.

## License

Free to use and modify as needed.
