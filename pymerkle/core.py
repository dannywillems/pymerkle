from pymerkle.exception import WrongElementTypeError


class MerkleTree:
    def __init__(self, hash_function=None, elements=None, class_elements=None):
        """
        :param hash_function: if None, use __hash__ of the element
        :param elements: list of initial elements
        :param class_elements: class of the elements. Must contain a method get_hash which returns the hash of the
        object.
        """
        self.hash_function = hash_function
        self.class_elements = class_elements
        self.elements = elements or []
        if self.class_elements is not None:
            for elem in self.elements:
                self._check_element_correspond_to_class(elem)

    def _check_element_correspond_to_class(self, element):
        if self.class_elements is None:
            return True
        if not isinstance(element, self.class_elements):
            raise WrongElementTypeError
        return True

    def add(self, elem):
        self._check_element_correspond_to_class(elem)
        self.elements.append(elem)

    def _reduce_hash_tree(self, hashes_list):
        # we must always have an even number.
        if len(hashes_list) == 0:
            return []
        elif len(hashes_list) == 1:
            return self._reduce_hash_tree(hashes_list * 2)
        # We build the list of hashes from left to right
        else:
            a, b = hashes_list[:2]
            new_hash = self.hash_function(a + b)
            tail = self._reduce_hash_tree(hashes_list[2:])
            return [new_hash] + tail

    def _get_hash(self, hashes_list):
        """
        :param hashes_list:
        :return:
        """
        if len(hashes_list) == 0:
            raise RuntimeError("The hashes list can not be empty")
        # It is the merkle tree root.
        elif len(hashes_list) == 1:
            return hashes_list[0]
        else:
            # We reduce the list until we only have one element.
            new_list = self._reduce_hash_tree(hashes_list)
            return self._get_hash(new_list)

    def get_hash(self):
        return self._get_hash(self.elements)
