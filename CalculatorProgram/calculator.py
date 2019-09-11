# incomplete
def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL < 60:
        return "Borderline low"
    else:
        return "low"

def check_LDL(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result <= 159:
        return "Borderline high"
    elif 160 <= LDL_result <=189:
        return "High"
    else: # > 190
        return "Very high"

def cholestorol_interface():
    print("Cholestorol check")
    chol_input = input("Enter your cholestorol test result:")
    chol_data = chol.split("=")
    if chol_data[0] in ["LDL", "HDL", "TLC"]:
        print("Good input")
    else:
        print("Bad input")
    if chol_data[0] == "HDL":
        result = check_HDL(chol_data[1])
        print("The cholestorol level is {}.".format(result))

def interface():
    print("My calculator program")
    keep_running = True
    while keep_running:
        print("My Program")
        print("Options")
        print("9-Quit")
        choice = input("Enter your choice:")
        if choice == '9':
            keep_running = False
    return

if __name__ == '__main__':
    interface()
