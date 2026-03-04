from reactpy import component, html, vdom_to_html


@component
def FormField(label_text, input_type, input_name):
   return html.div(
      html.label(label_text, html_for=input_name),
      html.input(type=input_type, name=input_name, id=input_name, class_name="form-control"),
   )


@component
def ContactForm():
   return html.div(
      {"id": "app", "class_name": "container"},
      html.form(
         {"hx_post": "/submit", "hx_target": "#result"},
         FormField("Name:", "text", "name"),
         FormField("Email:", "email", "email"),
         html.button({"type": "submit", "class_name": "btn-primary"}, "Submit"),
      ),
      html.div({"id": "result"}),
   )


def build_form():
   vdom = ContactForm()
   return vdom_to_html(vdom)


if __name__ == "__main__":
   print(build_form())
