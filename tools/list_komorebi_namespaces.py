import json
import subprocess



proc = subprocess.run(["komorebic.exe", "state"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
data = json.loads(proc.stdout.decode("utf-8"))
print(data)
