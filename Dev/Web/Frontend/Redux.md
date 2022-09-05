# [Redux](https://redux.js.org/)

- Redux is predictable state container for JavaScript app.
- Redux is a pattern and library for managing and updating application state, using events called `actions`.

## Create a Redux store

- Redux is a state management framework that can be combined with different web technologies (including React).
- In Redux, there is a single _state object_ being responsible for the entire state of our application. This mean if there are 10 different components, and each component has its own local state,
  the entire state would be centralized in a single state objects in Redux `store`.

- If the application needs to update state, it must do so through the Redux store.

## Get state from the Redux store

- Use `getState()` to retrieve the current state from the Redux store object.

## Dispatch a Redux Action Event

- The a only way to update state is to **dispatch actions**, _action_ is a JavaScript object describing information about the happened event.

```js
store.dispatch({ type: 'LOGIN' });
```

## Handle an Action in the Store

- React store needs to know how `state` gets updated in response to the dispatched `action`, we use pure `reducer` functions that calculate a new `state` based on the old `state` and the `action`.
- It is important to see that this is the only role of the reducer. It has no side effects — it never calls an API endpoint and it never has any hidden surprises.
  The reducer is simply a pure function that takes state and action, then returns new state.
- In Redux, `state` is read-only, which means, `reducer` function must **always** return a new copy of `state` and never modify it directly.

## Use a switch statement to handle multiple actions

- Use `switch` statement in the `reducer` to respond to different action events.
- Don't forget to write a `default` case, as app has multiple reducers, they are all run any time an action dispatch is made, even when the action isn't related to that reducer. In such a case, you want to make sure that you return the current `state`.

## Use const for action types

- A common practice when working with Redux is to assign action types as read-only constants, then reference these constants wherever they are used.

**Note**: It's generally a convention to write constants in all uppercase, and this is standard practice in Redux as well.

## Register a Store listener

`store.subscribe()` will subscribe listener functions to the store, which are called whenever an action is dispatched.

## Combine multiple reducers

- Step 1: Define multiple reducers to hand different pieces of your application's state.
- Step 2: Use `combineReducers()` method to combine multiple reducers into one root reducer.

  ```js
  const rootReducer = Redux.combineReducers({
    auth: authenticationReducer,
    notes: notesReducer,
  });
  ```

  Now, the key `notes` will contain all of the _state_ associated with our notes and handled by our `notesReducer`.

- Step 3: Pass the root reducer into the Redux `createStore()`
  **Note**: It is a good practice to create a reducer for each piece of application state when they are distinct or unique in some way.

## Send action data to the store

- An action commonly contain specific data, because it is usually originate from some user interaction and tend to carry some data with them.

```js
// Example of an action with data
action = {
  type: 'ADD_NOTE',
  text: 'Here is text data',
};
```

## Use middleware to handle asynchronous actions

- Redux `Thunk` middleware is a middleware to handle asynchronous actions.
- To include Redux Thunk middleware `Redux.applyMiddleware()`. Then, use it as the second optional parameter in `createStore()`:

```js
const store = Redux.createStore(
  asyncDataReducer,
  Redux.applyMiddleware(ReduxThunk.default)
);
```

- How to use:

```js
const requestingData = () => {
  return { type: REQUESTING_DATA };
};
const receivedData = (data) => {
  return { type: RECEIVED_DATA, users: data.users };
};

const handleAsync = () => {
  // In the action creator, we return a function that take `dispatch` as an argument
  // Within this function, we can dispatch actions and perform async requests

  return function (dispatch) {
    // To dispatch actions, we simply pass the action in to dispatch parameter
    // and the middleware takes care of the rest

    // It's common to dispatch an action before initiating any async behavior
    // so that the app state knows that some data is being requested (ex: this state
    // could display a loading icon)
    dispatch(requestingData());
    setTimeout(function () {
      let data = {
        users: ['Jeff', 'William', 'Alice'],
      };
      // One app receives the data, dispatch another action which carries the data as
      // a payload along with information that action is completed
      dispatch(receivedData(data));
    }, 2500);
  };
};
```

## Never mutate state

- Immutable state means that we never modify state directly, instead, we return a new copy of state.
- Recall in JS (ES6):

  - `string`, `number` is immutable.
  - `array`, `object` is mutable. To have a new shallow copy:
    - `array`: `Array.slice()`, `[...array]`.
    - `object`: `Object.assign()`, `{...object}`.

- **Shallow copy** only provides the immutability for one-dimensional arrays.
- **Spread operator**

```js
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const arr3 = [...arr1];
// arr3 = [1, 2, 3]
const arr4 = [...arr1, 4, 5];
// arr4 = [1, 2, 3, 4, 5]
const arr5 = [...arr1, ...arr2];
// arr5 = [1, 2, 3, 4, 5, 6]
const arr6 = [...arr1, arr2];
// arr6 = [1, 2, 3, [4, 5, 6]]
```

- `Object.assign()`: takes a target object and source objects and maps properties from the source objects to the target object.
  Any matching properties are overwritten by properties in the source objects.

```js
obj1 = {
  name: 'Giang',
  age: 25,
};
obj2 = {
  age: 26,
};
const newObject = Object.assign({}, obj1, obj2);
// newObject = {name: 'Giang', age: 26}
```
