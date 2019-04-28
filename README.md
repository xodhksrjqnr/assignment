# 1주차 과제 : Python을 이용한 Quick Sort
### 인력거 운행중 조 : 김태완(2015040031), 김진용(2015040025)

* assignment_1.py
  - -o : 정렬 방식, A/오름차순, D/내림차순
  - -i : 정렬할 배열
<pre><code>$ python assignment_1.py -o A -i 1 2 5 4 6 0 10
</code></pre>

![assignment_1_test](https://user-images.githubusercontent.com/48250370/54082615-f8658b00-435b-11e9-9c0d-d33123017f0f.PNG)


# 2주차 과제 : 클라이언트가 보낸 문자열을 거꾸로 전송해주는 서버 구현
### 인력거 운행중 조 : 김태완(2015040031), 김진용(2015040025)

* assignment_2
  - -i : 서버 아이피, -p : 포트번호
    
<pre><code>$ python server.py -p 8888
$ python client.py -i 127.0.0.1 -p 8888
</code></pre>

![image1](https://user-images.githubusercontent.com/48250370/54365055-7786f600-46b1-11e9-89d1-d3ee0489c7dd.PNG)

![image2](https://user-images.githubusercontent.com/48250370/54365056-781f8c80-46b1-11e9-921c-ffb491959764.PNG)

# 3주차 과제 : 클라이언트가 요청한 파일을 전송해주는 서버 구현
### 인력거 운행중 조 : 김태완(2015040031), 김진용(2015040025)

* assignment_3
  - python client_file.py -i 127.0.0.1 -p 8888 -f test.txt
    - -i : 서버 아이피, -p : 포트 번호, -f : 파일 이름
  - python server_file.py -p 8888 -d /home/famous/
    - -p : 포트 번호, -d : 파일 디렉토리
<pre><code>$ python server_file.py -p 8888 -d "test"
$ python client_py -i 127.0.0.1 -p 8888 -f "test.py"
</code></pre>

![캡처](https://user-images.githubusercontent.com/48250370/54867015-0fc26080-4dbf-11e9-8a29-db00ea4a468b.PNG)

![캡처1](https://user-images.githubusercontent.com/48250370/54867020-181a9b80-4dbf-11e9-81c5-c10664d6ca76.PNG)

# 4주차 과제 : 프로세스와 스레드에 대해서 조사
### 인력거 운행중 조 : 김태완(2015040031), 김진용(2015040025)

* assignment_4
  - 프로세스와 스레드의 정의 및 차이점
  - 스레드 사용 이유 및 스레드 모델
  - Python에서 프로세스 및 스레드를 사용하는 방법
  - HWP 및 DOC 포맷으로 3장 내외

![캡처](https://user-images.githubusercontent.com/48250370/56863818-0e0b3e80-69f6-11e9-839c-1c035f3e09e1.PNG)
![캡처1](https://user-images.githubusercontent.com/48250370/56863819-0ea3d500-69f6-11e9-8b9d-c8c174ed931d.PNG)
![캡처2](https://user-images.githubusercontent.com/48250370/56863820-0ea3d500-69f6-11e9-8969-961572a75eeb.PNG)

# 5주차 과제 : threading 모듈을 사용해 다수의 client의 요청을 받을 수 있는 서버 작성
### 인력거 운행중 조 : 김태완(2015040031), 김진용(2015040025)

* assignment_5
  - 서버는 클라이언트가 전송한 문자열을 뒤집어서 클라이언트에게 전송해준다.
  - 클라이언트는 서버 연결 후 input() 함수를 사용해 사용자로부터 문자열을 입력 받는다.
  - python thread_server.py -p 8888
  - python thread_client.py -p 8888 -i 127.0.0.1

<pre><code>$ python server_thread.py -p 8888
$ python client_thread.py -i 127.0.0.1 -p 8888 -i 127.0.0.1
$ python client_thread.py -i 127.0.0.1 -p 8888 -i 127.0.0.1
</code></pre>

![캡처](https://user-images.githubusercontent.com/48250370/55679961-88dcbe80-594e-11e9-9482-c0e425bc1eb2.PNG)

![캡처1](https://user-images.githubusercontent.com/48250370/55679935-4f0bb800-594e-11e9-96b9-f7dd795b000e.PNG)

![캡처2](https://user-images.githubusercontent.com/48250370/55679939-5206a880-594e-11e9-92fc-5c5b5c4a7a56.PNG)

# 6주차 과제 : threading 모듈을 사용해 서버와 클라이언트가 대화를 주고 받을 수 있는 프로그램 작성
### 인력거 운행중 조 : 김태완(2015040031), 김진용(2015040025)

* assignment_6
  - 서버는 클라이언트가 전송한 문자열 출력, input()으로 사용자 입력을 받아서 클라이언트에 전달
  - 클라이언트는 서버가 전송한 문자열 출력, input()으로 사용자 입력을 받아서 서버에 전달
  - 난이도 조절을 위해 서버는 1개의 클라이언트만 처리
  - python server_thread_talk.py -p 8888
  - python client_thread_talk.py -p 8888 -i 127.0.0.1

<pre><code>$ python server_thread_talk.file.py -p 8888
$ python client_thread_talk.py -i 127.0.0.1 -p 8888 -i 127.0.0.1
</code></pre>

![캡처](https://user-images.githubusercontent.com/48250370/56095331-895cf280-5f16-11e9-99c5-c9f9ca10f83c.PNG)

![캡처1](https://user-images.githubusercontent.com/48250370/56095332-895cf280-5f16-11e9-9437-4eaca9da0da0.PNG)

# 7주차 과제 : wireshark 프로그램에 대해서 조사한 뒤 보고서 작성
### 인력거 운행중 조 : 김태완(2015040031), 김진용(2015040025)

* assignment_7
  - wireshark 프로그램이란?
  - wireshark는 어떠한 라이브러리를 사용하는가?(Linux, Windows)
  - wireshark로 Assignment#2(문자열 거꾸로 전송)가 실행되면서 서버-클라이언트간 주고받은 TCP 패킷을 캡쳐해서 사진 첨부(문자열은 팀 이름을 전달)
  - 보고서는 3장 내로 작성(1~2장 : wireshark 조사, 3장 : 패킷 캡쳐 사진 및 설명)

![캡처](https://user-images.githubusercontent.com/48250370/56862989-a9e37d00-69eb-11e9-8c6d-06fb43355d26.PNG)
![캡처](https://user-images.githubusercontent.com/48250370/56864228-fedabf80-69fa-11e9-8dd1-d8caf040eb62.PNG)
![캡처1](https://user-images.githubusercontent.com/48250370/56864229-fedabf80-69fa-11e9-8408-17cc2fcec168.PNG)
![캡처2](https://user-images.githubusercontent.com/48250370/56864230-ff735600-69fa-11e9-8533-05be9f04a8ac.PNG)