# HTML

## Basic HTML tags

| Tag        | Description                                                           |
| ---------- | --------------------------------------------------------------------- |
| h1         | A heading element                                                     |
| h2         | A lower rank heading element than h1                                  |
| p          | A paragraph of text                                                   |
| main       | A main content of a document                                          |
| section    | A section of a document                                               |
| img        | A image element (a self-closing tag)                                  |
| a          | A hyperlink to another page                                           |
| ul         | A unordered list                                                      |
| ol         | A ordered list                                                        |
| li         | A list item element                                                   |
| figure     | A self-contained content                                              |
| figcaption | A caption to describe the image contained within `figure` element     |
| em         | A emphasized text                                                     |
| strong     | Some text with strong importance or urgent                            |
| form       | A form element                                                        |
| input      | A input element provides several ways to collect data from a web form |
| button     | A button element                                                      |
| label      | A label a element is used to associates the text for an `input`       |
| fieldset   | A element is used to group related input and its labels together      |
| legend     | A element is used to create caption for the content in the `fieldset` |
| footer     | A footer element                                                      |
| head       | A document metadata                                                   |
| body       | A body element represents the content of an HTML document             |
| title      | A element defines document's title shown in a browser's title bar     |
| div        | A division tag                                                        |
| article    | A article tag                                                         |
| hr         | A divider between sections of different content                       |

### [section tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)

- Sections should always have a heading.

### [form tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)

- The default behavior of clicking a button without any attribute submits the form

```html
<form action="">
  <input type="text" />
  <!--Submit form-->
  <button>Submit</button>
</form>
```

- The first `input` element with a `type` of `submit` is automatically set to submit its nearest parent `form` element

### [div tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)

- The `div` element is the generic container for flow content. It has no effect on the content or layout until styled in some way using CSS
- An empty `div` will have width and height that equal to zero. (Use CSS to change the div's width and height)

### [article tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)

- The `article` elements commonly contain multiple elements that have related information

### [input tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)

- Consider the `name` a required attribute (even though it's not). If an input has no `name` specified, or `name` is empty, the input's value is not submitted with the form.
- The server side accesses the data form via `name` attribute

### Set page's viewport

- The browser's viewport is the area of the window in which web content can be seen.
- A typical mobile-optimized site contains something like the following:

```html
<!-- The page will look good on all devices (mobiles, tablets and computers)>-->
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

Not all devices are the same width, so we should make sure that our pages work well in a large variation of scree sizes and orientations.

### [block-level element](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) and [inline-level element](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements)

- A block-level element always starts on a new line and takes up the full width available (stretches out to the left and right as far as it can).
- An inline element does not start on a new line and only takes up as much width as necessary

### select tag

- Submitting the form with an `option` selected would not send a useful value to the server. As such, each `option` needs to be given a value attribute. Without which, the text content of the `option` will be submitted to the server.
