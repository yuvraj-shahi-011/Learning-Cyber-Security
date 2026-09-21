Practical 3 — RBAC Simulation
Objective

Build a simple Role-Based Access Control (RBAC) system using Python.

The program gives different permissions to different users based on their roles.

Roles and Permissions
ADMIN
Create student
Update student
Delete student
View reports
TEACHER
View student
Mark attendance
View reports
STUDENT
View own attendance
How RBAC Works
User
  ↓
Role
  ↓
Permissions
  ↓
Access Granted / Access Denied
Example

If a student tries to delete a student:

Username: student
Permission: delete

ACCESS DENIED

If an admin tries to delete a student:

Username: admin
Permission: delete

ACCESS GRANTED
Authentication vs Authorization
Authentication

Answers:

Who are you?
Authorization

Answers:

What are you allowed to do?

RBAC is an authorization mechanism.

Technologies Used
Python

How to Run

Run the program:
python rbac.py