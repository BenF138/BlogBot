class Blogpost:
    """
    A class to represent a blogpost.

    ...

    Attributes
    ----------
    title : str
        title of the blogpost
    content : str
        content of the blogpost
    seo_analysis : str
        SEO analysis of the blogpost
    images : list
        list of images in the blogpost

    Methods
    -------
    get_title():
        Returns the title of the blogpost.
    get_content():
        Returns the content of the blogpost.
    get_seo_analysis():
        Returns the SEO analysis of the blogpost.
    get_images():
        Returns the list of images in the blogpost.
    """

    def __init__(self, title: str, content: str, seo_analysis: str, images: list):
        """
        Constructs all the necessary attributes for the blogpost object.

        Parameters
        ----------
            title : str
                title of the blogpost
            content : str
                content of the blogpost
            seo_analysis : str
                SEO analysis of the blogpost
            images : list
                list of images in the blogpost
        """

        self.title = title
        self.content = content
        self.seo_analysis = seo_analysis
        self.images = images

    def get_title(self) -> str:
        """
        Returns the title of the blogpost.

        Returns
        -------
        str
            title of the blogpost
        """

        return self.title

    def get_content(self) -> str:
        """
        Returns the content of the blogpost.

        Returns
        -------
        str
            content of the blogpost
        """

        return self.content

    def get_seo_analysis(self) -> str:
        """
        Returns the SEO analysis of the blogpost.

        Returns
        -------
        str
            SEO analysis of the blogpost
        """

        return self.seo_analysis

    def get_images(self) -> list:
        """
        Returns the list of images in the blogpost.

        Returns
        -------
        list
            list of images in the blogpost
        """

        return self.images
