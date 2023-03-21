# to check the authenticity of the user
    while (str1 == "Ajay Kumar" and str2 == "AjayKumar@22") or (str1 == "Gunjan Thakur" and str2 == "GunjanThakur@22") or (str1 == "Gayatri Koshal" and str2 == "GayatriKoshal@22"):
        N = int(input("What do you want to do? "))
        # to see the Dataframe: Attendance
        while N == 1:
            print(df)
            N=0
# to see the Dataframe: ST1, ST2, ETE1 Result and individual progress report
        while N == 2:
            var = input()
            if var == "ST 1":
                print(df1)
            elif var == "ST 2":
                print(df2)
            elif var == "ETE 1":
                print(df3)
            elif var == "Show Overall Progress Report":
                print(df6)
            elif var == "Show Subjectwise Progress Report":
                while True:
                    s = input("Enter the Subject: ")
                    if s == "MCP":
                        print(df4)
                    elif s == "Python":
                        print(df5)
                    else:
                        print("Subject Not Found")
                        break
            else:
                print("Invalid TestName")
                N=0
# to check the attendance of any particular student
        while N == 3:
            S4=int(input("Enter the Student Roll Number: "))
            data2 = df.loc[S4]
            print("\nStudent Attendance%: \n\n",data2)
            N=0
