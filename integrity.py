def verify_integrity(data_packet):
    return data_packet == data_packet[::-1]

if __name__ == "__main__":
    packet = input("Enter data packet: ")
    if verify_integrity(packet):
        print(f"[INTEGRITY OK]   '{packet}' is valid.")
    else:
        print(f"[INTEGRITY FAIL] '{packet}' is corrupted.")
