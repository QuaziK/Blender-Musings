import bpy

import os

bl_info = {
    "name": "Auto Save Render",
    "author": "quazik",
    "version": (1, 0),
    "blender": (4, 4, 3),
    "location": "Properties > Render",
    "description": "Automatically saves renders with unique names",
    "category": "Render",
}

def get_output_path():
# Fetch the output path from Blender's render settings
    render_path = bpy.context.scene.render.filepath
    base_path = bpy.path.abspath(render_path)
    directory, base_name = os.path.split(base_path)
# Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
# Append an incremented suffix to make the file name unique
    i = 1
    while os.path.exists(f"{directory}/{base_name}_{i:03d}.png"):
        i += 1
    return f"{directory}/{base_name}_{i:03d}.png"

def auto_save_render(scene, context):
    image_path = get_output_path()
    
    bpy.data.images['Render Result'].save_render(filepath=image_path)
    
    print(f"Saved: {image_path}")

def register():
    bpy.app.handlers.render_complete.append(auto_save_render)

def unregister():
    bpy.app.handlers.render_complete.remove(auto_save_render)

if __name__ == "__main__":
    register()