import sys
import psutil
import argparse

def find_process_by_port(port):
    """Finds the process ID (PID) and name using the specified port."""
    connections = psutil.net_connections()
    for conn in connections:
        if conn.laddr.port == port and conn.status == 'LISTEN':
            try:
                process = psutil.Process(conn.pid)
                return process
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                return None
    return None

def kill_process(process, force=False):
    """Terminates the given process."""
    try:
        name = process.name()
        pid = process.pid
        
        if not force:
            confirmation = input(f"Port is used by '{name}' (PID: {pid}). Kill it? [y/N]: ").lower()
            if confirmation != 'y':
                print("Operation cancelled.")
                return False

        process.terminate()
        process.wait(timeout=3)
        print(f"Successfully terminated '{name}' (PID: {pid}).")
        return True
    
    except psutil.AccessDenied:
        print(f"Error: Access denied. Try running as Administrator/Root.")
    except psutil.NoSuchProcess:
        print(f"Error: Process already ended.")
    except Exception as e:
        print(f"Error: {e}")
    return False

def main():
    parser = argparse.ArgumentParser(description="Kill processes locking a specific port.")
    parser.add_argument('port', type=int, help="The port number to free up")
    parser.add_argument('-f', '--force', action='store_true', help="Force kill without confirmation")
    
    args = parser.parse_args()
    
    print(f"Scanning for process on port {args.port}...")
    
    process = find_process_by_port(args.port)
    
    if process:
        kill_process(process, args.force)
    else:
        print(f"No process found listening on port {args.port}.")

if __name__ == "__main__":
    main()
