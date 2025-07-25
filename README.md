1. Algorithm
   - Searching (탐색)
      - [Brute-force Algorithm](#brute-force-algorithm-브루트포스-알고리즘)
      - [Backtracking](#backtracking-백트래킹-알고리즘)
   - Sorting (정렬)
      - [Counting Sort (계수 정렬)](#counting-sort-계수-정렬)
   - Number Theory (정수론)
      - [Primality Test (소수 판정)](#primality-test-소수-판정)
      - [Euclidean Algorithm (유클리드 호제법)](#euclidean-algorithm-유클리드-호제법)
2. Modules (모듈)
   - [General](#general)
   - [heapq](#import-heapq)
   - [re](#import-re)
   - [statistics](#import-statistics)
   - [math](#import-math)
   - [functools](#import-functools)
   - [collections](#import-collections)
   - [itertools](#import-itertools)
3. Data Type (자료형)
   - [List](#list)
   - [Set](#set)
   - [Dictionary](#dictionary)

---

# Algorithm
## Searching (탐색)
### Brute-force (브루트포스 알고리즘)
가능한 모든 경우의 수를 전부 탐색하여 답을 찾는 알고리즘<br>
-> 모든 경우를 탐색하므로 **시간 복잡도 O(n!), O(2^n)등 높음**

### Backtracking (백트래킹 알고리즘)
해를 찾는 도중 막히면 왔던 길을 되돌아가서 다시 해를 찾는 기법<br>
최적화 문제, 결정 문제에서 많이 사용 -> **미로 찾기, N-Queen, Map coloring, 부분 집합의 합 등**<br>
```
def recursive(n):
   if solution: print or save
   else:
      for all child node:
         if promising(m):
            move child node
            recursive(n+1)
            move parent node
def promising(m):
   if not condition: return False
   else: return True
```

## Sorting (정렬)
### Counting Sort (계수 정렬)
값의 범위가 작은 경우 빠른 속도를 갖는 정렬 알고리즘<br>
(Input Array = IA, Counting Array = CA, Result Array = RA)<br>
**양수 배열**
```
0. IA length = n = RA length
1. CA length = max(IA) + 1 = k
2. CA[IA[i]] += 1 (i = range(0, n))
3. CA[i] += CA[i-1] (i = range(1, k))
4. RA[CA[IA[i]]-1] = IA[i]
   CA[IA[i]] -= 1 (i = range(n-1, -1, -1))
```
**음수 포함 배열 (offset 이용)**
```
0. IA length = n = RA length;
   offset = -1 * min(IA)
1. CA length = max(IA) - min(IA) + 1 = k
2. CA[IA[i] + offset] += 1 (i = range(0, n))
3. CA[i] += CA[i-1] (i = range(1, k))
4. RA[CA[IA[i + offset]]-1] = IA[i];
   CA[IA[i + offset]] -= 1 (i = range(n-1, -1, -1))
```
-> **Stable Sort** (3 - Accumulate, 4 - Reverse Insertion)

1,2,4번 과정 O(n), 3번 과정 O(k) -> **시간 복잡도 O(n + k), 메모리 사용량 O(k)**
즉, IA의 최댓값이 변수로 작용 - 범위가 작을 때 높은 효율

## Number Theory (정수론)
### Primality Test (소수 판정)
주어진 정수가 소수인지 아닌지를 판별하는 알고리즘.
#### Trial Division (기본 소수 판별법)
가장 간단한 소수 판별법.
```
1. if n % i == 0 return False (i = range(2, n^0.5 + 1))
```
-> **시간 복잡도 O(n^0.5)**
#### Sieve of Eratosthenes (에라토스테네스의 체)
한꺼번에 많은 수의 소수를 판별할 때 사용. <br>
(Prime Array = PA)
```
1. PA length = n + 1, PA[0:2] = False
2. if PA[i], PA[j] = False (i = range(2, n^0.5 + 1), j = range(i*i, n+1, i))
3. if PA[i], isPrime(i) = True
```
-> **시간 복잡도 O(n log log n), log = 이진 로그** 
### Euclidean Algorithm (유클리드 호제법)
최대공약수를 구할 때 가장 빠르고 간단한 알고리즘.
```
1. a, b (a > b), a % b == r
2. a, b = b, a % b while b != 0 (gcd(a, b) = gcd(b, r))
```
-> **시간 복잡도 O(log(min(a, b)))**

---

# Modules
## General
**일반적인 함수에 대한 설명**
- `enumerate(iter)` : iterable한 객체를 반복하며 인덱스와 값 동시 추출

## import heapq
**리스트를 힙 구조로 다룰 수 있게 하는 모듈**
- `.heapify(list)` : 힙 구조 변경
- `.heappush(heap, x)` : 힙 추가(정렬) / `.heappop(heap)` : 가장 작은 값 추출
- `.nlargest(k, iter)` : 가장 큰 값 k개 리스트로 반환
- `.nsmallest(k, iter)` : 가장 작은 값 k개 리스트로 반환

## import re
**파이썬 정규표현식 모듈**<br/>
정규표현식 앞에 r(raw string)을 붙여 사용
- `.match(re, s)` : 문자열 시작부터 패턴 확인
- `.search(re, s)` : 문자열 어디든 패턴 확인
- `.findall(re, s)` : 모든 패턴을 리스트로 반환
- `.finditer(re, s)` : 모든 패턴을 이터레이터로 반환
- `.sub(re, s2, s1)` : 패턴을 다른 문자열로 치환
- `.split(re, s)` : 패턴을 기준으로 문자열 분리

## import statistics
**기초 통계 계산을 도와주는 내장 모듈**
- `.mean(x)` : 평균 / `.median(x)` : 중앙값 (짝수 개면 평균 중앙값)
- `.multimode(x)` : 최빈값 (값이 여러개여도 반환)
- `.[p]stdev(x)` : [모]표준편차 / `.[p]variance(x)` : [모]분산
- `.quantiles(data, n)` : 분위 계산

## import math
**수학 관련 함수들을 모아놓은 표준 라이브러리**
- `.ceil(x)` : 올림 / `.floor(x)` : 내림
- `.sqrt(x)` : 제곱근 / `.isqrt(n)` :  정수 제곱근
- `.pow(x, y)` : 거듭제곱(x^y) / `.factorial(n)` : 팩토리얼
- `.gcd(x, y)` : 최대공약수 / `.lcm(x, y)` : 최소공배수
- `.log(x, y)` : 로그(밑이 y, 기본 e) / `.exp(x)` : 자연상수 제곱
- `.prod(x)` : 곱셈
- `.sin(x), .cos(x), .tan(x)` : 삼각함수
- `.radians(deg)` : 각도 -> 라디안 / `degrees(rad)` : 라디안 -> 각도
- `.pi` : 원주율 / `.e` : 자연로그 밑 / `.inf` : 무한대 / `.nan` : 숫자 아님

## import functools
**함수를 다루는 데 유용한 내장 모듈**
- `.reduce(func, iter)` : iterable 객체에 왼쪽에서 오른쪽으로 누적 계산
- `.lru_cache(maxsize=None)` : 재귀 함수 자동 캐싱
- `.partial(func, *args, **kwargs)` : 함수 인자 일부 고정해서 새 함수 생성
- `.cmp_to_key(func)` : 옛날 방식 비교 함수 사용 가능
- `@ .wraps(func)` : 데코레이터 안에서 원래 함수 메타데이터 유지

## import collections
**고급 자료구조를 제공하여 다양한 방식으로 데이터를 다룰 수 있는 표준 라이브러리**
- `.Counter(iter)` : 요소의 개수를 셀 때 사용
- `.defaultdict(type)` : 기본값이 자동 설정되는 딕셔너리
- `.namedtuple(name, iter)` : 이름이 있는 튜플
- `.deque(iter)` : 덱

## import itertools
**반복과 관련된 작업을 쉽게 처리할 수 있도록 도와주는 고성능 표준 라이브러리**<br>
모든 함수의 반환값은 이터레이터라 list() 필수
- `.permutations(iter, r)` : r개 순열 / `.product(iter, r)` : r개 중복 순열
- `.combinations(iter, r)` : r개 조합 / `.combinations_with_replacement(iter, r)` : r개 중복 조합
- `.accumulate(iter)` : 누적 합 / `.accumulate(iter, func)` : 누적 함수 적용
- `.count(start, step)` : 무한 반복 숫자 생성
- `.cycle(iter)` : 객체 무한 반복 / `.repeat(element, times)` : 같은 값 반복
- `.groupby(iter, key)` : 연속된 동일한 값을 그룹화
- `.filterfalse(func, iter)` : 함수가 False인 값만 추출
- `.dropwhile(func, iter)` : 함수가 True인 동안 버리다가 첫 False부터 전부 반환
- `.takewhile(func, iter)` : 함수가 True인 동안 반환, False가 나오면 즉시 중단
---

# Data Type
## List
**순서가 있는(Ordered), 변경 가능한(Mutable) 자료구조**
- 순서가 있어 인덱스 접근 가능
- 중복 허용
- 삽입, 삭제, 정렬 등 다양하게 조작 가능
- 탐색 시간 O(n) - 선형 탐색(Linear Search) ex. `x in list`

**Method**
- `l.append(x)` : 리스트 끝에 x 추가
- `l.extend(iter)` : 리스트 끝에 iterable한 모든 요소 추가
- `l.index(x)` : x의 인덱스 추출

## Set
**순서가 없고(Unordered), 변경 가능한(Mutable) 자료구조**
<br/>
frozenset은 변경 불가능(Immutable)
- 순서가 없어 인덱스 접근 불가능
- 중복 자동 제거
- 탐색, 삽입, 삭제가 빠름
- 탐색 시간 O(1) - 해시 탐색(Hash Table) ex. `x in set`

**Method**
- `s.add(x)` : 원소 x 추가
- `s.remove(x)` : 원소 x 제거 (없으면 에러 발생)
/ `s.discard(x)` : 원소 x 제거 (없어도 에러 X)
- `s.clear()` : 모든 원소 제거
- `s.update(iter)` : 여러 요소 한번에 추가 (원본 변경)
/ `s.union(iter)` : 여러 요소 한번에 추가 (새 Set 반환)

## Dictionary
**변경 가능한(Mutable) Key - Value 쌍 자료구조**
- 입력 순서 보장
- 키 중복 불가
- 해시 가능한 키 값 (Immutable)
- 삽입, 조회, 삭제가 빠름
- 탐색 시간 O(1) - 해시 탐색(Hash Table, Map), 최악 O(n)

**Method**
- `d.get(key, default)` : 값 조회, 키 없으면 default 값 반환
/ `d["a"]` : 값 조회, 키 없으면 오류
- `d.keys()` : 키 목록 반환 / `d.values()` : 값 목록 반환
- `d.items()` : (키, 값) 쌍 반환
- `d.pop(key)` : 키 제거하고 값 반환
- `d.update({key: value}) == d.update(key=value) == d.update([(key, value)])`<br/>
: 키-값 쌍 한번에 추가, 키 존재 시 값 덮어씀 / 키워드 방식(key=value)은 문자열 키에만 사용 가능

## Stack, Queue, Deque
**Stack : LIFO(Last In, First Out) 방식의 자료구조**
- ex. 웹 브라우저 "뒤로 가기", 수식 괄호 검사, DFS, Undo 기능
**Queue : FIFO(First In, First Out) 방식의 자료구조**
- ex. 프린터 대기열, 멀티스레딩 작업 대기열, BFS
**Deque : 양방향 I/O 방식의 자료구조**
- ex. 슬라이딩 윈도우, BFS
-> 파이썬에서는 모두 collections.deque를 사용해서 구현 가능

**Method**
- `dq.append(x)` : 오른쪽 끝에 요소 추가 / `dq.appendleft(x)` : 왼쪽 끝에 요소 추가
- `dq.pop()` : 오른쪽 끝에서 요소 제거 / `dq.popleft()` : 왼쪽 끝에서 요소 제거
- `dq.extend(iterable)` : 오른쪽 끝에 iterable 요소 추가 / `dq.extendleft(iterable)` : 왼쪽 끝에 iterable 요소 추가
- `dq.rotate(n)` : 덱 회전(양수는 오른쪽으로, 음수는 왼쪽으로)
- `dq.clear()` : 덱 요소 모두 제거
- `dq.remove(value)` : 덱에서 첫 번째로 나오는 요소 제거
- `dq.count(x)` : 요소 개수 카운팅