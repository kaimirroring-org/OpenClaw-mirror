#!/usr/bin/env python3
import json
import os
import sys
import urllib.request

API = "https://api.notion.com/v1"
VERSION = "2025-09-03"


def req(method, url, token, body=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": VERSION,
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode("utf-8") if body is not None else None
    r = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode("utf-8"))


def rich(text):
    return [{"text": {"content": text}}]


def main():
    if len(sys.argv) < 3:
        print("Usage: notion_mirror_upsert.py <source_repo> <mirror_repo> [status] [cron] [visibility] [workflow_url] [notes]")
        sys.exit(2)

    token = os.getenv("NOTION_API_KEY")
    db_id = os.getenv("NOTION_MIRROR_DB_ID", "5a5d8653-8edc-4cff-bd66-9411a3fc242a")
    if not token:
        print("ERROR: NOTION_API_KEY is required")
        sys.exit(2)

    source_repo = sys.argv[1]
    mirror_repo = sys.argv[2]
    status = sys.argv[3] if len(sys.argv) > 3 else "Pending setup"
    cron = sys.argv[4] if len(sys.argv) > 4 else "*/30 * * * *"
    visibility = sys.argv[5] if len(sys.argv) > 5 else "Private"
    workflow_url = sys.argv[6] if len(sys.argv) > 6 else ""
    notes = sys.argv[7] if len(sys.argv) > 7 else "Managed by OpenClaw mirroring flow."

    db = req("GET", f"{API}/databases/{db_id}", token)
    data_sources = db.get("data_sources", [])
    if not data_sources:
        print("ERROR: No data_source found for database")
        sys.exit(1)
    ds_id = data_sources[0]["id"]

    query_body = {
        "filter": {
            "property": "Name",
            "title": {"equals": source_repo}
        },
        "page_size": 1
    }
    q = req("POST", f"{API}/data_sources/{ds_id}/query", token, query_body)
    results = q.get("results", [])

    props = {
        "Name": {"title": rich(source_repo)},
        "Repo Mirror": {"rich_text": rich(mirror_repo)},
        "Mirror Enabled": {"checkbox": status in ("Active", "Pending setup")},
        "Status": {"select": {"name": status}},
        "Cron": {"rich_text": rich(cron)},
        "Source Visibility": {"select": {"name": visibility}},
        "Notes": {"rich_text": rich(notes)},
    }
    if workflow_url:
        props["Workflow URL"] = {"url": workflow_url}

    if results:
        page_id = results[0]["id"]
        out = req("PATCH", f"{API}/pages/{page_id}", token, {"properties": props})
        print("UPDATED", out.get("url", page_id))
    else:
        body = {
            "parent": {"database_id": db_id},
            "properties": props,
        }
        out = req("POST", f"{API}/pages", token, body)
        print("CREATED", out.get("url", out.get("id")))


if __name__ == "__main__":
    main()
