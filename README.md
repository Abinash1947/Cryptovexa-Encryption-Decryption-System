# Cryptovexa 🔐

**Cryptovexa** is a secure encryption and decryption project designed to demonstrate modern cryptographic techniques and protect sensitive data from unauthorized access.

##  Project Overview

Cryptovexa provides a simple way to generate cryptographic keys and perform encryption and decryption operations. The project is designed for learning and demonstrating concepts related to **cryptography, data security, and secure communication**.

##  Objectives

* Understand encryption and decryption concepts.
* Generate secure cryptographic keys.
* Protect sensitive information from unauthorized access.
* Demonstrate the practical use of cryptographic algorithms.
* Provide a simple and easy-to-understand security project.

##  Features

* Secure random key generation using Python's `secrets` module.
* Support for AES key sizes:

  * 128-bit
  * 192-bit
  * 256-bit
* Key-size validation.
* Secure binary key generation.
* Encryption and decryption functionality.
* Simple command-line interface.
* Beginner-friendly implementation.

## 🛠️ Technologies Used

* **Python**
* **Cryptography**
* **AES**
* **Python `secrets` module**
* **Git & GitHub**

##  AES Key Generation

Cryptovexa supports the following AES key sizes:

| Key Size | Key Length |
| -------- | ---------- |
| 128-bit  | 16 bytes   |
| 192-bit  | 24 bytes   |
| 256-bit  | 32 bytes   |

The project uses Python's `secrets` module to generate cryptographically secure random keys.

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Cryptovexa.git
```

### 2. Navigate to the Project

```bash
cd Cryptovexa
```

### 3. Run the Program

```bash
python main.py
```

## Example

```text
Enter your key size: 128
128
Generated key: 7a3f91c2e8b45671d90a4c3f82b16e05
Key length: 128 bits
```

##  Project Structure

```text
Cryptovexa/
│
├── main.py
├── README.md
└── requirements.txt
```

##  Security Note

This project is intended primarily for **educational purposes**. Do not use a simplified or experimental implementation as the sole protection for sensitive production data. For real-world applications, use well-tested cryptographic libraries and secure encryption modes.

##  Future Improvements

* Add complete AES encryption and decryption.
* Add file encryption and decryption.
* Add password-based key derivation.
* Add graphical user interface.
* Add digital signature support.
* Add RSA/AES hybrid encryption.
* Add SHA-256 integrity verification.
* Add secure encrypted file storage.

##  Author

**Abinash Behera**

B.Tech – Computer Science and Engineering

##  License

This project is created for educational and academic purposes.
