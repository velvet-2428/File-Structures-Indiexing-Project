import pandas as pd
import csv
from itertools import zip_longest
import fileinput
import time
def indi():
    fi=open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv","r",errors="ignore")
    pos=fi.tell()
    line=fi.readline()
    a=line.split(",")
    l=[]
    l1=[]
    while line:
        pos=fi.tell()
        line=fi.readline()
        a=line.split(",")
        l.append(pos)
        l1.append(a[0])
           
    #print(l1)
        

    l2=[l1,l]

    export_data=zip_longest(*l2)
    with open(r'C:\Users\Preethi G\Desktop\fs mini proj\index2.csv','w', newline='',errors="ignore") as myfile:
        wr=csv.writer(myfile)
        wr.writerow(("PrimaryKey","Index Value"))
        wr.writerows(export_data)
    a=pd.read_csv("index2.csv",index_col=0)
    b=a.sort_values(["PrimaryKey"], axis=0,ascending=True)
    d=pd.DataFrame(b)
    d.to_csv("index2.csv")

    myfile.close()
    fi.close()   
def add1():
    start=time.time()
    id1=input("enter id: \n")
    with open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv", 'r',errors="ignore") as myfile:
        if id1 in myfile.read():
            print("primary key present")
        else:
            age1=input("enter category: \n")
            weight1=input("enter city: \n")
            des=input("enter company name: \n")
            des3=input("enter job title: \n")
            des4=input("enter job type: \n")
            des6=input("enter salary offered: \n")
            des7=input("enter Secondary ID: \n")
            with open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv", 'a',errors="ignore") as file:
                str=id1+","+age1+","+weight1+","+des+","+des3+","+des4+","+des6+","+des7
                file.write(str)
                file.write("\n")
                end=time.time()
                print('time taken to insert the file in ms ')
                print(int(end - start))
def dell():
    start=time.time()
    data =pd.read_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv",index_col="id",engine='python')
    del_id = int(input('Enter the id to delete: \n'))
    data.drop([del_id],inplace=True) 
    a=pd.DataFrame(data)
    print("DELETED SUCCESSFULLY")
    b=a.to_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv") 
    end=time.time()
    print('time taken to delete the file in ms ')
    print(int(end - start))
def search1():
    start=time.time()
    fi=open(r"C:\Users\Preethi G\Desktop\fs mini proj\index2.csv","r",errors="ignore")
    line=fi.readline()
    a=line.split(",")
    l=[]

    while line:
        line=fi.readline()
        a=line.split(",")
        l.append(a[0])
      
    l1= l[: len(l) -3]
    #print(l1)
    test_list1= list(map(float, l1))
    l2= list(map(int, test_list1))
       

    def binary_search(l2, low, high, x): 
        if high >= low: 
            mid=(high + low) // 2		
            if l2[mid] == x:
                return mid
            elif l2[mid] >x:
                return binary_search(l2, low, mid - 1, x)
            else:
                return binary_search(l2, mid + 1, high, x)
        else:
            return -1
    x = int(input("enter key "))
    result = binary_search(l2, 0, len(l2)-1, x) 
    if (result==-1):
        print("not found")
        
    else:
        print("found")
        fi=open(r"C:\Users\Preethi G\Desktop\fs mini proj\index2.csv","r",errors="ignore")
        line=fi.readline()
        a=line.split(",")
        l=[]
        while line:
            line=fi.readline()
            a=line.split(",")
            l.append(a[-1])
    
            res = l[: len(l) - 1]
            l2= list(map(int, res))
            for index,value in enumerate(l2): 
                if(result==index):
                    a=value
                    
                    
        
        print(a)
        fi=open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv","r",errors="ignore")
        fi.seek(a)
        b=fi.readline()
        c=b.split(",")
        
        d1=c[0]
        a1=c[1]
        b1=c[2]
        c1=c[3]
        e1=c[4]
        f1=c[5]
        g1=c[6]
        h1=c[7]
        print("Job id: " +c[0])
        print("\n")
        print("Job Category: "+c[1])
        print("\n")
        print("City of Job: " +c[2])
        print("\n")
        print("Company name: "+c[3])
        print("\n")
        print("Job Title: " +c[4])
        print("\n")
        print("Job Type: "+c[5])
        print("\n")
        print("Salary Offered: "+c[6])
        print("\n")
        print("Secondary ID: "+c[7])
        end=time.time()
        print('time taken to search the file in ms ')
        print(int(end - start))
        fi.close()
def modify():
    start=time.time()
    fi=open(r"C:\Users\Preethi G\Desktop\fs mini proj\index2.csv","r",errors="ignore")
    line=fi.readline()
    a=line.split(",")
    l=[]

    while line:
        line=fi.readline()
        a=line.split(",")
        l.append(a[0])
    l1= l[: len(l) - 2]
    #print(l1)
    test_list1= list(map(float, l1))
    l2= list(map(int, test_list1))
       

    def binary_search(l2, low, high, x): 
        if high >= low: 
            mid=(high + low) // 2		
            if l2[mid] == x:
                return mid
            elif l2[mid] >x:
                return binary_search(l2, low, mid - 1, x)
            else:
                return binary_search(l2, mid + 1, high, x)
        else:
            return -1
    x = int(input("enter key "))
    result = binary_search(l2, 0, len(l2)-1, x) 
    if (result==-1):
        print("not found")
    else:
        print("found")
        fi=open(r"C:\Users\Preethi G\Desktop\fs mini proj\index2.csv","r",errors="ignore")
        line=fi.readline()
        a=line.split(",")
        l=[]
        while line:
            line=fi.readline()
            a=line.split(",")
            l.append(a[-1])
    
            res = l[: len(l) - 1]
            l2= list(map(int, res))
            for index, value in enumerate(l2): 
                if(result==index):
                    a=value
        #fi.close()

    f1=open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv","a+",errors="ignore")
    f1.seek(a)
    b=f1.readline()
    c=b.split(",")
    d1=c[0]
    a1=c[1]
    b1=c[2]
    c1=c[3]
    e1=c[4]
    f1=c[5]
    g1=c[6]
    h1=c[7]
    print("Job id: " +c[0])
    print("\n")
    print("Job Category: "+c[1])
    print("\n")
    print("City of Job: " +c[2])
    print("\n")
    print("Company name: "+c[3])
    print("\n")
    print("Job Title: " +c[4])
    print("\n")
    print("Job Type: "+c[5])
    print("\n")
    print("Salary Offered: "+c[6])
    print("\n")
    print("Secondary ID: "+c[7])
    ch=0
    while (ch!=6):
        print("enter 1 to modify Category")
        print("enter 2 to modify City of job")
        print("enter 3 to modify Company name")
        print("enter 4 to modify Job title")
        print("enter 5 to modify Salary Offered")
        print("enter 6 to go back to main menu")
        ch=int(input("PLEASE ENTER YOUR OPTION: "))
        if(ch==1):
            name1=input("Enter the new Category")
            a1=name1
            str=d1+","+a1+","+b1+","+c1+","+e1+","+f1+","+g1+","+h1
            f1=open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv","a+",errors="ignore")
            f1.seek(a)
            f1.write(str)
            data =pd.read_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv",index_col="id")
            data.drop([int(d1)],inplace=True) 
            data1=pd.DataFrame(data)
            data2=data1.to_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv")            
            end=time.time()
            print('time taken to modify the file in ms ')
            print(int(end - start))
            f1.close()
        elif(ch==2):
            name1=input("Enter the new city")
            b1=name1
            str=d1+","+a1+","+b1+","+c1+","+e1+","+f1+","+g1+","+h1
            f1=open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv","a+",errors="ignore")
            f1.seek(a)
            f1.write(str)
            data =pd.read_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv",index_col="id")
            data.drop([int(d1)],inplace=True) 
            data1=pd.DataFrame(data)
            data2=data1.to_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv")
            f1.close()
            end=time.time()
            print('time taken to modify the file in ms ')
            print(int(end - start))
        elif(ch==3):
            name1=input("Enter the new company name")
            c1=name1
            str=d1+","+a1+","+b1+","+c1+","+e1+","+f1+","+g1+","+h1
            f1=open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv","a+",errors="ignore")
            f1.seek(a)
            f1.write(str)
            data =pd.read_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv",index_col="id")
            data.drop([int(d1)],inplace=True) 
            data1=pd.DataFrame(data)
            data2=data1.to_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv")
            f1.close()
            end=time.time()
            print('time taken to modify the file in ms ')
            print(int(end - start))
        elif (ch==4):
            name1=input("Enter the new job title")
            e1=name1
            str=d1+","+a1+","+b1+","+c1+","+e1+","+f1+","+g1+","+h1        
            print(str)
            f1=open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv","a+",errors="ignore")
            f1.seek(a)
            f1.write(str)
            data =pd.read_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv",index_col="id")
            data.drop([int(d1)],inplace=True) 
            data1=pd.DataFrame(data)
            data2=data1.to_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv")
            f1.close()
            end=time.time()
            print('time taken to modify the file in ms ')
            print(int(end - start))
        elif (ch==5):
            name1=input("enter the new salary offered")
            g1=name1
            str=d1+","+a1+","+b1+","+c1+","+e1+","+f1+","+g1+","+h1         
            print(str)
            f1=open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv","a+",errors="ignore")
            f1.seek(a) 
            f1.write(str)
            data =pd.read_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv",index_col="id")
            data.drop([int(d1)],inplace=True) 
            data1=pd.DataFrame(data)
            data2=data1.to_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv")
            f1.close()
            end=time.time()
            print('time taken to modify the file in ms ')
            print(int(end - start))
        
        else:
            main2()
        
    
    fi.close()
#modify()  
def ind():
    fi=open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv","r",errors="ignore")
    pos=fi.tell()
    line=fi.readline()
    a=line.split(",")
    l=[]
    l1=[]
    while line:
        pos=fi.tell()
        line=fi.readline()
        a=line.split(",")
        l.append(pos)
        l1.append(a[-1])
        
        

    l2=[l1,l]

    export_data=zip_longest(*l2)
    with open(r'C:\Users\Preethi G\Desktop\fs mini proj\index5.csv','w', newline='',errors="ignore") as myfile:
        wr=csv.writer(myfile)
        wr.writerow(("secondarykey","Index Value"))
        wr.writerows(export_data)
    a=pd.read_csv("index5.csv",index_col=0)
    b=a.sort_values(["secondarykey"], axis=0,ascending=True)
    d=pd.DataFrame(b)
    d.to_csv("index5.csv")

    myfile.close()
    fi.close()
def search2():
    start=time.time()
    fi=open(r"C:\Users\Preethi G\Desktop\fs mini proj\index5.csv","r",errors="ignore")
    line=fi.readline()
    a=line.split(",")
    l=[]

    while line:
        line=fi.readline()
        a=line.split(",")
        l.append(a[0])
    l1= l[: len(l) - 3]
    l2= list(map(float, l1))
    def binary_search(l2, low, high, x): 
        if high >= low: 
            mid=(high + low) // 2		
            if l2[mid] == x:
                return mid
            elif l2[mid] >x:
                return binary_search(l2, low, mid - 1, x)
            else:
                return binary_search(l2, mid + 1, high, x)
        else:
            return -1
    x = float(input("enter key "))
    result = binary_search(l2, 0, len(l2)-1, x) 
    if (result==-1):
        print("not found")
    else:
        print("found")
        fi=open(r"C:\Users\Preethi G\Desktop\fs mini proj\index5.csv","r",errors="ignore")
        line=fi.readline()
        a=line.split(",")
        l=[]
        while line:
            line=fi.readline()
            a=line.split(",")
            l.append(a[-1])
    
            res = l[: len(l) - 1]
            l2= list(map(int, res))
            for index, value in enumerate(l2): 
                if(result==index):
                    a=value
        

    fi=open(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv","r",errors="ignore")
    fi.seek(a)
    b=fi.readline()
    c=b.split(",")
    
    d1=c[0]
    a1=c[1]
    b1=c[2]
    c1=c[3]
    e1=c[4]
    f1=c[5]
    g1=c[6]
    h1=c[7]
    print("Job id: " +c[0])
    print("\n")
    print("Job Category: "+c[1])
    print("\n")
    print("City of Job: " +c[2])
    print("\n")
    print("Company name: "+c[3])
    print("\n")
    print("Job Title: " +c[4])
    print("\n")
    print("Job Type: "+c[5])
    print("\n")
    print("Salary Offered: "+c[6])
    print("\n")
    print("Secondary ID: "+c[7])
    fi.close()
def dell1():
    start=time.time()
    data =pd.read_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv",index_col="sid",engine='python')
    del_id = float(input('Enter the sid to delete: \n'))
    data.drop([del_id],inplace=True) 
    a=pd.DataFrame(data)
    print("DELETED SUCCESSFULLY")
    b=a.to_csv(r"C:\Users\Preethi G\Desktop\fs mini proj\reed.csv")
    ind() 
    end=time.time()
    print('time taken to delete the file in ms ')
    print(int(end - start))    
def main2(): 
    print("------WELCOME TO JOB DATASET------")
    ch=0
    while(ch!=7):
        print("PRESS 1 TO ADD A NEW JOB RECORD")
        print("PRESS 2 TO DELETE A JOB RECORD BASED ON PRIMARY KEY ")
        print("PRESS 3 TO DELETE A JOB RECORD BASED ON SECONDARY KEY ")
        print("PRESS 4 TO SEARCH FOR A RECORD BASED ON PRIMARY KEY")
        print("PRESS 5 TO SEARCH FOR A RECORD BASED ON SECONDARY KEY")
        print("PRESS 6 TO MODIFY A RECORD")
        print("PRESS 7 TO EXIT")
        ch=int(input("PLEASE ENTER YOUR OPTION: "))
        if(ch==1):
            indi()
            ind()
            add1()
            indi()
            ind()
        elif (ch==2):
            indi()
            ind()
            dell()
            indi()
            ind()
        elif (ch==3):
            ind()
            indi()
            dell1()
            ind()
        elif (ch==4):
            indi()
            search1()
            indi()
        elif (ch==5):
            ind()
            search2()
            ind()     
        elif (ch==6):
            indi()
            ind()
            modify()
            ind()
            indi()
        else:
           print("invalid choice") 
           
main2()