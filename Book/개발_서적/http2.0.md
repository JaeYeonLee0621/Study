# TCP

TCP는 보수적인 환경을 가정하고 공평하게 동작하도록 설걔

TCP는 데이터를 전송하는 가장 신뢰성 있는 방법

## 혼잡 윈도우

수신자가 확인하기 전까지 송신자가 전송할 수 있는 TCP 패킷 수

최근에는 그 수를 4~10으로 설정하고 상한선에 도달하면 혼잡 회피의 단계로 변화

또한 각 브라우저마다 보통 6개의 연결을 열고 있으므로 6개마다 혼잡제어를 해야함

## 비대한 메시지 헤더

http 1.0/1.1 (이하 hp 1)은 개체를 압축하는 메커니즘을 제공하긴 하지만 메시지 헤더를 압축하는 방법은 없다

2016년 말 요청 헤더의 평균 크기는 460 bytes이고 일반 웹페이지의 경우 63KB이다

이는 더 많은 왕복을 유발하고 네트워크 지연을 야기한다

헤더 압축 기능이 없으면 클라이언트가 대역폭 제한에 걸릴 수 있다

ex) 경기장 효과 : 많은 사람들이 동시에 같은 장소에서 같은 대역폭을 사용 > 저대역폭 과밀 링크

# HTTP2

## Sharding

HTTP 2는 단일 TCP/IP 에서만 동작하도록 만들어졌다

하나의 소켓을 열고 적절한 혼잡도에서 동작하는 것이 다수의 소켓을 조율하는 것보다 훨씬 신뢰성 있고 성능에 좋다고 생각했다

하지만 때에 따라 여러 소켓이 더 나은 경우가 있다

초기 혼잡 윈도우 크기가 매우 크면 이 문제를 줄이는 데 도움이 되지만, 큰 윈도우를 지원하지 못하는 네트워크에서는 문제가 될 수도 있다

### 바이너리 프로토콜

바이너리 프레임 형식의 프로토콜

기계는 쉽게 파싱할 수 있지만 사람이 읽기는 어렵다

### 헤어 압축

### 다중화

선호하는 디버깅 도구로 연결을 들여다보면, 요청과 응답이 뒤섞여있음

### 암호화

전송 중인 데이터의 부분이 암호화가 되기 때문에 전송되는 즉시 판독하기가 더 어려워짐

## 연결

 1. http2는 연결이 암호화되지 않은 경우 `Upgrade헤더`를 활용해 h2로 통신하려는 요구 전달

서버가 h2로 통신할 수 있으면 101 응답 회신

2. 연결이 TLS로 수립되는 경우 클라이언트는 ClientHello 메시지 안에 `ALPN`을 설정하여 h2로 통신하려는 요구 전달

이 방식에서 h2는 추가 왕복 없이 주고 받기 한 번으로 협상이 완료

3. h2 지원을 표시하는 마지막 방법은 `HTTP Alternative Services`를 사용하는 것

클라이언트에 보낼 응답 헤더에 Alt-Svc를 설정하여 더 나은 프로토콜을 사용할 수 있다는 사실을 표시할 수 있다

점점 더 많은 브라우저가 지원하고 있는 유연하여 강력한 기능

클라이언트 엔드 포인트가 h2로 통신한다는 사실을 서버에 한번 더 알려주기 위해 클라이언트는 연결 전문이라는 마법의 옥텟 스트림을 연결의 첫 번째 데이터로 전송

- PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n

이 메시지는 의도적으로 h1 메시지처럼 보이게 만들었는데, h1이 이 메시지를 수신할 경우 버전을 인식하지 못해 오류가 발생할 것이다

그렇다면 h2 클라이언트는 무언가가 잘못되었다는 것을 분명히 알 수 있다

## 프레임

HTTP/2 는 프레임 형식의 프로토콜이다

프레이밍은 프로토콜의 사용자가 쉽게 파싱하고 생성할 수 있는 방식의 중요한 모든 것을 포장하는 방법이다

만약 if문 태그(예) <crlf>) 등으로 이루어진 문자열은 파싱하는 것이 어렵지 않지만 느리고 오류가 발생하기 쉽다

```
GET /HTTP/1.1 <crlf>
Host: www.example.com <crlf>
...
```

이러한 코드는 쉽게 작성할 수 있지만, 문제점이 있다

1. 한 번에 하나의 요청/응답만이 이루어진다
2. 파싱에 얼마나 많은 메모리가 사용될 지 알 수 없다

프레임의 장점

1. 프레임을 사용한다면 수신자는 무엇을 수신할지 미리 알 수 있다 (h2 프레임의 시작에는 길이가 있다)

~~이외에도 많은 기능들이 있다. 자세한건 구글에~~

2. 프레임 형식 덕분에 요청과 응답을 서로 뒤섞는 방식이 가능하다

## 스트림

하나의 연결 위에서 개별 HTTP 요청/응답의 쌍을 구성하는 일련의 프레임 모음

프레이밍 덕분에 다수의 요청과 응답이 서로 차단하지 않고 뒤섞여 배치될 수 있다

## 메시지

HTTP의 요청이나 응답을 일컫는 총칭

### 모든 것이 다 헤더다

h1은 메시지를 요청/상태 줄과 헤더로 나눈다

h2는 이러한 구분을 없애고 그 줄들을 특별한 가상 헤더로 합친다

### 청크 분할 인코딩이 필요없다

청크 분할은 데이터의 길이를 미리 알릴 필요 없이 데이터를 전송하는데 사용되어왔기 때문에 더이상 필요 없다

### 101응답이 필요없다

ALPN은 더 적은 왕복 오버헤드로 더 명확한 프로토콜 협상 경로를 제공한다

## 흐름제어

h2에서는 클라이언트가 전송 속도를 조절하는 기능을 제공한다 (서버도 같은 기능을 할 수 있다)

클라이언트가 흐름 제어를 하는 이유

1. 여러 스트림이 서로 방해하지 않게 하기 위해
2. 클라이언트가 사용한 대역폭이나 메모리를 처리할 수 있는 만큼 데이터가 전송되도록하면 효율성이 개선될 수있음

## 우선순위

h2에서는 모든 자원 요청을 동시에 보낼 수 있고, 서버는 그 요청들의 처리를 한번에 시작할 수 있다

h2는 priority 프레임을 사용하여, 트리 안의 상대적인 가중치를 선언한다

ex) CSS → JS → jpg 

## 서버 푸쉬

그 개체가 요청되기 전에 브라우저의 캐시에 미리 가져다 두는 것

가까운 미래에 특정 개체가 필요하리라는 것을 알면 푸쉬를 통해 그 개체를 미리 전송할 수 있다

## 헤더 압축

SPDY, CRIME, GZIP은 공격에 취약

HPACK이 제안되었는데, 허프만 인코딩을 활용해 GZIP에 버금가는 압축률을 달성

## 전송 절차

http1.1 사용 웹사이트

```
nghttp -v -n --no-dep -w 14 -a -H "Header1:Foo" http://stage.laftel.net/

[  0.014] Connected
[  0.014] send SETTINGS frame <length=12, flags=0x00, stream_id=0>
          (niv=2)
          [SETTINGS_MAX_CONCURRENT_STREAMS(0x03):100]
          [SETTINGS_INITIAL_WINDOW_SIZE(0x04):16383]-> 윈도우 사이즈 2^14
[  0.014] send HEADERS frame <length=45, flags=0x05, stream_id=1>
          ; END_STREAM | END_HEADERS -> 더이상 전송할 Stream이 없다
          (padlen=0)
          ; Open new stream
          :method: GET
          :path: /
          :scheme: http
          :authority: stage.laftel.net
          accept: */*
          accept-encoding: gzip, deflate -> gzip으로 header 압축
          user-agent: nghttp2/1.41.0
          header1: Foo
[  0.053] [ERROR] Remote peer returned unexpected data while we expected SETTINGS frame. 
-> http2.0은 settings frame을 전송하는데, 해당 사이트가 그 프레임을 받을 수 없다
-> 즉 http2.0을 사용하지 않는다
Perhaps, peer does not support HTTP/2 properly.
Some requests were not processed. total=1, processed=0
```

http 2.0 사용 웹사이트

```
nghttp -v -n --no-dep -w 14 -a -H "Header1:Foo" https://www.google.com/
[  0.054] Connected
The negotiated protocol: h2 -> google은 http2 사용
[  0.199] send SETTINGS frame <length=12, flags=0x00, stream_id=0>
          (niv=2)
          [SETTINGS_MAX_CONCURRENT_STREAMS(0x03):100]
          [SETTINGS_INITIAL_WINDOW_SIZE(0x04):16383]
[  0.199] send HEADERS frame <length=45, flags=0x05, stream_id=1>
          ; END_STREAM | END_HEADERS
          (padlen=0)
          ; Open new stream
          :method: GET
          :path: /
          :scheme: https
          :authority: www.google.com
          accept: */*
          accept-encoding: gzip, deflate
          user-agent: nghttp2/1.41.0
          header1: Foo
[  0.324] recv SETTINGS frame <length=18, flags=0x00, stream_id=0>
          (niv=3)
          [SETTINGS_MAX_CONCURRENT_STREAMS(0x03):100]
          [SETTINGS_INITIAL_WINDOW_SIZE(0x04):1048576]
          [SETTINGS_MAX_HEADER_LIST_SIZE(0x06):16384]
[  0.324] recv WINDOW_UPDATE frame <length=4, flags=0x00, stream_id=0>
          (window_size_increment=983041)
[  0.325] send SETTINGS frame <length=0, flags=0x01, stream_id=0>
          ; ACK
          (niv=0)
[  0.327] recv SETTINGS frame <length=0, flags=0x01, stream_id=0>
          ; ACK
          (niv=0)
[  0.375] recv (stream_id=1) :status: 200
[  0.375] recv (stream_id=1) date: Fri, 19 Jun 2020 03:32:07 GMT
[  0.375] recv (stream_id=1) expires: -1
[  0.375] recv (stream_id=1) cache-control: private, max-age=0
[  0.375] recv (stream_id=1) content-type: text/html; charset=ISO-8859-1
[  0.375] recv (stream_id=1) p3p: CP="This is not a P3P policy! See g.co/p3phelp for more info."
[  0.375] recv (stream_id=1) content-encoding: gzip
[  0.375] recv (stream_id=1) server: gws
[  0.375] recv (stream_id=1) content-length: 5589
[  0.375] recv (stream_id=1) x-xss-protection: 0
[  0.375] recv (stream_id=1) x-frame-options: SAMEORIGIN
[  0.375] recv (stream_id=1) set-cookie: 1P_JAR=2020-06-19-03; expires=Sun, 19-Jul-2020 03:32:07 GMT; path=/; domain=.google.com; Secure
[  0.375] recv (stream_id=1) set-cookie: NID=204=CboRwJOQAB_3psxlvubE2STh7cq18kzIfhXor6RDjIwX5CDhWqwW09lbJYClThDQgKySZytnZqeHgDES9nP37kQsE530CDBCez8wU11XG_C6-BK3XT5RJJ7gU4cyVyECj-RB--0Aa5JN3Z6iuVPtIa3VYwhi6-LwntuK9SpXX2w; expires=Sat, 19-Dec-2020 03:32:07 GMT; path=/; domain=.google.com; HttpOnly
[  0.375] recv (stream_id=1) alt-svc: h3-28=":443"; ma=2592000,h3-27=":443"; ma=2592000,h3-25=":443"; ma=2592000,h3-T050=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
[  0.375] recv HEADERS frame <length=676, flags=0x04, stream_id=1>
          ; END_HEADERS
          (padlen=0)
          ; First response header
[  0.381] send HEADERS frame <length=64, flags=0x05, stream_id=3>
          ; END_STREAM | END_HEADERS
          (padlen=0)
          ; Open new stream
          :method: GET
          :path: /images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png
          :scheme: https
          :authority: www.google.com
          accept: */*
          accept-encoding: gzip, deflate
          user-agent: nghttp2/1.41.0
          header1: Foo
[  0.381] send HEADERS frame <length=28, flags=0x05, stream_id=5>
          ; END_STREAM | END_HEADERS
          (padlen=0)
          ; Open new stream
          :method: GET
          :path: /textinputassistant/tia.png
          :scheme: https
          :authority: www.google.com
          accept: */*
          accept-encoding: gzip, deflate
          user-agent: nghttp2/1.41.0
          header1: Foo
[  0.387] recv DATA frame <length=5679, flags=0x08, stream_id=1>
          ; PADDED
          (padlen=90)
[  0.387] recv DATA frame <length=244, flags=0x09, stream_id=1>
          ; END_STREAM | PADDED
          (padlen=244)
[  0.387] recv PING frame <length=8, flags=0x00, stream_id=0>
          (opaque_data=0000000000000000)
[  0.387] send PING frame <length=8, flags=0x01, stream_id=0>
          ; ACK
          (opaque_data=0000000000000000)
[  0.450] recv (stream_id=5) :status: 200
[  0.450] recv (stream_id=5) accept-ranges: bytes
[  0.450] recv (stream_id=5) content-type: image/png
[  0.450] recv (stream_id=5) content-length: 258
[  0.450] recv (stream_id=5) date: Thu, 11 Jun 2020 17:12:06 GMT
[  0.450] recv (stream_id=5) expires: Fri, 11 Jun 2021 17:12:06 GMT
[  0.450] recv (stream_id=5) last-modified: Fri, 27 Sep 2019 01:00:00 GMT
[  0.450] recv (stream_id=5) x-content-type-options: nosniff
[  0.450] recv (stream_id=5) server: sffe
[  0.450] recv (stream_id=5) x-xss-protection: 0
[  0.450] recv (stream_id=5) cache-control: public, max-age=31536000
[  0.450] recv (stream_id=5) age: 642001
[  0.450] recv (stream_id=5) alt-svc: h3-28=":443"; ma=2592000,h3-27=":443"; ma=2592000,h3-25=":443"; ma=2592000,h3-T050=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
[  0.450] recv HEADERS frame <length=151, flags=0x04, stream_id=5>
          ; END_HEADERS
          (padlen=0)
          ; First response header
[  0.453] recv DATA frame <length=258, flags=0x01, stream_id=5>
          ; END_STREAM
[  0.453] recv PING frame <length=8, flags=0x00, stream_id=0>
          (opaque_data=0000000000000002)
[  0.453] send PING frame <length=8, flags=0x01, stream_id=0>
          ; ACK
          (opaque_data=0000000000000002)
[  0.463] recv (stream_id=3) :status: 200
[  0.463] recv (stream_id=3) accept-ranges: bytes
[  0.463] recv (stream_id=3) content-type: image/png
[  0.463] recv (stream_id=3) content-length: 5482
[  0.463] recv (stream_id=3) date: Fri, 19 Jun 2020 03:32:07 GMT
[  0.463] recv (stream_id=3) expires: Fri, 19 Jun 2020 03:32:07 GMT
[  0.463] recv (stream_id=3) cache-control: private, max-age=31536000
[  0.463] recv (stream_id=3) last-modified: Tue, 22 Oct 2019 18:30:00 GMT
[  0.463] recv (stream_id=3) x-content-type-options: nosniff
[  0.463] recv (stream_id=3) server: sffe
[  0.463] recv (stream_id=3) x-xss-protection: 0
[  0.463] recv (stream_id=3) alt-svc: h3-28=":443"; ma=2592000,h3-27=":443"; ma=2592000,h3-25=":443"; ma=2592000,h3-T050=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
[  0.463] recv HEADERS frame <length=105, flags=0x04, stream_id=3>
          ; END_HEADERS
          (padlen=0)
          ; First response header
[  0.470] recv DATA frame <length=5482, flags=0x00, stream_id=3>
[  0.470] recv DATA frame <length=0, flags=0x01, stream_id=3>
          ; END_STREAM
[  0.470] send GOAWAY frame <length=8, flags=0x00, stream_id=0>
-> 보통 goaway를 이용하여 통신을 끊는다
          (last_stream_id=0, error_code=NO_ERROR(0x00), opaque_data(0)=[])
```

## 지연 시간

지연 시간 : 패킷이 한 지점에서 다른 지점으로 가는 데 걸리는 시간

가장 큰 영향을 미치는 것은 두 지점 사이의 거리를 사용하는 전송 매체의 속도

이 방법을 해결하는 것은 두 지점을 가까이 두면 된다 > CDN

+) 전송 매체와 관계 없이 빛의 속도는 제한되어 있으므로 두 지점을 가까이 두는 것이 지연 시간을 개선하는 가장 좋은 방법

또한 전송 도중 게이트웨이, 라우터, 스위치 등이 지연 시간을 더 길게 만든다

`출발지와 거리가 증가하여 지연 시간이 늘어날 수록 h1에 비해 h2의 성능이 더 나아진다`

## 패킷 손실

보통 원인은 네트워크 혼잡이다

높은 패킷 손실률은 h2로 전송되는 페이지에 악영향, h2는 단 하나의 TCP 연결만 수립하고, 손실/혼잡이 있을 때마다 TCP 프로토콜이 TCP 윈도우 크기를 줄이기 때문

**크기가 작은 개체가 많이 있는 웹페이지에서는 h2 페이지 로딩 시간이 h1보다 빨랐다**

**h1의 경우 단 6개의 개체만을 동시에 전송했으나, h2는 하나의 연결에 다수의 스트림을 다중화할 수 있기 때문이다**

네트워크가 열악할수록 h2가 더 큰 영향을 받았다

h2의 단일 연결 구조 때문이다

하나의 연결이 패킷 손실에 영향을 받으면 전체 작업이 느려지게 된다

크기가 큰 개체가 적게 있는 웹페이지는 h1가 h2보다 월등히 빨랐는데, h1은 6개의 연결을 열면서 초기 혼잡 윈도우 크기가 6배가 더 커진다 

따라서 h2의 윈도우가 최적화될 동안 h1이 6배가 더 큰 윈도우로 개체를 받는다

대부분 웹 페이지는 작은 개체가 많이 있는 데, h2 설계자는 이 경우를 최적화 했기 때문에 이외의 경우에는 성능이 좋지 않은 것은 당연하다

## 서버 푸쉬

클라이언트가 개체를 요청하기 전에 그 미리 그 개체를 전송할 수 있는 능력을 서버에 부여

적절히 활용하면 페이지 렌더링 시간을 20~50% 줄일 수 있다

하지만 서버가 클라이언트가 이미 가진 객체를 푸쉬하려고 할 때, 서버 푸쉬로 인해 대역폭이 낭비될 수 있다

페이지를 렌더링 하는 데 가장 필요한 CSS, JS 개체를 푸쉬할 때 가치가 있다

그리고 HTML 페이지의 전송에 필요한 대역폭과의 경쟁을 피할 수 있을 정도의 경쟁력으로 구현되어야한다

따라서 HTML을 백그라운드로 작업을 하던가, HTML을 요청할 때 푸쉬하는 것이 가장 이상적이다

## TTFB

Time To First Byte

웹 서버의 응답성을 나타내는 데 사용한다

h1의 경우 클라이언트는 호스트 연결 마다 한 번에 하나씩의 개체만 요청하고 그 개체들은 순서대로 하나씩 전송한다

모든 개체를 수신한 후에 그 개체들을 요청하며 이를 반복한다

h2의 경우 클라이언트는 HTML을 로딩한 후에 다중화를 사용해 h1보다 더 많은 요청을 동시에 서버로 전송한다 

대게 이 요청들은 h1보다 더 짧은 시간 안에 응답을 받는다

따라서 h1이 TTFB가 h2보다 짧지만 의미하는 것이 다르다

# HTTP2.0 안티 패턴

## 도메인 샤딩

샤딩 : 호스트 이름마다 다수의 연결을 열어 콘텐츠를 동시에 내려받고 h1의 순차적 특성을 극복하는 브라우저의 기능을 활용하는 것

헌대의 웹브라우저는 하나의 호스트에 6개의 연결을 열 수있게 하지만, h2에서는 불필요한 샤딩이다

## 인라이닝

인라이닝은 외부의 자원을 불러오는 데 필요한 추가적인 연결과 왕복을 줄이려는 목적으로 JS, CSS Image를 Html 태그에 삽입하는 것이다 

하지만 캐싱과 같은 기능을 사용하지 못하기 때문에 사용하지 않는 것이 좋다

성능이 좋지 않은 디바이스에서는 요청에 드는 오버헤드가 캐싱에서 얻는 이득보다 클 수 있다

## 결합

크기가 작은 여러 파일을 하나의 큰 파일로 통합하는 것이다

외부 자원을 불러올 때 왕복을 줄이고, 개체 수가 적으면 스크립트를 디코딩하거나 해석할 때 CPU 사용을 줄일 수 있다는 점에서 인라이닝과 비슷하다

## 쿠키 없는 도메인

정적 콘텐츠는 쿠키 없는 도메인이 성능에 더 좋다 

h1은 헤더를 압축할 수 없고, TCP 패킷의 크기를 초과하는 크기의 쿠키를 사용하는 웹사이트도 있기 때문이다

h2에서는 대용량의 크기의 쿠키를 압축할 수 있다

또한 쿠키 없는 도메인의 경우 더 많은 연결을 열어야함을 의미하므로 사용하지 않는 것이 좋다

## 스프라이팅

크기가 작은 개체들을 여러번 요청하는 일을 피하기 위한 또 다른 기법이다

여러 작은 이미지를 격자 무늬로 붙여 하나로 만든 후 보여주고 싶은 부분만 보여주는 것

h2에서는 다중화와 헤더 압축을 통해 많은 요청 오버헤드를 제거할 수 있기 때문에 사용하지 않는 것이 좋다

## 프리패치

개체를 가능한 시점에 미리 내려받아 두도록 브라우저에 알려주는 웹 성능 최적화 기법

하지만 h2에서는 서버 푸쉬 기능이 있기 때문에 사용하지 않아도 된다

# 추가

## 연결 병합

새로운 연결을 수립해야 할 때 기존 연결을 재사용하여 요청의 성능을 개선하는 것

TCP와 TLS 핸드 셰이크를 생략해 첫번재 요청의 성능이 줄어든다

# 차세대 질문

## TCP? UDP?

UDP를 사용하려면 TCP에서 이미 구현한 많은 부분들을 다시 구현해야한다

하지만 TCP는 성능상의 이유로 커널에 포함되어있고, 이는 OS개발사만이 TCP 개발에 참여할 수 있으며, 이를 변화시키는 것은 거의 불가능 하다는 것과 같다

따라서 사용자가 제어권을 가지는 User Interface에서 다시 구현하면, 브라우저를 자동 업데이트하기만 하지면 새 버전을 신속하게 개발하고 배포하는 일을 반복할 수 있게 된다

## QUIC

h2의 단점은 TCP연결에 의존적이라는 것이다

하지만 TCP는 현재 시작단계에서 3 hand shacking을 하는 등의 초기 연결 지연이 단점이다

따라서 구글에서는 UDP에 TCP의 기능을 추가한 QUIC이라는 매커니즘을 만들었다

## TLS 1.3

새연결 수립과 연결 재개에 RTT를 적게 만드는 것이다

왕복은 나쁜 것이니 없애야 한다