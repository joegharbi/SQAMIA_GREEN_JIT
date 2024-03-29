import sys, os, time, timeit, csv, json, subprocess
from subprocess import call, check_output, Popen, PIPE

path = '.'
action = 'compile'

def file_exists(file_path):
    if not file_path:
        return False
    else:
        return os.path.isfile(file_path)

def main():
  for root, dirs, files in os.walk(path):
    print ('Checking' + root)
    makefile = os.path.join(root, "Makefile")
    if file_exists(makefile):
      cmd = 'cd ' + root + '& make ' + action
      #cmd = 'ls -la'
      start_time = timeit.default_timer()
      # pipes = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
      pipes = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      # std_out, std_err = pipes.communicate()
      end_time = timeit.default_timer()
      runtime = end_time - start_time - 10

      
      if (action == 'compile') | (action == 'run'):
        if pipes.returncode != 0:
          # an error happened!
          err_msg = "%s. Code: %s" % (pipes.stderr.strip(), pipes.returncode)
          print ('[E] Error on ' + root + ': ')
          print (err_msg)
        elif len(pipes.stderr):
          # return code is 0 (no error), but we may want to
          # do something with the info on std_err
          # i.e. logger.warning(std_err)
          print ('[OK]')
        else:
          print ('[OK]')
    if action == 'measure':
      if root != ".":
        #Get the energy from the json file 
        json_path = root
        files_in_directory = os.listdir(json_path)
        json_files = [f for f in files_in_directory if f.endswith(".json")]
        # print("json_path" , json_path)
        # print(json_files[0])
        json_file_path = os.path.join(json_path, json_files[0])

        # Read JSON data from the file
        with open(json_file_path, "r") as file:
            data = json.load(file)

        # Initialize total consumption variables
        total_server_consumption = 0.0
        number_samples = 0

        # Iterate through entries
        for entry in data:
            consumers = entry.get("consumers", [])
            for consumer in consumers:
                exe = consumer.get("exe", "")
                consumption = consumer.get("consumption", 0.0)
                
                # Check the server consumption
                if "erl.exe" in exe.lower() and consumption != 0.0:
                    total_server_consumption += consumption
                    number_samples +=1
        if number_samples != 0:
          total_consumption = total_server_consumption / number_samples
        else:
           total_consumption = 0
                

        # Multiply runtime by energy 
        final_consumption = total_consumption * runtime
                    

        # Write runtime and function name to the csv file
        with open('output.csv', 'a', newline='') as csv_file:
                      csv_writer = csv.writer(csv_file, delimiter=';')
                      # csv_writer.writerow(['Function', 'Average Runtime'])
                      csv_writer.writerow([os.path.basename(root), final_consumption, runtime])

      
      # call(['sleep', '5'])
      time.sleep(5)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    act = sys.argv[1]
    if (act == 'compile') | (act == 'run') | (act == 'clean') | (act == 'measure'):
      print ('Performing \"' + act + '\" action...')
      action = act
    else:
      print ('Error: Unrecognized action \"' + act + '\"')
      sys.exit(1)
  else:
    print ('Performing \"compile\" action...')
    action = 'compile'
  
  main()
    
