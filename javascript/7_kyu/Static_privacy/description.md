# Static privacy (7 kyu)

- [Exercise link](https://www.codewars.com/kata/652a19cd7e92f356f437d059)

I wrote a class `Class`, with a private `static` property `foo` and a getter to retrieve it:

```javascript
class Class {
  static #foo = 42;

  static get foo() {
    return this.#foo;
  }
}
Class.foo; // 42
```

However, when I create a class Subclass that inherits from Class, the code breaks:

```javascript
class Subclass extends Class {}
Subclass.foo; // Error !
```

Can you fix the code ?

Modify `Class` so that `Subclass.foo` will work correctly. This should also work for any level of inheritance from `Class`, e.g. with:

```javascript
class Deepclass extends Subclass {}
Deepclass.foo; // should return 42
```
