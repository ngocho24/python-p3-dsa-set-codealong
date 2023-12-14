class MySet:

    def __init__(self, enumerable=None):
        """
        Constructor for MySet class.

        :param enumerable: An iterable to initialize the set. Defaults to an empty list.
        """
        if enumerable is None:
            enumerable = []
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        """
        Check if the set contains a specific value.

        :param value: The value to check.
        :return: True if the value is present, False otherwise.
        """
        return value in self.dictionary

    def __str__(self):
        """
        Return a string representation of the set.

        :return: A string representation of the set.
        """
        set_list = [str(key) for key in self.dictionary.keys()]
        return f'MySet: {{{",".join(set_list)}}}'

    def add(self, value):
        """
        Add a value to the set.

        :param value: The value to add.
        :return: The updated set.
        """
        self.dictionary[value] = True
        return self

    def delete(self, value):
        """
        Remove a value from the set.

        :param value: The value to remove.
        :return: The updated set.
        """
        self.dictionary.pop(value, None)
        return self

    def size(self):
        """
        Get the number of elements in the set.

        :return: The size of the set.
        """
        return len(self.dictionary)

    def clear(self):
        """
        Clear all elements from the set.

        :return: None
        """
        self.dictionary.clear()
