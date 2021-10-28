# Ch4. SOLID 원칙

- S : SRP(Single Responsibilty Principle) 단일 책임 원칙
- O : OPC(Open Closed Principle) 개방/폐쇄 원칙
- L : LSP(Liskov Substitusion Principle) 리스코프 치환 법칙
- I : ISP(Interface Segregation Principle) 인터페이스 분리 원칙
- D - DIP(Dependency Inversion Principle) 의존성 역전 법칙



- SOLID 원칙은 설계를 할 때 지켜야 할 당연한 원칙들
- 리팩토링할 때 이 원칙들에 기반하여 할 수 있음



### Reference

- [SOLID Coding in Python](https://towardsdatascience.com/solid-coding-in-python-1281392a6a94)

- [Polymorphism in Python](https://www.programiz.com/python-programming/polymorphism)

# 1. S, SRP 단일 책임 원칙

> A class should have one and only one reason to change, meaning that a class should have only one job.

- 소프트웨어 컴포넌트(일반적으로 클래스)는 단 하나의 책임을 져야한다.
- 유일한 책임은 하나의 구체적인 일을 담당한다는 것이며, 따라서 변화해야 할 이유는 단 하나임

- SW 디자인에서 SRP는 응집력과 밀접한 관련이 있다.
  - 클래스에 있는 프로퍼티와 속성이 항상 메서드를 통해서 사용되도록 하는 것



- 클래스의 메서드는 상호 배타적이며 서로 관련이 없어야 함
- 이들은 서로 다른 책임을 가지고 있으므로 더 작은 클래스로 분해할 수 있어야 함



# 2. O, OPC 개방/폐쇄 원칙

> Objects or entities should be open for extension but closed for modification.

- 모듈이 개방되어 있으면서도 폐쇄되어야 한다는 원칙
- 클래스를 디자인할 때는 유지보수가 쉽도록 로직을 캡슐화하여 확장에는 개방되고
  수정에는 폐쇄되도록 해야함
- 즉, 확장 가능하면서 새로운 요구사항이나 도메인 변화에 잘 적응하는 코드를 작성해야한다는 뜻



# 3. L, LSP 리스코프 치환 법칙

> Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.

- S가 T의 하위 타입이라면 프로그램을 변경하지 않고 T 타입의 객체를 S 타입의 객체로 치환 가능해야 함

- 자식 클래스는 언제나 자신의 부모클래스와 교체할 수 있다는 원칙

- 안정성을 유지하기 위해 객체 타입이 유지해야하는 일련의 특성
- 어떤 클래스에서든 **클라이언트는 특별한 주의를 기울이지 않고도 하위 타입을 사용할 수 있어야 한다는 것**



- 인터페이스의 메서드가 **올바른 계층구조**를 갖도록 하여 상속된 클래스가 부모 클래스와 다형성을 유지하도록 하는 것

- LSP는 객체지향 소프트웨어 설계의 핵심이 되는 **다형성**을 강조

## 다형성(Polymorphism)

> *다형성이란 프로그램 언어 각 요소들(상수, 변수, 식, 객체, 메소드 등)이 다양한 자료형(type)에 속하는 것이 허가되는 성질을 가리킨다. - 위키피디아 중 -*

- 같은 모양의 코드가 다른 동작을 하는 것



# 4. I, ISP 인터페이스 분리 원칙

> A client should never be forced to implement an interface that it doesn’t use, or clients shouldn’t be forced to depend on methods they do not use.

- 클래스에서 사용하지 않거나 상관없는 메서드는 분리해야 함

- 다중 메서드를 가진 인터페이스가 있다면 매우 정확하고 구체적인 구분에 따라 더 적은 수의 메서드(가능하면 하나)를 가진 여러 개의 메서드로 분할하는 것이 좋음



> 인터페이스(Interface)

- 객체 지향적인 용어로 인터페이스는 객체가 노출하는 메서드의 집합



### 덕 타이핑 (Duck Typing)

- reference : [Py300](https://uwpce-pythoncert.github.io/Py300/ABCs.html)

- 모든 객체는 자신이 가지고 있는 메서드와 자신이 할 수 있는 일에 의해서 표현된다
- 클래스의 유형, 이름, docstring, 속성 또는 인스턴스 속성에 관계없이
  **객체의 본질을 정의하는 것은 궁극적으로 메서드의 형태**

- 즉, 객체의 적합성은 객체의 실제 유형이 아니라 **특정 메서드와 속성의 존재에 의해 결정**

- 덕 타이핑은 파이썬에서 인터페이스를 정의하는 유일한 방법이었다.
- [PEP-3119](https://www.python.org/dev/peps/pep-3119/) 에서 덕 타이핑을 공식적으로 접근하는, 인터페이스를 정의하는 추상 기본 클래스 개념을 도입

```python
In [117]: isinstance([1,2,3], list)
Out[117]: True

In [118]: isinstance([1,2,3], tuple)
Out[118]: False
```

- 추상화 클래스를 이용 (ABC)

```python
from collections.abc import Sequence

In [121]: isinstance([1,2,3,4], Sequence)
Out[121]: True

In [122]: isinstance((1,2,3,4), Sequence)
Out[122]: True
```





# 5. D, DIP 의존성 역전 법칙

> Abstractions should not depend on details. Details should depend on abstraction. High-level modules should not depend on low-level modules. Both should depend on abstractions

- 9장, 10장에서 다시 한번 봄

- 의존성을 역전시킨다는 것은 코드가 세부 사항이나 구체적인 구현에 적응하도록 하지 않고, 대신에 API 같은 것에 적응하도록 하는 것

- 추상화에 의존하는게 좋다.



> Example

- A, B 두 객체가 상호 교류
- A는 B의 인스턴스를 사용
- 만약 코드가 B에 크게 의존하면, B코드가 변경되었을 때 원래의 코드는 쉽게 깨짐

=> 의존성을 뒤집는다. 즉, **B가 A에 적응하게 해야 함**

- 이는 인터페이스를 개발하고 코드가 B의 구체적인 구현에 의존하지 않도록 하면 됨
  - A는 인터페이스에 의존적
  - 인터페이스를 준수하는 것은 B의 책임
- 이러한 방식은 **API가 하는 방식과 동일함**

![img](https://miro.medium.com/max/633/1*7rFi864XfIo2VGG9DCCF8g.png)



### 의존성 주입(Dependecy Injection)

- 필요로 하는 객체를 스스로 생성하는 것이 아닌 외부로 부터 주입받는 기법

- DIP를 구현하는 기법중 하나(의존성을 동적으로 부여)
- DI 기법의 장점
  - 의존성이 줄어듬
  - 재사용성이 높은 코드
  - 테스트하기 좋은 코드
  - readability



