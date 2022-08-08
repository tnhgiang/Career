# [Basic HTML and HTML5](https://www.freecodecamp.org/learn/responsive-web-design/#basic-html-and-html5)

## Inform with the Paragraph Element
- `p` elements are the preferred element for paragraph text on website.
```html
<p>Paragraph Text </p>
```

## Introduce to HTML5 Elements
- `HTML5` introduces more descriptive HTML tags, including: `main`, `header`, `footer`, `nav`, `video`, `article`, `section` and others.

## Add Image to Your Website
- `img` tag is used for adding a image with specific url into the website.
```html
<img src="url" alt="Image description">
```

## Link to External Pages with Anchor Elements
- `a`*(anchor)* elements allow you to link to content outside of your web page:
	- `href` attribute describes a destination web address.
```html
<a href="google.com">Google</a>
```

## Link to Internal Sections of a Page with Anchor Elements
- `a` *(anchor)* elements can also be used to create internal links to different sections within webpage.
- To create an internal link, `href` attribute should be `#` + `id` of a specific element
```html
<a href="#contacts-header">Contacts</a>
<h2 id="contacts-header">Contacts</h2>
```
**Note**:
- An `id` attribute of a specific HTML element must be unique in the whole document.
- `target"` is an anchor tag attribute that specifies where to open the link:
	- `target="_blank"` will open the link in a new window tab.


## Make Dead Links Using the Hash Symbol
- Sometimes, we want to create `a` element before we know exactly to where we wanna link. But, we still can use `JavaScript` to change its behavior later.
- `href="#"` will create a dead link.


## Create a Text Field
- You can create a web form by using `input` element. It's a convenient way to get input from the user.

- Create a text input:
```html
<input type="text">
```


- `placeholder` is a default text that will be show in `input` element before anything has been inputted.
```html
<input type="text" placeholder="here is your placeholder">
```


## Create a Form Element
- We can build a web form that actually submit data to a server specified in `action` attribute of the `form` element.
```html
<form action="/url-where-you=want-to-submit-form-data">
	<input>
</form>
```


## Add a Submit Button to a Form
- Clicking the `submit` button will send the form data to URL specified in `action` attribute.
```html
<form action="URL">
	<input type="text" placeholder="type something">
	<button type="submit">Send data</button>
</form>
```


## Use HTML5 to Require a Filed
- Add `required` attribute within `input` element to make sure that the user won't be able to submit our form until they has filled it out.
```html
<input type="text" placeholder="default value" required>
```


## Create a Set of Radio Buttons
- Read more about [HTML label tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
- We can use `radio buttons` for questions where user must select one answer out of multiple options.
- `radio buttons` are a type of `input`.
- All related `radio buttons` should have the same `name` attribute to create a radio button group.
```html
<input id="indoor" type="radio" name="indoor-outdoor">
<label for="indoor">Indoor</label>
```
or in the nested form:
```html
<label for="indoor">
	<input id="indoor" type="radio" name="indoor-outdoor">Indoor
</label>
```

## Create a Set of Checkboxes
- Forms commonly use `checkboxes` for questions that may have more than one answer.
- To be similar to `Radio buttons`, `checkboxes` are type of `input` which should come along with `label`.
```html
<label for="loving">
	<input id="loving" type="checkbox" name="personality">
</label>
```

## Use the value attribute with Radio Buttons and Checkboxes
- The values of `radio` and `checkboxes` will be sent to the server for the further purpose.
	- If we omit `value`, the default value is `on`
```html
<label for="indoor">
  <input id="indoor" value="indoor" type="radio" name="indoor-outdoor">Indoor
</label>
```
- According to the example above, the received form data would be `indoor-outdoor=indoor`.


## Check Radio Buttons and Checkboxes by Default
- We can set a checkbox or radio button to be checked by default by adding `checked` attribute.
```html
<input type="radio" name="radio-button" checked>
```


## Nest Many Elements within a Single div Element
- The `div` element, also known as a division element, is a general purpose container for other elements.


## The overall structure of an HTML web page
```html
<!--HTML5 -->
<!DOCTYPE html>
<html>
	<head>
		<!--Any information about the page-->
	</head>
	<body>
		<!--The content of the page-->
	</body>
</html>
```
