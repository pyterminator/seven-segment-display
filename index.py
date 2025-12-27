# https://youtube.com/@PyTerminator

def p(text): print(text, end="\t")

def create(str_num):
    for row in range(1, 6):
        for ch in str_num:
            if row == 1:
                if ch == "1": p("  #")
                elif ch in "23567890": p("#"*3)
                elif ch == "4": p("# #")
            elif row == 2:
                if ch in "1237": p("  #")
                elif ch in "4890": p("# #")
                elif ch in "56": p("#  ")
            elif row == 3:
                if ch in "17": p("  #")
                elif ch in "2345689": p("#"*3)
                elif ch == "0": p("# #")
            elif row == 4:
                if ch in "134579": p("  #")
                elif ch in "2": p("#  ")
                elif ch in "680": p("# #")
            elif row == 5:
                if ch in "147": p("  #")
                elif ch in "2356890": p("#"*3)
        print()

while True:
    try:
        str_number = input("Ədəd daxil edin : ")
        int(str_number)
        if str_number == "-1": break
        create(str_number)
    except: 
        print("Ədəd daxil edin !!!")
        continue
    
    
