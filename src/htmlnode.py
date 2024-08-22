class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        text = ""

        for key, value in self.props.items():
            text += f' {key}="{value}"'
        
        return text

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        
        if not self.tag:
            return f"{self.value}"
        
        return f"<{self.tag}>{self.props_to_html()}{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All elements must have a tag.")
        
        if not self.children:
            raise ValueError("All parent nodes must have children.")

        # Recursive case
        children_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
