## Model

- app 하나에 model이 20개 이상 있다면 app을 분리 해야 한다

### 모델 상속 종류

- abstract base class
    - `abstract = True` 의 경우 모델이 생성되지 않는다
    - ex) TimeStampModel
- multitable ineritance
    - 최대한 피하는 것이 좋다
    - 멀티 테이블 상속 보다 `OneToOneField` `ForeignKey` 를 사용하는 것이 좋다
- proxy model

### 모델 상속 방법

1. 중복 내용이 최소라고 하면 모델 상속 자체가 필요가 없다 (그냥 두 곳에 필드를 추가한다)
2. 모델들 사이에 중복 필드가 혼란을 야기하거나 의도하지 않은 실수를 유발할정도로 많을 때 추상화 기초 모델로 리팰토링 할 수 있다

### Migration

- `sqlmigration` 을 이용하여 어떤 SQL문이 실행되는지 확인할 수 있다
- 생성되는 migration이 너무 많다면 `squashmigration` 을 이용한다
- MySQL의 경우
    - migrate 전 데이터베이스를 반드시 백업해둔다
        - schema 변경에 대한 transaction을 지원하지 않는다
        - 즉 rollback이 불가능하다

### 언제 null을 쓰고 blank를 쓸 것인가

- blank=True 만 사용해야 함
    - CharField, TextField, SlugField
    - EmailField
    - CommaSeparatedIntegerField ~~(이거 신기하다)~~

        ```python
        class Foo(models.Model):
            int_list = models.CommaSeparatedIntegerField(max_length=200)

        f = Foo(int_list="1,2,3,4,5") # Wooow
        ```

    - UUIDField
    - FileField, ImageField
- 둘다 사용하면 안됨
    - BooleanField
- 둘다 사용 가능
    - IntegerField, FloatField, DecimalField
    - DurationField, DateTimeField, DateField, TimeField
    - ForeignKey, ManyToManyField, OneToOneField

### GenericForeignKey

- 부정적인 입장
- 인덱싱이 존재하지 않으면 쿼리 속도에 손해를 가져온다
- 다른 테이블에 존재하지 않는 레코드를 참조할 수 있는 데이터 충돌 위험이 존재한다

### Fat Model

- model 안에 계속 추가하면 신의 객체 수준으로 폭발하게 되고 이는 유지보수를 어렵게 만든다
- 다른 해결 방법
    1. model 행동을 mixin으로 만들어 상속하자
    2. 상태 없는 helper 함수
        - 모델의 행동을 떼어내고 utility 함수로 넣는다

### Exception

- ObjectDoesNotExist와 `DoesNotExist`
    - DoesNotExist는 model에서만 이용할 수 있다
- `MultipleObjectsReturned` : 하나 이상의 쿼리가 반환되었다면

### Query

- 한 개의 쿼리를 페이지가 넘어갈 정도로 길게 쓰는 것보다는 `query chaining` 을 사용하는 것이 유용하다
- `F function` 을 이용하면 race condition을 피할 수 있다

```python
# 여러개의 프로세스가 count를 증가시키려고 한다면 오류가 일어날 수 있다
# visit의 count 값을 application 에서 가져와서 계산하기 때문에 다른 프로세스가 수정한 것을 읽을 수 없다
visit.count += 1
visit save()

# 이를 피하기 위해 해당 부분을 DB로 넘겨준다
# 그렇다면 현재 count가 어떤 값이던 상관없이 DB에 있는 값의 1을 더해서 저장한다
visit.count = F('count') + 1
visit.save()

```

- 필요한 상황이 아니라면 raw query 는 지양하자

### index를 추가 해야 하는 상황

- 인덱스가 쿼리의 10~25% 사이에서 이용될 때
- 실제 데이터 또는 실제와 비슷한 데이터가 존재해서 인덱싱 결과에 대한 분석이 가능할 때
- 인덱싱을 통해 성능이 향상되는 지 테스트할 수 있을 때

### Transaction

- `ATOMIC_REQUESTS` : HTTP 요쳥 Transaction
    - 성능 저하를 가져올 수 있음
        - 각 데이터베이스가 locking을 얼마나 잘 처리하는지에 따라 다양한 경우가 나올 수 있다
        - 데이터 쓰기가 많은 프로젝트의 초기 구성에서 무결성을 유지하는데 효과적이지만 트래픽 양이 늘어남에 따라 변경해야했다
    - 오직 에러가 발생할 때만 rollback이 된다
- query를 이용하여 데이터가 변경될 때 웬만하면 Transaction을 이용하자

<br/>

## Rest API

### HTTP Status

- 304 (unchanged) : 이전 요청으로부터 아무런 변화가 없음을 나타낸다
- 410 (gone) : 더이상 제공되지 않는 메서드로 호출
- 429 (Too much Requests) : 제한 시간 내에 너무 많은 요청을 보냄

### API 구현 팁

- 앱의 코드는 앱 안에 두기
- 비즈니스 로직을 API View에서 분리하기
- API Url을 모아두기
- API Test하기
- API Versioning 하기

### 외부 API 중단하는 방법

- 사용자들에게 서비스 중지 공지
- 410 status로 변경하기

### Class based view vs Function based view

- 클래스 기반 뷰를 더 선호

### 지연 서비스를 숨기는 방법 (오..호..) > Client

1. 애니매이션을 이용하여 지연 숨기기
2. 전송 성공 위조 하기
3. 지역적으로 이용자 제한하기

<br/>

## Django Core Module 교체 시 주의할 점

- 장고 코어 부분을 내가 변경할 필요? `없다`
    - +) 심지어 인스타그램도 포브스에 그럴 필요가 없다고 말했다..
- 그러니 FrankenDjango를 만들려고 하지 마로라..

<br/>

## Django Admin

- Django의 아주 강력한 기능

### Tip!

- Object 이름은 `__str__` 을 구현하여 보여주지 않는다
- 다중사용자가 이용하는 경우 `list_eidtable (리스트 상에서 수정하는 기능)` 을 피하자
- 이용하는 모든 admin 확장 시스템에 테스트 케이스를 작성하라

<br/>

## Django User Model

- `settings.AUTH_USER_MODEL` 을 사용하면 정의된 User Model을 가져올 수 있다

### 확장

- AbstractUser : 기존의 User를 유지하면서 필드 추가
- AbstractBaseUser : 기존의 User를 유지하지 않고 새로 생성 > 매우 까다로움
- `OneToOneField` 로 새로운 Table을 연결시키기

<br/>

## Django Third Party Package

- Django의 진면목은 빠르게 발전하는 Third Party Package다!

### 좋은 Django Package의 조건

- 목적 : 의도하는 목적이 명확해야한다
- 범위 : 해당 목적에 맞는 범위에만 초점이 맞춰져야 한다
- 문서화 : 문서가 없는 패키지는 완성되지 않은 것과 같다 > 무조건 문서화를 하자
- 테스트 : 제작되는 패키지는 무조건 테스트를 거쳐야한다! (무! 조! 건!)
- 템플릿 : 기본 기능을 구현해 둔 뼈대 역할을 하는 텀플릿 세트를 제공하는 것이 표준!
- 유지보수 : Pull Request를 잘 보고 유지보수 잘합시다
- 커뮤니티
- 모듈성 : 설치는 기본 장고에 최소한의 영향만을 미쳐야 한다
- Python Package Index에서 download 받을 수 있어야 한다

### Python Package Index에 올리기

1. 가능한 세세하게 requirements.txt를 작성한다
2. 버전 번호를 붙인다
3. 프로젝트 이름을 정확히 명명한다
4. 라이센스
    - 개인이라면? MIT
    - 특허에 대해 걱정한다면? Apache License
    - `LICENSE.rst` 파일을 생성
5. 코드는 간결해야한다

<br/>

## 테스트, 정말 거추장스럽고 낭비일까? (아니..)

- Python의 도 : 수평적인 것이 중첩된 것보다 낫다
    - 즉! 한 파일에 모든 기능이 있는 것보다 파일이 여러 개여도 수평적으로 있는 것이 낫다

### 단위 테스트 작성하기

- 각 테스트 메서드는 테스트를 `한 가지씩` 수행해야 한다
- `테스트가 필요한 테스트 코드를 작성하지 않는다`
- 같은 일을 반복하지 말라는 법칙은 테스트 케이스를 쓰는 데 적용되지 않는다
- 테스트를 해야하는 범위 : *다* *전부 다*
    - 뷰
    - 모델
    - 폼
    - 유효성 검사기
    - 시그널
    - 필터
    - 템플릿 태그
    등..
- Mock을 이용하여 실제 데이터에 문제를 일으키지 않고 테스트하기
    - Mock library를 이용하여 외부 API의 가짜 Response를 만들어서 테스트하기
- 각 테스트 목적을 문서화하라

### 통합테스트란

- 웹에 대한 셀레니움 테스트
- Third Party API에 대한 실제 테스팅 등

<br/>

## 문서화에 집착하자

- reStructuredText (rst) 를 사용하자
    - Python을 문서화하는데 가장 일반적으로 이용되는 마크업

### 어떤 것을 문서화할까

1. README.rst : 이 프로젝트가 무엇인지 적어도 짧은 문장이라도 설명을 제공
2. deployments.rst : 어떻게 프로젝트를 설치, 업데이트하는지에 대한 단계별 정리를 제공
3. installation.rst : 프로젝트를 처음 접하는 사람들에게 유용
4. architecture.rst : 프로젝트가 시간이 흐르면서 확장되어 감에 따라 각 요소가 어떻게 구성되어 있는지에 대한 이해를 돕는 가이드

<br/>

## Django 성능 향상 시키기

### Query 개선

- `django-debug-toolbar`를 이용하여 문제가 되는 쿼리 찾기
- 중복되는 쿼리를 최대한 줄인다
    - `select_related` `prefetch_related`
    - key-value 형식의 cache 이용하기

### 일반 쿼리 빠르게 하기

- Index로 최적화하기
- query plan을 자세히 살펴본다
- database에서 slow query logging 기능을 활용하여 빈번히 발생하는 느린 쿼리를 확인한다

### Database의 성능 최대화하기

- 규모가 큰 데이터베이스에서 절대로 하면 안되는 것
    1. 로그 : 데이터베이스에 로그 데이터를 저장하지 않는다
    2. 일시적 데이터 : 일시적 데이터를 데이터베이스에 저장하지 않는다

### Memchached 등을 이용해서 query caching

- 가장 많은 쿼리를 포함하는 뷰와 템플릿
- 어떤 URL이 가장 많은 요청을 받는가
- Cache를 삭제해야 할 시점은 언제인가

<br/>

## 비동기 테스크 큐

- producer : 나중에 실행될 테스크를 큐에 넣는 코드
- broker : 테스크들이 보관되어 있는 장소
- worker : 테스크를 브로커에서 가져와 실행하는 코드

### 테스크 큐가 정말로 필요할 때

- 결과에 시간이 걸린다
- 사용자에게 바로 결과를 제공해야 한다

### 테스트 큐 소프트웨어 선택

- Celery
    - 장점 : 장고의 표준으로 `저장 형식이 다양`하고 `유연`하며 `기능이 풍부`하고 `대용량에 적합`
    - 단점 : 세팅 절차가 까다롭고 트래픽이 적은 사이트의 경우 오히려 `낭비적인 측면`이 발생한다
- Redis Queue
    - 장점 : 유연하고 `셀러리에 비해 적은 메모리` 를 이용, `대용량에 적합`
    - 단점 : 셀러리에 비해 `기능이 적고`, 저장소로 `오직 레디스만 가능`하다
- django-backend-tasks
    - 장점 : 셋업이 쉽고 이용이 간편하며 `작은 크기`나 `배치 작업`에 용이하다
    - 단점 : `Django ORM을 백엔드로 이용해 중간 이상의 볼륨을 처리하는데 문제가 된다`
- 결론
    - 용량이 작은 프로젝트부터 용량이 큰 프로젝트까지 대부분 `레디스 큐`를 추천
    - `테스크 관리가 복잡한 대용량 프로젝트`는 `샐러리`를 추천
    - 소규모 프로젝트에는 django-backend-tasks를 추천

### Json화 가능한 값들만 테스크 함수에 전달하라

- ORM 인스턴스 같은 데이터는 경합 상황을 유발한다. 차라리 `PrimaryKey 를 넘겨 최신 데이터를 가져 올 수 있게 해라.`
- 복잡한 형태의 객체는 시간과 메모리가 더 많이 든다. (그러지 않으려고 테스크를 사용하는 건데)
- Json이 디버깅 하기 더 쉽다
- 사용중인 테스크 큐에 따라 json화 형식만 지원하는 경우도 있다

### 관리 및 운영

- 백로그 모니터링 하기
    - 테스크가 점점 증가하는데 워커가 그걸 따라잡지 못한다면?
        - 하나의 워커 : django-background-tasks
        - 여러 워커 : celery. redis queue
- 죽은 테스크를 주기적으로 지우기
- 불필요한 데이터 무시하기
    - 보통 브로커는 테스크의 결과값을 기록하는데 이를 주기적으로 지워주는 것이 좋다
- 큐의 에러 핸들링 이용하기
    - 테스크에 대한 최대 재시도 횟수
    - 재시도 전 지연 시간 (다시 시도하기 전에 최대 10초를 기다리는 것을 선호한다)
    - 만약 반복적으로 오류가 난다면 재시도 할 때마다 시간을 늘이는 것을 추천한다
        - 이로 인해 우리도 실패 원인을 복구하는 시간을 얻는다

<br/>

## Django 보안

### 지원하는 보안

- XSS 보안
    - 브라우저로 전달되는 데이터에 악성 스크립트가 포함되어 개인의 브라우저에서 실행되면서 해킹을 하는 것
    - 웹 서버에 구현된 웹 애플리케이션의 XSS 취약점을 이용하여 서버 측 또는 URL에 미리 삽입을 해놓은 것
    - ex) 웹 사이트의 게시판, 사용자 프로필 및 코멘트 필드 등에 악성 스크립트를 삽입해 놓으면, 사용자가 사이트를 방문하여 `저장되어 있는 페이지에 정보를 요청할 때`, 서버는 악성 스크립트를 사용자에게 전달하여 `사용자 브라우저에서 스크립트가 실행 되면서 공격`
- CSRF 보안
    - 인터넷 사용자(희생자)가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 만드는 공격
    - 조회성(HTTP GET Method) 데이터에는 방어 대상에 두지 않고, `쓰기/변경이 가능한 POST, PATCH, DELETE Method에만 적용`
    - CSRF Token
        - 우선 사용자의 `세션에 임의의 난수 값을 저장`하고 사용자의 요청 마다 해당 난수 값을 포함 시켜 전송시킵니다.
        - 이후 Back-end 단에서 요청을 받을 때마다 `세션에 저장된 토큰 값과 요청 파라미터에 전달되는 토큰 값이 일치하는 지 검증`하는 방법
- SQL Injection 보안
    - 클라이언트의 입력 값을 조작하여 서버의 데이터베이스를 공격할 수 있는 공격 방식
- 클릭 재킹 보안
    - 마우스 클릭(Click)과 항공기 불법탈취 또는 납치를 의미하는 하이재킹(hijacking)의 합성어
    - 사용자는 어떤 웹 페이지를 클릭하지만 실제로는 다른 어떤 페이지의 컨텐츠를 클릭하게 되는 것
    - 대표적인 방법으로는 정상적인 버튼 밑에 해킹 기능을 넣은 보이지 않는 버튼을 배치하는 것
- 보안 쿠키를 포함한 TLS, HTTPS, HSTS 지원
- SHA256, PBKDF2 알고리즘을 이용한 안전 패스워드 짱
- HTML 자동 이스케이핑
- expat 파서를 통한 XML 폭탄 공격 대비

### 안전한 Cookie 이용하기

- HTTPS가 아니면 브라우저가 쿠키를 전송하지 못하게 해야함

```python
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### HSTS 사용

- HSTS (HTTP strict transport security)
- HTTP링크를 HTTPS 링크로 변경시킨다
- 유의점
    - 하위 도메인으로 설정하는 것이 좋다
        - 안전하지 않은 하위 도메인이 상위 도메인으로 쿠키를 쓰는 것을 방지한다
    - HTTPS를 사용하지 못할 때를 대비해 max-age는 짧게 잡아둔다
        - 클라이언트에 저장된 HSTS는 변경할 수 없다

### 사용자가 올린 파일 다루기

- 사용자가 올린 파일을 서비스해야 할 때는 해당 파일은 잠재적으로 보안이 좋지 않다
- 따라서 CDN을 이용하여 우회할 수 있다
- CDN을 사용할 수 없는 경우 업로드된 파일들을 실행 불가능한 폴더 안으로 저장한다

<br/>

## Signal

- 시그널은 `최후의 수단`이다 (오호)

### 사용 해야 할 때

- Signal Receiver가 하나 이상의 모델을 변경
- 여러 앱에서 발생한 Sinal을 공통의 Receiver가 처리
- 모델이 저장된 후 캐시를 지우고 싶을 때

### 사용하지 않는 방법

- model의 save나 delete 메서드를 오버라이드
- 헬퍼 함수 생성

<br/>

## Utility

### 유틸리티를 위한 코어 앱 만들기