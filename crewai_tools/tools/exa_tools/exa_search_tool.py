import requests
from typing import Any

from .exa_base_tool import EXABaseTool

class EXASearchTool(EXABaseTool):
	def _run(
		self,
		**kwargs: Any,
	) -> Any:
		search_query = kwargs.get('search_query')
		if search_query is None:
			search_query = kwargs.get('query')

		payload = {
				"query": search_query,
		}

		response = requests.post(self.search_url, json=payload, headers=self.headers)
		results = response.json()
		if 'results' in results:
			results = super()._parse_results(results['results'])
		else:
			return results