import unittest

from htmlnode import HTMLNode, LeafNode

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

  def test_repr(self):
    node = LeafNode("p", "Hi")
    self.assertEqual(repr(node), "LeafNode(p, Hi, None)")

if __name__ == "__main__":
    unittest.main()