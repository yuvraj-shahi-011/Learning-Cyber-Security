1. Authentication & Authorization
1.1 Authentication

Authentication = Verifying identity.

It answers:

“Who are you?”

Examples:

Username + password
OTP
Fingerprint
Face recognition
Security key
Login with Google
Example
User → Username + Password
          ↓
       Server
          ↓
   Verify credentials
          ↓
       Login ✓

If the credentials are correct, the user is authenticated.

1.2 Authorization

Authorization = Determining what an authenticated user is allowed to do.

It answers:

“What are you allowed to access?”

Example:

Authentication
      ↓
   User = Yuvraj
      ↓
Authorization
      ↓
Can Yuvraj delete students?
      ↓
      NO
1.3 Authentication vs Authorization
Authentication	Authorization
Verifies identity	Verifies permissions
“Who are you?”	“What can you do?”
Happens first	Happens after authentication
Uses passwords, OTP, biometrics	Uses roles, permissions, policies
Example: Login	Example: Delete user
Easy way to remember

AuthN = Authentication → Identity

AuthZ = Authorization → Permission

1.4 Authentication Factors

Authentication factors are commonly divided into three categories.

1. Something you know

Examples:

Password
PIN
Security question
2. Something you have

Examples:

Smartphone
Hardware security key
Smart card
OTP device
3. Something you are

Examples:

Fingerprint
Face
Iris
Voice biometrics
1.5 Multi-Factor Authentication — MFA

MFA requires two or more different authentication factors.

Example:

Password
   +
OTP on phone
   ↓
Login

Another example:

Password
   +
Security key
   ↓
Login
MFA vs 2FA

2FA specifically uses two authentication factors.

MFA means two or more factors.

Therefore:

2FA ⊂ MFA
1.6 Single Sign-On — SSO

SSO allows a user to authenticate once and access multiple applications.

Example:

Google Account
      ↓
   Login once
      ↓
 ┌────┼────┐
 ↓    ↓    ↓
Gmail Drive YouTube

Advantages:

Fewer passwords
Centralized authentication
Easier account management

Risk:

If the central identity account is compromised, multiple services may be affected.

1.7 Session-Based Authentication

After successful login, the server can create a session.

Login
  ↓
Server verifies password
  ↓
Session created
  ↓
Session ID sent to browser
  ↓
Browser sends session ID
  ↓
Server identifies user

Example:

Cookie: session_id=abc123

The server associates:

abc123 → User 42
1.8 Token-Based Authentication

Another approach is token-based authentication.

Example:

User logs in
    ↓
Server verifies credentials
    ↓
Server issues token
    ↓
Client stores token
    ↓
Client sends token with requests

Common example:

JWT — JSON Web Token

Authorization: Bearer <token>

JWT typically contains:

Header
Payload
Signature

Important:

A JWT is generally signed, not encrypted. Do not put sensitive secrets in its payload.

1.9 Common Authentication Attacks
Brute Force

Attacker repeatedly tries passwords.

password123
Password1
admin123
qwerty
...

Defense:

Rate limiting
MFA
Account lockout/cooldowns
Strong passwords
Monitoring