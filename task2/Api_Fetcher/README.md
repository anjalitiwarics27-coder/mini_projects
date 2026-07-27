# 🌐 Public API Data Fetcher

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-Library-orange?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Ek hi terminal app se Weather, Jokes, Quotes aur Advice — bilkul free public APIs se, koi API key nahi chahiye! 🚀**

</div>

---

## ✨ Features

- ☀️ **Live Weather** — kisi bhi city ka current temperature, condition aur wind speed (Open-Meteo)
- 😄 **Random Joke** — mood fresh karne ke liye ek random joke (Official Joke API)
- 💬 **Inspirational Quote** — random motivational quote author ke saath (Quotable)
- 🧠 **Random Advice** — ek chutki gyaan har baar (Advice Slip API)
- 🎨 **Colorful Terminal UI** — ANSI colors ke saath clean aur readable output
- ⏳ **Loading Spinner** — har network call ke dauraan smooth spinner animation
- 🔁 **Automatic Retry Logic** — timeout ya connection issue par khud retry karta hai
- 🛡️ **Robust Error Handling** — timeout, connection error, HTTP error sab gracefully handle hote hain
- 🪟 **Windows ANSI Support** — purane Windows terminals par bhi colors enable karta hai

---

## 🛠️ Requirements

- Python 3.x
- `requests` library

```bash
pip install requests
```

---

## 🚀 Usage

Script run karein:

```bash
python api_fetcher.py
```

Fir menu se apni choice select karein:

```
  1. Get current weather for a city
  2. Get a random joke
  3. Get a random quote
  4. Get a random piece of advice
  5. Exit

Enter choice (1-5):
```

---

## 📤 Sample Output

### ☀️ Weather

```
════════════════════════════════════════════════
              ☀️  CURRENT WEATHER
════════════════════════════════════════════════
  Location      Delhi, India
  Condition     Clear sky
  Temperature   34.2 °C
  Wind Speed    9.4 km/h
────────────────────────────────────────────────
```

### 😄 Joke

```
════════════════════════════════════════════════
           😄  RANDOM JOKE  ·  General
════════════════════════════════════════════════
  Q: Why don't scientists trust atoms?
  A: Because they make up everything!
────────────────────────────────────────────────
```

### 💬 Quote

```
════════════════════════════════════════════════
                💬  RANDOM QUOTE
════════════════════════════════════════════════
  "The only way to do great work is to love what you do."
  — Steve Jobs
────────────────────────────────────────────────
```

### 🧠 Advice

```
════════════════════════════════════════════════
               🧠  RANDOM ADVICE
════════════════════════════════════════════════
  Don't wait for the perfect moment. Take the moment and make it perfect.
────────────────────────────────────────────────
```

---

## 🌍 APIs Used

| API | Purpose | Key Required? |
|-----|---------|----------------|
| [Open-Meteo](https://open-meteo.com/) | Weather + Geocoding | ❌ No |
| [Official Joke API](https://github.com/15Dkatz/official_joke_api) | Random Jokes | ❌ No |
| [Quotable](https://api.quotable.io/) | Random Quotes | ❌ No |
| [Advice Slip API](https://api.adviceslip.com/) | Random Advice | ❌ No |

---

## 🧩 Code Structure

| Component | Purpose |
|-----------|---------|
| `Color` class | ANSI escape codes for terminal styling |
| `enable_windows_ansi()` | Older Windows terminals par ANSI colors enable karta hai |
| `request_with_retries()` | Retry logic ke saath safe HTTP GET requests |
| `show_spinner()` | Network calls ke dauraan loading animation dikhata hai |
| `fetch_weather()` / `display_weather()` | Weather data fetch aur display |
| `fetch_joke()` / `display_joke()` | Joke fetch aur display |
| `fetch_quote()` / `display_quote()` | Quote fetch aur display |
| `fetch_advice()` / `display_advice()` | Advice fetch aur display |
| `main()` | Interactive menu loop control karta hai |

---

## 🛡️ Error Handling

Har API call ke liye ye scenarios gracefully handle kiye gaye hain:

- ⏱️ **Timeout** — request bahut der tak atki to friendly error message
- 🔌 **Connection Error** — internet na ho to clear message
- ⚠️ **HTTP Error** — API se error response aane par uska detail
- 🧩 **Invalid Response Format** — unexpected JSON structure par bhi crash nahi hota

Network hiccups (timeout/connection error) ke liye automatic retry bhi hoti hai, bina user ko dobara try karne ke liye kehne ke.

---

## ⌨️ Keyboard Interrupt

Program ko kabhi bhi `Ctrl + C` se safely exit kiya ja sakta hai — koi ugly traceback nahi, sirf ek clean goodbye message. 👋

---

## 🤝 Contributing

Contributions dil se welcome hain! Naye APIs add karna chahte hain (jaise News, Trivia, Currency Exchange)?

1. Repo ko **Fork** karein 🍴
2. Naya branch banayein (`git checkout -b feature/naya-api`)
3. Changes **Commit** karein (`git commit -m 'Added naya feature'`)
4. Branch **Push** karein (`git push origin feature/naya-api`)
5. Ek **Pull Request** open karein 🎉

---

## 📄 License

Ye project **MIT License** ke under available hai — free to use, modify aur share karein! 💙

---

<div align="center">

### 🌟 Agar ye project pasand aaya to ek Star zaroor de dein! 🌟

Made with ❤️ using Python & Free Public APIs

</div>
