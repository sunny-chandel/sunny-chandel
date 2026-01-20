#!/usr/bin/env python3
"""
Git Metadata Study - Analysis and Visualization Tools

This script provides tools to analyze the timestamped commits and
compare them with the platform's activity visualization.

Author: sunny-chandel
Date: 2026-01-20
"""

import subprocess
from datetime import datetime
from pathlib import Path
from typing import List, Dict
import json


class CommitAnalyzer:
    """Analyzes Git commits and their metadata."""
    
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
    
    def get_commit_metadata(self, branch: str = "git-metadata-study") -> List[Dict]:
        """Extract metadata from all commits in the study branch."""
        try:
            # Get commit information
            result = subprocess.run(
                [
                    "git", "log", branch,
                    "--format=%H|%an|%ae|%ai|%cn|%ce|%ci|%s"
                ],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            commits = []
            for line in result.stdout.strip().split('\n'):
                if not line:
                    continue
                    
                parts = line.split('|')
                if len(parts) >= 8:
                    commits.append({
                        'hash': parts[0],
                        'author_name': parts[1],
                        'author_email': parts[2],
                        'author_date': parts[3],
                        'committer_name': parts[4],
                        'committer_email': parts[5],
                        'committer_date': parts[6],
                        'subject': parts[7]
                    })
            
            return commits
            
        except subprocess.CalledProcessError as e:
            print(f"Error getting commit metadata: {e}")
            return []
    
    def analyze_date_distribution(self, commits: List[Dict]) -> Dict:
        """Analyze the distribution of commit dates."""
        if not commits:
            return {}
        
        dates = [datetime.fromisoformat(c['author_date'].replace(' +0530', '+05:30')) 
                 for c in commits]
        
        return {
            'total_commits': len(commits),
            'earliest_date': min(dates).isoformat(),
            'latest_date': max(dates).isoformat(),
            'date_range_days': (max(dates) - min(dates)).days,
            'commits_by_weekday': self._count_by_weekday(dates),
            'commits_by_month': self._count_by_month(dates),
        }
    
    def _count_by_weekday(self, dates: List[datetime]) -> Dict[str, int]:
        """Count commits by day of week."""
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        counts = {day: 0 for day in weekdays}
        
        for date in dates:
            counts[weekdays[date.weekday()]] += 1
        
        return counts
    
    def _count_by_month(self, dates: List[datetime]) -> Dict[str, int]:
        """Count commits by month."""
        counts = {}
        
        for date in dates:
            month_key = date.strftime('%Y-%m')
            counts[month_key] = counts.get(month_key, 0) + 1
        
        return counts
    
    def generate_report(self, output_path: Path):
        """Generate a comprehensive analysis report."""
        commits = self.get_commit_metadata()
        
        if not commits:
            print("No commits found in study branch")
            return
        
        analysis = self.analyze_date_distribution(commits)
        
        report = f"""# Git Metadata Study - Analysis Report

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary Statistics

- **Total Commits**: {analysis['total_commits']}
- **Date Range**: {analysis['earliest_date']} to {analysis['latest_date']}
- **Span**: {analysis['date_range_days']} days

## Commit Distribution by Weekday

"""
        
        for day, count in analysis['commits_by_weekday'].items():
            bar = '█' * count
            report += f"- **{day}**: {count:2d} {bar}\n"
        
        report += "\n## Commit Distribution by Month\n\n"
        
        for month, count in sorted(analysis['commits_by_month'].items()):
            bar = '█' * count
            report += f"- **{month}**: {count:2d} {bar}\n"
        
        report += f"""

## Sample Commits

"""
        
        for i, commit in enumerate(commits[:5], 1):
            report += f"""### Commit {i}
- **Hash**: `{commit['hash'][:8]}`
- **Author Date**: {commit['author_date']}
- **Subject**: {commit['subject']}

"""
        
        report += """
## Next Steps

1. **Push to GitHub**: `git push origin git-metadata-study`
2. **View on GitHub**: Check your profile's contribution graph
3. **Compare**: Note how GitHub visualizes these timestamped commits
4. **Document**: Record observations in `observations.md`

## Platform Visualization Checklist

- [ ] Contribution graph shows commits on correct dates
- [ ] Activity feed displays commits chronologically
- [ ] Commit count matches expected values
- [ ] Timezone handling is correct
- [ ] No anomalies or unexpected behavior

---
*This analysis is part of an educational study of Git metadata and platform visualization.*
"""
        
        output_path.write_text(report)
        print(f"✓ Report generated: {output_path}")
        
        # Also save JSON data
        json_path = output_path.with_suffix('.json')
        json_data = {
            'generated_at': datetime.now().isoformat(),
            'analysis': analysis,
            'commits': commits[:10]  # First 10 commits
        }
        json_path.write_text(json.dumps(json_data, indent=2))
        print(f"✓ JSON data saved: {json_path}")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Analyze Git metadata study commits")
    parser.add_argument(
        "--repo-path",
        default="/Users/sunny.chandel/sunny-chandel",
        help="Path to Git repository"
    )
    
    args = parser.parse_args()
    
    analyzer = CommitAnalyzer(args.repo_path)
    output_path = Path(args.repo_path) / "git-metadata-study" / "analysis" / "analysis-report.md"
    
    print("\n📊 Analyzing Git metadata study commits...\n")
    analyzer.generate_report(output_path)
    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()
