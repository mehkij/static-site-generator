from htmlnode import LeafNode

def text_node_to_html_node(text_node):
   text_type_text = "text"
   text_type_bold = "bold"
   text_type_italic = "italic"
   text_type_code = "code"
   text_type_link = "link"
   text_type_image = "image"

   if text_node.text_type == text_type_text:
      return LeafNode(None, text_node.text)
   
   if text_node.text_type == text_type_bold:
      return LeafNode("b", text_node.text)
   
   if text_node.text_type == text_type_italic:
      return LeafNode("i", text_node.text)
   
   if text_node.text_type == text_type_code:
      return LeafNode("code", text_node.text)
   
   if text_node.text_type == text_type_link:
      return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
   
   if text_node.text_type == text_type_image:
      return LeafNode("img", None, {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
   