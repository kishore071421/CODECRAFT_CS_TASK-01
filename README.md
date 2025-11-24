# 🔐 Caesar Cipher Encryption & Decryption Tool

This project implements a **Caesar Cipher**, one of the oldest and simplest encryption techniques.  
The program allows the user to:

- Encrypt a message  
- Decrypt a message  
- Choose any shift value  
- Automatically validate user input  

---

## 📌 **Features**

### ✔ Encrypt Text  
Enter any message and a shift value to encrypt it.

### ✔ Decrypt Text  
Decrypt any Caesar-encrypted message by applying the negative shift.

### ✔ Input Validation  
Prevents errors by ensuring only valid integers are accepted for shift values.

### ✔ Supports Uppercase & Lowercase  
Non-alphabetic characters remain unchanged.

---

## 📂 **Project Structure**

```
Caesar-Cipher/
│
├── caesar_cipher.py     # Main program
└── README.md            # Documentation
```

---

## 🛠 **How It Works**

Caesar Cipher shifts each letter by a fixed number within the alphabet.

Example:

```
Plain Text: HELLO
Shift: 3
Encrypted: KHOOR
```

Decryption simply reverses the shift.

---

## ▶️ **Usage**

### **Run the program**
```
python caesar_cipher.py
```

### **Menu Options**

```
1 → Encrypt a message
2 → Decrypt a message
3 → Exit the program
```

---

## 💻 **Code Snippet**

```python
def caesar_shift(char, shift):
    if not char.isalpha():
        return char
    shift %= 26
    base = 65 if char.isupper() else 97
    return chr((ord(char) - base + shift) % 26 + base)


def encrypt(text, shift):
    return "".join(caesar_shift(c, shift) for c in text)


def decrypt(text, shift):
    return encrypt(text, -shift)
```

---

## 📘 **Example Output**

```
=== Caesar Cipher Tool ===
1. Encrypt a message
2. Decrypt a message
3. Exit

Enter your choice: 1
Enter your message: hello world
Enter shift value: 5

Encrypted Message: mjqqt btwqi
```

---

## 🏆 **Author**

**B Bharath kishore**  
This project is developed as part of internship task requirements.

---

## 📄 **License**

This project is free to use for learning and educational purposes.

