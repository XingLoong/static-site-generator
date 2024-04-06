import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase): 
  def test_to_html(self):
    prop = HTMLNode(
      "p",
      "Hello World!",
      None,
      {"href": "https://www.google.com", "target": "_blank"}
    )
    self.assertEqual(
      prop.props_to_html(),
      ' href="https://www.google.com" target="_blank"'
    )
  
  def test_html2(self):
    prop2 = HTMLNode(
      "a",
      "Tested",
      None,
      {"div": "something", "href":"https://boot.dev"}
    )
    self.assertEqual(
      prop2.props_to_html(),
      ' div="something" href="https://boot.dev"'
    )
  
  def test_leaf_no_children_no_prop(self):
    node = LeafNode("p", "Hello World!")
    self.assertEqual(node.to_html(), "<p>Hello World!</p>")

  def test_leaf_no_tag(self):
    node = LeafNode(None, "Hello World!")
    self.assertEqual(node.to_html(), "Hello World!")

  def test_leaf_repr(self):
    node = LeafNode("p", "Hi")
    self.assertEqual(repr(node), "LeafNode(p, Hi, None)")

  def test_parent_child(self):
    child_node = LeafNode("p", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><p>child</p></div>")

  def test_parent_grandchild(self):
    granchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("p", [granchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><p><b>grandchild</b></p></div>")

  def test_many_grandchildren_eg(self):
    node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ]
    )
    self.assertEqual(node.to_html(), 
                     "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

if __name__ == "__main__":
    unittest.main()