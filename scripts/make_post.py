#!/usr/bin/env python

import git
import calendar
import datetime
from jinja2 import Environment, FileSystemLoader

git_repo = git.Repo(".", search_parent_directories=True)
root_dir = git_repo.working_dir

now = datetime.datetime.now()
values = {
    "YEAR": now.year,
    "MONTH": calendar.month_name[now.month]
}

env = Environment(loader=FileSystemLoader(f"{root_dir}/drafts/templates"))
template = env.get_template("listenings.md.j2")
target_name = f"{root_dir}/drafts/{values['MONTH'].lower()}-listenings.md"
with open(target_name, "w") as f:
    f.write(template.render(**values))
print(f"Generated {target_name}")
