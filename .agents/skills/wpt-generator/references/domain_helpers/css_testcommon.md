# CSS Property & Parsing Helpers (`css/support/*-testcommon.js`)

When writing WPTs for CSS APIs (such as testing property parsing, computed values, inheritance, or shorthands), **do not manually write out the Javascript to set styles, read `getComputedStyle`, and compare values**. Instead, you **MUST** use the robust canonical testing framework located in the `/css/support/` directory.

## Including the Frameworks
Since you are testing CSS, you **MUST** use an `.html` file because the CSS linter requires a `<link rel="help">` tag.

```html
<!DOCTYPE html>
<meta charset="utf-8">
<title>My CSS Test</title>
<link rel="help" href="https://drafts.csswg.org/css-align/">
<script src="/resources/testharness.js"></script>
<script src="/resources/testharnessreport.js"></script>
<script src="/css/support/parsing-testcommon.js"></script>
<script src="/css/support/computed-testcommon.js"></script>
<script src="/css/support/inheritance-testcommon.js"></script>
<script src="/css/support/shorthand-testcommon.js"></script>

<!-- A #target element is required by most of these helpers! -->
<!-- For inheritance tests, it MUST be inside a #container -->
<div id="container">
  <div id="target"></div>
</div>
```

## Parsing (`parsing-testcommon.js`)
Use these to test whether a browser correctly parses (or rejects) a specified CSS value for a property.
*   `test_valid_value(property, specified, serializedValue)`: Tests that setting the property to `specified` succeeds, and that reading it back (serialization) matches `serializedValue`. If `serializedValue` is omitted, it defaults to `specified`.
*   `test_invalid_value(property, specified)`: Tests that the browser correctly rejects the `specified` value as invalid.

**Example:**
```javascript
test_valid_value('align-items', 'center');
test_valid_value('align-items', 'flex-start', 'start'); // If it serializes differently
test_invalid_value('align-items', '10px');
```

## Computed Style (`computed-testcommon.js`)
Use these to test how a specified CSS value resolves in `getComputedStyle`.
*   `test_computed_value(property, specified, computed)`: Tests that setting the property to `specified` results in a `getComputedStyle` value of `computed`. If `computed` is omitted, it defaults to `specified`.

**Example:**
```javascript
test_computed_value('width', 'auto');
test_computed_value('width', '100px');
test_computed_value('margin-top', '10%', '50px'); // Assuming parent width is 500px
```

## Inheritance (`inheritance-testcommon.js`)
Use these to test whether a CSS property correctly inherits from its parent element.
*Note: This helper strictly requires BOTH a `#container` and `#target` element in the DOM.*
*   `assert_inherited(property, initial, other)`: Tests that the property inherits. `initial` is the computed initial value of the property, and `other` is a distinct valid value.
*   `assert_not_inherited(property, initial, other)`: Tests that the property does NOT inherit.

**Example:**
```javascript
// Color inherits by default. 'canvastext' is the initial value in many UAs.
assert_inherited('color', 'canvastext', 'red');

// Margin does not inherit. '0px' is the initial value.
assert_not_inherited('margin', '0px', '10px');
```

## Shorthands (`shorthand-testcommon.js`)
Use this to test that setting a shorthand property correctly sets the underlying longhand properties.
*   `test_shorthand_value(property, value, longhands)`: Tests that setting `property` to `value` correctly sets all the corresponding `longhands` (provided as an object mapping longhand names to expected values).

**Example:**
```javascript
test_shorthand_value('margin', '10px 20px', {
  'margin-top': '10px',
  'margin-right': '20px',
  'margin-bottom': '10px',
  'margin-left': '20px'
});
```