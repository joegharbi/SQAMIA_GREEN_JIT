import json

from paths import GENERATED_DIR


total_server_consumption = 0.0
total_erl_consumption = 0.0

for json_file_path in GENERATED_DIR.glob('*.json'):
    with json_file_path.open('r') as file_handle:
        data = json.load(file_handle)

    for entry in data:
        consumers = entry.get('consumers', [])
        for consumer in consumers:
            exe = consumer.get('exe', '')
            consumption = consumer.get('consumption', 0.0)
            if 'server_old.exe' in exe.lower():
                total_server_consumption += consumption
            elif 'erl.exe' in exe.lower():
                total_erl_consumption += consumption

print('Total consumption of server_old.exe:', total_server_consumption)
print('Total consumption of erl.exe:', total_erl_consumption)
