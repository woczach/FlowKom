import json
import subprocess



proc = subprocess.run(["komorebic.exe", "state"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
data = json.loads(proc.stdout.decode("utf-8"))

print(json.dumps(data, indent=4))
workspaces = [m["workspaces"]['elements'] for m in data["monitors"]["elements"]]
for index, workspace in enumerate(workspaces):
    for i, w in enumerate(workspace):
        windows = [m["windows"]['elements'] for m in w["containers"]["elements"]]
        print(w)
        print(f'windows {len(windows)} on ws {i} on bigger {index}')


#print(json.dumps(workspaces, indent=4))
