"""Generate TikZ code for objects description: present classes."""
from resources.class_description import ObjectClassToTikz
from van_emde_boas_tree import VanEmdeBoasTree
from binary_search_tree import BinarySearchTree


if __name__ == "__main__":
    # Example
    objects = [
        ObjectClassToTikz(object=VanEmdeBoasTree(16)),
        ObjectClassToTikz(object=BinarySearchTree()),
    ]
    for element in objects:
        element.save_drawing()
