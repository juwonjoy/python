
class User:
  
  #생성자의 self는 객체 생성시 자동 주입된다.
  #__init__이 함수가 생성자 
     def __init__(self,username,password="1234"):
      self.username = username
      self.password = password

    

u= User("ssar","1234")
u1=User("cos")

print(u.username)

#생성자가 있어야 가능! (클래스를 딕셔너리로 변환 해줌 )
print(u.__dict__)