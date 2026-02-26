#!/usr/bin/env python3
"""OpenAlex search script compatible with Python 3.8+"""
from __future__ import annotations
import json, sys, time, argparse, urllib.request, urllib.parse, urllib.error
from typing import List, Dict, Any, Optional

def search_openalex(query: str, max_results: int = 50, from_year: Optional[int] = None, to_year: Optional[int] = None) -> List[Dict[str, Any]]:
    """Search OpenAlex for papers matching the query."""
    papers = []
    per_page = min(max_results, 50)
    page = 1
    collected = 0

    while collected < max_results:
        params = {
            "search": query,
            "per_page": per_page,
            "page": page,
            "sort": "relevance_score:desc",
        }
        if from_year:
            params["filter"] = "from_publication_date:{}-01-01".format(from_year)
            if to_year:
                params["filter"] += ",to_publication_date:{}-12-31".format(to_year)

        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
        headers = {"User-Agent": "systematic-literature-review/1.0 (mailto:research@example.com)"}

        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print("  [WARN] Request failed for query '{}': {}".format(query[:50], e), file=sys.stderr)
            break

        results = data.get("results", [])
        if not results:
            break

        for work in results:
            # Extract abstract from inverted index
            abstract = ""
            aii = work.get("abstract_inverted_index")
            if aii:
                word_positions = []
                for word, positions in aii.items():
                    for pos in positions:
                        word_positions.append((pos, word))
                word_positions.sort()
                abstract = " ".join(w for _, w in word_positions)

            # Extract authors
            authors = []
            for authorship in work.get("authorships", []):
                author = authorship.get("author", {})
                name = author.get("display_name", "")
                if name:
                    authors.append(name)

            # Extract venue
            venue = ""
            primary_location = work.get("primary_location", {}) or {}
            source = primary_location.get("source", {}) or {}
            venue = source.get("display_name", "")

            paper = {
                "openalex_id": work.get("id", ""),
                "doi": work.get("doi", ""),
                "title": work.get("title", ""),
                "abstract": abstract,
                "authors": authors,
                "year": work.get("publication_year"),
                "venue": venue,
                "cited_by_count": work.get("cited_by_count", 0),
                "type": work.get("type", ""),
                "concepts": [c.get("display_name", "") for c in work.get("concepts", [])[:5]],
            }
            papers.append(paper)
            collected += 1
            if collected >= max_results:
                break

        page += 1
        time.sleep(0.3)  # polite delay

    return papers


def main():
    parser = argparse.ArgumentParser(description="Search OpenAlex")
    parser.add_argument("--queries-file", required=True, help="JSON file with queries")
    parser.add_argument("--output", required=True, help="Output JSONL file")
    parser.add_argument("--max-per-query", type=int, default=50)
    parser.add_argument("--from-year", type=int, default=None)
    parser.add_argument("--to-year", type=int, default=None)
    args = parser.parse_args()

    with open(args.queries_file) as f:
        queries_data = json.load(f)

    queries = queries_data.get("queries", [])
    all_papers = []
    seen_titles = set()

    for i, q in enumerate(queries):
        query_str = q["query"]
        rationale = q.get("rationale", "")
        print("[{}/{}] Searching: '{}' ({})".format(i+1, len(queries), query_str[:60], rationale[:40]))

        papers = search_openalex(query_str, max_results=args.max_per_query,
                                  from_year=args.from_year, to_year=args.to_year)

        new_count = 0
        for p in papers:
            title_lower = (p.get("title") or "").lower().strip()
            if title_lower and title_lower not in seen_titles:
                seen_titles.add(title_lower)
                p["search_query"] = query_str
                all_papers.append(p)
                new_count += 1

        print("  -> Got {} results, {} new unique".format(len(papers), new_count))

    with open(args.output, "w") as f:
        for p in all_papers:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    print("\nTotal unique papers: {}".format(len(all_papers)))
    print("Output: {}".format(args.output))


if __name__ == "__main__":
    main()
