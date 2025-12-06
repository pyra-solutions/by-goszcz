
import unittest
import asyncio
import os
from eli_for_polish_acts_client.client import Client
from download_acts import download_act
from eli_for_polish_acts_client.api.listing_acts import get_acts_in_year, get_publishers, get_years
from eli_for_polish_acts_client.models.act_info import ActInfo

class TestDownloadActsIntegration(unittest.TestCase):

    def setUp(self):
        os.makedirs("acts", exist_ok=True)
        self.client = Client(base_url="https://api.sejm.gov.pl/eli", timeout=30.0)
        self.semaphore = asyncio.Semaphore(1)

    def tearDown(self):
        # Clean up downloaded files
        # This is a simplified cleanup. A more robust solution would be needed for a full test suite.
        for file in os.listdir("acts"):
            if file.startswith("DU_2023"):
                os.remove(os.path.join("acts", file))

    async def test_single_act_download(self):
        """
        Tests the download of a single act by making real API calls.
        """
        publishers = await get_publishers.asyncio(client=self.client)
        self.assertIsNotNone(publishers)
        self.assertGreater(len(publishers), 0)

        # Find the 'DU' publisher
        du_publisher = next((p for p in publishers if p.code == 'DU'), None)
        self.assertIsNotNone(du_publisher)

        years_response = await get_years.asyncio(client=self.client, publisher=du_publisher.code)
        self.assertIsNotNone(years_response)
        self.assertIn(2023, years_response.years)

        acts_response = await get_acts_in_year.asyncio(client=self.client, year=2023, publisher=du_publisher.code)
        self.assertIsNotNone(acts_response)
        self.assertGreater(len(acts_response.items), 0)

        # Take the first act and download it
        first_act = acts_response.items[0]
        await download_act(self.semaphore, self.client, first_act)

        # Check if the file was downloaded
        expected_file = f"acts/{first_act.publisher}_{first_act.year}_{first_act.pos}.pdf"
        self.assertTrue(os.path.exists(expected_file))

    def run_async_test(self, test_func):
        asyncio.run(test_func())

    def test_run_single_act_download(self):
        self.run_async_test(self.test_single_act_download)


if __name__ == '__main__':
    unittest.main()
