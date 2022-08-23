# [React](https://reactjs.org/)

## Create a simple JSX element

- React uses a syntax extension of JavaScript called JSX which allows you to write HTML directly within Javascript.
- JSX code must be complied into JavaScript. The transpiler Babel is a popular tool for this process.

```jsx
const JSX = <div></div>;
```

## Create a complex JSX element

- A nested JSX must return a single element, which means, there is one parent element that wrap all of the other levels of nested elements.

  Example:

  **Valid JSX**

  ```jsx
  <div>
    <p>Paragraph One</p>
    <p>Paragraph Two</p>
    <p>Paragraph Three</p>
  </div>
  ```

  **Invalid JSX**

  ```jsx
  <p>Paragraph One</p>
  <p>Paragraph Two</p>
  <p>Paragraph Three</p>
  ```

## Add comments in JSX

- `{/* */}` is the comment syntax.

## Render HTMl elements to the DOM

- With React, we can render the JSX element directly to the HTML DOM using React's rendering API known as _ReactDOM_.

- `ReactDOM.render(JSXElement, targetNode)`:

  - The first argument: React element or component that we wanna render.
  - The second element: DOM node that we wanna to render the specified element or component.

- `ReactDOM.render()` must be called after the JSX element declarations, just like how we must declare variables before using them.

## Define an HTML class in JSX

- `class` in HTML is equivalent to `className` in JSX.
- The naming convention for all HTML attributes and event references in JSX become cameCase: `onclick` -> `onClick`, ...

## Learn about self-closing JSX tags

- Every React component can be self-closing `<div />`. `<div></div>` is also an equivalent.
- There is no way to include any content in `<div />`.

## Create a stateless functional component

- _Component_ is the core of React. Everything in React is a component.
- We can compose a complex UI from separate, isolated components (combining several components together).
- The _stateless component_ is the component that can receive data and render it, but is not able to track changes in data.
- The function name must be start with a capital letter.

## Create a React component

- All React _class-based components_ that have a `constructor` should start with a `super(props)` call.
- A component name always starts with a capital letter whether it's class-based or functional component. That's how React differentiate it from normal HTML element:
  - `<User />`: React recognize it as Component
  - `<user />`: React recognize it as HTML

## Use React to render nested components

- When working with React, it's important to start thinking of The UI in terms of components. The UI should be broken down into building blocks (components).
  This helps to separate the code responsible for the UI from the code responsible for handling your application logic. It can greatly simplify the development and maintenance of complex projects.

## Render a class component to the DOM

- `ReactDOM.render(<ComponentToRender />, targetNode)`
- The syntax above is used for both class and function components.

## Pass an Array as Props

- To pass and array to a JSX element, it must be treated as JavaScript and wrapper in curly braces.

## Use default props

- `MyComponent.defaultProps = {location: 'Vietnam'}`

## Use PropTypes to define the props

- To verify received props that has proper type: `MyComponent.propTypes = {handleClick: PropTypes.func.isRequired}`
- See [document](https://reactjs.org/docs/typechecking-with-proptypes.html#proptypes) for details.

## Create a stateful component

- Declaring `state` in the `constructor`

```jsx
this.state = {};
```

- We have access to the `state` object throughout the life of the component. It can be updated, rendered to UI, passed as `props` to child components.

## Render State in the User Interface

- To access the value of the state, we have to enclose the reference in curly braces `{}`.
- `state` keeps track of the internal data of the component. Whenever `state` changes, the UI will change accordingly.
- React uses _virtual DOM_ to keep track of changes behind the scenes. When `state` data changes, it trigger a re-render of the
  components using that data and relative child components (child components receive that data as `prop`). React updates the
  actual DOM, but only necessary parts.
- `state` is encapsulated, which means, no other components care about the `state` (unless the child components use it as `props`)

## Set State with this.setState

- To update the `state`:

```jsx
this.setState({
  username: 'Giang',
});
```

- Always use `this.setState` to modify `state`, **never do that directly**.
- Calling `setState` automatically re-renders the entire component using that `state` and all it child component.
- `setState` function is asynchronous in nature.

- **Nice article to get more about `state`**: [article](https://www.freecodecamp.org/news/what-is-state-in-react-explained-with-examples/)

## Bind this to a class method

- `bind()` creates a new function that will force `this` inside the function to be the parameter passed to `bind()`. Check [stackoverflow](https://stackoverflow.com/questions/2236747/what-is-the-use-of-the-javascript-bind-method)

- Need more time to investigate `this` keyword.

## Use State to toggle an element

- To get the previous value of `state` or `props` in the `setState` function, we should use a function as a `state` updater:

```jsx
this.setState((state, props) => ({
  counter: state.counter + props.increment,
}));
```

- Using a function with `setState` guarantees that we are working with the most current values of the `state` and `props`.

## Pass state as props to child components

- We can pass a state as props to child components. Passing props is how information flows in React apps, from parents to children

## Pass a callback as props

- We also can pass a function or method defined in a component to child components. It allow a child component to interact with their parent component.

## Use the Lifecycle method

- React provides several special methods that can perform actions at specific points in the lifecycle of a component. These method are called lifecycle methods or lifecycle hooks.

- `componentDidMount()` is invoked immediately **after** calling `render`, the component is mounted to the DOM. **Good practice**: this is the best place to have some API calls or event listeners.
- `componentWillUnmount()` is invoked immediately **before** a component is unmounted and destroyed. **Good practice**: this is the ideal place to perform any necessary cleanup such as clearing up timers, cancelling network requests, or cleaning up any subscriptions that were created in `componentDidMount()`:

```jsx
// e.g add event listener
componentDidMount() {
    el.addEventListener()
}

// e.g remove event listener
componentWillUnmount() {
    el.removeEventListener()
 }
```

- React will rerenders the component and its children when state or prop changes. But, `shouldComponentUpdate()` can have control over this behavior. This method is a useful way to optimize performance.

## Inline style

```jsx
<div style={{ color: 'yellow', fontSize: 16 }}>Mellow Yellow</div>
```

- Al hyphenated words (like :`font-size`) are written using camelCase in JSX (like: `fontSize`)
- In default, all length units are assumed to be `px` unless other units are explicitly specified.

## Use Advanced JavaScript in React Render Method

- We can also write JavaScript directly in your `render` methods, before the `return` statement, **without** inserting it inside of curly braces.

## Render with an If-Else Condition

- When the condition is true, one view renders. When it's false, it's a different view.

## Use && for a More Concise Conditional

```jsx
{
  condition && <p>markup</p>;
}
```

- If the `condition` is `true`, the markup will be returned, otherwise return nothing.

## Use a Ternary Expression for conditional rendering

- `if/else` statements can't be inserted directly into JSX code, But, ternary expressions can do it.

## Render Conditionally from Props

- Using the value of a given prop too automatically decide what to render.

## Change inline CSS conditionally based on component state

- CSS can be rendered conditionally based on the state or props of a React component.

## User Array.map() to dynamically render elements

- We can't know exactly how many element to render until runtime, using `Array.map()` to cope with the unknown number of element.
- **Note**: Each element in an array needs a `key` attribute which are unique among the array elements. React uses these keys to keep track of which items are added, changed, or removed. It make re-rendering process more efficient.

## Use Array.filter() to Dynamically Filter an Array

- `filter` returns a new array of elements which meet the condition.
