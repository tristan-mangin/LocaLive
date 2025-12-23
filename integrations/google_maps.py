"""Simple Google Maps / Geocoding helpers.

This module prefers the `googlemaps` client if available, otherwise it
falls back to a minimal HTTP call using `requests`.

Functions provided:
- geocode_address(address) -> (lat, lng) or None
"""
from typing import Optional, Tuple
from decouple import config


GOOGLE_MAPS_API_KEY = config("GOOGLE_MAPS_API_KEY", default="")


def _client_available() -> bool:
    try:
        import googlemaps  # type: ignore

        return True
    except Exception:
        return False


def geocode_address(address: str) -> Optional[Tuple[float, float]]:
    """Return (lat, lng) for the given address or None on failure.

    This is a thin wrapper safe to call during scraping. It never raises
    on missing API key; it returns None instead.
    """
    if not GOOGLE_MAPS_API_KEY:
        return None

    # Prefer official client when available
    if _client_available():
        import googlemaps  # type: ignore

        client = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
        try:
            results = client.geocode(address)
        except Exception:
            return None
        if not results:
            return None
        loc = results[0]["geometry"]["location"]
        return loc.get("lat"), loc.get("lng")

    # Fallback: use requests to call Google Geocoding API
    try:
        import requests
    except Exception:
        return None

    params = {"address": address, "key": GOOGLE_MAPS_API_KEY}
    try:
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
    except Exception:
        return None

    if not data or data.get("status") != "OK":
        return None
    results = data.get("results", [])
    if not results:
        return None
    loc = results[0]["geometry"]["location"]
    return loc.get("lat"), loc.get("lng")
