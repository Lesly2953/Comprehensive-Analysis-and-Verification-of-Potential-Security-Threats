import RunningProcess as run_proc


def main():
  print ("This is main")
  suspected_process = run_proc.info_running_process()
  print ("This are suspected process :\n" , suspected_process )

if __name__ == "__main__":
  main()