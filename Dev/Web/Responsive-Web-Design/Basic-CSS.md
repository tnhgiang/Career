# CSS

## HTML tags

| Tag  | Description                                                                                                              |
| ---- | ------------------------------------------------------------------------------------------------------------------------ |
| link | The external source link element specifies the relationships <br/> between the current document and an external resource |

## Basic CSS properties

| Property         | Description                                                                     |
| ---------------- | ------------------------------------------------------------------------------- |
| text-align       | A property sets the horizontal text alignment                                   |
| color            | A property sets the color of text                                               |
| background-color | A property sets the background color of an element                              |
| background-image | A property sets the one or more background images for an element                |
| width            | A property sets the width of an element                                         |
| margin           | A property sets the space around an element's border (space outside an element) |
| padding          | A property sets the space around an element's content (space inside an element) |
| display          | A property sets the display behavior of an element                              |
| font-family      | A property sets the font for an element                                         |
| font-style       | A property sets the font style for an text element                              |
| font-size        | A property sets the font size for an text element                               |
| border-color     | A property sets the border color of an element                                  |
| border-width     | A property sets the width of an element's borders                               |
| border-style     | A property sets the style of an element's borders                               |
| opacity          | A property sets the opacity level for an element                                |
| box-shadow       | A property attaches one or more shows to an element                             |
| vertical-align   | A property sets the vertical alignment of an element                            |

### Basic CSS functions

| Property        | Description                                                       |
| --------------- | ----------------------------------------------------------------- |
| rgb             | A function define colors using the RGB model                      |
| rgba            | A function define colors using the Red-Green-Blur-Alpha model     |
| hsl             | A function define colors using the Hue-Saturation-Lightness model |
| linear-gradient | A function sets a linear gradient as the background image         |

## The fallback value

```css
h1,
h2 {
  font-family: Impact, serif;
}
```

- `serif` is a fallback when `Impact` font is not found or available

## [The pseudo-selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)

- A CSS pseudo-class is a keyword added to a selector that specifies a special state of the selected element(s)

## Note:

- Browser has some default top margin for the `h1`, `h2`, ... element
- The value of the margin property can be a negative number.
- The `div` can be horizontally centered by using `margin`
- The `linear-gradient` will create a `image` element and it is usually paired with the `background` property which can accept an image as a value
- `border-left` shorthand

```css
border-left: width style color;
```
