# Ch5. Decorator

# 1. 파이썬의 데코레이터

- [PEP-318](https://www.python.org/dev/peps/pep-0318/) : 함수와 메서드의 기능을 쉽게 수정하기 위한 수단
- 데코레이터 이후에 나오는 것을 데코레이터의 첫 번째 파라미터로 하고 데코레이터의 결과 값을 반환하게 하는 **문법적 설탕**
- 데코레이터는 깔끔한 프로그래밍 interface를 정의하는 훌륭한 방법
- 좋은 데코레이터는 깔끔한 인터페이스를 제공하고 사용자가 내부 동작 원리를 자세히 몰라도 기대하는 바를 정확히 알 수 있게 해줘야 함

### Effective Python

- 감싸고 있는 함수를 호출하기 전이나 후에 추가로 코드를 실행하는 기능
- 이 기능으로 입력 인수와 반환 값을 접근하거나 수정
- 시맨틱 강조, 디버깅, 함수 등록을 비롯해 여러 상황에 유용

### 라이브러리

- 표준 라이브러리
  - `@staticmethod` : 인스턴스를 생성하지 않아도 calss의 메서드를 바로 실행
  - `@classmethod` : self 사용 가능
  - `@property`
    - 변수를 변경 할 때 제한을 둘 때
    - get, set 함수를 만들지 않고 접근 가능
    - reference([link1](https://www.programiz.com/python-programming/property))
- functools
  - `@wraps` : 원래의 함수를 디버깅, doctest 할 때 사용
    - reference([link1](https://velog.io/@doondoony/python-functools-wraps))

> **문법적 설탕(Syntax Sugar)**

- 어떤 언어에서 동일한 기능이지만 간결성, 가독성을 높이기 위해 다른 표현으로 코딩할 수 있게 해주는 기능

```python
def original(...):
...
original = modifier(original)
@modifier
def original(...):
    ...
```

## 1-1. 함수 데코레이터

- 어떤 종류의 로직이라도 적용가능
- 유효성 검사
- 사전조건 검사
- 기능 전체 재정의
- 서명을 변경
- 원래 함수 결과 캐싱

## 1-2. 클래스 데코레이터

- 클래스의 데코레이터는 남용할 경우
  - 복잡하고 가독성을 떨어뜨림
  - 클래스에서 정의한 속성과 메서드를 데코레이터 안에서 완전히 다른 용도로 변경 가능
- 코드 재사용, dry 원칙의 모든 이점 공유
  - 여러 클래스가 특정 interface나 기준을 따르도록 강제할 수 있음
  - 여러 클래스에 적용할 검사를 데코레이터에서 한 번만 하면 됨
- 작은 클래스를 생성하고, 데코레이터로 기능 보강
- 유지보수시 기존 로직을 훨씬 쉽게 변경

## 1-3. 다른 유형의 데코레이터

- 데코레이터는 스택 형태
  - 제너레이터, 코루틴, 데코레이트된 객체도 데코레이터 가능
- 코루틴으로 사용되는 제너레이터

## 1-4. 데코레이터에 인자 전달

### 중첩함수

- 고차 함수(higher-order function) : 함수를 파라미터로 받아서 함수를 반환하는 함수

### 데코레이터 객체

- 클래스를 사용하여 데코레이터 정의
  - `__init__` 메서드에 파라미터 전달
  - `__call__` 매직 메서드에 데코레이터의 로직 구현

## 1-5. 데코레이터 활용 우수 사례

- 파라미터 변환
- 코드 추적
- 파라미터 유효성 검사
- 재시도 로직 구현
- 일부 반복 작업을 데코레이터로 이동하여 클래스 단순화

------

# 2. 데코레이터의 활용 - 흔한 실수 피하기

## 2-1. 래핑된 원본 객체의 보존

- 원본 함수의 일부 프로퍼티나 또는 속성을 유지하지 않아 원하지 않는 부작용 발생
  - `help()` 함수가 새로운 함수의 이름을 출력
  - 개별 함수 확인이 어려움
  - docstring이 덮어씌워짐 ⇒ doctest 모듈(mypy, pylint 등)로 확인 x
- 내장 모듈인 functools 의 wraps 사용
  - 로그를 남기는 데코레이터
  - 래핑된 함수라는 것을 알려줌

```jsx
from functools import wraps
@wraps(func)
```

## 2-2. 부작용 처리

- 데코레이터 함수가 되기 위해 필요한 하나의 조건은 가장 안쪽에 정의된 함수여야 한다는 것
  - 그렇지 않으면 import에 문제가 발생할 수 있음

### 데코레이터 부작용의 잘못된 처리

- 데코레이터 내에 @wraps 를 활용해 해결

### 데코레이터 부작용의 활용

- 부작용을 의도적으로 사용하여 실제 실행이 가능한 시점까지 기다리지 않는 경우
- ex) 모듈의 공용 레지스트리에 객체를 등록하는 경우

## 2-3. 어느 곳에나 동작하는 데코레이터 만들기

- 데코레이터를 만들 때 일반적으로 재사용을 고려하여 함수뿐 아니라 메서드에서도 동작하길 바람
- `*args` , `**kwargs` 서명을 사용하여 데코레이터를 정의하면 모든 경우에 사용할 수 있음

> ```
> *args
> ```

- 여러개의 인자를 받을 때 사용
- tuple 형태로 받아옴
- 일반 변수보다 뒤에 위치해야 함

> ```
> **kwargs
> ```

- {'key': 'value} 형태로 함수를 호출
- dict 형태로 함수 내부로 전달
- 그러나 다음 두 가지 이유로 원래 함수의 서명과 비슷하게 데코레이터를 정의하는 것이 좋을 때가 있다.
  1. 원래의 함수와 모양이 비슷하기 때문에 읽기 쉽다. (가독성)
  2. 파라미터를 받아서 뭔가를 하려면 `*args` , `**kwargs` 사용하는 것이 불편

# 3. 데코레이터와 DRY 원칙

- 특정 기능을 한 번만 정의해서 사용(DRY)
- 컴포넌트가 충분히 재사용 가능한 추상화를 했다고 인정받기 위해서는 적어도 3가지 이상의 애플리케이션에서 시험해봐야 함
- 동시에 같은 레퍼런스에서 재사용 가능한 컴포넌트를 만드는 것은 일반 컴포넌트를 만드는 것보다 세 배 어렵다

### 다음과 같은 사항을 고려했을 때 데코레이터 사용을 권함

- 처음부터 데고레이터를 만들지 않는다. 패턴이 생기고 데코레이터에 대한 추상화가 명확해지면 그 때 리팩토링 한다.
- 데코레이터가 적어도 3회 이상 필요한 경우에만 구현
- 데코레이터 코드를 최소한으로 유지

# 4. 데코레이터와 관심사의 분리

- 데코레이터에 하나 이상의 책임을 두면 안 된다. (SRP)

# 5. 좋은 데코레이터 분석

### 훌륭한 데코레이터가 갖추어야 할 특성

- 캡슐화와 관심사의 분리
  - 좋은 데코레이터는 실제로 하는 일과 데코레이팅하는 일의 책임을 명확히 구분해야 함
  - 어설프게 추상화 하면 안 됨
  - 즉, 데코레이터의 클라이언트는 내부에서 어떻게 구현했는지 전혀 알 수 없는 **블랙박스 모드로 동작**해야 한다.
- 독립성
  - 데코레이터가 하는 일은 독립적이어야 하며 데코레이팅되는 객체와 최대한 분리되어야 함
- 재사용성
  - 데코레이터는 여러 유형에 적용 가능한 형태가 바람직
  - 충분히 범용적이어야 함(저자는 최소 3개)

https://github.com/celery/celery
