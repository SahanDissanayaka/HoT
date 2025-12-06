import os
import shutil

# Clear Python cache
for root, dirs, files in os.walk('.'):
    if '__pycache__' in dirs:
        shutil.rmtree(os.path.join(root, '__pycache__'))
        print(f"Removed {os.path.join(root, '__pycache__')}")
    for file in files:
        if file.endswith('.pyc'):
            os.remove(os.path.join(root, file))
            print(f"Removed {os.path.join(root, file)}")

print("Cache cleared!")
