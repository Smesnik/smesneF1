from common import run_get

endpoint = "sessions"
params = {"year":2026}
subdirs = "year=2026"

run_get(endpoint=endpoint, params=params, subdirs=subdirs)

