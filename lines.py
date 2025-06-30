import os
files = [r"components/"+file for file in os.listdir(r"components")] + [r"helpers/"+file for file in os.listdir("helpers")] + [r"styles/"+file for file in os.listdir("styles")] + ["main.py", "app.py"] + [r"widgets/"+file for file in os.listdir(r"widgets")]
lines = 0
# print(files)
for file in files:
    if file.endswith("__pycache__"):
        continue
    # print(file)
    try:
        lines += len(open(file).readlines())
    except Exception as e:
        print("Error while reading:", file)
print(lines)
