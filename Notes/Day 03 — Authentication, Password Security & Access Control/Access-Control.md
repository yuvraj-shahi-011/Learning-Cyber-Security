3. Access Control
3.1 What is Access Control?

Access control determines which users or systems can access which resources and what operations they can perform.

Example:

User
 ↓
Access Control
 ↓
Resource + Action

For example:

Teacher → Attendance → Mark
Student → Attendance → View
3.2 The Three Main Components

Think of access control as:

Subject → Action → Object

Example:

Teacher → UPDATE → Attendance

Where:

Subject = Who is requesting access

Action = What they want to do

Object = What they want to access

3.3 CRUD Permissions

Many applications use CRUD operations.

Operation	Meaning
C	Create
R	Read
U	Update
D	Delete

Example:

Student:
R → View profile

Teacher:
R → View students
C/U → Attendance

Admin:
C/R/U/D → Students
3.4 Principle of Least Privilege — PoLP

Give users only the permissions they need to perform their job.

Example:

A student does not need:

DELETE all students

A teacher may need:

MARK attendance

An administrator may need:

CREATE
READ
UPDATE
DELETE

Least privilege reduces the impact of compromised accounts.

3.5 RBAC — Role-Based Access Control

RBAC assigns permissions based on roles.

Example:

              SYSTEM
                 |
       ┌─────────┼─────────┐
       ↓         ↓         ↓
     ADMIN     TEACHER   STUDENT

Permissions:

ADMIN
 ├── Create student
 ├── Update student
 ├── Delete student
 └── View reports

TEACHER
 ├── View students
 ├── Mark attendance
 └── View reports

STUDENT
 └── View own attendance
3.6 RBAC Example

Suppose:

Role = Teacher

Request:

POST /attendance

System checks:

Is user authenticated?
        ↓
      YES
        ↓
Is user a teacher?
        ↓
      YES
        ↓
Is teacher allowed to mark attendance?
        ↓
      YES
        ↓
Allow
3.7 ABAC — Attribute-Based Access Control

ABAC makes decisions based on attributes.

Attributes can include:

User
Role
Department
Location
Device
Time
Resource classification

Example:

Teacher
+
Computer Lab
+
Working Hours
+
Attendance System
      ↓
Allow

Another request:

Student
+
Admin Endpoint
      ↓
Deny

ABAC can support more fine-grained policies than simple RBAC.

3.8 DAC — Discretionary Access Control

In DAC, resource owners can control access.

Example:

File Owner
    ↓
Choose who can access file

Common concept in operating systems and file permissions.

3.9 MAC — Mandatory Access Control

MAC uses centrally defined security policies.

Users generally cannot freely change the security classification rules.

Commonly associated with environments requiring strict information classification.

Example:

TOP SECRET
SECRET
CONFIDENTIAL
PUBLIC

A user with insufficient clearance cannot access higher-classified information.

3.10 RBAC vs ABAC vs DAC vs MAC
Model	Main Idea
RBAC	Access based on roles
ABAC	Access based on attributes/policies
DAC	Owner controls access
MAC	Central security policy controls access
3.11 Access Control Lists — ACL

An ACL defines who can perform what actions on a resource.

Example:

File: attendance.xlsx

Admin    → Read + Write
Teacher  → Read + Write
Student  → Read
Guest    → No Access
3.12 Authentication + Authorization + Access Control

Put everything together:

                 User
                   ↓
           Authentication
                   ↓
             Who are you?
                   ↓
              Identity
                   ↓
            Authorization
                   ↓
           What can you do?
                   ↓
            Access Control
                   ↓
       ┌───────────┼───────────┐
       ↓           ↓           ↓
      READ       UPDATE       DELETE