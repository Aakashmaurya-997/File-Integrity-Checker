import hashlib
import os

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as file:
        while chunk := file.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def monitor_files(directory):
    file_hashes = {}
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            file_hashes[path] = calculate_hash(path)

    print("Monitoring files for changes...\nPress Ctrl+C to exit.")
    try:
        while True:
            for path, old_hash in file_hashes.items():
                if not os.path.exists(path):
                    print(f"[ALERT] File deleted: {path}")
                else:
                    new_hash = calculate_hash(path)
                    if new_hash != old_hash:
                        print(f"[ALERT] File changed: {path}")
                        file_hashes[path] = new_hash
    except KeyboardInterrupt:
        print("\nStopped monitoring.")

if __name__ == "__main__":
    folder_to_monitor = input("Enter the folder path to monitor: ")
    monitor_files(folder_to_monitor)