## 명명법
- 함수와 변수의 이름은 길어도 괜찮으니 그 함수가 **어떤 역할을 하는지 정확하게 짓는다** (마치 읽으면 소설처럼 읽힐 수 있도록)
- 각 함수는 `하나의 기능` 을 해야하며 조건문으로 나누어서 기능이 분리되어도 안된다
- **함수의 인수는 하나도 없는 것** 을 추구하며 1개가 허용할 수 있는 범위이다
- 함수의 인수로 Boolean 값이 들어가면 조건문으로 분리가 된다는 뜻이기 때문에 Boolean을 쓴다는 것은 좋지 않은 함수를 썼다는 말과 같다
- 함수 인수의 타입을 명명해 놓는 것이 좋다
- **반복되는 함수는 무조건 지양**
- 오류처리도 한가지 작업이므로 함수로 분리한다

<br/>

## 주석
- **달지마라**
- 주석을 다는 경우는 자신이 코드를 잘 못 짰다는 것과 같다
- 보통의 코드는 주석 없이 읽힐 수 있도록 해야한다

<br/>

## 형식
- **신문 기사처럼 작성**
- 개념은 빈 행으로 분리하라
- 연관이 있는 것들은 세로 밀집도를 좁혀라
- 서로 **밀접한 개념은 세로로 가까이** 둬야한다 > 한 파일에 속해야한다
  - 변수 선언 : 변수는 사용하는 위치에 최대한 가까이 둬야 한다
  - 인스턴스 변수 : 클래스 맨 처음에 선언한다 간혹 가위 규칙으로 클래스 마지막에 선언하는 경우도 있으나 어쩻든 알아볼 수 있게만 선언하면 된댜
  - 종속 함수
    - 다른 함수를 호출한다면 두 함수는 세로로 가까이 배치한다
    - `가능하다면 호출하는 함수를 호출 되는 함수보다 먼저 배치한다`
  - 개념적 유사성 : 비슷한 행위를 하는 함수라면 코드를 가까이 배치한다

<br/>

## 객체와 자료구조
- **디미터의 법칙** : 모듈은 자신이 조작하는 객체의 속사정을 몰라야한다
- 객체는 동작을 공개하고 자료를 숨긴다 > 기존 동작을 변경하지 않으면서 새 객체타입을 추가하기는 쉽지만, 기존 객체에 새 동작을 추가하기는 어렵다
- 자료구조는 별다른 동작없이 자료를 노출한다 > 기존 자료구조에 새 동작을 추가하기는 쉬우나 기존함수에 새 자료구조를 추가하기는 어렵다
- 즉 OOP와 절차지향언어를 잘 섞어서 사용하자

<br/>

## 예외 처리
- try except를 너무 많이 사용하는 로직은 wrapper class를 만들어 분리하라 > 비즈니스 로직과 예외 처리가 분리된다
- **except 안에 비즈니스 로직을 넣지 마라** > 해당 부분을 빼서 작업해라
- ex) 매우 좋지 않은 코드
```python
try:
  sum_ += get_total()
except:
  sum_ += -1
```
- ex) 더 나은 코드
```python
sum_ += get_total()

def get_total():
  try: return total
  except: return -1
```
- **null을 반환하지 마라** > 모든 곳에서 None을 확인해야한다면 더러운 코드가 될 확률이 높다
- null대신 assert를 이용한다

<br/>

## 경계 
- **외부 코드 사용시에는 Class로 캡슐화** 를 하고 해당 Class를 실제 코드에 반영하는 것이 좋다
    - 이는 외부 패키지를 변경할 때 Class안의 내용만 변경해주면 되기 때문에 훨씬 용이하다
- 외부 패키지를 사용할 때는 `학습 테스트` 를 하는 것이 좋다

<br/>

## 단위 테스트
- 테스트 코드도 기존 코드와 맞게 발전해야한다
- 유연성, 유지보수성, 재사용성을 제공한다
- **한 함수에 하나의 개념을 테스트** 하도록 구현해야한다
- 한 개의 테스트 함수에 assert를 최대한 줄이도록 노력한다
- 테스트에 중복이 많다면 Template Method Pattern으로 중복되는 기능들을 부모 클래스에 두고 자식 클래스에서 해당 값을 상속하면 된다

### 깔끔한 테스트코드를 짜는 5가지 규칙
- F(Fast) : 테스트는 빨라야한다
- I(Independent) : 각 테스트는 서로 의존하면 안된다 즉 한 테스트가 다음 테스트가 실행할 환경을 준비해서는 안된다. 각 테스트는 `독립적` 으로 `어떤 순서` 로 실행해도 괜찮아야 한다
- R(Repeatable) : 테스트는 실제, QA 환경 등 환경에 상관없이 반복 가능해야한다
- S(Self Validating) : 테스트는 부울값으로 결과를 내야한다 성공을 알기 위해서 log를 분석하면 안된다
- T(Timely) : 테스트는 실제 코드를 구현하기 전에 구현한다

<br/>

## Class
- 클래스는 작아야한다
- 단일 책임 원칙 : 클래스는 한 개에 하나의 책임을 가져야한다
- 응집도 : 인스턴스 변수가 작아야한다
    - `함수는 작게 매개변수 목록을 짧게` 를 따르다 보면 때때로 몇몇 메서드만이 사용하는 인스턴스 변수가 많아진다 이는 Class를 쪼개야한다는 의미이다
    - 함수의 매개변수는 클래스 변수로 승격한다 이들 중 몇 함수는 특정 클래스 변수만 사용한다면 이 또한 Class로 쪼개야 한다는 의미이다
- OCP : 확장에 개방적이고 수정에 폐쇠적이다
- DIP : 클래스는 상세 구현이 아니라 추상적인 것에 의존해야한다

<br/>

## 시스템
- 시스템은 깨끗한 아키텍처를 사용하고 도메인이 정확히 분리되어있어야한다
- 시스템 생성과 시스템 사용을 정확히 분리해야한다

### main
- 생성과 관련된 코드를 main으로 옮기고 나머지 시스템은 모든 객체가 생성되었고 모든 의존성이 연결되었다고 가정한다
- 즉 어플리케이션은 main이 시스템에 필요한 객체를 생성한 후 넘긴 객체를 사용하기만 한다

### Factory
- 객체가 생성되는 시점을 애플리케이션이 결정해야할 때 사용한다
- 애플리케이션은 interface를 생성하고 나머지는 main에서 실행된다

<br/>

## 창발성
- 떠오름 현상

### 품질을 높이는 단순한 설계 규칙
- **모든 테스트를 실행** : 리팩토링 시에도 테스트가 있으니 안심해서 수정할 수 있다
- **중복을 없애라**
- 프로그래머 **의도를 표현** 하라
    - 좋은 이름을 선택하라
    - 함수와 클래스 크기를 가능한 줄여라
    - 표준 명칭을 사용하라
    - 단위 테스트 케이스를 꼼꼼히 작성하라
- **클래스와 매서드 수를 최소로 줄여라**
 
<br/>

## 동시성
- 처음부터 공유하지 않는다 
    - ex) 자료를 읽을 때 사본을 만들어서 읽는다
- 가능한 독립적으로 구현하라
- 학습 테스트

### 실행 모델
- 생산자 소비자
   - 생산자가 버퍼에 정보를 넣고 소비자가 대기열에서 정보를 가져와 사용한다
   - 생산자가 시그널을 보내면 소비자가 사용하는데 이는 동시에 서로에게서 시그널을 기다리게 하는 가능성이 존재한다
- 읽기 쓰기
    - 읽기 처리율을 강조하면 기아 현상(쓰기가 영원히 실행되지 않음)이 생기거나 오래된 정보를 가져올 수 있다
    - 쓰기가 오래 버퍼를 점유하면 읽기가 기다리느라 처리율이 떨어진다
    - 양쪽 균형을 잡으면서 동시 갱신 문제를 피하는 해법이 필요하다
- 식사하는 철학자들

### 해결 방법
- 동기화하는 메서드 사이에 존재하는 의존성을 이해하라
- 동기화하는 부분을 작게 만들어라
- 올바른 종료를 구현하라
    - 데드락 : 부모가 자식이 끝나기를 모두 기다렸다가 끝날때, 자식 중 두개가 생산자 소비자의 관계라 생산자가 종료되고 소비자는 남아있다면 부모는 자식을 영원히 기다린다
    - 따라서 깔끔하게 종료하는 다중 스레드 코드를 짜야한다
- **쓰레드 코드 테스트하기**
    - 말이 안되는 실패는 스레드의 실패로 취급하라
    - 다중 스레드를 고려하지 않은 코드부터 테스트하라
    - 다중 스레드를 사용하는 코드 부분은 상황에 맞게 조율할 수 있도록 작성하라
    - 프로세서 수보다 많은 스레드를 돌려보라
    - 다른 플랫폼에서 돌려보라
    - 코드에 보조 코드를 넣어 강제로 실패하게 해보라 > jiggle
 
> 여기까지 한 번 더 다시보기 
