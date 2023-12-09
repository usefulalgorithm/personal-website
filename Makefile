.PHONY: site
site:
	stack exec site watch

draft:
	@python ./scripts/make_post.py

finish:
	$(eval date := $(shell echo "from datetime import datetime; print(datetime.now().date())" | python3))
	$(eval base := $(shell basename drafts/*-listenings.md))
	fillin-release-dates-exe drafts/$(base) > posts/$(date)-$(base)
