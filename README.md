# 과제 수행
## https://github.com/dj-twenty-six/101/issues/22 
### docker 
--- 
Dockerfile
### Python 3.12 버전사용
FROM python:3.12
### 업데이트 및 vim 설치
RUN apt-get update && apt-get install -y vim
### 작업장소 app
WORKDIR /app
### 컨테이너와 호스트와의 연결을 app으로 설정
VOLUME ["/app"]
### 들어가기 위한 커맨드
CMD ["/bin/bash"]

###
내부 python 코드
명령어
* docker run -it --name mycontainer -v app dockerfile /bin/bash
* vi chocie.py (vi 파일 생성 및 내부 코드 수정)
  ![스크린샷 2023-10-31 112955](https://github.com/Sam1000won/random_chocie/assets/135206238/cfbf0138-d7d2-42a9-9d90-771d7649c931)
* python chocie.py(python 을 사용하여 코드 실행)
![스크린샷 2023-10-31 113051](https://github.com/Sam1000won/random_chocie/assets/135206238/fc8d9158-5689-4e6e-8e06-857ff48ad64e)

