# Ch3. 좋은 코드의 일반적 특징 Review

## 1. 추상화(Abstraction)

- 복잡한 소프트웨어 시스템을 효율적으로 설계하고 구현할 수 있는 방법
- 추상화는 뒷편 시스템의 기술적 복잡함을 단순한 API 뒤에 숨김(블랙박스화)

### 데이터 추상화의 장점

- 사용자가 낮은 수준의 코드를 작성하지 않도록 도움
- **코드 중복 방지 및 재사용성**
- 독립적으로 클래스의 내부 구현 변경 가능
- 중요한 세부 정보만 사용자에게 제공하므로 프로그램의 보안 향상



### Example) Django Decorator

```python
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```
---



## 2. 캡슐화(encapsulation)

- 데이터와 메소드를 하나의 단위로 결합
- 목적 : **데이터의 보호**
  - 유사 예) 의료 캡슐

- @property : getter, setter 
  - 파이썬은 private, public  예약어가 없음
  - 메서드를 은닉하고 속성처럼 사용하게 하기

```python
class Person:
    def __init__(self):
        self.__age = 0
 
    @property
    def age(self):           # getter: 값을 가져옴
        return self.__age
 
    @age.setter
    def age(self, value):    # setter: 값을 저장
        self.__age = value
 
james = Person()
james.age = 20      # 인스턴스.속성 형식으로 접근하여 값 저장
print(james.age)    # 인스턴스.속성 형식으로 값을 가져옴

# output : 20
```



##  3. SW Orthogonality

>*Changing A does not change B*

- 독립의 특수한 형태
- **독립성(independence), 결합도 줄이기(decoupling)**을 의미
- 생산성 향상



## 4. Defensive Programming

- 프로그램에서 정답을 얻는 첫번째 단계는 실수는 *일어난다고* 가정하고 이에 대비하여 방지하는 것
- 모든 오류에 대해 프로그래밍하는 것은 비효율적 => **Contract Programming**(DbC)으로 보완
- 가정 설정문(assertions)으로 구현
  - 올바르게 동작하기 위해서 함수의 시작점에서 참이여 되는 것은 [사전 조건(precondition)](http://statkclee.github.io/xwmooc-sc/gloss.html#precondition)이다.
  - 함수가 끝날 때 참을 보증하는 것이 [사후 조건(postcondition)](http://statkclee.github.io/xwmooc-sc/gloss.html#postcondition)이다.
  - 부분 코드 내부 특정한 지점에서 항상 참이어야 하는 것이 [불변식(invariant)](http://statkclee.github.io/xwmooc-sc/gloss.html#invariant)이다.



### TDD(Test-Driven Develipment)

- 함수를 작성하기 전에 테스트를 작성하는 것

- assertion 은 프로그램의 특정한 지점에서 무엇인가 참인지 확인 가능
- 다음 단계는 코드 일부분의 전반적인 동작을 확인
- 즉, 특정한 입력값에 대해 올바른 출력값을 만들어 내는지 확인
  - 각 test에 대해서 짧은 함수 작성(TDD)
  - 상기 테스트를 통한 목표(실제 테스트할) 함수를 작성
  - 만약 함수가 잘못된 대답을 준다면, 함수 리팩토링



## Summary

- **방어적으로 프로그램**하라. 즉, 오류가 발생한다고 가정하고 오류가 발생할 때 오류를 탐지하도록 코드를 작성하다.
- 프로그램에 가정 설정문을 넣어서 프로그램이 실행될 때 상태를 점검하게 하라. 그리고 프로그램을 읽는 사람이 작성한 프로그램이 어떻게 동작을 하는 것인지 이해할 수 있도록 도움을 줘라.
- 사전 조건을 사용해서 함수 입력값을 사용해도 안전한지 점검하라.
- 사후 조건을 사용해서 함수 출력값을 사용해도 안전한지 점검하라.
- 코드를 작성하기 전에 테스트를 작성해서 정확하게 코드가 무엇을 수행해야되는지 결정하도록 하라.



## refenrence

- [데이터 추상화와 캡슐화의 차이점](https://ko.strephonsays.com/difference-between-data-abstraction-and-encapsulation)
- [실용 파이썬 프로그래밍: 프로그래밍 유경험자를 위한 강좌](https://wikidocs.net/84421)

- [파이썬 코딩도장](https://dojang.io/mod/page/view.php?id=2476)

- [wikipedia](https://en.wikipedia.org/wiki/Orthogonality_(programming))

- [software-carpentry, 방어적 프로그래밍](http://statkclee.github.io/xwmooc-sc/novice/python/05-defensive.html)



# Ch4. Solid Principle in Python

- 데이터와 행위 => class
- 행위 => interface

## LSP

- **상속**의 메커니즘 표현
- User의 관점

- **부모 클래스의 인스턴스를 사용하는 위치에 자식 클래스의 인스턴스를 대신 사용했을 때 코드가 원래 의도대로 작동**
- `isinstance(자식 클래스의 인스턴스, 부모 클래스)` # True
- 반대로도 적용
- **부모 클래스의 인스턴스 자리에 자식 클래스의 인스턴스도 들어갈 수 있다**



### 문제점

- 오버라이딩
  - 자식클래스가 부모클래스의 변수 타입을 바꾸거나 메소드의 파라미터 혹은 리턴값의 타입이나 갯수를 바꾸는 경우
  - 자식클래스가 부모클래스의 의도와 다르게 메소드를 오버라이딩 하는 경우

### Example

#### Bad

```python
class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        """세로와 가로"""
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산 메소드"""
        return self.width * self.height

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._height = value if value > 0 else 1


class Square(Rectangle):
    """정사각형은 직사각형이다. isA 관계"""
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1
```

```python
rectangle_1 = Rectangle(3, 6)
rectangle_2 = Square(4)

rectangle_1.width = 2
rectangle_1.height = 5

print(rectangle_1.area())

rectangle_2.width = 2
rectangle_2.height = 5

print(rectangle_2.area())

#output
# 10
# 25
```

### Good

```python
class Square(Rectangle):
    def __init__(self, side):
        return self.side = side

    def area(self):
        """정사각형 넓이 계산 메소드"""
        return self.side * self.side

    @property
    def side(self):
        """한 변 getter 메소드"""
        return self._side

    @side.setter
    def side(self, value):
        """한 변 setter 메소드"""
        self._side = value if value > 0 else 1
```

```python
square = Square(4)
square.side = 6
print(square.area())
# output
# 36
```







## DIP

- **의존**과 관련

- 의존성을 역전시킨다는 것은 코드가 세부 사항이나 구체적인 구현에 적응하도록 하지 않고, 대신에 API 같은 것에 적응하도록 하는 것
- 추상화에 의존하는게 좋다.

>의존 관계(dependency)

- 한 클래스를 구현할 때 다른 클래스를 사용하면(클래스 간 관계, 객체 간 관계 모두 포함) 클래스 간에 의존 관계가 있다고 말한다.



### Example

#### Bad

```python
class SortManager:
    """A: B에 의존적(B의 메서드를 직접 사용)"""
    def __init__(self):
        self.sort_method = BubbleSort() # <--- SortManager 는 BubbleSort에 의존적
        
    def begin_sort(self):
        self.sort_method.bubble_sort() # <--- BubbleSort의 bubble_sort 메서드에 의존적

class BubbleSort:
    """B: 메서드의 이름을 바꾸면 A에 영향이 감"""
    def bubble_sort(self):
        # sorting algorithms
        pass
```

#### Good

````python
class SortManager:
    """의존성 역전
       하부 클래스가 바뀌더라도, 동일한 코드 활용 가능토록 인터페이스화 
    """
    def __init__(self, sort_method):    
        self.set_sort_method(sort_method)
        
    def set_sort_method(self, sort_method):
        self.sort_method = sort_method
        
    def begin_sort(self):
        self.sort_method.sort()        

class BubbleSort:
    def sort(self):
        print('bubble sort')
        pass

class QuickSort:
    def sort(self):
        print('quick sort')
        pass
````

```python
bubble_sort1 = BubbleSort()
quick_sort1 = QuickSort()

sorting1 = SortManager(bubble_sort1)
sorting1.begin_sort()

sorting2 = SortManager(quick_sort1)
sorting2.begin_sort()

# output
# bubble sort
# quick sort
```





## Reference

- [coding with Johan, SOLID Python](https://codingwithjohan.com/blog/solid-python-introduction/)
- [SOLID Coding in Python](https://towardsdatascience.com/solid-coding-in-python-1281392a6a94)

- [파이썬 클래스 설계방법](http://dbcafe.co.kr/wiki/index.php/%ED%8C%8C%EC%9D%B4%EC%8D%AC_%ED%81%B4%EB%9E%98%EC%8A%A4_%EC%84%A4%EA%B3%84%EB%B0%A9%EB%B2%95)

- [[자바 프로그래밍] 클래스 간 관계, 객체 간 관계 ](https://velog.io/@eunseo-kim/%EC%9E%90%EB%B0%94-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%81%B4%EB%9E%98%EC%8A%A4-%EA%B0%84-%EA%B4%80%EA%B3%84-%EA%B0%9D%EC%B2%B4-%EA%B0%84-%EA%B4%80%EA%B3%84)

- [[타키탸키's 컴퓨터 공부장], 리스코프 치환원칙](https://velog.io/@tataki26/%EB%A6%AC%EC%8A%A4%EC%BD%94%ED%94%84-%EC%B9%98%ED%99%98-%EC%9B%90%EC%B9%99)

