# Syl Grammar
## Basics
File extention: `.syl`

----
### Hello world
```
int _main():
    print("hello world");
    return 0;
```
----
### Functions
```
void _myFunction():
    print("hello");
    print("Random number") << rand.inRangeOf(100);
```
----
### Basic application
```
int _main():
    void _myFunction():
        print("Random number") << rand.inRangeOf(100);
    
    _myFucntion();
    return 0;
```
----
### Importing Code

```
#import <ep<some-package>>

#import <ip<other-package>>
```

`ep - External package`

`ip - Internal package`

----

### if/else/elif
If:
```
if <statement>:
    print("yes");
```

Else:
```
if <statement>:
    print("yes");
    else:
        print("no");
```

Elif
```
if <statement>:
    print("this");
    elif <statement>:
        print("that");
```

Example:
```
if 1 + 2 = 3:
    print("this");
    elif 1 + 2 = 5:
        print("that");
    else:
        print("no");
```
----
### Input
```
in(variable)
```

----

Example code:

```cpp
#import <<none>>

int _main():
    var one = "Hello World";
    print(one);

    void _myFunction():
        if 1 == '1' && 1 === '1':
            print("true"); // Will not print because 1 === '1' will return false
            else:
                print("false");
    
    void _input():
        in(newVar);
        print(newVar);

    return 0;
```
