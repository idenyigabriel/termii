class TermiiPageMixin:
    """Termii pagination mixins

    - protected methods:
        - _get_page_number: extract page from pagination url or return default 1
    """

    def _get_page_number(self, pagination_url: str = None) -> str:
        """Extract the page number from a given termii next or previous page URL string,
        which is generated on each response.
        """
        if pagination_url:
            splits = pagination_url.split("?")
            for split in splits:
                if "page=" in split and (split.split("page=")[1]).isdigit():
                    return split.split("page=")[1].strip("/")
        return 1
