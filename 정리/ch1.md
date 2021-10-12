# Ch1. 소개, 코드 포매팅과 도구

## 학습목표

- 클린코드는 포매팅 이상의 훨씬 중요한 것을 의미
- 표준 포메팅을 유지하는 것이 유지보수성의 핵심 유의사항
- 파이썬이 제공하는 기능을 사용하여 자체 문서화된 코드를 작성하는 방법
- 코드의 레이아웃을 일정하게 유지하기

------

## 클린 코드란

- 프로그래밍 언어의 진정한 의미는 아이디어를 컴퓨터에 전달하는 것이 아니라 **다른 개발자에게 전달하는 것**이다.
- 개발자인 우리가 좋은 코드와 나쁜 코드의 차이점을 확인하고,
- 훌륭한 코드와 좋은 아키텍처의 특징을 식별하여 자신만의 정의를 하기

------

## 클린 코드의 중요성

- 빠른 개발과 지속적인 배포 가능(유지보수성)
- 기술 부채 : 나쁜 결정이나 적당한 타협의 결과로 생긴 소프트웨어적 결함
  - 장기적이고 근본적인 문제를 내포
  - 잠재적인 문제

### 클린 코드에서 코드 포매팅의 역할

- PEP-8 또는 프로젝트 가이드라인 같은 표준 지침을 따라 코드 포매팅을 한다고 클린 코드는 아님
- 클린 코드는
  - 품질 좋은 소프트웨어를 개발하고,
  - 견고하고 유지보수가 쉬운 시스템을 만들고,
  - 기술 부채를 회피하는 것
- 요약하면 클린코드와 포메팅의 정의의 차이
- **코드를 올바르게 포매팅하는 것은 작업을 효율화**한다.

### 프로젝트 코딩 스타일 가이드 준수

- **품질 표준을 지키기 위해** 프로젝트에서 따라야만 하는 최소한의 요구사항

- [PEP-8](https://www.python.org/dev/peps/pep-0008/)

  - 검색 효율성(Grepability) : 코드에서 토큰을 grep 할 수 있는 기능

  ```bash
  $ grep -nr "pytest" .
  ./Makefile:5:   pytest tests/
  ./requirements.txt:2:pytest==3.7.1
  ./src/test_annotations.py:6:import pytest
  ./src/test_annotations.py:11:@pytest.mark.parametrize(
  ```

  - 일관성 : 가독성이 높아지고 이해하기 쉬워짐
  - 코드 품질

------

## Docstring & Annotation

- 훌륭한 코드는 그 자체로 자명하지만 문서화 또한 잘 되어 있다.
- 문서화
  - 데이터 타입이 무엇인지 설명하고 예제를 제공
  - 주석(Comment)는 가급적 피해야 한다.
- 어노테이션
  - 파이썬은 동적으로 타입을 결정하기 때문에 함수, 메서드를 거치면 변수나 객체의 값이 무엇인지 알기 어렵다.
  - 어노테이션을 통해 이러한 정보를 명시
  - `Mypy` 같은 도구를 사욯해 타입 힌트 등의 자동화된 검증을 실행

### Docstring

- 소스코드에 포함된 문서
- 코드에 **주석**을 다는 것은 **여러 가지 이유로 나쁜 습관**
  - 코드로 아이디어를 제대로 표현하지 못했음을 나타냄
  - 코드와 주석의 불일치 ( 수정했을 경우 포함)
- Docstring은 코드의 특정 컴포넌트에 대한 문서화

### Annotation

- [PEP-3107](https://www.python.org/dev/peps/pep-3107/)
- 코드 사용자에게 함수 인자로 어떤 값이 와야 하는지 **힌트**를 주자
- 타입만이 아니라 파이썬 인터프리터에서 유효한 어떤 것도 사용 가능
  - 변수의 의도를 설명하는 문자열
  - 콜백이나 유효성 검사 함수 : `collable`
- type hinting을 활성화

```python
class Point:  # pylint: disable=R0903
    """Example to be used as return type of locate"""
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

def locate(latitude: float, longitude: float) -> Point:
    """Find an object in the map by its coordinates"""
    return Point(latitude, longitude)

class NewPoint:  # pylint: disable=R0903
    """Example to display its __annotations__ attribute."""
    lat: float
    long: float

print(locate.__annotations__)
# {'latitude': <class 'float'>, 'longitude': <class 'float'>, 'return': <class '__main__.Point'>}
print(NewPoint.__annotations__)
# {'lat': <class 'float'>, 'long': <class 'float'>}
```

- ```
  __annotations__
  ```

  - 문서 생성, 유효성 검증 또는 타입 체크를 할 수 있다.

- 타입 힌팅은 인터프리터와 독립된 추가 도구를 사용하여 코드 전체에 올바른 타입이 사용되었는지 확인하고 호환되지 않는 타입이 발견되었을 때 사용자에게 **힌트**를 주는 것

- Mypy

- 버그를 찾는 데 도움이 될 수 있으므로 Mypy를 설정하고 다른 정적 분석 도구와 함께 사용하는 것이 좋다.

### Annotation은 Docstring을 대체하는 것일까?

- 일부 가능
- 둘은 서로 보완적인 개념
- 하지만 docstring을 통해 보다 나은 문서화를 위한 여지를 남겨두어야 함

```python
def data_from_response(response: dict) -> dict:
    """response에 문제가 없다면 response의 payload를 반환
    - reponse 사전의 예제::
    {
        "status": 200, # <int>
        "timestamp": "....", # 현재 시간의 ISO 포맷 문자열
        "payload": { ... } # 반환하려는 사전 데이터 
    }

    - 반환 사전 값의 예제::
    {"data": { .. } }

    - 발생 가능한 예외:
    - HTTP status가 200이 아닌 경우 ValueError 발생
    """
    if responce["status"] != 200:
        raise ValueError
    return {"data": response["payload"]}
```

- 데이터의 유효성을 검사하고 사전 값을 반환하는 함수
- Annotation으로는 다 알 수 없다.
  - response 객체의 올바른 인스턴스는 어떤 형태일까?
  - 결과의 인스턴스는 어떤 형태일까?
- docstring으로 함수 반환 값의 예상 형태를 문서화

### 기본 품질 향상을 위한 도구 설정

- 이 코드를 동료 개발자가 쉽게 이해하고 따라갈 수 있을까?
- 업무 도메인에 대해서 말하고 있는가?
- 팀에 새로 합류하는 사람도 쉽게 이해하고 효과적으로 작업할 수 있을까?

1. **Mypy를 사용한 타입 힌팅**

- http://mypy-lang.org/
- 정적 타입 검사 도구
- 프로젝트의 모든 파일을 분석하여 타입 불일치를 검사
- 가끔 잘못 탐지하는 경우도 있다
- `$ pip install mypy`
- `mypy {파일명}`

```python
type_to_ignore = "something" # type: ignore
```

1. **Pylint를 사용한 코드 검사**

- 코드의 구조 검사
- `$ pip install pylint`
- `$ pylint`

1. **자동 검사 설정**

- creating a python makefile(

  링크

  )

  - [cmake](https://pypi.org/project/cmake/)

- makefile : 파일을 묶어주는 곳(compile)

- 프로젝트를 싱행하기 위한 설정을 도와주는 파워풀한 도구

- 포매팅 검사나 코딩 컨벤션 검사를 자동화하기 위해 사용 가능

```python
typehint:
	mypy --ignore-missing-imports src/

test:
	pytest tests/

lint:
	pylint src/

checklist: lint typehint test

black:
	black -l 79 *.py

setup:
	$(VIRTUAL_ENV)/bin/pip install -r requirements.txt

.PHONY: typehint test lint checklist black
```

1. **Black**

- [black](https://github.com/psf/black)
- 자동으로 코드를 포매팅