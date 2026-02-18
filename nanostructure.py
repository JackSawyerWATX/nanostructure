import py3Dmol, random

v = py3Dmol.view(width=400, height=400)

for _ in range(100):
  v.addSphere({
    "center":{
      "x":random.uniform(-2,2),
      "y":random.uniform(-2,2),
      "z":random.uniform(-2,2),
    },
    "radius":0.3,
    "color":f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})",
  })
v.setBackgroundColor("white")
v.zoomTo(); v