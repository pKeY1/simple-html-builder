# simple-html-builder

A lightweight, zero-dependency Python library for programmatically building HTML with optional HTMX support.

## Installation

### From GitHub (recommended)
```bash
pip install git+https://github.com/pKeY1/simple-html-builder.git
```

### Or clone and install locally
```bash
git clone https://github.com/pKeY1/simple-html-builder.git
cd simple-html-builder
pip install .
```

### PyPI (coming soon)
```bash
pip install simple-html-builder
```

## Quick Start

```python
from html_builder import new_builder, r, e, TAG, to_string

# Create a new builder
b = new_builder()

# Use 'r' for nested elements (context manager)
with r(TAG.DIV, id="app", class_="container"):
    with r(TAG.FORM, hx_post="/submit", hx_target="#result"):
        e(TAG.LABEL, text="Name:")
        e(TAG.INPUT, type="text", name="name")
        e(TAG.BUTTON, type="submit", text="Submit")

# Get the HTML string
html = to_string(b)
print(html)
# <div id="container"><form hx-post="/submit" hx-target="#result"><label>Name:</label><input type="text" name="name"></input><button type="submit">Submit</button></form></div>
```

## API

### Functions

| Function | Description |
|----------|-------------|
| `new_builder()` | Create a new HTML builder context |
| `r(tag, ...)` | Create a nested element (context manager) |
| `e(tag, ...)` | Create a sibling element |
| `to_string(b)` | Render the builder to an HTML string |
| `end(b)` | Close the current element context |

### TAG Enum

All standard HTML tags are available via the `TAG` enum:
- `TAG.DIV`, `TAG.SPAN`, `TAG.P`, etc.
- `TAG.BUTTON`, `TAG.INPUT`, `TAG.FORM`, etc.
- `TAG.UL`, `TAG.LI`, `TAG.TABLE`, etc.

### Attributes

All standard HTML attributes are supported as keyword arguments:
- `id="my-id"`
- `class_="my-class"` (note: underscore suffix)
- `href="/url"`
- `src="image.png"`
- etc.

### HTMX Attributes

Built-in support for HTMX attributes:

| Parameter | HTML Attribute |
|-----------|----------------|
| `hx_get` | `hx-get` |
| `hx_post` | `hx-post` |
| `hx_put` | `hx-put` |
| `hx_delete` | `hx-delete` |
| `hx_patch` | `hx-patch` |
| `hx_target` | `hx-target` |
| `hx_trigger` | `hx-trigger` |
| `hx_vals` | `hx-vals` |
| `hx_include` | `hx-include` |
| `hx_push_url` | `hx-push-url` |

### Example: HTMX Form

```python
from html_builder import new_builder, r, e, TAG, to_string

b = new_builder()
with r(TAG.DIV, class_="container"):
    with r(TAG.FORM, hx_post="/api/submit", hx_target="#response", hx_push_url=True):
        e(TAG.INPUT, type="text", name="name", placeholder="Enter name")
        e(TAG.BUTTON, type="submit", text="Submit")

print(to_string(b))
# <div class="container"><form hx-post="/api/submit" hx-target="#response" hx-push-url="true"><input type="text" name="name" placeholder="Enter name"></input><button type="submit">Submit</button></form></div>
```

## Features

- **Zero dependencies** - Uses only Python standard library
- **HTMX support** - Built-in HTMX attribute helpers
- **XSS protection** - Automatic HTML escaping
- **Pythonic API** - Context managers for nested elements
- **Type hints** - Full type annotation support

## Benchmark

Performance comparison with other Python HTML builders (simple form with 2 inputs):

| Framework | Mean Time |
|-----------|-----------|
| **simple-html-builder** | 0.040ms |
| htbuilder | 0.040ms |
| FastHTML | 0.179ms |
| Jinja2 | 0.297ms |

Complex nested structure (50 elements):

| Framework | Mean Time |
|-----------|-----------|
| **simple-html-builder** | 0.496ms |
| htbuilder | 0.624ms |
| Jinja2 | 1.389ms |
| FastHTML | 2.890ms |

Run `python benchmark.py` to reproduce these results.

## Why Use This?

1. **Simplicity** - No templates, just Python code
2. **Zero dependencies** - No external packages required
3. **HTMX-native** - First-class HTMX support
4. **Fast** - Minimal overhead, maximum performance
5. **Debuggable** - Standard Python, easy to debug

## License

MIT License - see [LICENSE](LICENSE) file.
