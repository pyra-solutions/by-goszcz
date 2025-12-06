
import unittest
import asyncio
import os
import json
from unittest.mock import patch, MagicMock, AsyncMock

# Add the project root to the python path to allow importing download_acts
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from download_acts import main, download_act
from eli_for_polish_acts_client.models.act_info import ActInfo
from eli_for_polish_acts_client.models.publishing_house import PublishingHouse
from eli_for_polish_acts_client.models.acts import Acts

class TestDownloadActs(unittest.TestCase):

    def setUp(self):
        # Create dummy directories for testing
        os.makedirs("acts", exist_ok=True)
        os.makedirs("api_responses/publishers", exist_ok=True)
        os.makedirs("api_responses/years", exist_ok=True)
        os.makedirs("api_responses/acts/TEST", exist_ok=True)

    def tearDown(self):
        # Clean up dummy files and directories
        if os.path.exists("acts/TEST_2023_1.pdf"):
            os.remove("acts/TEST_2023_1.pdf")
        if os.path.exists("api_responses/publishers.json"):
            os.remove("api_responses/publishers.json")
        if os.path.exists("api_responses/years/TEST.json"):
            os.remove("api_responses/years/TEST.json")
        if os.path.exists("api_responses/acts/TEST/2023.json"):
            os.remove("api_responses/acts/TEST/2023.json")


    @patch('eli_for_polish_acts_client.api.listing_acts.get_publishers.asyncio', new_callable=AsyncMock)
    @patch('eli_for_polish_acts_client.api.listing_acts.get_years.asyncio', new_callable=AsyncMock)
    @patch('eli_for_polish_acts_client.api.listing_acts.get_acts_in_year.asyncio', new_callable=AsyncMock)
    @patch('eli_for_polish_acts_client.api.act_details.get_act_pdf.asyncio_detailed', new_callable=AsyncMock)
    def test_full_run_with_mocks(self, mock_get_act_pdf, mock_get_acts_in_year, mock_get_years, mock_get_publishers):
        # Mock API responses
        mock_publisher = PublishingHouse(code="TEST", name="Test Publisher")
        mock_get_publishers.return_value = [mock_publisher]
        
        mock_years = MagicMock()
        mock_years.to_dict.return_value = {"years": [2023]}
        mock_get_years.return_value = mock_years

        mock_act_info = ActInfo(publisher="TEST", year=2023, pos=1, address="TEST/2023/1")
        mock_acts = MagicMock()
        mock_acts.to_dict.return_value = {"items": [mock_act_info.to_dict()]}
        mock_acts.items = [mock_act_info]
        mock_get_acts_in_year.return_value = mock_acts

        mock_pdf_response = MagicMock()
        mock_pdf_response.content = b"fake pdf content"
        mock_get_act_pdf.return_value = mock_pdf_response

        # Run the main function
        asyncio.run(main())

        # Assertions
        mock_get_publishers.assert_called_once()
        mock_get_years.assert_called_once_with(client=unittest.mock.ANY, publisher="TEST")
        mock_get_acts_in_year.assert_called_once_with(client=unittest.mock.ANY, year=2023, publisher="TEST")
        mock_get_act_pdf.assert_called_once_with(client=unittest.mock.ANY, publisher="TEST", year=2023, position=1)

        # Check if files were created
        self.assertTrue(os.path.exists("api_responses/publishers.json"))
        self.assertTrue(os.path.exists("api_responses/years/TEST.json"))
        self.assertTrue(os.path.exists("api_responses/acts/TEST/2023.json"))
        self.assertTrue(os.path.exists("acts/TEST_2023_1.pdf"))
        with open("acts/TEST_2023_1.pdf", "rb") as f:
            self.assertEqual(f.read(), b"fake pdf content")

    @patch('eli_for_polish_acts_client.api.listing_acts.get_publishers.asyncio', new_callable=AsyncMock)
    @patch('eli_for_polish_acts_client.api.listing_acts.get_years.asyncio', new_callable=AsyncMock)
    @patch('eli_for_polish_acts_client.api.listing_acts.get_acts_in_year.asyncio', new_callable=AsyncMock)
    def test_cache_reading(self, mock_get_acts_in_year, mock_get_years, mock_get_publishers):
        # Pre-create cache files
        with open("api_responses/publishers.json", "w") as f:
            json.dump([{"code": "TEST", "name": "Test Publisher"}], f)
        with open("api_responses/years/TEST.json", "w") as f:
            json.dump({"years": [2023]}, f)
        with open("api_responses/acts/TEST/2023.json", "w") as f:
            json.dump({"items": [{"publisher": "TEST", "year": 2023, "pos": 1, "address": "TEST/2023/1"}]}, f)

        # Run the main function
        asyncio.run(main())

        # Assert that API functions were NOT called
        mock_get_publishers.assert_not_called()
        mock_get_years.assert_not_called()
        mock_get_acts_in_year.assert_not_called()

    @patch('eli_for_polish_acts_client.api.act_details.get_act_pdf.asyncio_detailed', new_callable=AsyncMock)
    def test_pdf_skipping(self, mock_get_act_pdf):
        # Pre-create a dummy PDF file
        with open("acts/TEST_2023_1.pdf", "w") as f:
            f.write("dummy pdf")
        
        # Pre-create cache files to lead to this PDF
        with open("api_responses/publishers.json", "w") as f:
            json.dump([{"code": "TEST", "name": "Test Publisher"}], f)
        with open("api_responses/years/TEST.json", "w") as f:
            json.dump({"years": [2023]}, f)
        with open("api_responses/acts/TEST/2023.json", "w") as f:
            json.dump({"items": [{"publisher": "TEST", "year": 2023, "pos": 1, "address": "TEST/2023/1"}]}, f)

        # Run the main function
        asyncio.run(main())

        # Assert that the PDF download function was NOT called
        mock_get_act_pdf.assert_not_called()



if __name__ == '__main__':
    unittest.main()
