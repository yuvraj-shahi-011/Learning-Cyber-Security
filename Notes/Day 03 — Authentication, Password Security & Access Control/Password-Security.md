2. Password Security
2.1 Why Password Security Matters

Passwords are often the first layer protecting an account.

A compromised password can allow attackers to:

Access accounts
Steal data
Impersonate users
Change account settings
Access other systems
2.2 Never Store Plaintext Passwords

 Bad:

username: yuvraj
password: Yuvraj123

If the database is compromised, the attacker immediately gets the passwords.

Instead, passwords should be stored using a password hashing algorithm.

Password
   ↓
Password Hashing Algorithm
   ↓
Password Hash
   ↓
Database
2.3 Hashing

A cryptographic hash function transforms data into a fixed-length output.

Example:

Input
"hello"

      ↓ SHA-256

Hash
2cf24dba5fb0a30e...

A good cryptographic hash is designed to make it computationally difficult to recover the original input.

However:

General-purpose hashes such as SHA-256 are not appropriate by themselves for password storage.

Why?

They are designed to be very fast.

Attackers can therefore test huge numbers of password guesses quickly.

2.4 Password Hashing Algorithms

Use password-specific hashing algorithms such as:

Argon2id
bcrypt
scrypt
PBKDF2

For modern applications, Argon2id is a strong choice when available.

2.5 Salt

A salt is a unique random value added to a password before hashing.

Conceptually:

Password + Salt
      ↓
Password Hash Function
      ↓
Hash

Example:

Password = hello123
Salt     = X7a9...

Different users with the same password should have different hashes because their salts differ.

Why salt?

Without unique salts:

User A → password123 → same hash
User B → password123 → same hash

With unique salts:

User A → password123 + Salt A → Hash A
User B → password123 + Salt B → Hash B
2.6 Hashing vs Encryption

This is extremely important.

Hashing

Generally one-way.

Password
   ↓
Hash

You don't normally decrypt a password hash.

Encryption

Designed to be reversible using a key.

Plaintext
   ↓
Encryption + Key
   ↓
Ciphertext
   ↓
Decryption + Key
   ↓
Plaintext
Remember

Passwords → Hash

Data that must later be recovered → Encryption

2.7 Password Verification

When the user logs in:

User enters password
        ↓
Retrieve stored password hash
        ↓
Password hashing function verifies input
        ↓
Compare/verify against stored hash
        ↓
Match?
   ┌────┴────┐
  YES       NO
   ↓         ↓
Login      Reject

The application should use the password-hashing library's verification function rather than manually comparing plaintext passwords.

2.8 Password Strength

A stronger password generally has:

Sufficient length
Unpredictability
No common patterns
No reused credentials

Example:

 Weak:

password123

 Weak:

yuvraj123

Better:

A long, unique passphrase

For important accounts, use a password manager to generate unique random passwords.

2.9 Password Reuse

Suppose:

Website A
Password = X

An attacker obtains that password from a breach.

If the same password is used on:

Email
GitHub
Banking
College portal

the attacker may attempt the same credentials elsewhere.

Therefore:

Use a unique password for every important service.

2.10 Password Managers

A password manager can:

Generate strong passwords
Store credentials securely
Autofill login forms
Reduce password reuse
Help manage many unique passwords

Instead of remembering 50 passwords:

One strong master credential
          +
Password manager
          ↓
Unique passwords everywhere
2.11 Common Password Attacks
Brute Force

Try many combinations.

Dictionary Attack

Try words and common passwords from a dictionary/list.

Credential Stuffing

Use leaked credentials from another service.

Password Spraying

Try one/few common passwords against many accounts.

Rainbow Tables

Precomputed tables can help attack unsalted hashes.

Salted password hashing significantly reduces the usefulness of precomputed tables.

2.12 Secure Password Storage Checklist

✓ Never store plaintext passwords
✓ Use Argon2id/bcrypt/scrypt/PBKDF2
✓ Use a unique salt per password
✓ Use appropriate work/memory factors
✓ Never log passwords
✓ Never send passwords in URLs
✓ Use HTTPS
✓ Support MFA
✓ Prevent common/breached passwords
✓ Rate-limit authentication attempts