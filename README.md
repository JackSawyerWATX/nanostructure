# Nanostructure Visualization

A collection of 3D molecular and nanostructure visualizations using interactive WebGL graphics. Explore random nanoparticles, complex carbohydrates, and other molecular structures in an interactive 3D environment.

## Overview

This project provides multiple visualization tools:

1. **Random Nanostructure Visualization** - 100 randomly colored spheres positioned in 3D space, useful for simulating nanoparticle arrangements
2. **Polysaccharide Molecular Viewer** - Interactive visualizations of complex carbohydrates including glucose, starch, cellulose, and glycogen with accurate atomic structures

## Files

- **visualization.html** - Random nanoparticle visualization with 100 spheres
- **polysaccharide.html** - Interactive molecular viewer for complex carbohydrates
- **nanostructure.py** - Original Python implementation using py3Dmol
- **README.md** - This file

## Usage

### Quick Start

Simply open either HTML file in any modern web browser - no installation required!

#### Random Nanostructure (visualization.html)
1. Open `visualization.html` in your browser
2. Interact with the visualization:
   - **Left Click + Drag** - Rotate the view
   - **Right Click + Drag** - Pan the view
   - **Scroll Wheel** - Zoom in/out

#### Polysaccharide Viewer (polysaccharide.html)
1. Open `polysaccharide.html` in your browser
2. Use the buttons to select different molecular structures:
   - **Single Glucose** - Shows C₆H₁₂O₆ monosaccharide ring
   - **Starch Chain** - Linear polymer with α-glycosidic bonds
   - **Cellulose Chain** - Glucose polymer with β-glycosidic bonds (different 3D arrangement)
   - **Glycogen (Branched)** - Branched polymer for energy storage
3. Interact with the same mouse controls as above

### Python Version (Jupyter)

If you have the required dependencies installed:
```bash
pip install py3Dmol
```

Then run `nanostructure.py` in a Jupyter notebook environment to display the interactive visualization.

## Features

### Random Nanostructure Viewer
- **100 Random Spheres** - Each with randomly assigned position and color
- **3D Interaction** - Full rotation, zoom, and pan capabilities
- **Real-time Rendering** - WebGL-based visualization for smooth performance
- **Standalone** - Requires no installation or dependencies

### Polysaccharide Molecular Viewer
- **Accurate Atomic Radii** - Uses van der Waals radii for atoms (C, H, O)
- **Multiple Structures** - View different polysaccharide types with one click
- **Atom Legend** - Color-coded atoms with size information
- **Educational Information** - Built-in explanations of polysaccharide structures and functions
- **Centered Display** - Models automatically centered in the viewer window

## Technical Details

### Atom Properties (Polysaccharide Viewer)

| Atom | Color | Radius | Usage |
|------|-------|--------|-------|
| Carbon (C) | Gray | 1.70 Å | Core structure |
| Hydrogen (H) | White | 1.20 Å | Bonding |
| Oxygen (O) | Red | 1.52 Å | Functional groups |

### Visualization Parameters

**Random Nanostructure:**
- Number of spheres: 100
- Sphere radius: 0.3 units
- Position range: ±2 units in each axis
- View size: 400×400 pixels

**Polysaccharide Structures:**
- Scale: 1 Ångström ≈ 0.1 nm
- Elements: C, H, O atoms with relative van der Waals radii
- Structures: Single unit, linear chains, and branched polymers

### Libraries Used

- **3Dmol.js** - JavaScript library for molecular visualization (CDN-hosted)
- **py3Dmol** - Python wrapper around 3Dmol.js (Python version)

## Browser Compatibility

Both HTML visualizations work in all modern browsers that support WebGL:
- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## About Polysaccharides

Polysaccharides are complex carbohydrates composed of multiple glucose units linked together:

- **Starch** - Plant energy storage with α-1,4 and α-1,6 glycosidic bonds
- **Cellulose** - Plant structural component with β-1,4 glycosidic bonds
- **Glycogen** - Animal energy storage, highly branched similar to starch
- **Chitin** - Insect exoskeletons and fungal cell walls (N-acetyl glucose polymer)

All are polymers of glucose (C₆H₁₂O₆)ₙ with different bonding patterns and structures.

## License

Open source - feel free to modify and use as needed.
