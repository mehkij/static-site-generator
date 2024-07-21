import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", None, ["p", "p", "a"])
        node2 = HTMLNode("p", "The cow jumped over the moon", None)
        node3 = HTMLNode("a", None, None, {"href": "https://boot.dev", "target": "_blank"})

        leaf = LeafNode("Best Backend Bootcamp Ever...!", "a", {"href": "https://boot.dev", "target": "_blank"})
        leaf2 = LeafNode("The koi leapt over the sun", "p", None)
        leaf3 = LeafNode("Lorem Ipsum", None, None)

        print(node)
        print(node2)
        print(node3)
        node3.props_to_html()

        print("Leaf 1:",leaf.to_html())
        print("Leaf 2:", leaf2.to_html())
        print("Leaf 3:", leaf3.to_html())

if __name__ == "__main__":
    unittest.main()
