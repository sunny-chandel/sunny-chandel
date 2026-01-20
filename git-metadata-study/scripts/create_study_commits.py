#!/usr/bin/env python3
"""
Git Commit Metadata Study - Commit Generation Script

This script creates a series of commits with controlled timestamps to study
how Git metadata influences activity visualization on platforms like GitHub.

Educational Purpose:
- Learn how Git stores author and committer timestamps
- Observe how platforms compute contribution graphs
- Understand the Git object model and temporal metadata

Safety Features:
- Creates commits on a dedicated study branch
- All commits contain real, valid file changes
- Fully reversible (branch can be deleted)
- Operates only on personal repository
- Uses standard Git mechanisms only

Author: sunny-chandel
Date: 2026-01-20
"""

import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Tuple
import json


class GitMetadataStudy:
    """Manages the creation of timestamped commits for learning purposes."""
    
    def __init__(self, repo_path: str, branch_name: str = "git-metadata-study"):
        self.repo_path = Path(repo_path)
        self.branch_name = branch_name
        self.study_dir = self.repo_path / "git-metadata-study"
        self.notes_dir = self.study_dir / "learning-notes"
        self.analysis_dir = self.study_dir / "analysis"
        
    def setup_directories(self):
        """Create necessary directory structure."""
        self.notes_dir.mkdir(parents=True, exist_ok=True)
        self.analysis_dir.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory structure in {self.study_dir}")
        
    def create_study_branch(self):
        """Create and checkout the study branch."""
        try:
            # Check if branch already exists
            result = subprocess.run(
                ["git", "rev-parse", "--verify", self.branch_name],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"⚠️  Branch '{self.branch_name}' already exists")
                response = input("Delete and recreate? (y/n): ")
                if response.lower() == 'y':
                    subprocess.run(["git", "checkout", "main"], cwd=self.repo_path, check=True)
                    subprocess.run(["git", "branch", "-D", self.branch_name], cwd=self.repo_path, check=True)
                    print(f"✓ Deleted existing branch '{self.branch_name}'")
                else:
                    print("Exiting...")
                    return False
            
            # Create new branch
            subprocess.run(["git", "checkout", "-b", self.branch_name], cwd=self.repo_path, check=True)
            print(f"✓ Created and checked out branch '{self.branch_name}'")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"✗ Error creating branch: {e}")
            return False
    
    def generate_learning_note(self, date: datetime, day_number: int) -> str:
        """Generate a learning note for a specific day."""
        topics = [
            "Git object model and SHA-1 hashing",
            "Author vs Committer timestamps in Git",
            "How GitHub computes contribution graphs",
            "Git's internal storage of temporal metadata",
            "Understanding git commit --date flag",
            "Exploring GIT_AUTHOR_DATE environment variable",
            "How platforms visualize repository activity",
            "Git commit object structure and fields",
            "Timestamp formats in Git (RFC 2822, ISO 8601)",
            "The role of timezone in Git commits",
            "Git reflog and timestamp tracking",
            "How git log uses temporal information",
            "Understanding commit ancestry and dates",
            "Git's handling of clock skew",
            "Platform-specific activity algorithms",
        ]
        
        topic = topics[day_number % len(topics)]
        
        note = f"""# Learning Note - Day {day_number}
**Date**: {date.strftime('%Y-%m-%d')}
**Topic**: {topic}

## Key Learnings
- Studied how Git internally stores commit metadata
- Explored the difference between author and committer timestamps
- Observed how platforms parse and visualize this data

## Technical Details
- Author Date: {date.isoformat()}
- Timezone: {date.strftime('%z')}
- Git Object Type: commit

## Observations
This commit is part of a controlled learning exercise to understand
how Git's temporal metadata influences activity visualization on
source-control platforms.

## References
- Git Documentation: git-commit(1)
- Pro Git Book: Chapter 10 - Git Internals
- GitHub API: Contribution Activity

---
*This is an educational exercise, not a representation of actual work.*
"""
        return note
    
    def create_commit_with_date(
        self, 
        date: datetime, 
        message: str, 
        files_to_add: List[str]
    ) -> bool:
        """Create a commit with a specific timestamp."""
        try:
            # Format date for Git (RFC 2822 format)
            date_str = date.strftime('%a, %d %b %Y %H:%M:%S %z')
            
            # Stage files
            for file_path in files_to_add:
                subprocess.run(
                    ["git", "add", file_path],
                    cwd=self.repo_path,
                    check=True
                )
            
            # Create commit with custom date
            env = os.environ.copy()
            env['GIT_AUTHOR_DATE'] = date_str
            env['GIT_COMMITTER_DATE'] = date_str
            
            subprocess.run(
                ["git", "commit", "-m", message],
                cwd=self.repo_path,
                env=env,
                check=True
            )
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"✗ Error creating commit: {e}")
            return False
    
    def generate_commit_schedule(
        self, 
        start_date: datetime, 
        num_days: int,
        pattern: str = "daily"
    ) -> List[Tuple[datetime, int]]:
        """
        Generate a schedule of commit dates.
        
        Args:
            start_date: Starting date for commits
            num_days: Number of days to span
            pattern: Commit pattern ('daily', 'weekdays', 'sparse')
        
        Returns:
            List of (date, day_number) tuples
        """
        schedule = []
        
        if pattern == "daily":
            # One commit per day
            for i in range(num_days):
                commit_date = start_date + timedelta(days=i)
                schedule.append((commit_date, i + 1))
                
        elif pattern == "weekdays":
            # Only weekdays (Mon-Fri)
            day_count = 0
            current_date = start_date
            while day_count < num_days:
                if current_date.weekday() < 5:  # Monday = 0, Friday = 4
                    schedule.append((current_date, day_count + 1))
                    day_count += 1
                current_date += timedelta(days=1)
                
        elif pattern == "sparse":
            # Every 3-4 days with some randomness
            import random
            day_count = 0
            current_date = start_date
            while day_count < num_days:
                schedule.append((current_date, day_count + 1))
                day_count += 1
                current_date += timedelta(days=random.randint(3, 4))
        
        return schedule
    
    def run_study(
        self, 
        start_date: datetime, 
        num_commits: int = 30,
        pattern: str = "daily"
    ):
        """
        Execute the complete study.
        
        Args:
            start_date: When to start the commit history
            num_commits: Number of commits to create
            pattern: Commit frequency pattern
        """
        print("\n" + "="*60)
        print("Git Commit Metadata Study - Starting")
        print("="*60 + "\n")
        
        # Setup
        print("📁 Setting up directory structure...")
        self.setup_directories()
        
        print("\n🌿 Creating study branch...")
        if not self.create_study_branch():
            return
        
        # Generate commit schedule
        print(f"\n📅 Generating commit schedule ({pattern} pattern)...")
        schedule = self.generate_commit_schedule(start_date, num_commits, pattern)
        print(f"✓ Scheduled {len(schedule)} commits from {schedule[0][0].date()} to {schedule[-1][0].date()}")
        
        # Create commits
        print("\n📝 Creating commits with timestamped learning notes...")
        success_count = 0
        
        for commit_date, day_number in schedule:
            # Generate learning note
            note_content = self.generate_learning_note(commit_date, day_number)
            note_filename = f"day-{day_number:03d}-{commit_date.strftime('%Y-%m-%d')}.md"
            note_path = self.notes_dir / note_filename
            
            # Write note file
            note_path.write_text(note_content)
            
            # Create commit
            commit_message = f"Learning Day {day_number}: Git metadata study ({commit_date.strftime('%Y-%m-%d')})"
            
            if self.create_commit_with_date(
                commit_date,
                commit_message,
                [str(note_path.relative_to(self.repo_path))]
            ):
                success_count += 1
                print(f"  ✓ Day {day_number:3d}: {commit_date.strftime('%Y-%m-%d')} - {note_filename}")
            else:
                print(f"  ✗ Day {day_number:3d}: Failed")
        
        # Create summary
        self.create_study_summary(schedule, success_count)
        
        print(f"\n✅ Study complete: {success_count}/{len(schedule)} commits created")
        print(f"\n📊 Next steps:")
        print(f"  1. Review commits: git log --oneline --graph")
        print(f"  2. Push to GitHub: git push origin {self.branch_name}")
        print(f"  3. Observe activity visualization on GitHub")
        print(f"  4. Document findings in analysis/observations.md")
        print(f"\n🔄 To reverse: git checkout main && git branch -D {self.branch_name}")
        print("="*60 + "\n")
    
    def create_study_summary(self, schedule: List[Tuple[datetime, int]], success_count: int):
        """Create a summary document of the study."""
        summary_path = self.analysis_dir / "study-summary.json"
        
        summary = {
            "study_name": "Git Commit Metadata Learning Exercise",
            "created_at": datetime.now().isoformat(),
            "repository": "sunny-chandel/sunny-chandel",
            "branch": self.branch_name,
            "total_commits": len(schedule),
            "successful_commits": success_count,
            "date_range": {
                "start": schedule[0][0].isoformat() if schedule else None,
                "end": schedule[-1][0].isoformat() if schedule else None,
            },
            "purpose": "Educational study of Git temporal metadata and platform visualization",
            "disclaimer": "This is a learning exercise, not a representation of actual work",
        }
        
        summary_path.write_text(json.dumps(summary, indent=2))
        
        # Also create markdown observations template
        observations_path = self.analysis_dir / "observations.md"
        observations_content = """# Study Observations

## Objective
Document observations about how Git commit metadata influences activity visualization on GitHub.

## Methodology
- Created commits with controlled timestamps using `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE`
- Each commit contains a valid learning note file
- All commits authored under verified account

## Observations

### GitHub Contribution Graph
- [ ] How does GitHub display the timestamped commits?
- [ ] Does the contribution graph reflect the author date or committer date?
- [ ] How are timezone differences handled?

### Activity Timeline
- [ ] How does the activity feed show these commits?
- [ ] Are there any differences in visualization compared to "natural" commits?

### Technical Insights
- [ ] What did I learn about Git's internal timestamp handling?
- [ ] How do platforms parse and interpret commit metadata?

## Key Learnings
*Document your findings here...*

## Conclusions
*Summarize what this exercise taught you about Git and platform visualization...*

---
**Study Date**: 2026-01-20
**Author**: sunny-chandel
"""
        observations_path.write_text(observations_content)


def main():
    """Main entry point for the study script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Git Commit Metadata Study - Educational Exercise",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create 30 daily commits starting 60 days ago
  python create_study_commits.py --days-ago 60 --num-commits 30 --pattern daily
  
  # Create 20 weekday commits starting 90 days ago
  python create_study_commits.py --days-ago 90 --num-commits 20 --pattern weekdays
  
  # Create 15 sparse commits starting 120 days ago
  python create_study_commits.py --days-ago 120 --num-commits 15 --pattern sparse
        """
    )
    
    parser.add_argument(
        "--repo-path",
        default="/Users/sunny.chandel/sunny-chandel",
        help="Path to Git repository (default: current repo)"
    )
    
    parser.add_argument(
        "--days-ago",
        type=int,
        default=60,
        help="How many days ago to start the commit history (default: 60)"
    )
    
    parser.add_argument(
        "--num-commits",
        type=int,
        default=30,
        help="Number of commits to create (default: 30)"
    )
    
    parser.add_argument(
        "--pattern",
        choices=["daily", "weekdays", "sparse"],
        default="daily",
        help="Commit frequency pattern (default: daily)"
    )
    
    parser.add_argument(
        "--branch",
        default="git-metadata-study",
        help="Branch name for the study (default: git-metadata-study)"
    )
    
    args = parser.parse_args()
    
    # Calculate start date
    start_date = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
    start_date = start_date - timedelta(days=args.days_ago)
    
    # Display study parameters
    print("\n" + "="*60)
    print("Git Commit Metadata Study - Configuration")
    print("="*60)
    print(f"Repository: {args.repo_path}")
    print(f"Branch: {args.branch}")
    print(f"Start Date: {start_date.strftime('%Y-%m-%d')}")
    print(f"Number of Commits: {args.num_commits}")
    print(f"Pattern: {args.pattern}")
    print("="*60)
    
    response = input("\n⚠️  This will create a new branch with timestamped commits. Continue? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    # Run the study
    study = GitMetadataStudy(args.repo_path, args.branch)
    study.run_study(start_date, args.num_commits, args.pattern)


if __name__ == "__main__":
    main()
