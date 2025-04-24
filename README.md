# Algorithm
1. [Sorting](#sorting)
2. [Modules](#modules)

## Sorting

### Counting Sort (계수 정렬)
**값의 범위가 작은 경우 빠른 속도를 갖는 정렬 알고리즘.**

(Input Array = IA, Counting Array = CA, Result Array = RA)

#### 양수 배열
```
0. IA length = n = RA length
1. CA length = max(IA) + 1 = k
2. CA[IA[i]] += 1 (i = range(0, n))
3. CA[i] += CA[i-1] (i = range(1, k))
4. RA[CA[IA[i]]-1] = IA[i]; CA[IA[i]] -= 1 (i = range(n-1, -1, -1))
```

#### 음수 포함 배열 (offset 이용)
```
0. IA length = n = RA length; offset = -1 * min(IA)
1. CA length = max(IA) - min(IA) + 1 = k
2. CA[IA[i] + offset] += 1 (i = range(0, n))
3. CA[i] += CA[i-1] (i = range(1, k))
4. RA[CA[IA[i + offset]]-1] = IA[i]; CA[IA[i + offset]] -= 1 (i = range(n-1, -1, -1))
```
-> Stable Sort (3 - Accumulate, 4 - Reverse Insertion)

1,2,4번 과정 O(n), 3번 과정 O(k) -> **시간 복잡도 O(n + k), 메모리 사용량 O(k)**
즉, IA의 최댓값이 변수로 작용 - 범위가 작을 때 높은 효율

## Modules
### General
**일반적인 함수에 대한 설명**
- `enumerate(iter)` : iterable한 객체를 반복하며 인덱스와 값 동시 추출
- `append(x)` : 리스트 끝에 x 추가 / `extend(iter)` : 리스트 끝에 iterable한 모든 요소 추가

### import heapq
**리스트를 힙 구조로 다룰 수 있게 하는 모듈**
- `heapify(list)` : 힙 구조 변경
- `heappush(heap, x)` : 힙 추가(정렬) / `heappop(heap)` : 가장 작은 값 추출
- `nlargest(k, iter)` : 가장 큰 값 k개 리스트로 반환
- `nsmallest(k, iter)` : 가장 작은 값 k개 리스트로 반환

### import re
**파이썬 정규표현식 모듈**<br/>
정규표현식 앞에 r(raw string)을 붙여 사용
- `match(re, s)` : 문자열 시작부터 패턴 확인
- `search(re, s)` : 문자열 어디든 패턴 확인
- `findall(re, s)` : 모든 패턴을 리스트로 반환
- `finditer(re, s)` : 모든 패턴을 이터레이터로 반환
- `sub(re, s2, s1)` : 패턴을 다른 문자열로 치환
- `split(re, s)` : 패턴을 기준으로 문자열 분리

### import statistics
**기초 통계 계산을 도와주는 내장 모듈**
- `mean(x)` : 평균 / `median(x)` : 중앙값 (짝수 개면 평균 중앙값)
- `multimode(x)` : 최빈값 (값이 여러개여도 반환)
- `[p]stdev(x)` : [모]표준편차 / `[p]variance(x)` : [모]분산
- `quantiles(data, n)` : 분위 계산


### import math
**수학 관련 함수들을 모아놓은 표준 라이브러리**
- `ceil(x)` : 올림 / `floor(x)` : 내림
- `sqrt(x)` : 제곱근 / `isqrt(n)` :  정수 제곱근
- `pow(x, y)` : 거듭제곱(x^y) / `factorial(n)` : 팩토리얼
- `gcd(x, y)` : 최대공약수 / `lcm(x, y)` : 최소공배수
- `log(x, y)` : 로그(밑이 y, 기본 e) / `exp(x)` : 자연상수 제곱
- `prod(x)` : 곱셈
- `sin(x), cos(x), tan(x)` : 삼각함수
- `radians(deg)` : 각도 -> 라디안 / `degrees(rad)` : 라디안 -> 각도
- `.pi` : 원주율 / `.e` : 자연로그 밑 / `.inf` : 무한대 / `.nan` : 숫자 아님