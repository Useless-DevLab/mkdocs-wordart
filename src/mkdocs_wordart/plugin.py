import re
import json
from json import JSONDecodeError
from typing import Any, Match, Optional
from jinja2 import Environment, PackageLoader
from mkdocs.plugins import BasePlugin
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files

class WordartPlugin(BasePlugin):

    def __init__(self) -> None:
        print("ok")

    def parse_json(self, content: str) -> Any:
        try:
            return json.loads(content)
        except JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
        return None

    def render_template(self, data: dict[Any, Any]) -> str:
        env = Environment(
            loader=PackageLoader("mkdocs_wordart", "templates"),
            lstrip_blocks=True,
            trim_blocks=True,
            autoescape=True,
        )
        return env.get_template("wordart.html").render(data)

    def replace_wordart_match(self, match: Match[str]) -> str:
        parsed_json = self.parse_json(match.group(1))
        if parsed_json is None:
            return ""
        return self.render_template(parsed_json)

    def on_page_markdown(self, markdown: str, page: Page, config: MkDocsConfig, files: Files) -> Optional[str]:
        return re.sub(
            re.compile(r"```wordart\n(.*?)\n```", re.DOTALL),
            self.replace_wordart_match,
            markdown
        )
