# Branching Strategy & Repository Management

This document outlines the branching strategy and repository management workflow for the Azure Functions project.

## Repository Structure

### Primary Repositories

1. **🔵 Azure Repository (Primary Development)**
   - **Purpose**: Main development and collaboration hub
   - **Access**: Organization members only
   - **Branches**: `main`, `release`, feature branches
   - **Usage**: All development work, code reviews, testing

2. **🟢 GitHub Repository (Mirror/Backup)**
   - **Purpose**: Public mirror and backup
   - **Access**: Public repository
   - **Branches**: `main`, `release` (synced from Azure repo)
   - **Usage**: Read-only, documentation, public access

### Repository Relationship
```
Azure Repo (Private)          GitHub Repo (Public)
├── main                 ──►  ├── main
├── release              ──►  ├── release
├── feature/NA/1234           └── (sync only)
└── feature/JS/5678
```

## Branching Convention

### Branch Naming Format
All feature branches must follow this naming convention:
```
{InitialsOfDeveloper}/{UserStoryNumber}
```

### Examples
- `NA/1234` - Developer with initials "NA" working on user story #1234
- `JS/5678` - Developer with initials "JS" working on user story #5678
- `MK/9012` - Developer with initials "MK" working on user story #9012

### Branch Types

#### 1. Main Branch (`main`)
- **Purpose**: Integration branch for completed features
- **Protection**: Protected, requires PR and code review
- **Source**: Merged from feature branches after code review
- **Target**: Merges into `release` after testing

#### 2. Release Branch (`release`)
- **Purpose**: Production-ready code
- **Protection**: Highly protected, only main can merge into it
- **Source**: Merged from `main` after thorough testing
- **Deployment**: Used for production deployments

#### 3. Feature Branches (`{Initials}/{StoryNumber}`)
- **Purpose**: Individual feature development
- **Source**: Branched from `main`
- **Target**: Merged back into `main` via PR
- **Lifecycle**: Created → Developed → Code Review → Merged → Deleted

## Development Workflow

### 1. Starting New Work

```bash
# 1. Ensure you're on the latest main branch
git checkout main
git pull origin main

# 2. Create your feature branch
git checkout -b NA/1234

# 3. Start development
# Make your changes, commits, etc.
```

### 2. Development Process

```bash
# Regular commits during development
git add .
git commit -m "feat(test-functions): implement hello function validation"

# Push your branch to Azure repo
git push origin NA/1234
```

### 3. Code Review & Merge Process

#### Step 1: Create Pull Request (Azure Repo)
1. Push your feature branch to Azure repository
2. Create Pull Request: `NA/1234` → `main`
3. Add detailed description of changes
4. Request code review from team members

#### Step 2: Code Review Requirements
- ✅ At least 2 reviewers must approve
- ✅ All automated tests must pass
- ✅ No merge conflicts
- ✅ Code follows project conventions
- ✅ Documentation updated if needed

#### Step 3: Merge to Main
- Only after approval, branch is merged into `main`
- Feature branch is deleted after merge
- `main` branch is updated with new feature

### 4. Release Process

#### Step 1: Testing Phase
```bash
# After features are merged to main
git checkout main
git pull origin main

# Thorough testing of main branch
# - Unit tests
# - Integration tests  
# - Manual testing
# - Performance testing
```

#### Step 2: Release Merge (Azure Repo Only)
```bash
# Only after successful testing
git checkout release
git pull origin release
git merge main
git push origin release
```

#### Step 3: GitHub Sync
```bash
# Sync Azure repo with GitHub repo
git push github main
git push github release
```

## Repository Access & Restrictions

### ❌ Prohibited Actions on GitHub Repository
- **No Direct Commits**: Direct commits to GitHub repo are not allowed
- **No Pull Requests**: GitHub PRs will not be reviewed or merged  
- **No Branch Creation**: Feature branches should not be created on GitHub
- **Read-Only Access**: GitHub repo is for reference and backup only

### ✅ Allowed Actions

#### Azure Repository
- Create feature branches following naming convention
- Make commits and push to feature branches
- Create Pull Requests for code review
- Participate in code reviews
- Merge approved PRs (with permissions)

#### GitHub Repository  
- View code and documentation
- Clone for reference
- Report issues (if enabled)
- View project history

## Commit Message Guidelines

### Format
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test additions or updates
- `chore`: Maintenance tasks

### Examples
```bash
feat(cite-functions): add citation validation endpoint
fix(test-functions): resolve parameter validation issue
docs(readme): update module creation instructions
refactor(logger): improve error handling and formatting
```

## Branch Protection Rules

### Main Branch Protection
- ✅ Require pull request reviews (minimum 2)
- ✅ Dismiss stale reviews when new commits are pushed
- ✅ Require status checks to pass
- ✅ Require branches to be up to date before merging
- ✅ Include administrators in restrictions

### Release Branch Protection  
- ✅ Require pull request reviews (minimum 3)
- ✅ Require status checks to pass
- ✅ Restrict who can merge (release managers only)
- ✅ Include administrators in restrictions

## Quick Reference Commands

### Starting New Feature
```bash
git checkout main
git pull origin main
git checkout -b {YourInitials}/{StoryNumber}
```

### Daily Development
```bash
git add .
git commit -m "feat(module): description of changes"
git push origin {YourInitials}/{StoryNumber}
```

### Staying Updated
```bash
git checkout main
git pull origin main
git checkout {YourInitials}/{StoryNumber}
git rebase main  # or git merge main
```

### After PR Approval
```bash
git checkout main
git pull origin main
git branch -d {YourInitials}/{StoryNumber}  # Delete local branch
```

## Troubleshooting

### Common Issues

#### 1. Branch Behind Main
```bash
git checkout {YourInitials}/{StoryNumber}
git rebase main
# Resolve conflicts if any
git push origin {YourInitials}/{StoryNumber} --force-with-lease
```

#### 2. Merge Conflicts
```bash
git checkout main
git pull origin main
git checkout {YourInitials}/{StoryNumber}
git merge main
# Resolve conflicts in VS Code
git commit
git push origin {YourInitials}/{StoryNumber}
```

#### 3. Accidental Commit to Main
```bash
# Never push directly to main
# If you committed locally to main:
git reset HEAD~1  # Undo last commit
git checkout -b {YourInitials}/{StoryNumber}
git commit -m "your commit message"
```

## Contact & Support

For questions about branching strategy or repository access:
- **Team Lead**: [Contact Information]
- **DevOps Team**: [Contact Information]  
- **Documentation**: This README and main project README

---

**Remember**: All development work happens in Azure repository. GitHub is read-only mirror for backup and public access.
