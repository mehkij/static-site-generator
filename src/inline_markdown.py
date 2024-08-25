from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        
        temp = []
        split = node.text.split(delimiter)
        
        if len(split) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        for i in range(len(split)):
            if split[i] == "":
                continue
            
            if i % 2 == 0:
                temp.append(TextNode(split[i], text_type_text))
            else:
                temp.append(TextNode(split[i], text_type))
                
        new_nodes.extend(temp)

    return new_nodes
