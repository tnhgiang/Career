# React and Redux

## Getting started with React Redux

- Typically, in a _React Redux_ app:

  - We have a single _Redux store_ that manages the state of the entire app.
  - _React components_ subscribe to the pieces of data in the _Redux store_ that are relevant to their role. Then, actions are directly dispatched from _React component_.

- Although React components can manage their own state locally, when the application becomes more complex, it's generally better to keep the app state in a single location with Redux. There are exceptions when individual components may have local state specific only to them.

- `react-redux` package provides a way for you to pass Redux `state` and `dispatch` to your React components as `props`.

## User Provider to connect Redux to React

- `Provider` is a wrapper component from React-Redux that wraps the React app.

```js
<Provider store={store}>
  <App />
</Provider>
```

## Map State, Dispatch to Props

- This `Provider` allows `React Component` to access the Redux `store` and `dispatch` functions, but we must specify exactly what state and actions we want. By this way, each component only has access to the state it needs.
- `mapStateToProps()`: specify what pieces of state to use.

```js
const mapStateToProps = (state) => {
  return {
    messages: state,
  };
};
```

- `mapDispatchToProps()`: specify which action creators to dispatch.

```js
const mapDispatchToProps = (dispatch) => {
  return {
    submitNewMessage: (message) => {
      dispatch(addMessage(message));
    },
  };
};
```

## Connect Redux to React

- `connect` can use `mapStateToProps()` and `mapDispatchToProps()` functions to map `state` and `dispatch` to the `props` of a React **component**.

```js
connect(mapStateToProps, mapDispatchToProps)(MyComponent);
```

- Two arguments above is optional, as there are components that only needs access to `state`, but doesn't need to dispatch any actions, or vice versa. To omit one of the arguments, pass `null` to its place.

## Overall code

```js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider, connect } from 'react-redux';
import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';

import rootReducer from './redux/reducers';
import App from './components/App';

const store = createStore(rootReducer, applyMiddleware(thunk));

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```
