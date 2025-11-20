from scapy.all import *
import psutil
import time

# ---------------------------------------------------
# LIST USER-FRIENDLY WINDOWS INTERFACES
# ---------------------------------------------------
def list_interfaces():
    print("===== AVAILABLE NETWORK INTERFACES =====")

    interfaces = []
    addrs = psutil.net_if_addrs()

    for index, iface in enumerate(addrs.keys(), 1):
        interfaces.append(iface)
        print(f"{index}. {iface}")

    print("\nSelect an interface by number (e.g., 1):")
    return interfaces

# ---------------------------------------------------
# PACKET CALLBACK
# ---------------------------------------------------
def packet_callback(packet):
    print(f"[+] Packet: {packet.summary()}")

# ---------------------------------------------------
# SNIFF FOR A FIXED TIME
# ---------------------------------------------------
def sniff_for_time(iface, duration):
    print(f"\nSniffing on: {iface} for {duration} seconds...\n")
    sniff(iface=iface, prn=packet_callback, store=False, timeout=duration)
    print("\n⏳ Time limit reached. Stopping capture...\n")

# ---------------------------------------------------
# SNIFF CONTINUOUSLY
# ---------------------------------------------------
def sniff_continuous(iface):
    print(f"\nSniffing on: {iface} (Press CTRL + C to stop)\n")
    sniff(iface=iface, prn=packet_callback, store=False)

# ---------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------
def main():
    interfaces = list_interfaces()

    choice = input("> Enter interface number: ").strip()

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(interfaces):
        print("Invalid choice. Exiting...")
        return

    iface = interfaces[int(choice) - 1]

    print("\n===== SNIFFING MODE =====")
    print("1. Set time limit")
    print("2. Continue without time limit")
    mode = input("> Enter choice (1 or 2): ").strip()

    if mode == "1":
        duration = input("Enter duration in seconds: ").strip()

        if not duration.isdigit() or int(duration) <= 0:
            print("Invalid duration. Exiting...")
            return

        sniff_for_time(iface, int(duration))

    elif mode == "2":
        sniff_continuous(iface)

    else:
        print("Invalid option. Exiting...")

# ---------------------------------------------------
if __name__ == "__main__":
    main()
