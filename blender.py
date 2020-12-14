import bpy
import os
import time
import sys
# # add scripts dir
script_dirs = ["D:/Blender/BlenderScripts","D:/Blender/BlenderScripts/domino",
               "D:/Blender/BlenderScripts/domino/shapes","D:/Blender/BlenderScripts/domino/utils"
               "D:/GoPath/src/taro.117/gospyc/pyc"]
for script_dir in script_dirs:
    if script_dir not in sys.path:
        sys.path.append(script_dir)
main_dir = "D:/GoPath/src/taro.117/gospyc"

print('\n\n\n')
start_time = time.time()
filename = os.path.join(main_dir, "pyc/main.py")
exec(compile(open(filename).read(), filename, 'exec'))

end_time = time.time()
print("\nblender used all time: %f" % (end_time - start_time))