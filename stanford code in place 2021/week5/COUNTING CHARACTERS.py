def main():
    string=input("ENTER A STRING PLEASE : ")
    string=string.lower()
    dictionary={}
    for ch in string:
        if ch in dictionary:
            dictionary[ch]+=1
        else:
            dictionary[ch]=1
    print(dictionary)


if __name__=="__main__":
    main()
    
