# 📇 Contact Book

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Class%20Based-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Apne saare contacts ek jagah manage karein — Add, View, Search aur Delete, sab kuch ek simple CLI app me! 📞**

</div>

---

## ✨ Features

- ➕ **Add Contact** — Name, Phone aur Email ke saath naya contact save karein
- 📋 **View All Contacts** — saare saved contacts ek clean, numbered list me dekhein
- 🔍 **Search by Name** — case-insensitive aur partial-match keyword search
- 🗑️ **Delete Contact** — naam se contact turant remove karein
- 🛡️ **Empty Input Protection** — koi bhi field khali nahi ja sakti, hamesha valid input maanga jaata hai
- 🏗️ **Clean OOP Design** — `ContactBook` class ke through organized aur reusable code
- 🖥️ **Simple Menu-Driven CLI** — koi extra dependency nahi, sirf pure Python

---

## 🛠️ Requirements

- Python 3.x
- Koi external library ki zarurat nahi — sirf Python ki built-in functionality! ✅

---

## 🚀 Usage

Script run karein:

```bash
python contact_book.py
```

Fir menu se apni choice select karein:

```
========================================
           CONTACT BOOK MENU
========================================
1. Add a new contact
2. View all contacts
3. Search contact by name
4. Delete a contact
5. Exit
========================================

Enter your choice (1-5):
```

---

## 📤 Sample Output

### ➕ Adding a Contact

```
Enter name: Rahul Sharma
Enter phone number: 9876543210
Enter email: rahul.sharma@example.com

Contact 'Rahul Sharma' added successfully.
```

### 📋 Viewing Contacts

```
==================================================
               ALL CONTACTS
==================================================
1. Name : Rahul Sharma
   Phone: 9876543210
   Email: rahul.sharma@example.com
--------------------------------------------------
```

### 🔍 Searching a Contact

```
Enter name to search: rahul

==================================================
       SEARCH RESULTS FOR 'rahul'
==================================================
1. Name : Rahul Sharma
   Phone: 9876543210
   Email: rahul.sharma@example.com
--------------------------------------------------
```

### 🗑️ Deleting a Contact

```
Enter name to delete: Rahul Sharma

Contact 'Rahul Sharma' deleted successfully.
```

---

## 🧩 Code Structure

| Component | Purpose |
|-----------|---------|
| `ContactBook` class | Contacts ki poori list manage karti hai (add, view, search, delete) |
| `add_contact()` | Naya contact dictionary ke roop me list me append karta hai |
| `view_contacts()` | Saare contacts ko numbered, formatted list me print karta hai |
| `search_contact()` | Name ke andar keyword dhoondh kar case-insensitive matches dikhata hai |
| `delete_contact()` | Exact name match par contact(s) ko list se remove karta hai |
| `get_non_empty_input()` | Ensure karta hai ki koi bhi field khali submit na ho |
| `main()` | Menu-driven loop ke through poora program flow control karta hai |

---

## 🛡️ Input Validation

- ❌ Khali input (sirf spaces ya kuch bhi nahi) → dobara sahi value maangega
- 🔎 Search **partial match aur case-insensitive** hai (jaise "rah" → "Rahul Sharma" mil jayega)
- 🎯 Delete **exact name match** (case-insensitive) par kaam karta hai

---

## 🎯 Use Cases

- 👥 Personal ya small business contacts manage karna
- 🎓 Python OOP concepts (classes, methods, list of dicts) seekhne ka example
- 🧩 CRUD operations practice karne ke liye beginner-friendly project
- 💼 Quick CLI-based address book

---

## 🤝 Contributing

Contributions dil se welcome hain! Kuch naye feature ideas:

- 💾 File/JSON me contacts save karna (persistent storage)
- ✏️ Existing contact edit/update karne ka option
- 📊 Contacts ko alphabetically sort karna
- 📤 Contacts export karna (CSV/vCard)

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
