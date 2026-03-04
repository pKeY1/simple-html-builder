import time
import statistics
import sys


def benchmark_simple(name, build_fn, iterations=1000):
   times = []
   for _ in range(iterations):
      start = time.perf_counter()
      result = build_fn()
      end = time.perf_counter()
      times.append((end - start) * 1000)

   return {
      "name": name,
      "min": min(times),
      "max": max(times),
      "mean": statistics.mean(times),
      "median": statistics.median(times),
      "stdev": statistics.stdev(times) if len(times) > 1 else 0,
   }


def your_impl_nested():
   from html_builder import new_builder, r, e, TAG, to_string
   b = new_builder()
   with r(TAG.DIV, class_="container"):
      for i in range(10):
         with r(TAG.DIV, class_="item"):
            e(TAG.H1, text=f"Item {i}")
            with r(TAG.UL):
               for j in range(5):
                  with r(TAG.LI):
                     e(TAG.A, href=f"/item/{i}/{j}", text=f"Link {j}")
            e(TAG.BUTTON, class_="btn", text="Click", hx_post=f"/action/{i}")
   return to_string(b)


def htbuilder_nested():
   from htbuilder import div, h1, ul, li, a, button
   return str(div(
      div(
         *[div(
            h1(f"Item {i}"),
            ul(
               *[li(a(f"Link {j}", href=f"/item/{i}/{j}")) for j in range(5)]
            ),
            button("Click", class_="btn", hx_post=f"/action/{i}"),
            class_="item",
         ) for i in range(10)],
         class_="container",
      )
   ))


def fasthtml_nested():
   from fasthtml.common import Div, H1, Ul, Li, A, Button
   return str(Div(
      *[Div(
         H1(f"Item {i}"),
         Ul(
            *[Li(A(f"Link {j}", href=f"/item/{i}/{j}")) for j in range(5)]
         ),
         Button("Click", hx_post=f"/action/{i}", cls="btn"),
         cls="item",
      ) for i in range(10)],
      cls="container",
   ))


def jinja2_nested():
   from jinja2 import Template
   template = Template("""<div class="container">
{% for i in range(10) %}
<div class="item">
  <h1>Item {{ i }}</h1>
  <ul>
  {% for j in range(5) %}
    <li><a href="/item/{{ i }}/{{ j }}">Link {{ j }}</a></li>
  {% endfor %}
  </ul>
  <button class="btn" hx-post="/action/{{ i }}">Click</button>
</div>
{% endfor %}
</div>""")
   return template.render()


def benchmark_complex(name, build_fn, iterations=500):
   times = []
   for _ in range(iterations):
      start = time.perf_counter()
      result = build_fn()
      end = time.perf_counter()
      times.append((end - start) * 1000)

   return {
      "name": name,
      "min": min(times),
      "max": max(times),
      "mean": statistics.mean(times),
      "median": statistics.median(times),
   }


def run_benchmarks():
   print("=" * 75)
   print("HTML Builder Benchmark - Simple Form (1 form with 2 inputs)")
   print("=" * 75)
   print(f"Iterations: 1000")
   print()

   results = []

   from examples.your_impl import build_form as your_build
   results.append(benchmark_simple("Your Implementation", your_build))

   from examples.htbuilder_ex import build_form as htbuilder_build
   results.append(benchmark_simple("htbuilder", htbuilder_build))

   from examples.fasthtml_ex import build_form as fasthtml_build
   results.append(benchmark_simple("FastHTML", fasthtml_build))

   from examples.jinja2_ex import build_form as jinja2_build
   results.append(benchmark_simple("Jinja2", jinja2_build))

   print(f"{'Framework':<25} {'Mean (ms)':<10} {'Median (ms)':<10} {'Min (ms)':<10} {'Max (ms)':<10}")
   print("-" * 75)
   for r in results:
      print(f"{r['name']:<25} {r['mean']:<10.3f} {r['median']:<10.3f} {r['min']:<10.3f} {r['max']:<10.3f}")

   print()
   fastest = min(results, key=lambda x: x['mean'])
   print(f"Fastest: {fastest['name']}")
   print()

   print("=" * 75)
   print("HTML Builder Benchmark - Complex Nested (10 lists, 5 items each)")
   print("=" * 75)
   print(f"Iterations: 500")
   print()

   results2 = []

   results2.append(benchmark_complex("Your Implementation", your_impl_nested))
   results2.append(benchmark_complex("htbuilder", htbuilder_nested))
   results2.append(benchmark_complex("FastHTML", fasthtml_nested))
   results2.append(benchmark_complex("Jinja2", jinja2_nested))

   print(f"{'Framework':<25} {'Mean (ms)':<10} {'Median (ms)':<10} {'Min (ms)':<10} {'Max (ms)':<10}")
   print("-" * 75)
   for r in results2:
      print(f"{r['name']:<25} {r['mean']:<10.3f} {r['median']:<10.3f} {r['min']:<10.3f} {r['max']:<10.3f}")

   print()
   fastest2 = min(results2, key=lambda x: x['mean'])
   print(f"Fastest: {fastest2['name']}")

   print()
   print("=" * 75)



if __name__ == "__main__":
   run_benchmarks()
