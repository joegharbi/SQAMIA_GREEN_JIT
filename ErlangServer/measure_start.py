import json
import subprocess
import sys
import time

from paths import GENERATED_DIR

if __name__ == "__main__":
    num_clients = 10
    server_name = "erl"
    file_name = f"report_{server_name}_{num_clients}"
    json_file_path = GENERATED_DIR / f"{file_name}.json"
    report_file = GENERATED_DIR / f"{file_name}.txt"

    command = f'scaphandre json -n 100000 -f "{json_file_path}"'
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
    time.sleep(5)

    start_time = time.time()
    end_time = time.time()
    runtime = end_time - start_time

    subprocess.run('taskkill /F /IM scaphandre.exe', shell=True)

    with json_file_path.open('r') as file_handle:
        data = json.load(file_handle)

    total_server_consumption = 0.0
    number_samples = 0
    for entry in data:
        consumers = entry.get('consumers', [])
        for consumer in consumers:
            exe = consumer.get('exe', '')
            consumption = consumer.get('consumption', 0.0)
            if f'{server_name}.exe' in exe.lower() and consumption != 0.0:
                total_server_consumption += consumption
                number_samples += 1

    with report_file.open('w') as file_handle:
        file_handle.write(f'The runtime of {file_name} is: {runtime} seconds\n')
        file_handle.write(f'Total consumption of {server_name}: {total_server_consumption}\n')
        file_handle.write(f'Total samples of {server_name}: {number_samples}\n')

    sys.exit()
