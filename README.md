# Nanostructure Visualization

A 3D visualization of randomly generated nanostructures using interactive WebGL graphics.

## Overview

This project generates a 3D visualization of 100 randomly colored spheres positioned in 3D space. Each time the visualization loads, a new random configuration is created, making it useful for simulating nanoparticle arrangements, molecular structures, or abstract spatial distributions.

## Files

- **visualization.html** - Standalone HTML file with embedded JavaScript visualization
- **nanostructure.py** - Original Python implementation using py3Dmol

## Usage

### Quick Start (HTML Version)
1. Open `visualization.html` in any modern web browser
2. Interact with the 3D visualization:
   - **Left Click + Drag** - Rotate the view
   - **Right Click + Drag** - Zoom in/out
   - **Scroll Wheel** - Zoom in/out

### Python Version (Jupyter)
If you have the required dependencies installed:
```bash
pip install py3Dmol
```

Then run `nanostructure.py` in a Jupyter notebook environment to display the interactive visualization.

## Features

- **100 Random Spheres** - Each sphere has a randomly assigned position and color
- **3D Interaction** - Full 3D rotation, zoom, and pan capabilities
- **Real-time Rendering** - WebGL-based visualization for smooth performance
- **Standalone** - HTML version requires no installation or dependencies

## Technical Details

### Visualization Parameters

- **Sphere Radius**: 0.3 units
- **Position Range**: ±2 units in x, y, and z axes
- **Colors**: Random RGB values (0-255)
- **Background**: White
- **View Size**: 400×400 pixels

### Libraries Used

- **3Dmol.js** - JavaScript library for molecular visualization (HTML version)
- **py3Dmol** - Python wrapper around 3Dmol.js (Python version)

## Browser Compatibility

The HTML visualization works in all modern browsers that support WebGL:
- Chrome/Chromium
- Firefox
- Safari
- Edge

## License

Open source - feel free to modify and use as needed.
