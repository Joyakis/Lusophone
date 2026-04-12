import sys
import urllib.request
import urllib.error
import socket

# Default path - the CSV file is in the same folder as this script
DEFAULT_CSV_PATH = "Task 2 - Intern.csv"

def fetch_status(url: str) -> int:
    """Fetches the HTTP status code of a given URL."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.getcode()

def main(csv_path: str) -> None:
    
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()

    if not lines:
        return

    header = lines[0].strip().lower()
    start_index = 1 if header in ("url", "urls") else 0

    for line in lines[start_index:]:
        url = line.strip()
        
        if not url:
            continue

        # --- ROBUST ERROR HANDLING ---
        try:
            status = fetch_status(url)
            
        except urllib.error.HTTPError as e:
            # The server was reached, but returned an error code (e.g., 404, 403)
            status = f"HTTP {e.code}"
            
        except urllib.error.URLError as e:
            # The server could not be reached (e.g., dead link, blocked connection)
            # We check if the specific reason was a network timeout
            if isinstance(e.reason, socket.timeout):
                status = "TIMEOUT"
            else:
                status = f"CONNECTION FAILED: {e.reason}"
                
        except TimeoutError:
            # Catches built-in Python timeouts
            status = "TIMEOUT"
            
        except Exception as e:
            status = f"UNEXPECTED ERROR: {type(e).__name__}"
   
        print(f"({status}) {url}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CSV_PATH
    main(path)