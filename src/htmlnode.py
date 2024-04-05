class HTMLNode:
  def __init__(self, tag = None, value = None, children = None, props = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError("no done yet")
  
  def props_to_html(self):
    if self.props == None:
      return ""
    temp_string = ""
    for prop in self.props:
      temp_string += f' {prop}="{self.props[prop]}"'
    return temp_string
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props = None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if self.value == None:
      raise ValueError("All Leaf Nodes require a value")
    if self.tag == None:
      return self.value
    return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
  
  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"
  
  