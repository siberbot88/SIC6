from typing import List, Dict, Optional, Union, Callable
import numpy as np

list_str = ['indonesia', 'dua belas', 'bahrain', '88']
values = 4.7, 4.4, 6.3

def should_use(annotations: List[str]) -> bool:
    print("They're awesome")
    return True

def add(a: int, b:int) -> int:
    return a+b 

def process_names(names: List[str]) -> Dict[str,int]:
    return {name:len(name) for name in names}

def greet(name: Optional[str]) -> str:
    return f"hello, {name or 'guest'}"

def process_number(value: Union[int, float]) -> float:
    return value * 2.5

# or 

class person:
    def __init__ (self, name: str, age: int):
        self.name: str = name
        self.age: int = age
    
    def get_info(self) -> str:
        return f"{self.name} is {self.age} years old"
    

NamesList = List[str]
def apply_function(f: Callable[[int, int], int], x:
    int, y:int) -> int:
    return f(x,y)


################################################
print(add("5", "1"))
print(process_names(list_str))
print(should_use(list_str))
print(greet(list_str))
print(process_number(4.9))




