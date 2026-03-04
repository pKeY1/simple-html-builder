from html_builder import *


def test_basic_with_r():
   b = new_builder()
   with r(class_="container"):
      e(TAG.BUTTON, id="btn", hx_get="/api", text="Click me")
      e(TAG.A, href="/other", class_="link", text="Link")

   expected = '<div class="container"><button id="btn" hx-get="/api">Click me</button><a class="link" href="/other">Link</a></div>'
   result = to_string(b)
   assert result == expected, f"Expected: {expected}\nGot: {result}"
   print("test_basic_with_r: PASSED")


def test_nested_elements():
   b = new_builder()
   with r(class_="outer"):
      with r(class_="inner"):
         e(text="Nested text")

   expected = '<div class="outer"><div class="inner"><div>Nested text</div></div></div>'
   result = to_string(b)
   assert result == expected, f"Expected: {expected}\nGot: {result}"
   print("test_nested_elements: PASSED")


def test_htmx_attributes():
   b = new_builder()
   e(TAG.BUTTON, hx_get="/api", hx_target="#result", hx_trigger="click", hx_push_url=True, text="Submit")

   expected = '<button hx-get="/api" hx-target="#result" hx-trigger="click" hx-push-url="true">Submit</button>'
   result = to_string(b)
   assert result == expected, f"Expected: {expected}\nGot: {result}"
   print("test_htmx_attributes: PASSED")


def test_default_div():
   b = new_builder()
   e(class_="default-div")

   expected = '<div class="default-div"></div>'
   result = to_string(b)
   assert result == expected, f"Expected: {expected}\nGot: {result}"
   print("test_default_div: PASSED")


def test_empty_builder():
   b = new_builder()
   result = to_string(b)
   assert result == "", f"Expected: empty string\nGot: {result}"
   print("test_empty_builder: PASSED")


def test_form_with_children():
   b = new_builder()
   with r(TAG.FORM, id="myform", on_click="submitForm()"):
      e(TAG.INPUT, class_="input", id="email")
      e(TAG.BUTTON, text="Submit")

   expected = '<form id="myform" onclick="submitForm()"><input id="email" class="input"></input><button>Submit</button></form>'
   result = to_string(b)
   assert result == expected, f"Expected: {expected}\nGot: {result}"
   print("test_form_with_children: PASSED")


def test_multiple_htmx_attrs():
   b = new_builder()
   with r(class_="flex gap-4"):
      e(TAG.BUTTON, hx_get="/api", hx_post="/submit", hx_target="#result", hx_trigger="click", hx_vals='{"key": "value"}', hx_include=".input", text="Submit")

   result = to_string(b)
   assert 'hx-vals="{&quot;key&quot;: &quot;value&quot;}"' in result, f"Expected hx-vals in result, got: {result}"
   assert 'hx-include=".input"' in result, f"Expected hx-include in result, got: {result}"
   print("test_multiple_htmx_attrs: PASSED")


def test_event_handlers():
   b = new_builder()
   e(TAG.INPUT, id="name", on_click="handleClick()", on_change="handleChange()")

   expected = '<input id="name" onclick="handleClick()" onchange="handleChange()"></input>'
   result = to_string(b)
   assert result == expected, f"Expected: {expected}\nGot: {result}"
   print("test_event_handlers: PASSED")


def test_html_escaping():
   b = new_builder()
   e(text='<script>alert("xss")</script>')

   expected = '<div>&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;</div>'
   result = to_string(b)
   assert result == expected, f"Expected: {expected}\nGot: {result}"
   print("test_html_escaping: PASSED")


def run_all_tests():
   print("Running all tests...\n")
   test_basic_with_r()
   test_nested_elements()
   test_htmx_attributes()
   test_default_div()
   test_empty_builder()
   test_form_with_children()
   test_multiple_htmx_attrs()
   test_event_handlers()
   test_html_escaping()
   print("\nAll tests PASSED!")
