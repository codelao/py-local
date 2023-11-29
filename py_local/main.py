import subprocess
from . import config as cfg


def iface():
    possible_wifi_ifaces = ['en', 'wlan', 'eth']
    for iface in possible_wifi_ifaces:
        for i in range(10):
            if iface+str(i)+':' in cfg.ifaces_list or iface+str(i) in cfg.ifaces_list:
                return iface+str(i)
            else:
                if i+1 == 10:
                    raise OSError('No active Wi-Fi or Ethernet interfaces found!')
                else:
                    continue

def status(iface):
    if iface in cfg.ifaces_list or iface+':' in cfg.ifaces_list:
        get_iface_status = subprocess.run(['ifconfig', iface], stdout=subprocess.PIPE, text=True)
        if 'status:' in get_iface_status.stdout:
            if not 'inactive' in get_iface_status.stdout:
                return True
            else:
                return False
        elif 'inet' in get_iface_status.stdout:
            return True
        else:
            raise ValueError('Can\'t find information about interface status! Probably your network configuration doesn\'t support status parameters.')
    else:
        raise ValueError('Unknown interface provided!')
    
def ipv4():
    active_iface = iface()
    get_iface_ipv4 = subprocess.run(['ifconfig', active_iface], stdout=subprocess.PIPE, text=True)
    if 'inet' in get_iface_ipv4.stdout:
        iface_info = get_iface_ipv4.stdout.split()
        inet_ix = iface_info.index('inet')
        return iface_info[inet_ix+1]
    else:
        raise ValueError('Can\'t find IPv4 address in current active Wi-Fi or Ethernet interface!')
    
def ipv6():
    active_iface = iface()
    get_iface_ipv4 = subprocess.run(['ifconfig', active_iface], stdout=subprocess.PIPE, text=True)
    if 'inet6' in get_iface_ipv4.stdout:
        iface_info = get_iface_ipv4.stdout.split()
        inet_ix = iface_info.index('inet6')
        return iface_info[inet_ix+1]
    else:
        raise ValueError('Can\'t find IPv6 address in current active Wi-Fi or Ethernet interface!')
