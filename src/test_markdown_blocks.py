import unittest
from markdown_blocks import (
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


if __name__ == "__main__":
  unittest.main()