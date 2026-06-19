# age = 10
# if age > 18 and age <60:
#    print ("pay taxes")
#else: 
#    print ("enjoy life")


if_logged = True
if_admin = True

if if_logged:
    print ("User logged in")
    if not if_admin:
        print ("Regular User")
    else:
        print ("Admin user ")
else:
    print ("User not logged in")
