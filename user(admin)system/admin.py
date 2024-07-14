from user import User,Admin,Privileges

user_1=User('Kobe','Bryant')
user_1.describe_user()
user_1.greet_user()
admin_1=Admin('Li','Bai')
admin_1.describe_user()
admin_1.privileges.show_privileges()

