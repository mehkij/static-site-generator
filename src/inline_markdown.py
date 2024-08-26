import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes: 
        if node.text_type == text_type_text:
            new_nodes.append(node)
            continue

        node_text = node.text
        images = extract_markdown_images(node_text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            split = node_text.split(f"![{image[0]}]({image[1]})", 1)

            if len(split) != 2:
                raise ValueError("Invalid mardown, image section not closed")
            
            if split[0] != "":
                new_nodes.append(TextNode(split[0]), text_type_text)
            
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )

            node_text = split[1]

        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        node_text = node.text
        links = extract_markdown_links(node_text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            split = node_text.split(f"[{link[0]}]({link[1]})", 1)

            if len(split) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            
            if split[0] != "":
                new_nodes.append(TextNode(split[0], text_type_text))
            
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            node_text = split[1]
        
        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))
        
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)

    return (matches)

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

    return (matches)
