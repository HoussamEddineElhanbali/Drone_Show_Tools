# Some scripts that I use daily when working on drone shows plus a custom 3d viewport panel that lets you run any of them with a click

- Scale_Mesh : script that scales a mesh so that its closest pair of vertices matches a target distance (ensuring the minimum safe distance between drones).
- Scale_Mesh : script that scales selected objects to a consistent preview size (so drones remain clearly visible, especially in large scenes).
- Check_Minimum_Distance : script that finds and selects the two closest vertices in a mesh (Edit Mode) to determine the minimum distance between drones.
- Connect_Vertices : script that lets you quickly connect vertices while using Circle Select. it keeps the selection order making it much faster and easier to connect large groups of vertices than Blender's default Connect Vertex Path.

- Adding more tools :
Just add another file path to "scripts_paths = ["C:\\path\\Preview_Scaler.py"]" a new button will appear in the panel automatically (No code changes needed).
Each script runs with access to "custom_value"(you can add as many as you want) the int from the panel input field to use it in a script just reference the variable name directly