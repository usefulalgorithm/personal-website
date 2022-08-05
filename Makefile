.PHONY: site
site:
	stack exec site watch

draft:
	$(eval month := $(shell echo "import calendar;print(calendar.month_name[calendar.datetime.datetime.now().month].lower())" | python))
	cp drafts/templates/listenings.md drafts/$(month)-listenings.md

finish:
	$(eval date := $(shell echo "from datetime import datetime; print(datetime.now().date())" | python))
	$(eval base := $(shell basename drafts/*-listenings.md))
	fillin-release-dates-exe drafts/$(base) > posts/$(date)-$(base)
