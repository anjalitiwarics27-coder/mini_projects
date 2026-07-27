# 📓 Field Notes — a small blog

<div align="center">

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Ek chota sa, journal-jaisa personal blog — bina kisi backend, database, ya internet ke! ✍️**

</div>

---

## ✨ Features

- 📝 **Title + Entry Composer** — clean, distraction-free writing space
- 💾 **Auto Local Storage** — har entry browser ke `localStorage` me safely save hoti hai
- 🗓️ **Auto Timestamp** — har entry par date aur time automatically stamp hota hai
- 🔢 **Entry Tally** — header me total entries ka live count
- 🗑️ **Delete with Confirmation** — accidental delete se bachne ke liye confirm dialog
- ⌨️ **Keyboard Shortcut** — `Ctrl/Cmd + Enter` se seedha entry file karein
- 🔃 **Newest First** — sabse recent entry hamesha top par dikhti hai
- 🛡️ **XSS-Safe Rendering** — har entry ka text safely escape hokar render hota hai
- 📱 **Responsive Design** — mobile aur desktop dono par sundar dikhta hai
- 🎨 **Vintage Paper Aesthetic** — ruled paper background, typewriter-style fonts aur soft shadows

---

## 🖼️ Design Vibe

Ye app ek **field journal / paper notebook** ke look-and-feel se inspired hai:

| Element | Style |
|---------|-------|
| Background | Ruled paper texture (`#EEEBE3`) with subtle horizontal lines |
| Headings/Labels | Monospace typewriter font (`Courier New`) |
| Body Text | Classic serif font (`Georgia`) |
| Accent Colors | Rust 🟤 (`#A8462F`) & Olive 🟢 (`#5C6B4E`) |
| Cards | Off-white paper cards with hard drop shadows |

---

## 🛠️ Tech Stack

- **HTML5** — semantic structure
- **CSS3** — custom properties (CSS variables), flexbox, keyframe animations
- **Vanilla JavaScript** — no frameworks, no build tools, no dependencies
- **Browser `localStorage`** — client-side data persistence

> ✅ Bas ek single `.html` file — kuch bhi install karne ki zarurat nahi!

---

## 🚀 Usage

1. `blog_app.html` file ko kisi bhi modern browser me open karein (double-click karein ya drag-and-drop karein)
2. **Title** aur **Entry** likhein
3. **"File Entry"** button dabayein (ya `Ctrl/Cmd + Enter` press karein)
4. Entry turant list me save ho jayegi — permanently, us browser me

```bash
# Bas file open karein — koi server ki zarurat nahi
open blog_app.html   # macOS
start blog_app.html  # Windows
```

---

## 📁 Project Structure

```
📦 field-notes
 ┗ 📜 blog_app.html   ← Sab kuch ek hi file me (HTML + CSS + JS)
```

---

## 🧩 Code Structure

| Function | Purpose |
|----------|---------|
| `loadPosts()` | `localStorage` se saari entries safely load karta hai |
| `savePosts()` | Entries ko `localStorage` me save karta hai (error handling ke saath) |
| `formatDate()` | Timestamp ko readable date/time format me convert karta hai |
| `escapeHtml()` | User input ko safely escape karta hai (XSS prevention) |
| `render()` | Entries list ko dobara draw karta hai, tally update karta hai |
| `addPost()` | Naya entry create karta hai, validate karta hai, save karta hai |
| `deletePost()` | Confirmation ke baad entry delete karta hai |

---

## ⚠️ Important Note

> 🔒 **Data sirf isi browser me store hota hai.**
> Entries kisi server par nahi jaati — agar aap browser cache/history clear karte hain, ya kisi doosre device/browser par file open karte hain, to purani entries dikhai nahi degi.
>
> Regular backup ke liye, entries ko manually copy karke kahin aur save kar lena behtar hoga.

---

## 🎯 Use Cases

- 📔 Daily journaling / diary
- 🧳 Travel field notes
- 💡 Quick idea logging
- 🌱 Habit / mood tracking notes
- ✍️ Personal micro-blogging

---

## 🤝 Contributing

Contributions dil se welcome hain! Kuch naye feature ideas:

- 🔍 Search/filter entries
- 🏷️ Tags ya categories
- 📤 Export to JSON/Markdown
- ✏️ Edit existing entries
- 🌙 Dark mode toggle

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

Made with ❤️ using HTML, CSS & Vanilla JavaScript

</div>
