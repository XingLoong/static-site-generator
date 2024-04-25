import unittest 
from inline_markdown import (
  split_nodes_delimiter,
  split_nodes_image,
  split_nodes_link,
  extract_markdown_images,
  extract_markdown_links,
  text_to_textnodes
)

from textnode import (
  TextNode, 
  text_type_text, 
  text_type_bold,
  text_type_italic,
  text_type_code,
  text_type_link,
  text_type_image
)

class TestInlineMarkdown(unittest.TestCase):
  def test_delim_bold(self):
    node = TextNode("This is text with a **bolded** word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
      [
        TextNode("This is text with a ", text_type_text),
        TextNode("bolded", text_type_bold),
        TextNode(" word", text_type_text)
      ],
      new_nodes
    )

  def test_delim_bold_double(self):
    node = TextNode(
      "This is text with a **bolded** word and **another** one", text_type_text
    )
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
      [
        TextNode("This is text with a ", text_type_text),
        TextNode("bolded", text_type_bold),
        TextNode(" word and ", text_type_text),
        TextNode("another", text_type_bold),
        TextNode(" one", text_type_text)
      ],
      new_nodes
    )
  def test_bold_multi(self):
    node = TextNode(
      "This is text with **bolded words** and **single**", text_type_text
    )
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
      [
        TextNode("This is text with ", text_type_text),
        TextNode("bolded words", text_type_bold),
        TextNode(" and ", text_type_text),
        TextNode("single", text_type_bold)
      ],
      new_nodes
    )

  def test_italic(self):
    node = TextNode("This is text with an *italic* word", text_type_text)
    new_node = split_nodes_delimiter([node], "*", text_type_italic)
    self.assertListEqual(
      [
        TextNode("This is text with an ", text_type_text),
        TextNode("italic", text_type_italic),
        TextNode(" word", text_type_text)
      ],
      new_node
    )
  
  def test_code(self):
    node = TextNode("This is a `code block` text", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    self.assertListEqual(
      [
        TextNode("This is a ", text_type_text),
        TextNode("code block", text_type_code),
        TextNode(" text", text_type_text)
      ],
      new_nodes
    )

  def test_image_markdown(self):
    matched = extract_markdown_images(
      "This is text with ![image](https://i.imgur.com/OVSaodK.jpg) and ![image](https://i.imgur.com/tO87JEn.jpg)"
    )
    self.assertListEqual(
      [
        ("image", "https://i.imgur.com/OVSaodK.jpg"),
        ("image", "https://i.imgur.com/tO87JEn.jpg")
      ], 
      matched
    )
    
  def test_links_markdown(self):
    matched = extract_markdown_links(
      "This is text with a [link](https://boot.dev) and [another link](https://google.com)"
    )
    self.assertListEqual(
      [
        ("link", "https://boot.dev"), 
        ("another link", "https://google.com")
      ],
      matched
      )

  def test_image_split(self):
    node = TextNode(
      "This is text with ![image](https://i.imgur.com/4Uczhus.jpg)", text_type_text
    )
    new_node = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("This is text with ", text_type_text),
        TextNode("image", text_type_image, "https://i.imgur.com/4Uczhus.jpg")
      ],
      new_node
    )

  def test_images_split(self):
    node = TextNode(
      "This is text with ![image](https://i.imgur.com/4Uczhus.jpg) and another ![second image](https://i.imgur.com/Nrb3rEK.jpg)", text_type_text
    )
    new_node = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("This is text with ", text_type_text),
        TextNode("image", text_type_image, "https://i.imgur.com/4Uczhus.jpg"),
        TextNode(" and another ", text_type_text),
        TextNode("second image", text_type_image, "https://i.imgur.com/Nrb3rEK.jpg")
      ],
      new_node
    )

  def test_links(self):
    node = TextNode(
      "This is text with [link](https://boot.dev) and secondary [second link](https://google.com) and more text", text_type_text
    )
    new_node = split_nodes_link([node])
    self.assertListEqual(
      [
        TextNode("This is text with ", text_type_text),
        TextNode("link", text_type_link, "https://boot.dev"),
        TextNode(" and secondary ", text_type_text),
        TextNode("second link", text_type_link, "https://google.com"),
        TextNode(" and more text", text_type_text)
      ],
      new_node
    )

  def test_text_conversion(self):
    node = text_to_textnodes(
      "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    )
    self.assertListEqual(
      [
        TextNode("This is ", text_type_text),
        TextNode("text", text_type_bold),
        TextNode(" with an ", text_type_text),
        TextNode("italic", text_type_italic),
        TextNode(" word and a ", text_type_text),
        TextNode("code block", text_type_code),
        TextNode(" and an ", text_type_text),
        TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        TextNode(" and a ", text_type_text),
        TextNode("link", text_type_link, "https://boot.dev"),
      ],
      node
    )

if __name__ == "__main__":
  unittest.main()