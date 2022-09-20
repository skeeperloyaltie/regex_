# Write a python script called hoster-toaster.py that is used to gather information about a machine's local hostname resolution file. The details of how it works are below:

# It requires one argument on the command line:  the absolute path to a file it will write output to.
#   If the script is run with no options it will update create a summary of the data currently in /etc/hosts.  For each ip address other than the IPv4 and IPv6 localhost addresses, it will count how many hostnames are associated with that address and write the ip address, and the number of associated hostnames to the file the user provided, overwriting any data that was already there.
#   If the script is run with the option -p it will act similar to the no-option run described above, but instead of overwriting the file, 
# it will add the new data to the end of the existing file.  In oder to separate new data from old, it will write a blank line, then the current 
# date and time to the file before writing the new data.
#   If it is run with the option -m it will search the contents of /etc/hosts for the hostname provided as an argument to the -m option 
# and write a message to the provided file indicating what ip address is associated with that hostname (in addition to any other data the script is writing). 
# If the hostname is not found in /etc/hosts, a message stating it was not found will be written instead.  Note:  Completing this step is optional. 
# A submission that does not include it can be counted as complete, but will receive reduced marks.

# Note that regardless of the options used, the /etc/hosts must not be altered.
# Note that if any issues are encountered while accessing either of /etc/hosts or the file provided by the user, your script must handle them gracefully.  Giving an error message and exiting is permissable, crashing is not.
# Note that you must make use of python's file editing capabilities.  Simply re-directing output from a command into the provided file will not be accepted.

import sys 
import os 

def main():
    if len(sys.argv) == 1:
        update_hosts()
    elif sys.argv[1] == '-p':
        append_hosts()
    elif sys.argv[1] == '-m':
        search_hosts(sys.argv[2])
    else:
        print('Invalid option')
        sys.exit(1)
        
def update_hosts():
    with open('/etc/hosts', 'r') as f:
        hosts = f.read()
    hosts = hosts.split('\n')
    hosts = [x for x in hosts if x != '']
    

    

