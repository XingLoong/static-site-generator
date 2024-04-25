import unittest
from markdown_blocks import (
  markdown_to_html_node,
  markdown_to_blocks,
  block_to_block_type,
  block_type_paragraph,
  block_type_heading,
  block_type_code,
  block_type_quote,
  block_type_ulist,
  block_type_olist
)

class TestMarkdown(unittest.TestCase):
  def test_markdown(self):
    test = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
    blocks = markdown_to_blocks(test)
    self.assertEqual(
      [
        "This is **bolded** paragraph",
        "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
        "* This is a list\n* with items",
      ],
      blocks
    )

  def test_markdown_more_lines(self):
    md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
      blocks,
      [
        "This is **bolded** paragraph",
        "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
        "* This is a list\n* with items",
      ],
    )

  def test_block_to_block_types(self):
    block = "## heading"
    self.assertEqual(block_to_block_type(block), block_type_heading)
    block = "```\mcode\n```"
    self.assertEqual(block_to_block_type(block), block_type_code)
    block = "> quote\n> quote 2\n> quote 3"
    self.assertEqual(block_to_block_type(block), block_type_quote)
    block = "* list\n* list 2"
    self.assertEqual(block_to_block_type(block), block_type_ulist)
    block = "1. first\n2. second\n3. third"
    self.assertEqual(block_to_block_type(block), block_type_olist)

  def test_paragraph(self):
    test = """
This is **bolded** paragraph
text in a p
tag here

"""
    node = markdown_to_html_node(test)
    html = node.to_html()
    self.assertEqual(
      "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
      html
    )
  
  def test_paragraphs(self):
    test = """
Paragraph 1

Paragraph 2

"""
    node = markdown_to_html_node(test)
    html = node.to_html()
    self.assertEqual(
      "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>",
      html
    )
  
  def test_lists(self):
    test = """
- This list
- with multiple
- *items*

1. This is an `ordered`
2. list
3. with stuff

"""
    node = markdown_to_html_node(test)
    html = node.to_html()
    self.assertEqual(
      "<div><ul><li>This list</li><li>with multiple</li><li><i>items</i></li></ul><ol><li>This is an <code>ordered</code></li><li>list</li><li>with stuff</li></ol></div>",
      html
    )
  
  def test_headings(self):
    test = """
# h1

paragraph

## h2
"""
    node = markdown_to_html_node(test)
    html = node.to_html()
    self.assertEqual(
      "<div><h1>h1</h1><p>paragraph</p><h2>h2</h2></div>",
      html
    )


  def test_quote(self):
    test = """
> this
> is quote

paragraph
"""
    node = markdown_to_html_node(test)
    html = node.to_html()
    self.assertEqual(
      "<div><blockquote>this is quote</blockquote><p>paragraph</p></div>",
      html
    )

if __name__ == "__main__":
  unittest.main()