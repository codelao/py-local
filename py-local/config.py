import os, subprocess
import check_connection as con


if con.check_internet_connection() == True:
    try:
        get_net_ifaces = subprocess.run(['ifconfig'], stdout=subprocess.PIPE, text=True)
        net_ifaces = get_net_ifaces.stdout
        ifaces_list = net_ifaces.split()
    except:
        if os.name == 'nt':
            raise OSError('py-local works on Unix systems only!')
        else:
            raise OSError('Can\'t get information about your network interfaces! Seems like your OS doesn\'t support \'ifconfig\' command.')
else:
    raise ConnectionError('Check your internet connection!')
