# Git Commit Metadata Study

## Purpose
This directory contains a **learning exercise** to study how Git commit metadata (particularly author and committer timestamps) influences activity visualization on source-control platforms like GitHub.

## Educational Goals
- Understand how Git stores temporal metadata in commit objects
- Observe how platforms compute contribution graphs and activity summaries
- Learn about the difference between author date and committer date
- Explore Git's internal object model and timestamp handling

## Methodology
This study uses **standard Git mechanisms** to create authentic commit objects with controlled timestamps:
- All commits contain real, valid file changes (daily learning notes)
- Timestamps are set using `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environment variables
- All commits are authored under the verified account: sunny-chandel
- The process is fully reversible and transparent

## Important Disclaimers
⚠️ **This is a learning exercise, NOT:**
- A representation of actual productivity or work history
- An attempt to misrepresent professional contributions
- Intended for use on shared/collaborative repositories
- A replacement for genuine development activity

## Repository Safety
- ✅ Operating on personal repository only
- ✅ Uses dedicated branch (`git-metadata-study`)
- ✅ Fully reversible (branch can be deleted)
- ✅ No history rewriting on main branch
- ✅ All commits are authentic Git objects

## Structure
```
git-metadata-study/
├── README.md                    # This file
├── learning-notes/              # Daily learning notes (commit content)
├── scripts/                     # Automation scripts
│   └── create_study_commits.py  # Main commit generation script
└── analysis/                    # Analysis and observations
    └── observations.md          # Findings from the study
```

## Usage
See `scripts/create_study_commits.py` for the implementation.

## Reversibility
To remove this study:
```bash
git checkout main
git branch -D git-metadata-study
```

---
**Created**: 2026-01-20  
**Author**: sunny-chandel  
**Purpose**: Educational exploration of Git internals
