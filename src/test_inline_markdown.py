import unittest
from textnode import *
from inline_markdown import split_nodes_delimiter

class TestInlineMarkdown(unittest.TestCase):
    def test_eq(self):
        split = TextNode("This is a text with a `code block` word", text_type_text)
        split2 = TextNode("This is a text with a *italicized word*", text_type_text)
        split3 = TextNode("This is a text with a **bold word**", text_type_text)
        
        new_nodes = split_nodes_delimiter([split], "`", text_type_code)
        new_nodes2 = split_nodes_delimiter([split2], "*", text_type_italic)
        new_nodes3 = split_nodes_delimiter([split3], "**", text_type_bold)

        print(new_nodes)
        print(new_nodes2)
        print(new_nodes3)

if __name__ == "__main__":
    unittest.main()
