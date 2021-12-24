# Auto Generated Password

## 개요

프로젝트의 요구에 따라 1000개의 계정에 대한 비밀번호를 생성해서 제공해달라 라는 경우가 있었다.

그럴때마다 엑셀로 짜서 넘겼었는데, 이번에 한 1~20분 짬내서 이걸 만드는 소스 코드를 짜보려고 한다.

## 구성

1. 비밀번호 생성 갯수

1. 어떤 비밀번호를 사용할건지 ? 
    1. 대문자로만?
    1. 소문자로만?
    1. 특수문자 포함?

2. 비밀번호의 길이는?
    1. 숫자 입력 받기

3. 비밀번호 저장 방식은?
    1. csv, txt

## 사용 방법

```cmd
> #명령 프롬프트 실행
> python createRandomPassword.py
```