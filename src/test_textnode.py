import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    # Equal TextType
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    # Not equal TextType
    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    # Not Equal Text
    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    # Equal URL
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.example.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.example.com")
        self.assertEqual(node, node2)

    # Equal __repr__
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.example.com")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.example.com)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()