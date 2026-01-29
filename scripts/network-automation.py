#!/usr/bin/env python3
"""
Network Automation Script
For CML2/GNS3 device configuration
"""

import sys

def configure_router(hostname, interface, ip_address):
    """Generate router configuration commands."""
    config = f"""
! Configuration for {hostname}
hostname {hostname}
!
interface {interface}
 ip address {ip_address}
 no shutdown
!
end
"""
    return config

def main():
    print("Network Automation Tool")
    print("======================")
    
    # Example configuration
    router_config = configure_router(
        "AUTO-ROUTER-1",
        "GigabitEthernet0/0",
        "10.1.1.1 255.255.255.0"
    )
    
    print(router_config)
    print("Configuration generated successfully!")

if __name__ == "__main__":
    main()