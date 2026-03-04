from html_builder import new_builder, r, e, TAG, to_string


def build_form():
   b = new_builder()
   with r(TAG.DIV, id="app", class_="container"):
      with r(TAG.FORM, hx_post="/submit", hx_target="#result"):
         e(TAG.LABEL, text="Name:")
         e(TAG.INPUT, type="text", name="name", id="name", class_="form-control")
         e(TAG.LABEL, text="Email:")
         e(TAG.INPUT, type="email", name="email", id="email", class_="form-control")
         e(TAG.BUTTON, type="submit", text="Submit", class_="btn-primary")
      with r(TAG.DIV, id="result"):
         pass
   return to_string(b)


if __name__ == "__main__":
   print(build_form())
