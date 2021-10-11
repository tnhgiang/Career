# [Basic Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/#basic-data-structures)

## Summary
- Basic operation for `Array`:
	- Adding new item: `push()`, `unshift()`
	- Removing items: `pop()`, `shift()`, `splice()`
	- Modifying array: `assignment` follows `bracket notation`
	- Copying an array: `slice()`, `spread operator`
	- Combining two arrays: `spread operation`
	- Checking if an item exists: `indexOf()`
	- Iterating over a array: `for`, `forEach()`, `map()`, ...

- Basic operation for `Object`:
	- Adding new key-value or modifying value: `assignment` follows `bracket notation` or `dot notation`
	- Removing key-value pair: `delete`
	- Check if a key exists: `hasOwnProperty` or `in` statement
	- Iterating over all object keys: `Object.keys()`

## Use an Array to Store a Collection of Data
- Array can store multiple values in one place.

- Like `Python`, arrays are mutable.

- Like `Python` array contains booleans, strings, numbers and nested arrays (multi-dimensional array).

- Example: one-dimensional array
``` js
let simpleArray = ['one', 2, 'three', true, false, undefined, null]
```

- `length` property gets the length of an array.

## Access an Array's Contents Using Bracket Notation
- Like `Python`, we can use `bracket notation` to access and modify value. Js arrays are `zero-indexed`.

## Add Items to an Array with `push()` and `unshift()`
- `push()` add **one or many elements** to the end of an array.
- `unshift()` add **one or many elements** to the beginning of an array.
- **Note**: we can pass `variables` or `Spread Operator` to have more flexibility.
```js
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];

// Shorthand to concatenate two arrays
arr1.push(...arr2);
// arr1 = [1, 2, 3, 4, 5, 6]
```

## Remove Items from an Array with `pop()` and `shift()`
- Both `pop()` and `shift()` are nearly opposite to `push()` and `unshfit()`.

- `pop()` removes **an element** from the end of an array.
- `shift()` removes **an element** from the beginning of an array.

| push(), unshift() 	| pop(), shift()              	|
|-------------------	|-----------------------------	|
| Take arguments    	| Does not take any arguments 	|

```js
let greetings = ["what's up", "hello", "see ya!"];

greetings.pop();
// greetings = ["what's up", "hello"]

let popped = greetings.shift();
// greetings = ["hello"]
// popped = "what's up"
```

## Remove Items Using splice()
- `splice()` allows us to remove **any number of consecutive** from **anywhere** in an array.

- `splice(1st_parameter, 2nd_parameter)`
	- 1st_parameter: the index where we start removing elements
	- 2nd_parameter: the number of elements to delete

- `splice()` not only modifies the array on which is called, but it also returns a new array containing the values of the removed elements.

```js
let array = ['today', 'was', 'not', 'so', 'great'];

words = array.splice(2, 2)
// array = ['today', 'was', 'great']
// words = ['not', 'so']
```

## Add Items Using splice()

- `splice()` can also replace a number of elements starting at a specific index by one or more elements.
- `splice(1st_parameter, 2nd_parameter, 3rd_parameter)`
	- 1st_parameter: the index where we start replacing elements
	- 2nd_parameter: the number of elements to be replaced
	- 3rd_parameter: one or more elements to replace
```js
const numbers = [10, 11, 12, 12, 15];

numbers.splice(3, 1, 13, 14);
// numbers = [10, 11, 12, 13, 14, 15]
```

## Copy Array Items Using `slice()`
`slice()` creates a **new array** by copying a given number of elements.
- Like `Python Slicing`, `slice()` takes 2 parameters which can be both negative and positive.
```js
let weatherConditions = ['rain', 'snow', 'sleet', 'hail', 'clear'];

let todaysWeather = weatherConditions.slice(1, 3);
// todaysWeather = ['snow', 'sleet']
```

## Copy an Array with the Spread Operator
- `Spread Operator` helps us easily copy all of array's elements.
```js
let array = [true, 1, "hello"];
let newArray = [...array];
// newArray = [true, 1, "hello"]
```

## Combine Arrays with the Spread Operator
- `Spread Operator` also allows us to insert all elements of one array into another array at any index

```js
let arr = [3, 4];
let newArray = [1, 2, ..arr, 5];
//newArray = [1, 2, 3, 4, 5]
```

## Check For The Presence of an Element With indexOf()
- Due to `Array` is a mutate data, there's no guarantee about what the index of an element is, or whether that element still exists or not.
- So, `JS` provides `indexOf()` to check the presence of an arbitrary element of the array:
	- return -1 if that element does not exits
	- Or return its index

## Iterate Through All an Array Items Using For Loops
- We can use `every()`, `forEach()`, `map()`, `for` or `while` to iterate over all an array.

## Create complex multi-dimensional arrays
- An array can easily contains other arrays with arbitrary levels of depth to create a multi-dimensional array.

## Add Key-value Pairs to JS Objects
- We can add a new Key-Value (Property-Value) by using assignment following dot or bracket notation.

## Modify an Object Nested Within an Object
- Object properties can be nested to an arbitrary depth, and their values can be any type of data supported by JavaScript, including arrays and even other objects.
- Use nested dot or bracket notation to access nested objects.

## Use the delete Keyword to Remove Object Properties
- Syntax:
```js
let character = {
	name: "Giang",
	height: 178,
	nation: Vietnam,
	status: "undefined"
}
delete character.status;
```

## Check if an Object has a Property
- There are two ways to check whether an object has a specific property:
	- `hasOwnProperty()`
	- `in` keyword

## Iterate Through the Keys of an object with a for...in Statement
- `for..in` statement iterate through all the keys within an object.

## Generate an Array of All Object Keys with Object.keys()
```js
let character = {
	name: "Giang",
	height: 178,
	nation: Vietnam
}
// list all object properties
Object.keys(character);
```
