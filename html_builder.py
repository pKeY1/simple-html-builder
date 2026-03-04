from contextlib import contextmanager
from contextvars import ContextVar
from enum import StrEnum


_current_builder: ContextVar[dict | None] = ContextVar('builder', default=None)


def new_builder():
   b = {"root": None, "stack": []}
   _current_builder.set(b)
   return b


def _get_builder(b: dict | None = None) -> dict:
   if b is not None:
      return b
   builder = _current_builder.get()
   if builder is None:
      raise RuntimeError("No builder in context: call new_builder() first or pass b explicitly")
   return builder


class TAG(StrEnum):
   DIV = "div"
   BUTTON = "button"
   A = "a"
   INPUT = "input"
   FORM = "form"
   LABEL = "label"
   SPAN = "span"
   P = "p"
   H1 = "h1"
   H2 = "h2"
   H3 = "h3"
   H4 = "h4"
   H5 = "h5"
   H6 = "h6"
   UL = "ul"
   OL = "ol"
   LI = "li"
   TABLE = "table"
   TR = "tr"
   TD = "td"
   TH = "th"
   THEAD = "thead"
   TBODY = "tbody"
   IMG = "img"
   SCRIPT = "script"
   STYLE = "style"
   LINK = "link"
   META = "meta"
   HEAD = "head"
   BODY = "body"
   HTML = "html"
   TITLE = "title"
   IFRAME = "iframe"
   TEXTAREA = "textarea"
   SELECT = "select"
   OPTION = "option"
   PRE = "pre"
   CODE = "code"
   BR = "br"
   HR = "hr"
   MAIN = "main"
   HEADER = "header"
   FOOTER = "footer"
   NAV = "nav"
   SECTION = "section"
   ARTICLE = "article"
   ASIDE = "aside"
   DETAILS = "details"
   SUMMARY = "summary"
   DIALOG = "dialog"
   TEMPLATE = "template"
   SLOT = "slot"
   CANVAS = "canvas"
   SVG = "svg"
   PATH = "path"
   FIGURE = "figure"
   FIGCAPTION = "figcaption"


def _build_attrs(
   id=None,
   class_=None,
   text=None,
   on_click=None,
   on_change=None,
   hx_get=None,
   hx_post=None,
   hx_put=None,
   hx_delete=None,
   hx_patch=None,
   hx_target=None,
   hx_trigger=None,
   hx_vals=None,
   hx_include=None,
   href=None,
   hx_push_url=False,
   **attr,
):
   attrs = {}

   if id:
      attrs["id"] = id
   if class_:
      attrs["class"] = class_
   if text:
      attrs["_text"] = text
   if on_click:
      attrs["onclick"] = on_click
   if on_change:
      attrs["onchange"] = on_change
   if hx_get:
      attrs["hx-get"] = hx_get
   if hx_post:
      attrs["hx-post"] = hx_post
   if hx_put:
      attrs["hx-put"] = hx_put
   if hx_delete:
      attrs["hx-delete"] = hx_delete
   if hx_patch:
      attrs["hx-patch"] = hx_patch
   if hx_target:
      attrs["hx-target"] = hx_target
   if hx_trigger:
      attrs["hx-trigger"] = hx_trigger
   if hx_vals:
      attrs["hx-vals"] = hx_vals
   if hx_include:
      attrs["hx-include"] = hx_include
   if href:
      attrs["href"] = href
   attrs["hx-push-url"] = str(hx_push_url).lower()

   for k, v in attr.items():
      attrs[k] = v

   return attrs


def _create_node(tag, attrs):
   return {
      "type": "element",
      "tag": tag,
      "attrs": attrs,
      "children": [],
   }


@contextmanager
def r(
   tag=TAG.DIV,
   id=None,
   class_=None,
   text=None,
   on_click=None,
   on_change=None,
   hx_get=None,
   hx_post=None,
   hx_put=None,
   hx_delete=None,
   hx_patch=None,
   hx_target=None,
   hx_trigger=None,
   hx_vals=None,
   hx_include=None,
   href=None,
   hx_push_url=False,
   b=None,
   **attr,
):
   b = _get_builder(b)

   attrs = _build_attrs(
      id=id,
      class_=class_,
      text=text,
      on_click=on_click,
      on_change=on_change,
      hx_get=hx_get,
      hx_post=hx_post,
      hx_put=hx_put,
      hx_delete=hx_delete,
      hx_patch=hx_patch,
      hx_target=hx_target,
      hx_trigger=hx_trigger,
      hx_vals=hx_vals,
      hx_include=hx_include,
      href=href,
      hx_push_url=hx_push_url,
      **attr,
   )

   node = _create_node(tag, attrs)

   if not b["stack"]:
      b["root"] = node
   else:
      b["stack"][-1]["children"].append(node)

   b["stack"].append(node)

   try:
      yield
   finally:
      b["stack"].pop()


def e(
   tag=TAG.DIV,
   id=None,
   class_=None,
   text=None,
   on_click=None,
   on_change=None,
   hx_get=None,
   hx_post=None,
   hx_put=None,
   hx_delete=None,
   hx_patch=None,
   hx_target=None,
   hx_trigger=None,
   hx_vals=None,
   hx_include=None,
   href=None,
   hx_push_url=False,
   b=None,
   **attr,
):
   b = _get_builder(b)

   attrs = _build_attrs(
      id=id,
      class_=class_,
      text=text,
      on_click=on_click,
      on_change=on_change,
      hx_get=hx_get,
      hx_post=hx_post,
      hx_put=hx_put,
      hx_delete=hx_delete,
      hx_patch=hx_patch,
      hx_target=hx_target,
      hx_trigger=hx_trigger,
      hx_vals=hx_vals,
      hx_include=hx_include,
      href=href,
      hx_push_url=hx_push_url,
      **attr,
   )

   node = _create_node(tag, attrs)

   if not b["stack"]:
      if b["root"]:
         raise RuntimeError("Cannot add sibling to root: use r() to create a parent first")
      b["root"] = node
   else:
      b["stack"][-1]["children"].append(node)


def end(b=None):
   b = _get_builder(b)
   if not b["stack"]:
      raise RuntimeError("Stack underflow: nothing to end")
   b["stack"].pop()


def _escape(s):
   return __import__("html").escape(str(s), quote=True)


def _render_attrs(attrs):
   result = []
   for k, v in attrs.items():
      if k == "_text":
         continue
      result.append(f' {k}="{_escape(v)}"')
   return "".join(result)


def _render(node, out):
   tag = node["tag"]
   attrs = node["attrs"]
   children = node["children"]
   text = attrs.get("_text")

   attrs_str = _render_attrs(attrs)

   if children or text:
      out.append(f"<{tag}{attrs_str}>")
      if text:
         out.append(_escape(text))
      for child in children:
         _render(child, out)
      out.append(f"</{tag}>")
   else:
      out.append(f"<{tag}{attrs_str}></{tag}>")


def to_string(b):
   if b["root"] is None:
      return ""
   out = []
   _render(b["root"], out)
   return "".join(out)
