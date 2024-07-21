class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        text = ""

        if self.props is not None:
            for key, value in self.props.items():
                text += f' {key}="{value}"'
        else:
            text = ""
        
        return text

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, props)
        self.value = value

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        
        if not self.tag:
            return f"{self.value}"
        
        if self.tag == "a":
            return f"<{self.tag}{self.props_to_html()} {self.value}/>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"