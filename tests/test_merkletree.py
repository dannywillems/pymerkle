import pytest
from pymerkle.core import MerkleTree


@pytest.fixture
def identity_merkle_tree():
    return MerkleTree(hash_function=lambda s: s)


@pytest.mark.parametrize("elements,expected_results", [
    (["h", "e", "l", "l", "o"], "helloo"),
    (["h", "e", "l", "l"], "hell")
])
def test_get_hash_with_identity_hash_function(identity_merkle_tree, elements, expected_results):
    for x in elements:
        identity_merkle_tree.add(x)
    assert identity_merkle_tree.get_hash() == expected_results

