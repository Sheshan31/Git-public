observe1="What's happening!!"
def passport_check(passport_no):
    observe4="actual copied to formal"
    observe5="func. execution starts"
    if(len(passport_no)==8):
        if(passport_no[0]>="A" and passport_no[0]<="Z"):
            status="valid"
        else:
            status="invalid"
    else:
        status= "invalid"
    observe6="func. execution ends"
    return status
observe2="function with formal arg."
observe3="calling with actual arg."
passport_status=passport_check("M9993471")
print("Passport is",passport_status)
#observe1,2,3,4,5,6 are temporary variables used to explain this concept
