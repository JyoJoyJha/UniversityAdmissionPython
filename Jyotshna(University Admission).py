def numseat():
    import pickle
    c=0
    with open('University.dat','rb') as f:
        try:
            d=pickle.load(f)
            for i in d:
                c+=1
            global n
            n=1270-c
        except EOFError: n=1270
    if n>0:
        return True
    else:
        return False

def option4():
    import pickle
    import random
    import os
    adno=random.randint(10000,99999)
    f1=open('University.dat','rb')
    try:
        d=pickle.load(f1)
        f1.close()
        print('The Courses Available:')
        print("1. Bachelor's in Science(4 years)")
        print("2. Master's in Science(3 years)")
        print('3. Computer Engineering(4 years)')
        print("4. Bachelor's in Technology(4 years)")
        print("5. Master's in Technology(3 years)")
        print(' ')
        print('Please Enter the following details for admission:')
        print(' ')
        l=[]
        l.append(input('Enter the Students name(As in Passport): '))
        l.append(input('Enter Nationality(As in Passport): '))
        l.append(input('Enter Parent/Guardian Mobile number: '))
        l.append(input("The course student is interested in(CAPITAL LETTERS): "))
        l.append(int(input('Percentile acheived by Student in Entrance Examination: ')))
        l.append(input('Name of the School(graduated Grade 12): '))
        l.append(input('Any Dissability? If any please mention or NA: '))
        l.append(input('Passport Number(9 Digits): '))
        l.append(input('Type of Visa(Block Letters): '))
        l.append(input('Enter the VISA Number(8 Digits): '))
        l.append('NOT PAID')
        l.append('NOT PAID')
        f2=open('University1.dat','ab')
        d[adno]=l
        pickle.dump(d,f2)
        f2.close()
        os.remove('University.dat')
        os.rename('University1.dat','University.dat')
        global n
        n-=1
        print(' ')
        print('Congratulations!!! The student code of your child is:',adno)
        print(' ')
        print('Details entered:',d[adno])
    except EOFError:
        d={}
        f=open('University.dat','ab')
        pickle.dump(d,f)
        f.close()
        print('End Of File Error! Please Try Again.')

def option5():
    import pickle
    f=open('University.dat','rb')
    try:
        d=pickle.load(f)
        no=int(input('Please Enter the student code:'))
        print(' ')
        if no in d:
            print('The Details Entered Are as Follows: ')
            print('Name of the student:                  ',d[no][0])
            print('Nationality:                          ',d[no][1])
            print('Parent/Guardian Mobile number entered:',d[no][2])
            print('Course opted:                         ',d[no][3])
            print('Entrance examination percentile:      ',d[no][4])
            print('School(Graduated Grade 12):           ',d[no][5])
            print('Disability(if any):                   ',d[no][6])
            print('Passport Number(As Entered):          ',d[no][7])
            print('Type of Visa(As Entered):             ',d[no][8])
            print('Visa number(As Entered):              ',d[no][9])
            print('Registration Amount status:           ',d[no][10])
            print('Fee Status:                           ',d[no][11])
        else:
            print('Student ID not valid')
    except EOFError: print('No Student Information Available.')
    
def option6():
    import pickle
    f=open('University.dat','rb')
    try:
        d=pickle.load(f)
        if d=={}:
            print('No Students Are Enrolled')
        else:
            print('%15s'%'Student ID','%25s'%'Name Of The Student', '%30s'%'Course Opted')
            for no in d:
                print('%15s'%no,'%25s'%d[no][0], '%30s'%d[no][3])
    except EOFError: print('No Students Are Enrolled')
    f.close()

def option7():
    import pickle
    import os
    f=open('University.dat','rb')
    try:
        d=pickle.load(f)
        f.close()
        no=int(input('Enter the Student Code:'))
        if no in d:
            print('The Information that can modify:')
            print('1. Name')
            print('2. Parent/Guardian Mobile number:')
            print('3. Any Disability')
            print('4. Passport Number')
            print('5. Type of Visa')
            print('6. Visa Number')
            print(' ')
            ch=int(input('Enter the choice you want to modify(1/2/3/4/5/6):'))
            print(' ')
            if ch==1:
                n=input('Enter the Modified Name(As in Passport):')
                d[no][0]=n
            elif ch==2:
                mob=input('Enter Changed Parent/Guardian Mobile Number:')
                d[no][2]=mob
            elif ch==3:
                a=input('Any Disability? If any please Mention or NA:')
                d[no][6]=a
            elif ch==4:
                p=input('Enter the Modified Passport Number:')
                d[no][7]=p
            elif ch==5:
                t=input('Enter the modified type of visa(BLOCK LETTERS):')
                d[no][8]=t
            elif ch==6:
                v=input('Enter the Modified Visa Number:')
                d[no][9]=v
            f2=open('University1.dat','ab')
            pickle.dump(d,f2)
            f2.close()
            os.remove('University.dat')
            os.rename('University1.dat','University.dat')
        else:
            print('Student ID Not Valid')
    except EOFError: print('No Student Details Available')    

def option8():
    import pickle
    import os
    f=open('University.dat','rb')
    try:
        d=pickle.load(f)
        f.close()
        print('Congratulations!!! Your child has Graduated!!!')
        print('Certificate must be collected at the University Reception')
        print('For final certificate and Confirmation, please enter student code:')
        print(' ')
        no=int(input('Enter Student Code:'))
        if no in d:
            del d[no]
            print('NOTE: Another Certificate will not be Issued on request.')
            print('      Do collect the certificate within 3 months from graduation')
            f2=open('University1.dat','ab')
            pickle.dump(d,f2)
            f2.close()
            os.remove('University.dat')
            os.rename('University1.dat','University.dat')
        else:
            print('Student ID Not Valid!')
    except EOFError: print('No Student Details Available.')

def option9():
    import pickle
    import os
    f=open('University.dat','rb')
    try:
        d=pickle.load(f)
        f.close()
        print('Do Ensure that you have registered the students details for admission and recieved student code')
        print(' ')
        no=int(input('Enter student code:'))
        if no in d:
            print('Registration amount status:',d[no][10])
            if d[no][10]=='NOT PAID':
                print('The total Registration amount is: $350')
                print('MODE OF PAYMENT:(1.CARD//2.CHEQUE)')
                mop=int(input('Enter Mode Of Payment(1/2):'))
                if mop==1:
                    cardno=int(input('Enter Card Number:'))
                    code=int(input('Enter three-digit CVV:'))
                    print('Please Wait...')
                    import random
                    r=random.randrange(10000,99999)
                    import time
                    for i in range(2,0,-1):
                        time.sleep(1)
                    print('***MOBILE: The code for your Transaction with Vanderwall Science University is***:',r)
                    c=int(input('Enter the Code sent on your mobile number:'))
                    if c==r:
                        print('Transaction Successful')
                        d[no][10]='PAID'
                    else:
                        print('Transaction Unsuccessful')
                elif mop==2:
                    print("Make Sure that the cheque is named to: 'Vanderwall Science University, Florida'")
                    print(' ')
                    chno=int(input('Enter 10 digit Cheque number(ONLY DIGITS):'))
                    print('Please Email the Photocopy of the cheque to: VanderwallScience.University@outlook.com')
                    print('Transaction Successful')
                    d[no][10]='PAID'
                print('Registration amount status:',d[no][10])
            else:
                print('Registeration Amount Already Paid')
            f2=open('University1.dat','ab')
            pickle.dump(d,f2)
            f2.close()
            os.remove('University.dat')
            os.rename('University1.dat','University.dat')
        else:
            print('Student ID Not Valid')
    except EOFError: print('No Student Details Available')

def option10():
    import pickle
    import os
    f=open('University.dat','rb')
    try:
        d=pickle.load(f)
        f.close()
        no=int(input('Enter the student code:'))
        print(' ')
        print('Do ensure that you have paid the registration amount:')
        if no in d:
            if d[no][10]=='PAID':
                if d[no][11]=='NOT PAID':
                    print("1. For BACHELOR'S IN SCIENCE: $10000/annum")
                    print("2. For MASTER'S IN SCIENCE: $13000/annum")
                    print('3. For COMPUTER ENGINEERING: $9599/annum')
                    print("4. For BACHELOR'S IN TECHNOLOGY: $14000/annum")
                    print("5. For MASTER'S IN TECHNOLOGY: $15000/annum")
                    print(' ')
                    ch=int(input('Enter your chosen choice of course:'))
                    if ch==1:
                        print('Total Amount to be paid: $', (10000)*(4))
                    elif ch==2:
                        print('Total Amount to be paid: $', (13000)*(3))
                    elif ch==3:
                        print('Total Amount to be Paid: $', (9599)*(4))
                    elif ch==4:
                        print('Total Amount to be Paid: $', (14000)*(4))
                    elif ch==5:
                        print('Total Amount to be Paid: $', (15000)*(3))
                    print(' ')
                    print('Mode of Payment(1.CARD//2.CHEQUE)')
                    mop=int(input('Enter Mode Of Payment(1/2):'))
                    if mop==1:
                        cardno=int(input('Enter Card Number:'))
                        code=int(input('Enter three-digit CVV:'))
                        print('Please Wait...')
                        import random
                        r=random.randrange(10000,99999)
                        import time
                        for i in range(2,0,-1):
                            time.sleep(1)
                        print('***MOBILE: The code for your Transaction with Vanderwall Science University is***:',r)
                        c=int(input('Enter the Code sent on your mobile number:'))
                        if c==r:
                            print('Transaction Successful')
                            d[no][11]='PAID'
                        else:
                            print('Transaction Unsuccessful')
                    elif mop==2:
                        print("Make Sure that the cheque is named to: 'Vanderwall Science University, Florida'")
                        print(' ')
                        chno=int(input('Enter 10 digit Cheque number:'))
                        print('Please Email the Photocopy of the cheque to: VanderwallScience.University@outlook.com')
                        print('Transaction Successful')
                        d[no][11]='PAID'
                    print('Fee Payment status:',d[no][11])
                else:
                    print('Payment Already done')
            else:
                print('   ')
                print('Please Pay Registration Amount!!!')
            f2=open('University1.dat','ab')
            pickle.dump(d,f2)
            f2.close()
            os.remove('University.dat')
            os.rename('University1.dat','University.dat')
        else:
            print('Student ID Not Valid')
    except EOFError: print('No Student Details Available.')

ch='y'
while ch.lower()=='y':
    l=[]
    print('VANDERWALL SCIENCE UNIVERSITY')
    print("         Welcome to Vanderwall Science University")
    print("Please make a suitable Selection:")
    print("**********************************************")
    print("MENU")
    print("**********************************************")
    print("1.  NO. OF SEATS AVAILABLE")
    print("2.  ELIGIBILTY CRITERIA(COURSES AVAILABLE)")
    print("3.  FEE STRUCTURE(ANNUAL)")
    print("**********************************************")
    print("MAINTENANCE")
    print("**********************************************")
    print("4.  NEW ADMISSION")
    print("5.  VIEW DETAILS OF STUDENT(ROLL NO. WISE)")
    print("6.  VIEW ALL STUDENTS WITH COURSE")
    print("7.  MODIFY STUDENT DETAILS")
    print("8.  GRADUATES (REMOVAL OF INFORMATION)")
    print("**********************************************")
    print("TRANSACTION")
    print("**********************************************")
    print("9.  REGISTRATION PAYMENT")
    print("10. FEE PAYMENT")
    print("**********************************************")
    print("11. EXIT")
    print(' ')
    choice=int(input("Enter your choice(1 - 11):"))
    print(' ')
    if choice==1:
        if numseat():
            print('The Number of seats available:',n)
        else:
            print('No Seats available')
    elif choice==2:
        print('The Courses Available:')
        print("1. Bachelor's in Science(4 years)")
        print("2. Master's in Science(3 years)")
        print('3. Computer Engineering(4 years)')
        print("4. Bachelor's in Technology(4 years)")
        print("5. Master's in Technology(3 years)")
        print(' ')
        print('Please Confirm That Your Ward Has Written The Entrance Examination!!!')
        print(' ')
        ch=int(input('Enter the choice(1/2/3/4/5):'))
        print(' ')
        if ch==1:
            print('Eligibility: 80 percentile and above in Entrance Exam')
        elif ch==2:
            print("Eligibility: 85 percentile and above in BACHELOR'S IN SCIENCE OR in Entrance Exam")
        elif ch==3:
            print('Eligibility: 80 percentile and above in Entrance Exam')
        elif ch==4:
            print('Eligibility: 85 percentile and above in Entrance Exam')
        elif ch==5:
            print("Eligibility: 87 percentile and above in BACHELORS'S IN TECHNOLOGY OR in Entrance Exam")
    elif choice==3:
        print("For BACHELOR'S IN SCIENCE: $10000/annum")
        print("For MASTER'S IN SCIENCE: $13000/annum")
        print('For COMPUTER ENGINEERING: $9599/annum')
        print("For BACHELOR'S IN TECHNOLOGY: $14000/annum")
        print("For MASTER'S IN TECHNOLOGY: $15000/annum")
    elif choice==4:
        if numseat():
            option4()
        else:
            print('Sorry Seats unavailable')
    elif choice==5:
        option5()
    elif choice==6:
        option6()
    elif choice==7:
        option7()
    elif choice==8:
        option8()
    elif choice==9:
        option9()
    elif choice==10:
        option10()
    elif choice==11:
        print('Thank You For Visiting Our Website')
        print('Have a Nice Day')
        break
    else:
        print('Invalid Option')
    print(' ')
    ch=input('Do You Want to visit the homepage Again?(Y/N):')
