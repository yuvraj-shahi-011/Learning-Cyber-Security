Part 1 — CIA Triad

The CIA Triad is a fundamental information-security model used to understand what security is trying to protect.

CIA stands for:

Confidentiality
Integrity
Availability

1. Confidentiality

Confidentiality means ensuring that information is accessible only to authorized users.

Example:
Suppose a college has a database containing:

1.Student names
2.Phone numbers
3.Addresses
4.Marks
Only authorized staff should be able to access this information.

If a hacker steals the database and reads the student information, confidentiality has been violated.

Common controls:
1.Passwords
2.Authentication
3.Authorization
4.Encryption
5.Access control
6.MFA

Remember:

Confidentiality = Prevent unauthorized access/disclosure

2. Integrity

Integrity means ensuring that information remains accurate, complete, and unchanged unless an authorized person modifies it.

Example:
Suppose a student's actual marks are:
85

An attacker changes them to:
95

The data has been modified without authorization.
Therefore, integrity has been compromised.

Common controls
1.Hashing
2.Digital signatures
3.Access controls
4.File permissions
5.Audit logs
6.Version control

Remember:
Integrity = Data should remain correct and trustworthy

3. Availability

Availability means ensuring that authorized users can access systems, applications, and data when they need them.

Example:
Suppose your college website normally allows students to download examination forms.

An attacker launches a DDoS attack, causing the website to become unavailable.

The system cannot be accessed by students.

Therefore, availability has been compromised.

Common controls:
1.Backups
2.Redundant servers
3.Disaster recovery
4.Load balancing
5.UPS
6.DDoS protection
7.Failover systems

Remember:
Availability = System should be accessible when needed

🧠 CIA Triad Examples:

Attack/Incident 	   CIA Property Affected
Hacker steals customer -data	Confidentiality
Hacker modifies database records -	Integrity
DDoS takes website offline-	Availability
Ransomware encrypts files-	Availability + Integrity
Employee leaks confidential documents -	Confidentiality
Attacker changes financial records	-Integrity

Easy trick:
C = Secret
I = Correct
A = Accessible