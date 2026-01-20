# Git Metadata Study - Quick Reference

## 🚀 Quick Start (3 Commands)

```bash
# 1. Run the study (30 commits over 60 days)
python3 git-metadata-study/scripts/create_study_commits.py

# 2. Analyze the results
python3 git-metadata-study/scripts/analyze_commits.py

# 3. Push to GitHub to see visualization
git push origin git-metadata-study
```

## 📋 Common Commands

### Create Study Commits

```bash
# Default: 30 daily commits starting 60 days ago
python3 git-metadata-study/scripts/create_study_commits.py

# Custom: 45 weekday commits starting 90 days ago
python3 git-metadata-study/scripts/create_study_commits.py --days-ago 90 --num-commits 45 --pattern weekdays

# Sparse: 20 commits over 120 days
python3 git-metadata-study/scripts/create_study_commits.py --days-ago 120 --num-commits 20 --pattern sparse
```

### View Commits

```bash
# List all study commits
git log git-metadata-study --oneline

# Show commit dates
git log git-metadata-study --format="%ai | %s" -20

# View commit graph
git log git-metadata-study --oneline --graph --all
```

### Analyze Results

```bash
# Generate analysis report
python3 git-metadata-study/scripts/analyze_commits.py

# View the report
cat git-metadata-study/analysis/analysis-report.md

# View JSON data
cat git-metadata-study/analysis/analysis-report.json
```

### Push to GitHub

```bash
# Push study branch
git push origin git-metadata-study

# View on GitHub
open https://github.com/sunny-chandel/sunny-chandel/tree/git-metadata-study
```

### Clean Up

```bash
# Delete local branch
git checkout main
git branch -D git-metadata-study

# Delete remote branch
git push origin --delete git-metadata-study
```

## 🎯 Study Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--days-ago` | 60 | How many days back to start |
| `--num-commits` | 30 | Number of commits to create |
| `--pattern` | daily | Frequency: daily, weekdays, sparse |
| `--branch` | git-metadata-study | Branch name |

## 📊 Patterns Explained

- **daily**: One commit every day
- **weekdays**: Only Monday-Friday (skips weekends)
- **sparse**: Every 3-4 days (irregular pattern)

## 🔍 What to Observe on GitHub

1. **Contribution Graph**: Do commits appear on the correct dates?
2. **Activity Feed**: How are commits displayed chronologically?
3. **Commit Count**: Does it match your expectations?
4. **Timezone**: Are timestamps handled correctly?

## ⚠️ Important Notes

- ✅ This is a **learning exercise**
- ✅ Use only on **personal repositories**
- ✅ All commits are **authentic Git objects**
- ✅ Fully **reversible** by deleting the branch
- ❌ Not for professional portfolios
- ❌ Not for shared repositories

## 📚 Documentation

- Full guide: `git-metadata-study/USAGE.md`
- Study overview: `git-metadata-study/README.md`
- Scripts: `git-metadata-study/scripts/`

## 🆘 Troubleshooting

**Script won't run?**
```bash
chmod +x git-metadata-study/scripts/*.py
python3 git-metadata-study/scripts/create_study_commits.py
```

**Branch exists?**
- Script will prompt to delete and recreate

**Want to start over?**
```bash
git checkout main
git branch -D git-metadata-study
python3 git-metadata-study/scripts/create_study_commits.py
```

---
**Created**: 2026-01-20 | **Author**: sunny-chandel
