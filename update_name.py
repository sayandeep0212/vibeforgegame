import os

file_path = 'data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('"name":"3d lane runner"', '"name":"Run Ninja Run"')
content = content.replace('"string":"LANE RUNNER"', '"string":"RUN NINJA RUN"')
content = content.replace('"text":"LANE RUNNER"', '"text":"RUN NINJA RUN"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated data.js successfully.")
