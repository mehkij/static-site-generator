import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text", "bold")
        node4 = TextNode("This is a text node", "italics")
        node5 = TextNode("This is a text node", "bold", "https://boot.dev")

        html = TextNode(None, "link", "https://github.com/mehkij")
        html2 = TextNode("A picture of a cat", "image", "https://example_url.com")
        html3 = TextNode("An italicized work of fiction", "italic")
        html4 = TextNode("A bold statement", "bold")
        html5 = TextNode("A profound text", "text")
        html6 = TextNode("return 'You're awesome!' if cool else 'You suck!'", "code")

        # self.assertEqual(node, node2)
        # self.assertEqual(node, node3)
        # self.assertEqual(node, node4)
        # self.assertEqual(node, node5)

        # print("Text Node 1:", text_node_to_html_node(html))
        # print("Text Node 2:", text_node_to_html_node(html2))        
        # print("Text Node 3:", text_node_to_html_node(html3))
        # print("Text Node 4:", text_node_to_html_node(html4))
        # print("Text Node 5:", text_node_to_html_node(html5))
        # print("Text Node 6:", text_node_to_html_node(html6))
        
if __name__ == "__main__":
    unittest.main()
