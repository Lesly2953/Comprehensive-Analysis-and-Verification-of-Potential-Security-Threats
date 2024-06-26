import RunningProcess as run_proc
import NetworkDetails as net_det


def main():
  #print ("This is main")
  dump_file = open("main_memory_dump.dmp","w")
  suspected_process = run_proc.info_running_process()
  network_details=[]
  for proc in suspected_process:
    t = []
    t.append(proc[0]);
    t.append(proc[1]);
    t.append(net_det.get_network_details(proc[0]));
    network_details.append(t)
  print(network_details)

if __name__ == "__main__":
  main()