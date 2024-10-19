from memory_stream import MemoryStream, extract_recency, extract_importance, extract_relevance
from typing import List, Dict

# Create a mock memory stream with a few ConceptNode objects for testing
def create_mock_memory_stream() -> MemoryStream:
    nodes = [
        {"node_id": 0, "node_type": "observation", "content": "The sky is blue", "importance": 0.8, "created": 100, "last_retrieved": 110, "pointer_id": None},
        {"node_id": 1, "node_type": "observation", "content": "The sun is bright", "importance": 0.6, "created": 90, "last_retrieved": 105, "pointer_id": None},
        {"node_id": 2, "node_type": "reflection", "content": "It might rain tomorrow", "importance": 0.9, "created": 95, "last_retrieved": 115, "pointer_id": None}
    ]
    # Embeddings are dummy vectors for this example
    embeddings = {
        "The sky is blue": [0.1, 0.2, 0.3],
        "The sun is bright": [0.4, 0.5, 0.6],
        "It might rain tomorrow": [0.7, 0.8, 0.9]
    }
    return MemoryStream(nodes, embeddings)

# Test the extract_recency function
def test_extract_recency(memory_stream: MemoryStream):
    recency_scores = extract_recency(memory_stream.seq_nodes)
    print("Recency Scores:")
    for node_id, score in recency_scores.items():
        print(f"Node ID {node_id}: {score}")

# Test the extract_importance function
def test_extract_importance(memory_stream: MemoryStream):
    importance_scores = extract_importance(memory_stream.seq_nodes)
    print("\nImportance Scores:")
    for node_id, score in importance_scores.items():
        print(f"Node ID {node_id}: {score}")

# Test the extract_relevance function
def test_extract_relevance(memory_stream: MemoryStream, focal_point: str):
    relevance_scores = extract_relevance(memory_stream.seq_nodes, memory_stream.embeddings, focal_point)
    print("\nRelevance Scores:")
    for node_id, score in relevance_scores.items():
        print(f"Node ID {node_id}: {score}")

if __name__ == "__main__":
    # Create a mock memory stream for testing
    memory_stream = create_mock_memory_stream()

    # Run tests
    test_extract_recency(memory_stream)
    test_extract_importance(memory_stream)
    test_extract_relevance(memory_stream, "The sky is blue")
