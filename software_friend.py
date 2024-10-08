import re  # 정규표현식을 사용하기 위해 re 모듈을 불러옴

def print_menu():
    # 메뉴 출력
    print("\n=== 친구 연락처 관리 프로그램 ===")
    print("1. 친구 추가")
    print("2. 친구 삭제")
    print("3. 친구 이름 변경")
    print("4. 친구 리스트 출력")
    print("5. 즐겨찾기 추가")
    print("6. 즐겨찾기 목록 ")
    print("7. 종료")

# 연락처와 생일 형식 
def friend_birthday(birthday):
    # 정규표현식을 사용하여 생일이 YYYY-MM-DD 형식인지 확인
    return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", birthday))

def friend_phone(phone):
    # 정규표현식을 사용하여 연락처가 010-XXXX-XXXX 형식인지 확인
    return bool(re.match(r"^010-\d{4}-\d{4}$", phone))

# 친구 추가 함수
def add_friend(contacts):
    # 친구의 이름과 그룹
    name = input("추가할 친구의 이름: ")
    group = input("그룹(친구와 어떤 관계):")

    # 유효한 연락처 
    while True:
        # 연락처 입력
        phone = input("연락처를 입력(ex.010-1234-5678): ")
        #예시 대로 입력하지 않으면 다시 입력
        if friend_phone(phone):
            break
        print("형식이 잘못되었습니다. 다시 입력 해주세요!")

    # 유효한 생일 
    while True:
        # 생일 입력
        birthday = input("생일을 입력(ex. YYYY-MM-DD): ")
        # 예시대로 입력하지 않으면 다시 입력
        if friend_birthday(birthday):
            break
        print("잘못된 형식입니다. 다시 입력하세요.")
    
    contacts[name] = {'phone': phone, 'birthday': birthday, 'group':group}
    print(f"{name} 친구가 추가되었습니다.") 

# 친구 삭제 함수
def remove_friend(contacts):
    # 삭제할 친구 이름 입력받음
    name = input("삭제할 친구의 이름을 입력하세요: ")
    if name in contacts:
        del contacts[name]  
        print(f"{name} 친구가 삭제되었습니다.")  
    else:
        print(f"{name} 친구를 찾을 수 없습니다.")

# 친구 이름 변경 함수
def update_friend(contacts):
    # 변경할 친구 이름 입력받음
    name = input("변경할 친구의 이름을 입력하세요: ")
    # 입력한 친구가 딕셔너리에 있는지 확인
    if name in contacts:
        # 새 이름 입력받음
        new_name = input(f"{name}의 새 이름을 입력하세요: ")
        # 기존 이름을 삭제하고 새 이름으로 정보 옮기기
        contacts[new_name] = contacts.pop(name)  
        print(f"{name}의 이름이 {new_name}(으)로 변경되었습니다.") 
    else:
        # 친구 이름을 찾을 수 없으면 에러 메시지 출력
        print(f"{name} 친구를 찾을 수 없습니다.")

# 친구 리스트 출력 함수
def list_friend(contacts):
    if contacts:
        print("\n친구 리스트")
        print(f"{'이름':<15}{'연락처':<15}{'생일':<15}{'그룹':<15}")
        print("="*60)  # 구분선 출력
       
        [print(f"{name:<15}{info['phone']:<15}{info['birthday']:<15}{info['group']:<15}") for name, info in contacts.items()]
    else:
        print("등록된 친구가 없습니다.")

# 즐겨찾기 추가 함수
def bookmark_add_friend(contacts, favorites):
    name = input("즐겨찾기에 추가할 친구 이름: ")
    if name in contacts:
        if name not in favorites:
            favorites.append(name)
            print(f"{name} 친구가 즐겨찾기에 추가되었습니다.")
        else:
            print(f"{name} 친구는 이미 즐겨찾기에 있습니다.")
    else:
        print(f"{name} 친구를 찾을 수 없습니다.")    

# 즐겨찾기 목록 출력 함수
def bookmark_friend(favorites):
    if favorites:
        print("\n즐겨찾기 리스트")
        print(f"{'이름':<15}")
        print("="*60)  # 구분선 출력
        [print(f"{name:<15}") for name in favorites]
    else:
        print("즐겨찾기에 등록된 친구가 없습니다.")

# 메인 함수
def main():
    contacts = {}  # 친구 정보를 저장할 딕셔너리 초기화
    favorites = []  # 즐겨찾기 목록을 저장할 리스트 초기화
    
    while True:
        print_menu()  # 메뉴 출력
        choice = input("원하는 기능을 선택하세요 (1-7): ")
        
        if choice == '1':
            add_friend(contacts)  # 친구 추가
        elif choice == '2':
            remove_friend(contacts)  # 친구 삭제
        elif choice == '3':
            update_friend(contacts)  # 친구 이름 변경
        elif choice == '4':
            list_friend(contacts)  # 친구 리스트 출력
        elif choice == '5':
            bookmark_add_friend(contacts, favorites)  # 즐겨찾기에 추가
        elif choice == '6':
            bookmark_friend(favorites)  # 즐겨찾기 목록 출력
        elif choice == '7':
            print("프로그램을 종료합니다.")  # 프로그램 종료
            break  # while 루프 탈출
        else:
            print("올바른 번호를 선택하세요.")

# 프로그램 시작
if __name__ == "__main__":
    main()  # 메인 함수 실행
