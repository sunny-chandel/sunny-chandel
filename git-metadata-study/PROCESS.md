# Git Metadata Study - Process Flow

## Overview Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                   Git Metadata Study Process                     │
└─────────────────────────────────────────────────────────────────┘

Step 1: Setup
┌──────────────────────────────────────────────────────────────┐
│  • Review repository structure                               │
│  • Verify Git configuration                                  │
│  • Read documentation (README.md, USAGE.md)                  │
└──────────────────────────────────────────────────────────────┘
                            ↓
Step 2: Configure Study Parameters
┌──────────────────────────────────────────────────────────────┐
│  Choose:                                                      │
│  • Start date (e.g., 60 days ago)                           │
│  • Number of commits (e.g., 30)                             │
│  • Pattern (daily/weekdays/sparse)                          │
└──────────────────────────────────────────────────────────────┘
                            ↓
Step 3: Run Study Script
┌──────────────────────────────────────────────────────────────┐
│  python3 git-metadata-study/scripts/create_study_commits.py  │
│                                                               │
│  The script will:                                            │
│  1. Create branch: git-metadata-study                        │
│  2. Generate learning notes (one per day)                    │
│  3. Create commits with past timestamps                      │
│  4. Use GIT_AUTHOR_DATE and GIT_COMMITTER_DATE              │
└──────────────────────────────────────────────────────────────┘
                            ↓
Step 4: Local Analysis
┌──────────────────────────────────────────────────────────────┐
│  python3 git-metadata-study/scripts/analyze_commits.py       │
│                                                               │
│  Generates:                                                   │
│  • analysis-report.md (human-readable)                       │
│  • analysis-report.json (machine-readable)                   │
│  • Distribution charts and statistics                        │
└──────────────────────────────────────────────────────────────┘
                            ↓
Step 5: Push to GitHub
┌──────────────────────────────────────────────────────────────┐
│  git push origin git-metadata-study                          │
│                                                               │
│  GitHub will:                                                 │
│  • Process commit metadata                                   │
│  • Update contribution graph                                 │
│  • Reflect activity in timeline                              │
└──────────────────────────────────────────────────────────────┘
                            ↓
Step 6: Observe & Document
┌──────────────────────────────────────────────────────────────┐
│  • Visit GitHub profile                                      │
│  • Check contribution graph                                  │
│  • Compare with analysis report                              │
│  • Document findings in observations.md                      │
└──────────────────────────────────────────────────────────────┘
                            ↓
Step 7: Clean Up (Optional)
┌──────────────────────────────────────────────────────────────┐
│  git checkout main                                            │
│  git branch -D git-metadata-study                            │
│  git push origin --delete git-metadata-study                 │
└──────────────────────────────────────────────────────────────┘
```

## Commit Creation Process

```
For each commit in the schedule:
┌─────────────────────────────────────────────────────────────┐
│ 1. Generate Learning Note                                   │
│    ├─ Create markdown file                                  │
│    ├─ Include: date, topic, learnings, references           │
│    └─ Save to: learning-notes/day-XXX-YYYY-MM-DD.md        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Stage File                                                │
│    └─ git add learning-notes/day-XXX-YYYY-MM-DD.md         │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Create Commit with Timestamp                             │
│    ├─ Set GIT_AUTHOR_DATE=<past_date>                      │
│    ├─ Set GIT_COMMITTER_DATE=<past_date>                   │
│    └─ git commit -m "Learning Day X: ..."                  │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Git Creates Commit Object                                │
│    ├─ Stores file content (blob)                            │
│    ├─ Creates tree object                                   │
│    ├─ Creates commit object with metadata:                  │
│    │  • Author: sunny-chandel                               │
│    │  • Author Date: <past_date>                            │
│    │  • Committer: sunny-chandel                            │
│    │  • Committer Date: <past_date>                         │
│    │  • Parent: <previous_commit>                           │
│    └─ Computes SHA-1 hash                                   │
└─────────────────────────────────────────────────────────────┘
```

## Repository Structure

```
sunny-chandel/sunny-chandel (repository)
│
├── main (branch)
│   ├── README.md
│   ├── .github/
│   └── git-metadata-study/
│       ├── README.md              ← Study documentation
│       ├── USAGE.md               ← Detailed guide
│       ├── QUICKREF.md            ← Quick reference
│       ├── PROCESS.md             ← This file
│       └── scripts/
│           ├── create_study_commits.py
│           └── analyze_commits.py
│
└── git-metadata-study (branch) ← Created by script
    └── git-metadata-study/
        ├── README.md
        ├── USAGE.md
        ├── QUICKREF.md
        ├── PROCESS.md
        ├── learning-notes/
        │   ├── day-001-2025-11-21.md
        │   ├── day-002-2025-11-22.md
        │   └── ... (30+ files)
        ├── scripts/
        │   ├── create_study_commits.py
        │   └── analyze_commits.py
        └── analysis/
            ├── study-summary.json
            ├── observations.md
            ├── analysis-report.md
            └── analysis-report.json
```

## Git Commit Object Structure

```
Commit Object (SHA-1: abc123...)
┌─────────────────────────────────────────────────────────────┐
│ tree: def456...                                              │
│ parent: 789abc...                                            │
│ author: sunny-chandel <sunnychandel73@gmail.com>            │
│         2025-11-21 10:00:00 +0530                           │
│ committer: sunny-chandel <sunnychandel73@gmail.com>         │
│            2025-11-21 10:00:00 +0530                        │
│                                                              │
│ Learning Day 1: Git metadata study (2025-11-21)             │
└─────────────────────────────────────────────────────────────┘
```

## Timeline Visualization

```
Past ←─────────────────────────────────────────────────→ Present

Nov 21  Nov 22  Nov 23  ...  Dec 15  Dec 16  ...  Jan 20
  │       │       │            │       │            │
  ●       ●       ●            ●       ●            ●
  │       │       │            │       │            │
Day 1   Day 2   Day 3       Day 25  Day 26      Today
                                                   │
                                                   └─ Run script
                                                      Creates commits
                                                      with past dates

After pushing to GitHub:
═══════════════════════════════════════════════════════════════
GitHub Contribution Graph will show activity on Nov 21-Dec 16
═══════════════════════════════════════════════════════════════
```

## Data Flow

```
User Input                Git Operations              GitHub
─────────                 ──────────────              ──────

Parameters  ──────────►  Create Branch
(days, count,            git checkout -b
 pattern)                git-metadata-study
                                │
                                ↓
                         Generate Files
                         (learning notes)
                                │
                                ↓
                         Stage & Commit
                         with timestamps
                         GIT_*_DATE env
                                │
                                ↓
                         Local Repository
                         (.git/objects/)
                                │
                                ↓
                         git push  ──────────────►  Remote Repo
                                                    Process commits
                                                    Update graphs
                                                         │
                                                         ↓
User  ◄──────────────────────────────────────────  Contribution
Observes                                            Graph Updated
```

## Safety Mechanisms

```
┌─────────────────────────────────────────────────────────────┐
│ Safety Layer 1: Isolated Branch                             │
│ • All commits on separate branch                            │
│ • Main branch untouched                                     │
│ • Can be deleted without affecting main                     │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Safety Layer 2: Authentic Commits                           │
│ • Real Git objects (not fake/empty)                         │
│ • Valid file content (learning notes)                       │
│ • Proper author attribution                                 │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Safety Layer 3: Transparency                                │
│ • Clear documentation                                       │
│ • Explicit commit messages                                  │
│ • Educational purpose stated                                │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ Safety Layer 4: Reversibility                               │
│ • Simple branch deletion                                    │
│ • No history rewriting                                      │
│ • No permanent changes                                      │
└─────────────────────────────────────────────────────────────┘
```

## Learning Outcomes

```
┌─────────────────────────────────────────────────────────────┐
│ Technical Understanding                                      │
│ ├─ Git object model                                         │
│ ├─ Commit metadata structure                                │
│ ├─ Timestamp handling                                       │
│ └─ Environment variables (GIT_*_DATE)                       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Platform Insights                                            │
│ ├─ How GitHub processes commits                             │
│ ├─ Contribution graph algorithms                            │
│ ├─ Activity visualization logic                             │
│ └─ Timezone considerations                                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Practical Skills                                             │
│ ├─ Creating timestamped commits                             │
│ ├─ Analyzing Git history                                    │
│ ├─ Branch management                                        │
│ └─ Automation with Python                                   │
└─────────────────────────────────────────────────────────────┘
```

---
**Created**: 2026-01-20  
**Author**: sunny-chandel  
**Purpose**: Visual guide to the Git metadata study process
