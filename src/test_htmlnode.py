import unittest

from htmlnode import HTMLNode

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