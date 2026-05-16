import csv
import json
import socket
import subprocess
import sys
import threading
import time
import timeit

from paths import GENERATED_DIR, RAW_RESULTS_DIR


def communicate_with_erlang_server(message, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as erlang_socket:
        erlang_socket.connect((host, port))
        erlang_socket.sendall(message.encode())
        erlang_socket.recv(1024).decode()
        erlang_socket.close


def erlang_client_thread(message, host, port_erlang):
    communicate_with_erlang_server(message, host, port_erlang)


if __name__ == "__main__":
    message = "Hello, Servers!"
    host = "localhost"
    num_clients = 4000
    server_name = "erl"
    file_name = f"report_{server_name}_{num_clients}"
    json_file_path = GENERATED_DIR / f"{file_name}.json"

    erl_server_command = "erl -noshell -run echo_server_prod"
    subprocess.Popen(erl_server_command, shell=True)
    time.sleep(5)

    command = f'scaphandre json -n 100000 -f "{json_file_path}"'
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
    time.sleep(5)

    port_erlang = 12345
    erlang_threads = []
    start_time = timeit.default_timer()

    for _ in range(1, num_clients + 1):
        erlang_thread = threading.Thread(target=erlang_client_thread, args=(message, host, port_erlang))
        erlang_threads.append(erlang_thread)
        erlang_thread.start()
        time.sleep(0.1)

    for erlang_thread in erlang_threads:
        erlang_thread.join()

    end_time = timeit.default_timer()
    runtime = end_time - start_time - (num_clients * 0.1)

    subprocess.run('taskkill /F /IM scaphandre.exe', shell=True)
    subprocess.run('taskkill /F /IM erl.exe', shell=True)

    with json_file_path.open('r') as file_handle:
        data = json.load(file_handle)

    total_server_consumption = 0.0
    number_samples = 0
    average_energy = 0

    for entry in data:
        consumers = entry.get('consumers', [])
        for consumer in consumers:
            exe = consumer.get('exe', '')
            consumption = consumer.get('consumption', 0.0)
            if f'{server_name}.exe' in exe.lower():
                total_server_consumption += consumption
                number_samples += 1

    if number_samples != 0:
        average_energy = total_server_consumption / number_samples

    final_consumption = average_energy * runtime
    output_file = RAW_RESULTS_DIR / 'erlang_output.csv'
    with output_file.open('a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerow([file_name, final_consumption, runtime])

    sys.exit()
