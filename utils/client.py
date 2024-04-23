import argparse
from loguru import logger
import requests
import webbrowser


base_api = f"http://localhost:8081"

class ClassifyToxicComment:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="arguments")
        parser.add_argument(
            "--save_dir", type=str, help="html file to display", required=True
        )

        query_group = parser.add_mutually_exclusive_group()
        query_group.add_argument("--text_query", type=str, help="text query")

        args = parser.parse_args()
        self.save_dir = args.save_dir
        self.text_query = args.text_query

    def request_text(self, text_query):
        text_api = f"{base_api}/classify_text"

        headers = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
        }

        params = {"text": text_query}
        logger.info(f"Classification Query: {text_query}.")
        response = requests.post(text_api, params=params, headers=headers)
        if response.status_code == 200:
            self._writeHTML(text_query, response)

    def _writeHTML(self, text_query, response):
        with open(self.save_dir, "a", encoding="utf-8") as f:
            f.write(text_query+" ")
            f.write(response.text+"\n")
            logger.info(f"Written in '{self.save_dir}' successfully.")
            webbrowser.open(self.save_dir)

    def main(self):
        if self.text_query is not None:
            self.request_text(self.text_query)

if __name__ == "__main__":
    ClassifyToxicComment().main()
