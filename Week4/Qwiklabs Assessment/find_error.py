import re
def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
	  #use the search() method (present in re module) to check whether the file fishy.log has the user defined pattern and, 
	  #if it is available, append them to the list returned_errors
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors
  
def file_output(returned_errors):
  #os.path.expanduser ('~'), which returns the home directory of your system instance. 
  #Then, we'll concatenate this path (to the home directory) to the file errors_found.log in /data directory.
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)

#----Sample Input----
#./find_error.py ~/data/fishy.log
#CRON ERROR Failed to start
#----Sample Output----
#July 31 04:11:32 mycomputername CRON[51253]: ERROR: Failed to start CRON job due to script syntax error. Inform the CRON job owner!
