## 인터페이스
- 기능에 대한 선언과 구현을 분리

## 델리게이트
- 특정 객체의 기능을 사용하기 위해 다른 객체의 기능을 호출하는 것

## strategy pattern
- 여러 알고리즘의 추상적인 접근점을 만들어 `접근점` 에서 서로 교환 가능하도록 하는 패턴

### 예시
- `weapon` 이라는 `interface` 가 있고 `attack` 이라는 `추상 메소드` 가 존재한다
- 그리고 그 interface를 상속받아서 구현한 `knife`, `sword` 등이 있다
- `character` 라는 `class` 에서는 `interface weapon 변수를 세팅` 한다
- 즉 여기서 `character가 접근점` 이다
- 실제로 사용할 때는 
````python
character = Character()
# 이 접근점에서 구현체들을 넣을 수 있다
character.set_weapon(Knife())
character.attack()
````

### 만약 도끼 추가를 원한다면?
- weapon interface를 가져와서 Ax 구현체를 만들어주면 된다
- OCP에 좋다!
