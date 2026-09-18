Day 1 — Cybersecurity Fundamentals

Cybersecurity

Definition:
Cybersecurity is the practice of protecting computers, networks, applications, devices, and data from unauthorized access, attacks, damage, theft, or disruption.
Example: Protecting a company's server from hackers and malware.

CIA Triad

The CIA Triad is the foundation of information security.

Confidentiality:

Ensures that information is accessible only to authorized people or systems.
Example: Passwords, access controls, and encryption protect confidential data.

Integrity:

Ensures that data remains accurate, complete, and unaltered by unauthorized users.
Example: A hacker should not be able to modify a bank transaction from ₹1,000 to ₹10,000.

Availability:

Ensures that systems and data are available when authorized users need them.
Example: A website should remain accessible to customers even during an attack.

Easy memory:

C = Secret | I = Correct | A = Accessible

Threat

Definition:
A threat is a potential danger that could exploit a vulnerability and cause harm to a system or organization.
Example: A hacker attempting to steal passwords is a threat.

Vulnerability

Definition:
A vulnerability is a weakness or security flaw in a system that can be exploited by a threat.
Example: Outdated software containing a known security flaw.

Exploit

Definition:
An exploit is a method, technique, or piece of code used to take advantage of a vulnerability.
Example: An attacker uses specially crafted input to exploit a vulnerable web application.

Risk

Definition:
Risk is the potential for loss or damage when a threat exploits a vulnerability.
A simple way to understand it:
Risk = Threat × Vulnerability × Impact
Example:
Weak password → hacker can guess it → account gets compromised.

Malware

Malware means malicious software designed to damage, disrupt, spy on, or gain unauthorized access to systems.

Virus:

A malicious program that attaches itself to a legitimate file/program and usually requires user action to spread.

Worm:

Malware that can self-replicate and spread across networks without requiring a user to execute an infected file.

Trojan:

Malware that pretends to be legitimate software to trick the user into installing or running it.

Ransomware:

Malware that locks or encrypts files/systems and demands payment from the victim.

Spyware:

Malware designed to secretly monitor and collect information about a user or system.

RAT:

Remote Access Trojan (RAT) is malware that gives an attacker unauthorized remote control over an infected computer.

Botnet:

A network of compromised devices controlled by an attacker, often used to perform coordinated malicious activities.

Phishing
Definition:

Phishing is a social engineering attack in which an attacker impersonates a trusted person or organization to trick victims into revealing information, clicking malicious links, or installing malware.
Example:
A fake bank email asks you to "verify your account" using a malicious website.

Types:
Email Phishing — fake emails
Spear Phishing — targeted attack against a specific person/organization
Whaling — targets executives or high-value individuals
Smishing — phishing through SMS
Vishing — phishing through voice calls
Clone Phishing — legitimate message is copied and modified with malicious content

Authentication

Definition:
Authentication is the process of verifying who a user or system is.
Example: Logging into Gmail using a username and password.

Question it answers:
"Who are you?"

Authorization

Definition:
Authorization determines what an authenticated user is allowed to access or perform.
Example: An employee can view company files but cannot delete them.

Question it answers:
"What are you allowed to do?"

Remember:

Authentication → Identity
Authorization → Permissions

Encryption

Definition:
Encryption converts readable plaintext into unreadable ciphertext using an encryption algorithm and key.
Only someone with the appropriate key can decrypt the information.
Example:
Hello → encrypted data
Used to protect data during storage or transmission.

Hashing

Definition:
Hashing converts data into a fixed-length hash value using a hash function.
Unlike encryption, cryptographic hashing is designed to be one-way.
Example:
password → SHA-256 → hash
Hashing is commonly used for password storage, integrity verification, and digital signatures.

Key difference:

Encryption → designed to be decrypted
Hashing → designed to be one-way

Firewall

Definition:
A firewall is a security system that monitors and controls network traffic based on predefined security rules.
It can allow legitimate traffic and block unauthorized or suspicious traffic.
Example: Blocking incoming connections to a protected server.

VPN

Definition:
A Virtual Private Network (VPN) creates an encrypted connection between a device and a VPN endpoint, helping protect data while it travels across an untrusted network.
Example: Using a VPN on public Wi-Fi to protect network traffic from local interception.

Important: A VPN does not make you completely anonymous or automatically protect you from malware/phishing.

IDS

Definition:
Intrusion Detection System (IDS) monitors network or system activity and detects suspicious or malicious behavior.
It generally alerts administrators rather than automatically blocking the attack.

Easy memory:

IDS = Detect + Alert

IPS

Definition:
Intrusion Prevention System (IPS) monitors network/system activity and can automatically block or prevent detected malicious activity.

Easy memory:

IPS = Detect + Prevent

IDS vs IPS
IDS	IPS
Detects attacks	Detects and prevents attacks
Generates alerts	Can block malicious traffic
Usually passive	Usually inline/active

Endpoint Security

Definition:
Endpoint security protects end-user devices such as laptops, desktops, smartphones, and servers from cyber threats.
Examples:
Antivirus
EDR
Host firewall
Device control
Application control

Endpoint Detection and Response

Definition:
Endpoint Detection and Response (EDR) is a security technology that continuously monitors endpoint activity, detects suspicious behavior, investigates threats, and supports response actions.
For example, an EDR system may detect:
Word → PowerShell → suspicious command → unusual network connection and help a security analyst investigate what happened.

EDR commonly provides:
Continuous endpoint monitoring
Threat detection
Investigation
Alerting
Incident response
Endpoint isolation
