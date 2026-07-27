# 💰 Loan EMI Calculator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Apni Loan ki Monthly EMI turant calculate karein — simple, fast aur accurate! 🚀**

</div>

---

## ✨ Features

- 📊 **Instant EMI Calculation** – Principal, Interest Rate aur Tenure ke basis par
- 💸 **Total Interest Payable** ka breakdown
- 💵 **Total Payment** (Principal + Interest) ki poori jaankari
- 🖥️ **Simple Command-Line Interface** – koi complex setup nahi
- ⚡ **Lightweight & Fast** – bina kisi heavy dependency ke
- 🧮 **Accurate Formula-Based Calculation** – standard banking formula use karta hai

---

## 📐 EMI Formula

Ye calculator standard reducing balance EMI formula use karta hai:

```
EMI = P × R × (1 + R)^N / ((1 + R)^N - 1)
```

| Symbol | Meaning |
|--------|---------|
| `P` | Principal Loan Amount |
| `R` | Monthly Interest Rate (Annual Rate ÷ 12 ÷ 100) |
| `N` | Loan Tenure in Months |

---

## 🛠️ Installation

```bash
# Repository clone karein
git clone <your-repo-url>

# Project folder me jayein
cd loan-emi-calculator
```

> ✅ Koi extra library install karne ki zarurat nahi — sirf Python 3.x chahiye!

---

## 🚀 Usage

Script run karein:

```bash
python LoanEMICalculator.py
```

Fir bas puchhe gaye details enter karein:

```
Enter Loan Amount (₹): 500000
Enter Annual Interest Rate (%): 8.5
Enter Loan Tenure (in years): 5
```

### 📤 Sample Output

```
====================================
       LOAN EMI CALCULATION
====================================
Monthly EMI        : ₹ 10,258.83
Total Interest      : ₹ 115,529.80
Total Payment       : ₹ 615,529.80
====================================
```

---

## 📁 Project Structure

```
📦 loan-emi-calculator
 ┣ 📜 LoanEMICalculator.py
 ┗ 📜 README.md
```

---

## 🎯 Use Cases

- 🏠 Home Loan EMI planning
- 🚗 Car Loan calculation
- 🎓 Education Loan estimate
- 💼 Personal Loan budgeting

---

## 🤝 Contributing

Contributions dil se welcome hain! Agar aapke paas koi naya feature idea hai:

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
