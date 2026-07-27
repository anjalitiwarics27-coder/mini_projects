
"""
Public API Data Fetcher (Polished Edition)
--------------------------------------------
Fetches and displays data from free public APIs — no API key required:
  1. Weather        (Open-Meteo)
  2. Random Joke     (Official Joke API)
  3. Random Quote    (Quotable)
  4. Random Advice    (Advice Slip API)

Requires: requests  ->  pip install requests
Run:      python api_fetcher.py
"""

import sys
import time
import requests


# ---------------------------------------------------------------------------
# TERMINAL COLORS (ANSI escape codes — work on macOS/Linux and modern Windows
# terminals; degrade gracefully to plain text on very old consoles)
# ---------------------------------------------------------------------------

class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"


def enable_windows_ansi():
    """Enable ANSI escape sequences on older Windows terminals."""
    if sys.platform == "win32":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass  # Fails silently on unsupported systems; colors just won't show


def c(text, color):
    """Wrap text in a color code."""
    return f"{color}{text}{Color.RESET}"


# ---------------------------------------------------------------------------
# SHARED HELPERS
# ---------------------------------------------------------------------------

REQUEST_TIMEOUT = 10  # seconds
MAX_RETRIES = 2


def print_header(title, width=48):
    print("\n" + c("═" * width, Color.CYAN))
    print(c(title.center(width), Color.BOLD + Color.CYAN))
    print(c("═" * width, Color.CYAN))


def print_divider(width=48):
    print(c("─" * width, Color.DIM))


def show_spinner(message, duration=0.6):
    """Simple loading indicator so the app feels responsive during network calls."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{c(frames[i % len(frames)], Color.BLUE)} {message}", end="", flush=True)
        time.sleep(0.08)
        i += 1
    print("\r" + " " * (len(message) + 4) + "\r", end="", flush=True)


def request_with_retries(url, params=None):
    """GET a URL with basic retry logic for transient network hiccups."""
    last_error = None
    for attempt in range(1, MAX_RETRIES + 2):
        try:
            response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            return response
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            last_error = e
            if attempt <= MAX_RETRIES:
                show_spinner(f"Retrying ({attempt}/{MAX_RETRIES})...", duration=0.8)
            continue
        except requests.exceptions.HTTPError:
            raise  # No point retrying a genuine HTTP error (404, 500, etc.)
    raise last_error


# ---------------------------------------------------------------------------
# 1. WEATHER
# ---------------------------------------------------------------------------

WEATHER_CODES = {
    0: ("Clear sky", "☀️"), 1: ("Mainly clear", "🌤️"), 2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"), 45: ("Fog", "🌫️"), 48: ("Depositing rime fog", "🌫️"),
    51: ("Light drizzle", "🌦️"), 53: ("Moderate drizzle", "🌦️"), 55: ("Dense drizzle", "🌧️"),
    61: ("Slight rain", "🌧️"), 63: ("Moderate rain", "🌧️"), 65: ("Heavy rain", "🌧️"),
    71: ("Slight snow fall", "🌨️"), 73: ("Moderate snow fall", "🌨️"), 75: ("Heavy snow fall", "❄️"),
    80: ("Slight rain showers", "🌦️"), 81: ("Moderate rain showers", "🌧️"), 82: ("Violent rain showers", "⛈️"),
    95: ("Thunderstorm", "⛈️"), 96: ("Thunderstorm with slight hail", "⛈️"), 99: ("Thunderstorm with heavy hail", "⛈️"),
}


def get_coordinates(city_name):
    """Convert a city name into latitude/longitude via Open-Meteo geocoding."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    response = request_with_retries(url, params={"name": city_name, "count": 1})
    data = response.json()

    results = data.get("results")
    if not results:
        return None

    place = results[0]
    return {
        "name": place.get("name"),
        "country": place.get("country"),
        "latitude": place.get("latitude"),
        "longitude": place.get("longitude"),
    }


def fetch_weather(city_name):
    """Fetch current weather for a given city and return a parsed dict."""
    location = get_coordinates(city_name)
    if location is None:
        return None

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current_weather": True,
    }
    response = request_with_retries(url, params=params)
    data = response.json()

    current = data.get("current_weather", {})
    code = current.get("weathercode")
    description, emoji = WEATHER_CODES.get(code, ("Unknown", "❓"))

    return {
        "city": location["name"],
        "country": location["country"],
        "temperature_c": current.get("temperature"),
        "windspeed_kmh": current.get("windspeed"),
        "description": description,
        "emoji": emoji,
    }


def print_row(label, value, value_color=None):
    """Print a padded 'label: value' row, coloring only after padding so ANSI
    codes (which are invisible but count as characters) don't break alignment."""
    padded_label = c(f"{label:<14}", Color.BOLD)
    if value_color:
        value = c(str(value), value_color)
    print(f"  {padded_label}{value}")


def display_weather(weather):
    print_header(f"{weather['emoji']}  CURRENT WEATHER")
    print_row("Location", f"{weather['city']}, {weather['country']}")
    print_row("Condition", weather["description"])
    print_row("Temperature", f"{weather['temperature_c']} °C", Color.YELLOW)
    print_row("Wind Speed", f"{weather['windspeed_kmh']} km/h")
    print_divider()


def handle_weather():
    city = input(c("\nEnter city name: ", Color.CYAN)).strip()
    if not city:
        print(c("City name cannot be empty.", Color.RED))
        return
    try:
        show_spinner(f"Looking up weather for {city}...")
        weather = fetch_weather(city)
        if weather is None:
            print(c(f"\nCould not find a location named '{city}'. "
                     f"Check the spelling and try again.", Color.RED))
        else:
            display_weather(weather)
    except requests.exceptions.Timeout:
        print(c("\nError: The request timed out. Please try again.", Color.RED))
    except requests.exceptions.ConnectionError:
        print(c("\nError: Could not connect to the weather service. "
                 "Check your internet connection.", Color.RED))
    except requests.exceptions.HTTPError as e:
        print(c(f"\nError: The weather service returned an error ({e}).", Color.RED))
    except (KeyError, ValueError):
        print(c("\nError: Received an unexpected response format.", Color.RED))


# ---------------------------------------------------------------------------
# 2. JOKE
# ---------------------------------------------------------------------------

def fetch_joke():
    """Fetch a random joke from the Official Joke API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = request_with_retries(url)
    data = response.json()
    return {
        "setup": data.get("setup"),
        "punchline": data.get("punchline"),
        "type": data.get("type"),
    }


def display_joke(joke):
    print_header(f"😄  RANDOM JOKE  ·  {joke['type'].title()}")
    print(f"  {c('Q:', Color.BOLD + Color.GREEN)} {joke['setup']}")
    print(f"  {c('A:', Color.BOLD + Color.MAGENTA)} {joke['punchline']}")
    print_divider()


def handle_joke():
    try:
        show_spinner("Fetching a joke...")
        joke = fetch_joke()
        display_joke(joke)
    except requests.exceptions.Timeout:
        print(c("\nError: The request timed out. Please try again.", Color.RED))
    except requests.exceptions.ConnectionError:
        print(c("\nError: Could not connect to the joke service. "
                 "Check your internet connection.", Color.RED))
    except requests.exceptions.HTTPError as e:
        print(c(f"\nError: The joke service returned an error ({e}).", Color.RED))
    except (KeyError, ValueError):
        print(c("\nError: Received an unexpected response format.", Color.RED))


# ---------------------------------------------------------------------------
# 3. QUOTE
# ---------------------------------------------------------------------------

def fetch_quote():
    """Fetch a random inspirational quote from the Quotable API."""
    url = "https://api.quotable.io/random"
    response = request_with_retries(url)
    data = response.json()
    return {
        "content": data.get("content"),
        "author": data.get("author"),
    }


def display_quote(quote):
    print_header("💬  RANDOM QUOTE")
    print(f'  "{c(quote["content"], Color.YELLOW)}"')
    print(f"  {c('—', Color.DIM)} {c(quote['author'], Color.BOLD)}")
    print_divider()


def handle_quote():
    try:
        show_spinner("Fetching a quote...")
        quote = fetch_quote()
        display_quote(quote)
    except requests.exceptions.Timeout:
        print(c("\nError: The request timed out. Please try again.", Color.RED))
    except requests.exceptions.ConnectionError:
        print(c("\nError: Could not connect to the quote service. "
                 "Check your internet connection.", Color.RED))
    except requests.exceptions.HTTPError as e:
        print(c(f"\nError: The quote service returned an error ({e}).", Color.RED))
    except (KeyError, ValueError):
        print(c("\nError: Received an unexpected response format.", Color.RED))


# ---------------------------------------------------------------------------
# 4. ADVICE
# ---------------------------------------------------------------------------

def fetch_advice():
    """Fetch a random piece of advice from the Advice Slip API."""
    url = "https://api.adviceslip.com/advice"
    response = request_with_retries(url)
    data = response.json()
    return data.get("slip", {}).get("advice")


def display_advice(advice_text):
    print_header("🧠  RANDOM ADVICE")
    print(f"  {c(advice_text, Color.GREEN)}")
    print_divider()


def handle_advice():
    try:
        show_spinner("Fetching advice...")
        advice_text = fetch_advice()
        if not advice_text:
            print(c("\nNo advice returned this time. Try again.", Color.RED))
        else:
            display_advice(advice_text)
    except requests.exceptions.Timeout:
        print(c("\nError: The request timed out. Please try again.", Color.RED))
    except requests.exceptions.ConnectionError:
        print(c("\nError: Could not connect to the advice service. "
                 "Check your internet connection.", Color.RED))
    except requests.exceptions.HTTPError as e:
        print(c(f"\nError: The advice service returned an error ({e}).", Color.RED))
    except (KeyError, ValueError):
        print(c("\nError: Received an unexpected response format.", Color.RED))


# ---------------------------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------------------------

MENU_ACTIONS = {
    "1": ("Get current weather for a city", handle_weather),
    "2": ("Get a random joke", handle_joke),
    "3": ("Get a random quote", handle_quote),
    "4": ("Get a random piece of advice", handle_advice),
}


def print_menu():
    print()
    for key, (label, _) in MENU_ACTIONS.items():
        print(f"  {c(key, Color.BOLD + Color.CYAN)}. {label}")
    print(f"  {c('5', Color.BOLD + Color.CYAN)}. Exit")


def main():
    enable_windows_ansi()
    print_header("🌐  PUBLIC API DATA FETCHER")

    while True:
        print_menu()
        choice = input(c("\nEnter choice (1-5): ", Color.CYAN)).strip()

        if choice in MENU_ACTIONS:
            _, action = MENU_ACTIONS[choice]
            action()
        elif choice == "5":
            print(c("\nGoodbye! 👋\n", Color.GREEN))
            break
        else:
            print(c("\nInvalid choice. Please enter a number between 1 and 5.", Color.RED))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(c("\n\nInterrupted. Goodbye! 👋\n", Color.YELLOW))
        sys.exit(0)
