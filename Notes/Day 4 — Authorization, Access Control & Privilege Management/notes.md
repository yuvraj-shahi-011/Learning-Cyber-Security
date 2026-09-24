# Day 04 — Authorization & Access Control

## 1. What is Authorization?

Authorization is the process of determining what an authenticated user is allowed to access or perform.

Authentication asks:

> Who are you?

Authorization asks:

> What are you allowed to do?

Example:

User logs in successfully.

Authentication:
User = Yuvraj

Authorization:
Yuvraj is a Student

Student can:
- View attendance
- View profile

Student cannot:
- Delete students
- Manage users
- Change system settings

---

## 2. Authentication vs Authorization

| Authentication | Authorization |
|---|---|
| Verifies identity | Verifies permissions |
| Who are you? | What can you do? |
| Happens before authorization | Happens after authentication |
| Password, OTP, biometric | Roles, permissions, policies |
| Example: Login | Example: Delete user |

---

## 3. Authorization Process

A typical authorization flow:

User
  ↓
Login
  ↓
Authentication
  ↓
User Identity
  ↓
Check Role/Permissions
  ↓
Authorization
  ↓
Allow / Deny
  ↓
Resource

Example:

Student → DELETE /students/10

Server checks:

Is user authenticated?
        ↓
       YES

Does user have delete permission?
        ↓
        NO

Response:
403 Forbidden

---

## 4. Permission

A permission defines an action a user can perform.

Common permissions:

- Create
- Read
- Update
- Delete
- Execute

These are often called CRUD operations:

C = Create
R = Read
U = Update
D = Delete

---

## 5. Role

A role is a collection of permissions.

Example:

Admin:
- Create user
- Read user
- Update user
- Delete user

Teacher:
- View students
- Mark attendance
- View reports

Student:
- View profile
- View own attendance

---

## 6. Principle of Least Privilege

The Principle of Least Privilege means:

> A user should receive only the permissions required to perform their work.

Example:

A student does not need:

DELETE students

A teacher may need:

MARK attendance

An administrator may need:

CREATE + READ + UPDATE + DELETE

Benefits:

- Reduces attack surface
- Limits damage from compromised accounts
- Reduces accidental changes
- Improves security

---

## 7. Default Deny

A secure authorization system should generally follow:

> Deny access unless permission is explicitly granted.

Example:

User requests:

/admin/users

If the user does not have the required permission:

403 Forbidden

---

## 8. Role-Based Access Control (RBAC)

RBAC gives permissions according to roles.

Example:

Admin
├── Create User
├── Read User
├── Update User
└── Delete User

Teacher
├── View Students
├── Mark Attendance
└── View Reports

Student
├── View Profile
└── View Attendance

---

## 9. RBAC Flow

User
 ↓
Role
 ↓
Permissions
 ↓
Requested Resource
 ↓
Allow / Deny

Example:

Yuvraj
 ↓
Teacher
 ↓
mark_attendance
 ↓
POST /attendance
 ↓
ALLOW

---

## 10. Privilege Escalation

Privilege escalation occurs when a user obtains permissions beyond those intended.

### Vertical Privilege Escalation

A low-privileged user gains higher privileges.

Example:

Student → Admin

### Horizontal Privilege Escalation

A user accesses another user's resources at a similar privilege level.

Example:

User A → User B's profile

---

## 11. Broken Access Control

Broken access control occurs when an application fails to properly enforce authorization rules.

Example:

A student should only access:

/student/101

But changes the URL to:

/student/102

and sees another student's information.

The server must verify whether the authenticated user is authorized to access resource 102.

---

## 12. 401 vs 403

### 401 Unauthorized

The request lacks valid authentication.

Example:

User is not logged in.

### 403 Forbidden

The user is authenticated but does not have permission.

Example:

Student attempts to access an admin endpoint.

Remember:

401 → Authentication problem

403 → Authorization problem

---

## 13. Authorization Best Practices

- Enforce authorization on the server
- Use least privilege
- Use default deny
- Use strong RBAC/ABAC policies
- Validate resource ownership
- Never trust frontend restrictions
- Log important authorization failures
- Review permissions regularly
- Remove unnecessary privileges
- Use HTTPS
- Protect administrative endpoints

---

## 14. Important Terms

Authentication:
Who are you?

Authorization:
What can you do?

Role:
Collection of permissions.

Permission:
Allowed action.

Access Control:
Mechanism that controls access.

Least Privilege:
Minimum required permissions.

Privilege Escalation:
Obtaining unauthorized higher or different privileges.

RBAC:
Role-Based Access Control.

ABAC:
Attribute-Based Access Control.

ACL:
Access Control List.

