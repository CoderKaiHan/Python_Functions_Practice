#define functions
def hello():
    print("Hello!")

def pack(arg1, arg2,arg3):
    return [arg1, arg2, arg3]

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty.")
    else:
        print(f"First I eat {lunch_list[0]}.")
        lunch_list.pop(0)
        print("Next I eat", lunch_list)


#Call functions

hello()

pack("Moring","Noon","Afternoon")

eat_lunch(["appetizers","entrees","sides","juice","deserts","tea"])

my_lunch = ["appetizers","entrees","sides","juice","deserts","tea"]
eat_lunch(my_lunch)


pack = pack("Moring","Noon","Afternoon")
eat_lunch(pack)
