
# Access Control

## 1. What is Access Control?

Access control is the process of controlling who or what can access a resource and what actions they can perform.

Example:

User → Resource → Action

Teacher → Attendance → Update

---

## 2. Components of Access Control

### Subject

The entity requesting access.

Examples:

- User
- Application
- Process
- Device

### Object

The resource being accessed.

Examples:

- File
- Database
- API
- Account
- Server

### Action

The operation being requested.

Examples:

- Read
- Write
- Update
- Delete
- Execute

---

## 3. Access Control Decision

A basic decision process:

Subject
 ↓
Requests Action
 ↓
Object
 ↓
Policy Check
 ↓
Allow / Deny

Example:

Teacher
 ↓
Update
 ↓
Attendance
 ↓
Permission check
 ↓
Allow

---

# 4. Access Control Models

## RBAC

Role-Based Access Control.

Permissions are assigned to roles.

Example:

Admin → All administrative permissions

Teacher → Attendance permissions

Student → View permissions

---

## ABAC

Attribute-Based Access Control.

Access depends on attributes.

Possible attributes:

- User role
- Department
- Location
- Device
- Time
- Resource type

Example:

Teacher + IT Department + Working Hours

→ Allow

---

## DAC

Discretionary Access Control.

The owner of a resource controls access.

Example:

A file owner decides which users can access the file.

---

## MAC

Mandatory Access Control.

Access is controlled using centrally defined security policies.

Often used where information has security classifications.

Example:

Public
Confidential
Secret
Top Secret

---

# 5. ACL

ACL stands for Access Control List.

An ACL specifies permissions for subjects on a resource.

Example:

File: report.pdf

Admin:
Read + Write

Teacher:
Read + Write

Student:
Read

Guest:
No access

---

# 6. Least Privilege

Users should receive only the permissions they need.

Example:

Student:

READ attendance

Teacher:

READ + UPDATE attendance

Admin:

CREATE + READ + UPDATE + DELETE

---

# 7. Separation of Duties

Separation of Duties means sensitive operations should be divided among different people or roles.

Example:

Employee A:

Creates payment

Employee B:

Approves payment

This reduces the risk of one account having complete control over a sensitive process.

---

# 8. Default Deny

Access should be denied unless a valid rule allows it.

Example:

No permission
    ↓
DENY

Explicit permission
    ↓
ALLOW

---

# 9. Server-Side Access Control

Never rely only on frontend controls.

Bad:

```javascript
if (user.role === "admin") {
    showDeleteButton();
}

Hiding the button is not security.

An attacker can directly send the request.

The backend must verify:

Authenticated?
     ↓
Role?
     ↓
Permission?
     ↓
Resource ownership?
     ↓
Allow / Deny
10. IDOR / BOLA

An application may expose resources through identifiers.

Example:

/api/users/101

If User 101 can change the request to:

/api/users/102

and access User 102's private information without authorization, the application has an access-control problem.

The server must verify that the current user is authorized to access the requested object.

11. Privilege Escalation
Vertical

User gains a higher privilege level.

Example:

Student → Admin

Horizontal

User accesses another user's resource.

Example:

User A → User B's account

12. HTTP Responses

401:

Authentication is missing or invalid.

403:

Authentication exists, but access is forbidden.

13. Access Control Best Practices
Use least privilege
Use default deny
Verify permissions server-side
Validate object ownership
Use RBAC where appropriate
Review permissions regularly
Remove unused accounts
Remove unnecessary privileges
Log security-sensitive access
Protect administrative endpoints
Test authorization controls
14. Access Control Checklist

[ ] Authentication implemented

[ ] Authorization implemented

[ ] Roles defined

[ ] Permissions defined

[ ] Least privilege applied

[ ] Default deny applied

[ ] Server-side authorization

[ ] Object ownership checked

[ ] Administrative endpoints protected

[ ] Authorization failures logged