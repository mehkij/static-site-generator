import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", None, ["p", "p", "a"])
        node2 = HTMLNode("p", "The cow jumped over the moon", None)
        node3 = HTMLNode("a", None, None, {"href": "https://boot.dev", "target": "_blank"})

        leaf = LeafNode("a", "Best Backend Bootcamp Ever...!", {"href": "https://boot.dev", "target": "_blank"})
        leaf2 = LeafNode("p", "The koi leapt over the sun")
        leaf3 = LeafNode(None, "Lorem Ipsum")

        parent1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        parent2 = ParentNode(
            "body",
            [
                LeafNode("h1", "Title"),
                ParentNode("p", [LeafNode("b", "Example_Username: "), LeafNode("i", "Today @ 4:55PM: "), LeafNode(None, "Nothing out of the ordinary. What's up with you though?")])
            ],
        )

        parent3 = ParentNode(
            "html",
            [
                ParentNode("head", [LeafNode("title", "My Personal Portfolio"), LeafNode("link", " ", {"rel": "stylesheet", "href": "styles.css"})]),
                ParentNode("body", [LeafNode("h1", "Welcome to my Software Development Portfolio"), LeafNode("a", "Here are my projects. You can check them out on GitHub", {"href": "https://www.github.com/mehkij"})])
            ],
            {"lang": "en"},
        )

        print(node)
        print(node2)
        print(node3)
        print(node3.props_to_html())

        print("Leaf 1:", leaf.to_html())
        print("Leaf 2:", leaf2.to_html())
        print("Leaf 3:", leaf3.to_html())

        print("Parent 1:", parent1.to_html())
        print("Parent 2:", parent2.to_html())
        print("Parent 3:", parent3.to_html())

if __name__ == "__main__":
    unittest.main()
