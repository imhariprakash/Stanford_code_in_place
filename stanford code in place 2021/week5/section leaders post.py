import json

def main():
    ed_data=json.load(open("ed.json"))
    teacher_count=0
    print("Total number of posts: ",len(ed_data))

    for role in ed_data:
        
        role_str=role['user']['role']
        if role_str=='admin' or role_str=='tutor':
            teacher_count+=1
    print("Total number of posts by teachers: ",teacher_count)
    print((teacher_count / len(ed_data))*100)
        
    
        
        
        



if __name__=="__main__":
    main()
