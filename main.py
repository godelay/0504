import datetime
import re

def create_membership():
		# 아래 코드는 python에 내장되어 있는 datetime 모듈을 활용하여 오늘 날짜를 입력하는 코드입니다. 
		# stnr_date 코드는 제가 작성했으니, 건드리지 않으셔도 되옵니다 :)
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    
    users = []

    while  True:
        user = {}
		# user 딕셔너리에 username, password, email을 아래 주어진 제한 조건에 알맞게 입력받는 코드를 작성하세요.
	    # user 딕셔너리 값에는 username, password, email, stnr_date 총 4가지 값이 저장되어야 합니다.

        while True:
            print('회원가입을 진행하시겠습니까?\ny:진행       n:취소')
            register_input = input('>> ')
            register_input = register_input.lower()

            if register_input == 'y':
                register = True
                print('==============\n 회원가입이 진행됩니다 \n==============')
            elif register_input == 'n':
                print ('==============\n 회원가입이 취소됩니다 \n==============')
                exit()
            else: 
                print ('입력 값을 확인해주세요')

            while True:
                id = input ('ID: ')
                regex_hangeul = re.compile("^[ㄱ-힣]+$")
                hangeul_check = regex_hangeul.match(id)
                if (len(id) >= 2 and len(id) <= 4 and hangeul_check):
                    break
                else:
                    print("한글로 2~4글자로 입력해주세요")
                    continue

            while True:
                password = input('PW: ')
                if (len(password) >= 8 and password[0].isupper() == True and ("!" in password or "@" in password or "#" in password or "$" in password)):
                    break
                else:
                    print("Try again")
                    continue

            name = input('이름: ')

            while True:
                email = input ('email: ')
                if email.endswith('.com'):
                    print(email)
                    break
                else:
                    print('처리할 수 없는 이메일 주소입니다.')

    sers.append(user)

    return users
        
'''        
id 제한 조건
- 한글만 입력 받아야 함
- 총 글자 수는 2-4글자

password 제한 조건
- 첫 문자는 영문 대문자
- 총 글자 수는 8글자 이상
- 특수문자 (!, @, #, $) 중 1가지 반드시 포함

email 제한 조건
- @를 제외한 특수문자는 입력될 수 없음 (입력 가능한 문자는 숫자와 영문)
- 통상적인 email 포맷을 따름
  * @을 포함하고, '.com'으로 이메일 주소가 끝나야 함
  

/데이터 예시/
{홍산하, Asdf1234!, sannah@naver.com, 20230427}
{김한준, Q1w2e3r4!, zhivagokim@naver.com, 20230427}
{천승범, Zxcv4860!, vision6@naver.com, 20230427}

반복문과 조건문을 잘 활용하여, 사용자가 입력을 중단할 때까지 입력 받을 수 있도록 코드를 작성할 것
"""
''' 

def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding='UTF-8')
    # user_list에 있는 user 3명의 딕셔너리 값을 txt에 작성하세요.
	  # 올바르게 생성된 텍스트 파일i의 예시는 상단에 이미지로 첨부되어 있습니다.https://github.com/yg111703/HW5
    f.close()
    
def run():
		# 위에서 정의한 create_membership 함수가 실행되어 반환된 결과값을 user_list 객체에 저장합니다.
    user_list = create_membership()
    # 위에 생성된 user_list 객체를 load_to_txt 함수의 입력변수로 활용하여 txt 파일을 생성합니다.
    load_to_txt(user_list)
    
run()