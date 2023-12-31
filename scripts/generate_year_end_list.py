import re
from datetime import datetime
import os


def gen_year_end_list():
    albums = []

    year = str(datetime.now().year)

    for post in os.listdir("posts"):
        if year in post:
            with open(f"posts/{post}") as f:
                lines = f.readlines()
                titles = [line for line in lines if "##" in line]
                release_dates = [line for line in lines if "Release date: " in line]
                scores = [line for line in lines if "/10]" in line]
                for title_line, release_date_line, score_line in zip(titles, release_dates, scores):
                    if f"{year}-" not in release_date_line:
                        continue
                    artist, title = title_line[2:].strip().split(" - ", 1)
                    score = float(next(match for match in re.finditer(r"[01]*\d\.\d", score_line)).group())
                    if score > 8.0:
                        release_date = next(re.finditer(r"[\d-]+", release_date_line)).group()
                        albums.append((score, artist, title, release_date))
    albums.sort(key=lambda album: album[0], reverse=True)
    with open(f"drafts/{year}_year_end_list.md", "w") as f:
        for (score, artist, title, _) in albums:
            f.write(
                f"### {artist} - {title} ({score})\n\n"
            )


if __name__ == "__main__":
    gen_year_end_list()
