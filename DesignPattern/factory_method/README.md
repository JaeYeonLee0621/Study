## 목표
- 구조와 구현 분리를 이해하고 구조와 구현의 분리의 장점을 안다

## 예시

### 요구 사항
- 게임 아이템과 아이템 생성 구현
    - 아이템 생성 전 데이터 베이스에서 아이템 정보 요청
    - 아이템 생성 후 불법 복제 방지를 위한 로그 남김
- 아이템 생성 주체는 item_creator
- 아이템은 item interface
    - item은 use함수를 가짐
    - 아이템 종류는 체력, 마력 물약
    
### 구현
- ItemCreator 추상 클래스를 생성한다
    - 아이템을 생성하는 함수를 create 함수로 생성한다
        - 아이템을 생성하는 로직대로 함수를 놓는다
            - request_item_information 
            - create_item
            - create_item_log
    - request_item_information이라는 추상 함수를 생성한다 (protected)
    - create_item_log라는 추상 함수를 생성한다 (protected)
    - create_item이라는 아이템 생성 알고리즘을 위한 함수를 생성한다
- Item 인터페이스를 생성한다 
- HpPotion이라는 구현체를 만들고 Item 인터페이스를 상속한다
    - use라는 추상 함수를 만들고 그 안에 구현한다
- MpPotion이라는 구현체를 만들고 Item 인터페이스를 상속한다
    - use라는 추상 함수를 만들고 그 안에 구현한다
- HpCreator라는 구현체를 만들고 ItemCreater 추상 클래스를 생성한다
    - 그 안에 함수를 구현한다
    - create_item에서는 HpPotion을 return 한다
- MpCreator라는 구현체를 만들고 ItemCreater 추상 클래스를 생성한다
    - 그 안에 함수를 구현한다  
    - create_item에서는 MpPotion을 return 한다
- Main
    - ItemCreator를 선언하고 Creator에 HpCreator, MpCreator를 만든다
    - 그리고 두 아이템의 Potion을 받아본다
    - 두 아이템을 사용해본다