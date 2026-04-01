import sys
import urllib.request
import urllib.error
import socket

# Default path - the CSV file is in the same folder as this script
DEFAULT_CSV_PATH = "Task 2 - Intern.csv"
# We define a new file to  hold  detailed error messages
ERROR_LOG_PATH = "error_details.log" 

def fetch_status(url: str) -> int:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}, 
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.getcode()

def main(csv_path: str) -> None:
    # Read the file with the BOM fix to ignore invisible characters
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()

    if not lines:
        return

    header = lines[0].strip().lower()
    start_index = 1 if "url" in header else 0

    # Open the log file to write detailed errors
    with open(ERROR_LOG_PATH, "w", encoding="utf-8") as log_file:
        log_file.write("Detailed Error Log:\n" + "-"*20 + "\n")

        for line in lines[start_index:]:
            url = line.strip()
            
            if not url:
                continue

            try:
                status = fetch_status(url)
                
            except urllib.error.HTTPError as e:
                # The server was reached, but returned an error code (e.g., 404, 403)
                status = e.code
                
            except urllib.error.URLError as e:
                # Check if the specific reason was a network timeout or some other connection issue
                if isinstance(e.reason, socket.timeout):
                    detail = "TIMEOUT"
                else:
                    detail = f"CONNECTION FAILED: {e.reason}"
                
                # 1. Write the detailed reason to our log file for reference
                log_file.write(f"[{detail}] -> {url}\n")
                # 2. Set the status to "ERROR" for the main output, while the log contains the specific reason
                status = "ERROR"
                
            except TimeoutError:
                log_file.write(f"[TIMEOUT] -> {url}\n")
                status = "ERROR"
                
            except Exception as e:
                log_file.write(f"[UNEXPECTED ERROR: {type(e).__name__}] -> {url}\n")
                status = "ERROR"

            # The main terminal output remains strictly (CODE) URL
            print(f"({status}) {url}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CSV_PATH
    main(path)