user={"admin":["create", "update", "delete","reports"],
      "teacher":["view", "attendance", "reports"],
      "student":["own_attendance"]}
def check_permission(username, permission):
    if permission in user[username]:
        print("Permission granted")
    else:
        print("Permission denied")
print("user:")
print("1.admin")
print("2.teacher")
print("3.student")
username = input("\nEnter username: ") 
print("\nPermissions:")
print("1.create")
print("2.update")
print("3.delete")
print("4.view")
print("5.attendance")
print("6.reports")
print("7.own_attendance")
permission = input("\nEnter permission to check: ")
check_permission(username, permission)

