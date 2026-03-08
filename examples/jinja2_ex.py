from jinja2 import Template

FORM_TEMPLATE = Template("""
<div id="app" class="container">
    <form hx-post="/submit" hx-target="#result">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" class="form-control">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" class="form-control">
        <button type="submit" class="btn-primary">Submit</button>
    </form>
    <div id="result"></div>
</div>
""")

def build_form():
    return FORM_TEMPLATE.render()

if __name__ == "__main__":
    print(build_form())
