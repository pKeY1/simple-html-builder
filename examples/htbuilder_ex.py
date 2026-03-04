from htbuilder import div, form, label, input_, button


def build_form():
   result = div(
      form(
         label("Name:", for_="name"),
         input_(type="text", name="name", id="name", class_="form-control"),
         label("Email:", for_="email"),
         input_(type="email", name="email", id="email", class_="form-control"),
         button("Submit", type="submit", class_="btn-primary"),
         hx_post="/submit",
         hx_target="#result",
      ),
      div(id="result"),
      id="app",
      class_="container",
   )
   return str(result)


if __name__ == "__main__":
   print(build_form())
