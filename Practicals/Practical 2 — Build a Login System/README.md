# 🔐 Practical 2 — Authentication Demo

## Objective

Build a simple Python authentication system demonstrating secure password storage and basic authentication functionality.

## Features

* User registration
* User login
* User logout
* SQLite database
* Password hashing using bcrypt
* Password verification using bcrypt

## Security Concept

Passwords are **never stored in plaintext**.

During registration, the password is passed through bcrypt to generate a password hash.

During login, the entered password is verified against the stored hash using `bcrypt.checkpw()`.

### Authentication Flow

```text
USER
  ↓
Login / Registration
  ↓
Authentication System
  ↓
bcrypt Password Hashing
  ↓
SQLite Database
```

## Technologies

* Python
* SQLite
* bcrypt

## Security Principle Demonstrated

**Never store plaintext passwords.**

A password database should contain password hashes rather than the original passwords.
