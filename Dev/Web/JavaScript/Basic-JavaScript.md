# [Basic JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/#basic-javascript)

## Declare JavaScript Variables

- In computer science, _data_ is anything that is meaningful to the computer. JavaScript provides 8 different _data types_ which are:
  - undefined
  - null
  - boolean
  - string
  - symbol
  - bigint
  - number
  - object
- We use the keyword `var` to tell JavaScript to _declare_ a new variable.

```js
var aNewVariable;
```

## Declare String Variables

- A _string literal_ or _string_ is a series of zero or more characters enclosed in single quotes `''` or double quotes `""`.

```js
var myName = 'Giang';
```

## Understanding Uninitialized Variables

- When a new JavaScript variables are declared, the have an initial value of `undefined`:
  - If we do a mathematical operation on an `undefined` variable, the result will be `NaN`
  - If we concatenate a string with an `undefined`, you will get a string of `undefined`

## Understanding Case Sensitivity in Variables

- All variables and functions in JS are all _case sensitivity_ which means that `MYVAR` is not the same as `MyVar` and `myvar`.

**Best Practice**

- Write variable names in _camelCase_
- Example:

```js
var newVariable;
var anotherVariableName;
```

## Explore Differences between the var and let Keywords

- One of the biggest problems with declaring variables with the `var` keyword is that we can easily override the variable declarations:

```js
var camper = 'James';
var camper = 'David';
// camper = "David"
```

- In some small applications, we might not run into this kind of problem. But as the program is getting larger, we might accidentally redeclare a variable and JS doesn't throw any errors. So, searching and fixing bugs becomes more difficult.

- `let` keyword was introduced in ES6 to solve this potential problem with the `var` keyword.

```js
let camper = 'James';
let camper = 'David';
// SyntaxError: Identifier 'camper' has already been declared"
```

## Declare a Read-only Variable with const Keyword

- In ES6, we can declare read-only variables using `const` keyword. They are constant values, which means that one a variable initially assigned with `const`, the cannot be reassigned.
  **Best practice**
- We should always declare constant variables with `const`.
- The name of `const` variables should be all uppercase letters with underscore `_` between words.

## Increment and Decrement a Number

- Like `Python`, we also have `++` and `--` operator to add one or subtract one from a variable.

```js
var i = 0;
// Add one to i
i++;
// i = 1
//Subtract one from i
i--;
// i = 0
```

## Compound Assignment

- Everything to the right of the _equals sign_ or _assignment operation_ is evaluated first, and then the result will be assigned to our variables.
- We have 4 compound assignment: `+=`, `-=`, `*=`, `/=`.

## Escape sequences in Strings

- There are two reasons to use escaping characters:
  - To allow we to use characters we may not be able to type out.
  - To allow we to represent single quotes `''`, double quotes `""` and backslash `\` in a string.

| Code |     Output      |
| :--: | :-------------: |
|  \'  |  single quote   |
|  \"  |  double quote   |
|  \\  |    backslash    |
|  \n  |     newline     |
|  \r  | carriage return |
|  \t  |       tab       |
|  \b  |  word boundary  |
|  \f  |    form feed    |

## Concatenating Strings

- Both `+` and `+=` operator are able to concatenate strings together.

```js
var greeting = 'Hello. How are you doing?';
var name = 'Giang';
var lastName = 'Trinh';
var string = greeting + ', ' + name + '?';
// string = "Hello. How are you doing?, Giang?
name += lastName;
name += 'Nguyen Hoang';
// name = "Giang Trinh Nguyen Hoang"
```

## Find the length of a String

```js
console.log('12345'.length);
// 5
```

## Understand String Immutability

- Like `Python`, _String_ in Javascript is immutable, which means that we cannot alter the individual characters of the created string.

```js
let string = '12345';
string[0] = '0';
// Error!!!
```

- Immutability is different from changing the value of the variable. We are able to assign it with a **new string**.

```js
let str = '12345';
// Assign str with a new string of "01234"
str = '01234';
// it works
```

## JavaScript Array

- With _Array_ we can store several pieces of data in one place.

```js
const info = ['Giang', 24, 'years old'];
```

## Write Reusable JavaScript with Functions

- Like `Python`, we can divide up our code into reusable parts called _functions_.
- Syntax:

```js
function hello() {
  // All of code between the curly braces will be executed
  // every time when the function is invoked.
  console.log('Hello World');
}
// Invoke the defined function
hello();
```

## Passing values to Functions with Arguments

- _Parameters_ are variables that act as placeholders for the actual values that are input to a function when it is called.
- _Arguments_ are the actual values that we input (or _pass_) into a function when it's invoked.

```js
function hello(greeting, name) {
  // 2 parameters: greeting and name
  console.log(greeting + ', ' + name);
}

// Invoke a function with 2 passed arguments
hello('How your doing?', 'Giang');
```

## Return a Value from a Function with Return

- We can pass values into function with _parameters_. So, we also can use `return` statement to send a value back out of a function.

```js
function plusThree(num) {
  return num + 3;
}
plusThree(2);
// 5
```
