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