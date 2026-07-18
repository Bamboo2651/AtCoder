import argparse
import datetime
import json

import bs4
import requests


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("contest_id")
    args = parser.parse_args()

    url = f"https://atcoder.jp/contests/{args.contest_id}?lang=en"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    times = soup.select("small.contest-duration time.fixtime-full")
    if len(times) != 2:
        raise RuntimeError("Could not read the contest start and end times.")

    start = datetime.datetime.fromisoformat(times[0].get_text(strip=True))
    end = datetime.datetime.fromisoformat(times[1].get_text(strip=True))
    now = datetime.datetime.now(datetime.timezone.utc)

    if now < start:
        phase = "before"
    elif now < end:
        phase = "ongoing"
    else:
        phase = "ended"

    print(json.dumps({"phase": phase, "start": start.isoformat(), "end": end.isoformat()}))


if __name__ == "__main__":
    main()
