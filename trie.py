from graphviz import Digraph

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

def visualize_trie_vertical(trie, node, parent_label='', graph=None):
    if graph is None:
        graph = Digraph(format='png')
        graph.attr(rankdir='TB')  # Set direction from top to bottom

    label = parent_label
    if node.is_end_of_word:
        label += '*'
        graph.node(label, label=label, shape='doublecircle')
    else:
        graph.node(label, label=label)

    for char, child in node.children.items():
        child_label = parent_label + char
        graph.edge(label, child_label, label=char)
        visualize_trie_vertical(trie, child, child_label, graph)

    return graph

# Example usage:
trie = Trie()
words = ["app", "apps", "application", "applicent",'apply']
for word in words:
    trie.insert(word)

# Visualize the trie and save as PNG
graph = visualize_trie_vertical(trie, trie.root)
graph.render(filename='trie_visualization_vertical', directory='.', cleanup=True, format='png', engine='dot')

print("Visualization saved as 'trie_visualization_vertical.png'")

