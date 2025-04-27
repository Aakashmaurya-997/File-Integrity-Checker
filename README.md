# 📂 File-Integrity-Checker

---

**🏢 COMPANY**: CODTECH IT SOLUTIONS PVT. LTD

**👤 NAME**: AAKASH JAYDEV MAURYA

**🆔 INTERN ID**: CT04WS67

**🌐 DOMAIN**: CYBER SECURITY & ETHICAL HACKING

**🕓 DURATION**: 4 WEEKS

**👨‍🏫 MENTOR**: NEELA SANTOSH KUMAR

---

## 📜 DESCRIPTION OF THE TASK

---

### 🔹 Introduction

In today’s digital environment, file tampering, data corruption, and unauthorized modifications pose a significant threat to the integrity of sensitive files.  
File integrity monitoring is crucial for ensuring that important files remain unchanged and secure.  
As part of this task, a robust **File Integrity Checker** tool was built using **Python**.  
The goal was to monitor files within a directory by calculating their **SHA-256 hash values** and detecting any unauthorized changes or deletions.

---

### 🔹 Working Principle

The tool utilizes the powerful **hashlib** library in Python to generate cryptographic hash values for every file.  
Each file’s content is read in binary mode, and its hash is computed. The script initially records a baseline of hashes and continuously monitors files to detect any differences between the original and current states.

- If the file's hash changes, it indicates that the content was altered.
- If a file suddenly disappears, it indicates unauthorized deletion.

---

### 🔹 Key Features

- **Real-Time Monitoring**: Continuously scans for changes in real-time.
- **SHA-256 Cryptographic Hash**: Ensures high security and very low collision chances.
- **Alert System**: Prints warnings when a file is modified or deleted.
- **Lightweight Design**: Very efficient, minimal CPU usage.

---

### 🔹 Importance

In professional cybersecurity, **file integrity monitoring (FIM)** is a critical compliance requirement for standards like:
- PCI DSS
- HIPAA
- GDPR

By ensuring that key files remain unaltered, companies can protect against insider threats, ransomware attacks, and accidental corruption.

---

### 🔹 Use Cases

- Monitoring web server files (e.g., detecting if someone modifies `index.html`).
- Monitoring sensitive configuration files in production systems.
- Monitoring software builds to detect any unauthorized code injection.

---

### 🔹 Technologies Used

- Python
- Hashlib

---

### 🔹 Future Enhancements

In a real-world application, this tool could be extended to:
- Send email or SMS alerts if file changes are detected.
- Integrate with SIEM systems for enterprise-scale monitoring.
- Log all changes with timestamps into a secure database.

---

### 🔹 Conclusion

This **File Integrity Checker** is a simple yet effective security solution that strengthens the first line of defense against data integrity threats.  
It demonstrates how powerful even basic cryptographic hashing can be when applied thoughtfully in cybersecurity contexts.

---

## 📷 OUTPUT

![Image](https://github.com/user-attachments/assets/63d2b762-02ab-4ffb-985b-c22f070235d4)

---

## ⚙️ How to Run

---

### Step 1: Install Required Libraries

*(Only built-in libraries used for this project. No need to install external libraries.)*

### Step 2: Run the Script

```bash
python file_integrity_checker.py
```

---

# 🚀 Enjoy Monitoring Files Securely!
