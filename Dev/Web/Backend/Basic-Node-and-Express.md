# [Basic Node and Express](https://www.freecodecamp.org/learn/back-end-development-and-apis/#basic-node-and-express)

- _Node.js_ is a JavaScript runtime environment that allow developers to write backend (server-side) programs in JavaScript. It runs on the V8 engine and includes everything we need to execute a program written in JavaScript.
- Read more about [_node.js_](https://www.freecodecamp.org/news/what-exactly-is-node-js-ae36e97449f5/)
- _Express_ is a lightweight web application framework, and is one of the most popular packages on _npm_. Express makes it much easier to create a server and handle routing.

## Start a Working Express Server

- To create an _Express_ app object.

```js
var express = require('express');
var app = express();
```

- `app.listen(port)` tells the server to listen on the given port and puts the server in running state.
- **_Routing_** refers to determining how an application responds to a client request to a particular endpoint, which is a URI (or path) and a specific HTTP request method (GET, POST, and so on).
- In _Express_, routes takes the following structure: `app.METHOD(PATH, HANDLER)`:
  - METHOD is an http method in lowercase: `app.get()`, `app.post()`, ...
  - PATH is a relative path on the server (it can be string, or even a Regex).
  - HANDLER is a function that _Express_ calls when the route is matched. Handlers take the form:
  ```js
  // req is the request object
  // res is the response object
  function(req, res) {
  	// Serve the string 'Response String'
  	res.send('Response String');
  }
  ```

## Serve an HTML File

- `res.sendFile(path)` is to respond to requests with a file.
- This method will set the appropriate headers to instruct the browser on how to handle the file according to type of that file. Then it will read and send the file.
- This method requires an absolute file path. So, Node global variable `__dirname` is recommended: `absolutePath = __dirname + relativePath/file.ext`

**Note**: _Express_ evaluates routes from the top to bottom, and executes the handler for the first match.

## Serve Static Assets

- An HTML server usually has one or more directories that are accessible by the user (e.g.: `/public/`) to store the static assets (stylesheets, scripts, images).
- To serve static files: `express.static(path)`, where path is an absolute path.
- Official document: [express.static](https://expressjs.com/en/starter/static-files.html)

## Serve JSON on a Specific Route

- While HTML server serves HTML, an API serves data. A REST API allows data exchange in a simple way, without the need for clients to know any detail about the server. The client only needs to know where the resource is (the URL) and the actions users want to perform on the server (The verb: GET, POST, DELETE, ..):

  - GET verb is used when users are fetching some information without modifying anything

- JSON is a preferred data format to exchange data.
- To respond to request with a JSON: `res.json(object)`
- This method will convert a valid JavaScript object into a string, then sets the appropriate headers to tell the browser that we are serving JSON and sends the data.
- A valid object has the usual structure: `{key: data}`

## Use the .env File

- The `.env` file is hidden file that store environment variables. It is secret, no one but we can access it.
- Environment variables are a great way to securely and conveniently store configuration that don't change often and some private things. For example: (URLs, authentication keys, passwords and database URI, ...).
- By setting configuration options, we can change the behavior of the application without rewriting some code.
- To access environment variables: `process.env.VAR_NAME`. `env` is a property of `process` which is a global Node object.
- `.env` is _shell_ file.
- To load `.env` into `process.env`, we need the `dotenv` packages which is installed by executing `npm install dotenv`. Then, we import and load the variable with `require('dotenv').config()`.

## Implement a Root-Level Request Logger Middleware

- **_Middleware_** functions are functions that have access to the request object (req), response object (res), and the next function in the application's [request-response cycle](https://iq.opengenus.org/middlewares-in-express/#:~:text=%E2%AD%90%20Request%2DResponse%20Cycle%20%2D,send%20back%20a%20meaningful%20response.).
- Middleware functions can perform the following tasks:
  - Execute any code.
  - Make changes to the request and the response objects.
  - End the request-response cycle.
  - Call the next middleware in the stack.
- If the current middleware function does not end the request-response cycle by calling _response method_ (`res.send()` for example), it must call next() to pass control to the next middleware function. Otherwise, the request will be left hanging.

- Middleware function take the following structure:

```js
function(req, res, next) {
	// do something
	// To invoke the next middleware function
	// in request-response cycle
	next();
}
```

- This example shows a middleware function with no mount path. The function is executed **every time the app receives a request**.

```js
app.use(function (req, res, next) {
  console.log('Time:', Date.now());
  next();
});
```

- This example shows a middleware function mounted on the `/user/:id` path. The function is executed for **any type of HTTP request on the `/user/:id` path**.

```js
app.use('/user/:id', function (req, res, next) {
  console.log('Request Type:', req.method);
  next();
});
```

- If we want middleware to be executed only for _POST_ request:
  `app.post(path, middleware-function)`. Similar to other HTTP requests: _GET_, _DELETE_, _PUT_, ...

## Chain Middleware to Create a Time Server

```js
app.get('/path', middlewareFunction, routeHandler);
// It is equivalent to
app.get('/path', middlewareFunction);
app.get('/path', routeHandler);
```

## Get Route Parameters Input from the Client

- Route parameters are named URL segment that are used to capture the values specified at their position in the URL.
- The captured values are populated in the `req.params` object with the name of the route parameters specified in the path as their respective keys.

```
Route path: /users/:userId/books/:bookId
Request URL: http://localhost:3000/users/34/books/8989
req.params: { "userId": "34", "bookId": "8989" }
```

## Get Query Parameter Input from the Client

- _Query string_ is a common way to get input from the client.
- That encodes the data after the route path following the format:

```
route_path: '/library'
actual_request_URL: '/library?userId=546&bookId=6754'
req.query: {userId: '546', bookId: '6754'}
```

- Express can parse the data from the query string and populate the object `req.query`.
- Some character, like the percent (%) cannot be in the URLs have to be encoded in a different format before you can send them. If you use the API from JavaScript, you can use specific methods to encode/decode these characters.

## Use body-parser to Parse POST Requests

- _POST_ is the default method used to send client data with HTML forms. In REST convention, POST is used to send data to create new items in the database (a new user, or a new blog post).
- In these kind of requests, the data doesn't appear in the URL, it's in the HTTP request body.
- The body is a part of the HTTP request which is called the _payload_.
- Take a look at the raw content of an HTTP _POST_ request from HTML forms:

```
POST /path/subpath HTTP/1.0
From: john@example.com
User-Agent: someBrowser/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 20

name=John+Doe&age=25
```

- To parse the data coming from POST requests, you have to install the `body-parser` package. This package allows you to use a series of middleware, which can decode data in different formats.

## Get Data from POST Requests

- `body-parser` parses data from POST requests and populates `req.body`
- Except from GET method, the others HTTP methods can have a payload (i.e. the data in the request body).
