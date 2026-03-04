from fasthtml.common import Div, Form, Label, Input, Button


def build_form():
   return Div(
      Div(
         Form(
            Label("Name:", html_for="name"),
            Input(type="text", name="name", id="name", cls="form-control"),
            Label("Email:", html_for="email"),
            Input(type="email", name="email", id="email", cls="form-control"),
            Button("Submit", type="submit", cls="btn-primary"),
            hx_post="/submit",
            hx_target="#result",
         ),
         Div(id="result"),
         id="app",
         cls="container",
      )
   )


if __name__ == "__main__":
   result = build_form()
   print(result)
