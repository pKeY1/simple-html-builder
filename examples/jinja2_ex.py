from jinja2 import Template


FORM_TEMPLATE = """<div id="app" class="container">
  <form hx-post="/submit" hx-target="#result">
    <label for="name">Name:</label>
    <input type="text" name="name" id="name" class="form-control" />
    <label for="email">Email:</label>
    <input type="email" name="email" id="email" class="form-control" />
    <button type="submit" class="btn-primary">Submit</button>
  </form>
  <div id="result"></div>
</div>"""


def build_form():
   template = Template(FORM_TEMPLATE)
   return template.render()


if __name__ == "__main__":
   print(build_form())
