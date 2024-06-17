import random
import time
from binary_search_tree import BinarySearchTree
from van_emde_boas_tree import VanEmdeBoasTree

from jinja2 import Template

def run_tests(universe_size: int =1000000) -> dict:
    elements = random.sample(range(universe_size), universe_size // 2)

    # Testing Van Emde Boas Tree
    veb = VanEmdeBoasTree(universe_size)
    start_time = time.process_time()
    for elem in elements:
        veb.insert(elem)
    veb_insert_time =time.process_time() - start_time

    start_time =time.process_time()
    for elem in elements:
        veb.find_next(elem)
    veb_search_time =time.process_time() - start_time

    # Testing Binary Search Tree
    bst = BinarySearchTree()
    start_time =time.process_time()
    for elem in elements:
        bst.insert(elem)
    bst_insert_time =time.process_time() - start_time

    start_time =time.process_time()
    for elem in elements:
        bst.search(elem)
    bst_search_time =time.process_time() - start_time

    return {
        "universe_size": universe_size,
        "veb_insert_time": veb_insert_time,
        "veb_search_time": veb_search_time,
        "bst_insert_time": bst_insert_time,
        "bst_search_time": bst_search_time
    }
    
def generate_pgf(results: list):
    
    with open('resources/template_performances.tex.jinja', 'r') as file:
        template_content = file.read()

    template = Template(template_content)
    rendered_latex = template.render(results=results)

    # Save the rendered LaTeX to a file
    output_path = 'documentation/images/visualizations/time_performance_plot.tex'
    with open(output_path, 'w') as f:
        f.write(rendered_latex)

if __name__ == "__main__":
    universe_sizes = [i * (10 ** power) for power in range(1, 6) for i in range(1, 11)]
    results = [run_tests(size) for size in universe_sizes]

    generate_pgf(results)
