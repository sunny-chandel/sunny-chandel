# Git Metadata Study - Quick Start Guide

## Overview
This guide will walk you through the Git commit metadata learning exercise step by step.

## Prerequisites
- ✅ Git installed and configured
- ✅ Python 3.7+ installed
- ✅ Personal GitHub repository (sunny-chandel/sunny-chandel)
- ✅ Repository cloned locally

## Step-by-Step Instructions

### Step 1: Review the Study Plan

First, understand what this study does:
- Creates a dedicated branch (`git-metadata-study`)
- Generates commits with past timestamps
- Each commit contains a real learning note file
- All commits are authentic Git objects
- Fully reversible and transparent

### Step 2: Choose Your Study Parameters

Decide on:
- **Start date**: How far back to begin (e.g., 60 days ago)
- **Number of commits**: How many commits to create (e.g., 30)
- **Pattern**: Commit frequency
  - `daily`: One commit per day
  - `weekdays`: Only Monday-Friday
  - `sparse`: Every 3-4 days

### Step 3: Run the Study Script

```bash
# Navigate to your repository
cd /Users/sunny.chandel/sunny-chandel

# Make the script executable
chmod +x git-metadata-study/scripts/create_study_commits.py

# Run with default settings (30 daily commits starting 60 days ago)
python3 git-metadata-study/scripts/create_study_commits.py

# Or customize the parameters
python3 git-metadata-study/scripts/create_study_commits.py \
  --days-ago 90 \
  --num-commits 45 \
  --pattern weekdays
```

### Step 4: Review the Generated Commits

```bash
# View the commit history
git log --oneline --graph git-metadata-study

# View detailed commit information
git log git-metadata-study --format="%ai | %s" -10

# Check the learning notes
ls -la git-metadata-study/learning-notes/
```

### Step 5: Analyze the Commits

```bash
# Generate analysis report
python3 git-metadata-study/scripts/analyze_commits.py

# View the report
cat git-metadata-study/analysis/analysis-report.md
```

### Step 6: Push to GitHub (Optional)

```bash
# Push the study branch to GitHub
git push origin git-metadata-study
```

### Step 7: Observe Platform Visualization

1. Visit your GitHub profile: https://github.com/sunny-chandel
2. Check your contribution graph
3. View the repository activity
4. Compare with the analysis report

### Step 8: Document Your Findings

```bash
# Edit the observations file
nano git-metadata-study/analysis/observations.md

# Add your findings about:
# - How GitHub displays the commits
# - Contribution graph behavior
# - Activity timeline representation
# - Any insights about Git metadata
```

### Step 9: Clean Up (When Done)

```bash
# Switch back to main branch
git checkout main

# Delete the study branch locally
git branch -D git-metadata-study

# Delete from GitHub (if pushed)
git push origin --delete git-metadata-study
```

## Example Workflows

### Workflow 1: Quick Daily Study (30 days)
```bash
python3 git-metadata-study/scripts/create_study_commits.py \
  --days-ago 30 \
  --num-commits 30 \
  --pattern daily
```

### Workflow 2: Extended Weekday Study (3 months)
```bash
python3 git-metadata-study/scripts/create_study_commits.py \
  --days-ago 90 \
  --num-commits 60 \
  --pattern weekdays
```

### Workflow 3: Sparse Long-term Study (6 months)
```bash
python3 git-metadata-study/scripts/create_study_commits.py \
  --days-ago 180 \
  --num-commits 40 \
  --pattern sparse
```

## Understanding the Output

### Directory Structure After Running
```
git-metadata-study/
├── README.md                           # Study documentation
├── USAGE.md                            # This guide
├── learning-notes/                     # Daily learning notes
│   ├── day-001-2025-11-21.md
│   ├── day-002-2025-11-22.md
│   └── ...
├── scripts/                            # Automation scripts
│   ├── create_study_commits.py         # Main commit generator
│   └── analyze_commits.py              # Analysis tool
└── analysis/                           # Study results
    ├── study-summary.json              # Study metadata
    ├── observations.md                 # Your findings
    ├── analysis-report.md              # Generated report
    └── analysis-report.json            # Data export
```

### Commit Message Format
```
Learning Day 1: Git metadata study (2025-11-21)
Learning Day 2: Git metadata study (2025-11-22)
...
```

### Learning Note Format
Each commit includes a markdown file with:
- Date and topic
- Key learnings
- Technical details
- Observations
- References

## Safety Features

✅ **Isolated Branch**: All commits are on a separate branch  
✅ **No Main Branch Changes**: Your main branch remains untouched  
✅ **Reversible**: Can be completely removed by deleting the branch  
✅ **Authentic Commits**: All commits are real Git objects  
✅ **Valid Changes**: Each commit contains actual file content  
✅ **Transparent**: Clear documentation and commit messages  

## Troubleshooting

### Issue: "Branch already exists"
**Solution**: The script will prompt you to delete and recreate it.

### Issue: "Permission denied"
**Solution**: Make the script executable:
```bash
chmod +x git-metadata-study/scripts/*.py
```

### Issue: "Git not found"
**Solution**: Ensure Git is installed and in your PATH:
```bash
git --version
```

### Issue: "Python not found"
**Solution**: Use `python3` instead of `python`:
```bash
python3 --version
```

## Learning Objectives

By completing this study, you will understand:

1. **Git Internals**
   - How Git stores commit metadata
   - Difference between author and committer dates
   - Git object model and SHA-1 hashing

2. **Platform Behavior**
   - How GitHub computes contribution graphs
   - Activity visualization algorithms
   - Timezone handling in platforms

3. **Practical Skills**
   - Using `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE`
   - Creating commits with specific timestamps
   - Analyzing Git history programmatically

## Important Reminders

⚠️ **This is a learning exercise**
- Not a representation of actual work
- Not for use on shared repositories
- Not for professional portfolios
- Purely educational in nature

✅ **Best Practices**
- Only use on personal repositories
- Document your findings
- Share learnings with others
- Be transparent about the exercise

## Further Reading

- [Git Internals - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
- [Git Commit Documentation](https://git-scm.com/docs/git-commit)
- [GitHub API - Events](https://docs.github.com/en/rest/activity/events)
- [Understanding GitHub Contributions](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/viewing-contributions-on-your-profile)

## Support

If you encounter issues or have questions:
1. Check the troubleshooting section above
2. Review the script comments and documentation
3. Examine the generated analysis reports
4. Consult Git documentation

---

**Happy Learning!** 🎓

*Created: 2026-01-20*  
*Author: sunny-chandel*  
*Purpose: Educational exploration of Git metadata*
