import heapq
from collections import defaultdict

# Define a Huffman Node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # Character
        self.freq = freq  # Frequency
        self.left = None  # Left child
        self.right = None  # Right child

    # Comparison operators for priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq


# Build the Huffman Tree
def build_huffman_tree(char_freq):
    # Priority queue (min-heap)
    heap = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    # Merge nodes until only one node (root) remains in the heap
    while len(heap) > 1:
        # Pop two nodes with the smallest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node with the combined frequency
        new_node = HuffmanNode(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        # Add the new node back to the heap
        heapq.heappush(heap, new_node)

    # The remaining node is the root of the Huffman Tree
    return heap[0]


# Generate Huffman Codes from the Huffman Tree
def generate_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return

    # If it's a leaf node, assign the current code to the character
    if root.char is not None:
        huffman_codes[root.char] = current_code
        return

    # Recur for the left and right subtrees
    generate_huffman_codes(root.left, current_code + "0", huffman_codes)
    generate_huffman_codes(root.right, current_code + "1", huffman_codes)


# Huffman Encoding Function
def huffman_encoding(data):
    # Step 1: Calculate frequency of each character
    if not data:
        return "", {}

    char_freq = defaultdict(int)
    for char in data:
        char_freq[char] += 1

    # Step 2: Build the Huffman Tree
    root = build_huffman_tree(char_freq)

    # Step 3: Generate Huffman Codes
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)

    # Step 4: Encode the input data using the generated codes
    encoded_data = "".join([huffman_codes[char] for char in data])
    
    return encoded_data, huffman_codes


# Huffman Decoding Function
def huffman_decoding(encoded_data, huffman_codes):
    # Reverse the Huffman codes dictionary
    reverse_huffman_codes = {v: k for k, v in huffman_codes.items()}

    # Decode the encoded data
    decoded_data = []
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_huffman_codes:
            decoded_data.append(reverse_huffman_codes[current_code])
            current_code = ""

    return "".join(decoded_data)


# Example usage
if __name__ == "__main__":
    data = "huffman encoding is a greedy algorithm"

    print(f"Original Data: {data}")

    # Perform Huffman encoding
    encoded_data, huffman_codes = huffman_encoding(data)
    print(f"Encoded Data: {encoded_data}")
    print(f"Huffman Codes: {huffman_codes}")

    # Perform Huffman decoding
    decoded_data = huffman_decoding(encoded_data, huffman_codes)
    print(f"Decoded Data: {decoded_data}")
