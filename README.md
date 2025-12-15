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

1. Make sure you have Python 3 installed on your Mac

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

**Note:** You'll need to activate the virtual environment (step 3) each time you open a new terminal session before running the application.

## Usage

Run the application:

```bash
python mouse_jiggler.py
```

Or make it executable and run directly:

```bash
chmod +x mouse_jiggler.py
./mouse_jiggler.py
```

### How to Use

1. Launch the application - a small window will appear
2. Position the window somewhere convenient on your screen
3. Hover your mouse over the window to activate it (turns green)
4. The mouse will automatically move randomly within the window
5. Move your mouse away from the window to stop it (turns gray)

## Requirements

- Python 3.6 or higher
- macOS (tested on macOS Ventura and later)
- PyAutoGUI library

## Notes

- The window does not stay on top, so you can work normally with other applications
- Resize the window to make it larger or smaller as needed
- The mouse movements are contained within the window boundaries
- Movement intervals are randomized between 1-2 seconds for natural behavior

## Troubleshooting

If PyAutoGUI doesn't work on macOS, you may need to grant Accessibility permissions:

1. Go to System Settings > Privacy & Security > Accessibility
2. Add Terminal or Python to the allowed applications
3. Restart the application

## License

Free to use and modify as needed.
