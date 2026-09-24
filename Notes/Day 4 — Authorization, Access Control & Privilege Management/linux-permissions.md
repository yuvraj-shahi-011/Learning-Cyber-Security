# Linux File Permissions

## 1. Introduction

Linux uses file permissions to control who can access files and directories.

The three main permission categories are:

- User (Owner)
- Group
- Others

The three basic permissions are:

- Read (r)
- Write (w)
- Execute (x)

---

## 2. Checking Permissions

Use:

```bash
ls -l

Example:

-rwxr-xr--

The permission string can be understood as:

- rwx r-x r--
  │   │   │
  │   │   └── Others
  │   └────── Group
  └────────── Owner
3. File Type

The first character identifies the file type.

-   Regular file
d   Directory
l   Symbolic link

Example:

-rwxr-xr--

The first - means it is a regular file.

4. Read Permission

r means read.

For a file:

r = View/read file contents

For a directory:

r = List directory contents
5. Write Permission

w means write.

For a file:

w = Modify file

For a directory:

w = Create/delete/rename entries
6. Execute Permission

x means execute.

For a file:

x = Execute the file

For a directory:

x = Access/traverse the directory
7. Permission Groups

Example:

-rwxr-xr--

Break it into:

Owner  = rwx
Group  = r-x
Others = r--

Therefore:

Owner:

Read
Write
Execute

Group:

Read
Execute

Others:

Read
8. chmod

chmod changes file permissions.

Example:

chmod 755 script.sh

This gives:

Owner:

rwx

Group:

r-x

Others:

r-x
9. Numeric Permissions

Linux assigns numeric values:

Read     = 4
Write    = 2
Execute  = 1

Therefore:

rwx = 4 + 2 + 1 = 7

rw- = 4 + 2 = 6

r-x = 4 + 1 = 5

r-- = 4
10. Common Permission Values
755
Owner  = rwx
Group  = r-x
Others = r-x
644
Owner  = rw-
Group  = r--
Others = r--
700
Owner  = rwx
Group  = ---
Others = ---
600
Owner  = rw-
Group  = ---
Others = ---
11. chmod Symbolic Mode

Instead of numbers, permissions can be changed using symbols.

Example:

chmod u+x script.sh

Meaning:

u = user/owner
+ = add
x = execute

Another example:

chmod g-w file.txt

Remove write permission from the group.

12. chown

chown changes file ownership.

Example:

sudo chown user file.txt

Change owner and group:

sudo chown user:developers file.txt
13. chgrp

chgrp changes the group ownership.

sudo chgrp developers project.txt
14. Practical Commands

Check current directory:

pwd

List files:

ls

Show permissions:

ls -l

Create a file:

touch test.txt

Create directory:

mkdir security

Change permissions:

chmod 600 test.txt
15. Security Importance

Incorrect permissions can expose sensitive information.

Bad example:

-rw-rw-rw-

Everyone can potentially modify the file.

Better:

-rw-------

Only the owner can read and modify it.

16. Principle of Least Privilege

File permissions should provide only the access required.

Sensitive files should not be unnecessarily accessible to:

Other users
Untrusted processes
Unnecessary groups
Practical Exercise
Create a file:
touch secret.txt
Check permissions:
ls -l secret.txt
Set permissions:
chmod 600 secret.txt
Check again:
ls -l secret.txt
Try:
chmod 644 secret.txt
Observe the difference.
Key Takeaways

r = Read
w = Write
x = Execute

u = User
g = Group
o = Others

chmod = Change permissions
chown = Change owner
chgrp = Change group
