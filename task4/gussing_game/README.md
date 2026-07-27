# 🎯 Number Guessing Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Computer ne socha ek number 1 se 100 ke beech — kya aap use guess kar paayenge? 🎲**

</div>

---

## ✨ Features

- 🎲 **Random Number Generation** — har game me 1 se 100 ke beech ek naya secret number
- 🛡️ **Smart Input Validation** — non-numeric ya out-of-range input par friendly error message
- 📊 **Attempt Counter** — track karta hai ki number guess karne me kitne attempts lage
- 🔼🔽 **Too High / Too Low Hints** — har galat guess par direction ka clue
- 🔁 **Play Again Option** — game khatam hone ke baad turant naya round shuru karein
- 🖥️ **Simple Command-Line Interface** — koi extra dependency nahi, sirf pure Python

---

## 🛠️ Requirements

- Python 3.x
- Koi external library ki zarurat nahi — sirf Python ki built-in `random` module! ✅

---

## 🚀 Usage

Script run karein:

```bash
python guessing_game.py
```

Fir bas apna guess enter karte jayein:

```
========================================
      NUMBER GUESSING GAME
========================================
I'm thinking of a number between 1 and 100.
Try to guess it!

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
```

### 📤 Sample Winning Output

```
========================================
🎉 Congratulations! You guessed it right!
The number was 37.
It took you 3 attempts.
========================================

Would you like to play again? (y/n):
```

---

## 🧩 Code Structure

| Function | Purpose |
|----------|---------|
| `play_game()` | Ek complete game round handle karta hai — random number, guesses, hints aur win condition |
| `main()` | Program flow control karta hai, loop ke saath "play again" facility deta hai |

---

## 🛡️ Input Validation

Ye game har input ko carefully validate karta hai:

- ❌ Non-numeric input (jaise letters ya symbols) → "Please enter a valid whole number."
- ❌ 1–100 range se bahar ka number → "Please guess a number between 1 and 100."
- ✅ Sirf valid whole numbers hi accept honge

---

## 🎮 How It Works

1. Game shuru hote hi computer **1 se 100** ke beech ek random number choose karta hai
2. Aap apna guess enter karte hain
3. Game batata hai ki aapka guess **"Too High"** hai ya **"Too Low"**
4. Sahi number guess hone tak process repeat hoti hai
5. Ant me total **attempts count** ke saath congratulations message milta hai
6. Aap chaahe to naya round turant shuru kar sakte hain

---

## 🎯 Use Cases

- 🧠 Quick logic/brain teaser break
- 🐍 Python beginners ke liye great learning project
- 🎓 Loops, conditionals & input validation seekhne ka example
- 😄 Casual timepass game dosto ke saath

---

## 🤝 Contributing

Contributions dil se welcome hain! Kuch naye feature ideas:

- 🎚️ Difficulty levels (range badalna — jaise 1-1000)
- ⏱️ Timer-based challenge mode
- 🏆 Best score / leaderboard tracking
- 💡 Hint system (jaise "warmer/colder")

1. Repo ko **Fork** karein 🍴
2. Naya branch banayein (`git checkout -b feature/naya-feature`)
3. Changes **Commit** karein (`git commit -m 'Added naya feature'`)
4. Branch **Push** karein (`git push origin feature/naya-feature`)
5. Ek **Pull Request** open karein 🎉

---

## 📄 License

Ye project **MIT License** ke under available hai — free to use, modify aur share karein! 💙

---

<div align="center">

### 🌟 Agar ye project pasand aaya to ek Star zaroor de dein! 🌟

Made with ❤️ using Python

</div>
