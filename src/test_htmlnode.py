import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", None, ["p", "p", "a"])
        node2 = HTMLNode("p", "The cow jumped over the moon", None)
        node3 = HTMLNode("a", None, None, {"href": "https://boot.dev", "target": "_blank"})

        print(node)
        print(node2)
        print(node3)
        node3.props_to_html()

if __name__ == "__main__":
    unittest.main()
