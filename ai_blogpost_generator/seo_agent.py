from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class SEOAgent:
    """
    A class to represent a SEOAgent.

    ...

    Attributes
    ----------
    api_key : str
        API key for Google's PageSpeed Insights API
    service : googleapiclient.discovery.Resource
        Google's PageSpeed Insights API service

    Methods
    -------
    perform_seo_analysis(url: str):
        Performs SEO analysis on the given URL using Google's PageSpeed Insights API and returns the analysis.
    """

    def __init__(self, api_key: str):
        """
        Constructs all the necessary attributes for the SEOAgent object.

        Parameters
        ----------
            api_key : str
                API key for Google's PageSpeed Insights API
        """

        self.api_key = api_key
        self.service = build('pagespeedonline', 'v5', developerKey=self.api_key)

    def perform_seo_analysis(self, url: str) -> dict:
        """
        Performs SEO analysis on the given URL using Google's PageSpeed Insights API and returns the analysis.

        Parameters
        ----------
            url : str
                The URL to perform SEO analysis on.

        Returns
        -------
        dict
            SEO analysis.
        """

        try:
            result = self.service.pagespeedapi().runpagespeed(url=url).execute()
            return result
        except HttpError as e:
            print(f"An error occurred: {e}")
            return None
