class safedict(dict):
    """
    A dictionary subclass that ensures safe access to nested keys by returning a default value
    when a key is not found or its value is None. All returned dictionaries are safedict instances.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the safedict with optional initial data.

        Args:
            *args: Positional arguments passed to the base dict.
            **kwargs: Keyword arguments passed to the base dict.
        """
        super().__init__(*args, **kwargs)

    # def __getitem__(self, key):
    #     """
    #     Override the default `__getitem__` method to provide safe access to keys.

    #     Args:
    #         key: The key to access in the dictionary.

    #     Returns:
    #         The value associated with the key if it exists and is not None, otherwise an empty safedict.
    #     """
    #     value = super().get(key, None)
    #     return safedict(value) if isinstance(value, dict) else value if value is not None else safedict()

    def get(self, key, default=None):
        """
        Override the default `get` method to provide additional safety when accessing keys.

        Args:
            key: The key to access in the dictionary.
            default: The default value to return if the key does not exist or its value is None.

        Returns:
            The value associated with the key if it exists and is not None, otherwise the default wrapped in a safedict.
        """
        value = super().get(key)
        return safedict(value) if isinstance(value, dict) else value if value is not None else default

