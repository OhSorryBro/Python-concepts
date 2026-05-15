# 9.10. Imported class Restaurant. 
# Move the latest version of the Restaurant class into a module and create a separate file that imports this class. 
# Create an instance of the Restaurant class, then call one of its methods to verify that the import works correctly.
import restaurant
restaurant_1 = restaurant.Restaurant('Dodo', 'Unknown')
restaurant_1.describe_restaurant()

# 9.11. Imported class Admin.
# Start from exercise 9.8. Place the User, Privileges, and Admin classes in a single module. 
# Prepare a separate file, create an instance of the Admin class in it, and call the show_privileges() method to verify that everything works correctly.
print("====")


# 9.12. Multiple modules. 
# Place the User class in one module, and Privileges and Admin in a separate one. Then in another file, create an instance of the Admin class and call the show_privileges() method to verify that everything works correctly.
print("====")
import priviliges
admin_1 = priviliges.Admin('name','b','any',12)
admin_1.privileges.show_privileges()