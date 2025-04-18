# Algorithm

## import re
### re 모듈
파이썬 정규표현식 모듈. 정규표현식 앞에 r(raw string)을 붙여 사용.
- match(re, s) : 문자열 시작부터 패턴 확인
- search(re, s) : 문자열 어디든 패턴 확인
- findall(re, s) : 모든 패턴을 리스트로 반환
- finditer(re, s) : 모든 패턴을 이터레이터로 반환
- sub(re, s2, s1) : 패턴을 다른 문자열로 치환
- split(re, s) : 패턴을 기준으로 문자열 분리리

## import statistics
### statistics 모듈
기초 통계 계산을 도와주는 내장 모듈.
- mean(x) : 평균 / median(x) : 중앙값 (짝수 개면 평균 중앙값)
- multimode(x) : 최빈값 (값이 여러개여도 반환)
- [p]stdev(x) : [모]표준편차 / [p]variance(x) : [모]분산
- quantiles(data, n) : 분위 계산


## import math
### math 모듈
수학 관련 함수들을 모아놓은 표준 라이브러리.
- ceil(x) : 올림 / floor(x) : 내림
- sqrt(x) : 제곱근 / isqrt(n) :  정수 제곱근
- pow(x, y) : 거듭제곱(x^y) / factorial(n) : 팩토리얼
- gcd(x, y) : 최대공약수 / lcm(x, y) : 최소공배수
- log(x, y) : 로그(밑이 y, 기본 e) / exp(x) : 자연상수 제곱

- sin(x), cos(x), tan(x) : 삼각함수
- radians(deg) : 각도 -> 라디안 / degrees(rad) : 라디안 -> 각도

- .pi : 원주율 / .e : 자연로그 밑 / .inf : 무한대 / .nan : 숫자 아님