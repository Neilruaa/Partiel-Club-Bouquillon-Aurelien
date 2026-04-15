import urllib.request

def fetch_reservations(sport_type: str) -> str:
    url = f"http://notreclubdesport.fr/{sport_type}/reservation.txt"
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception:
        return ""
