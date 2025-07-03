# Contribution Guidelines

Welcome! This document describes how to contribute to the project, our branching strategy, issue management rules, and GitLab integrations.

---

## 📦 Participation Rules

- Be respectful and collaborative.
- Discuss major changes in an issue before opening a Merge Request (MR).
- Keep PRs small and focused.

---

## 🌿 Branching Policy

We use **GitFlow-lite**:
- `main` – Production-ready code.
- `develop` – Latest development changes.
- Feature branches:
  - Named as: `feature/<issue-id>-short-description`
  - Example: `feature/42-login-api`
- Bugfix branches:
  - Named as: `bugfix/<issue-id>-short-description`
  - Example: `bugfix/17-fix-null-error`
- Hotfix branches:
  - Named as: `hotfix/<issue-id>-short-description`
- Release branches:
  - Named as: `release/<version>`

✅ All branches start from `develop` unless fixing production (`hotfix` → from `main`).

---

## 🔗 GitLab Integration

### Issues
- Open an issue for every feature, enhancement, or bug.
- Use labels:
  - `bug`, `feature`, `enhancement`, `documentation`
- Link issues in MRs using `Closes #<issue-id>`.

### Merge Requests
- Branch → MR → `develop`
- MR title format: `[<Type>] <short description>`
  - Example: `[Feature] Add user login API`
- Write a clear MR description:
  - What was done
  - Why
  - How to test
- Enable `Squash commits` before merge.

---

## 🚨 Rules for Opening Issues

When opening an issue:
- Title: concise and descriptive.
- Description: include:
  - Steps to reproduce (for bugs)
  - Expected behavior
  - Additional context/screenshots
- Assign priority: `low`, `medium`, `high`
- Add assignees and labels where appropriate.

---

## 📦 Initial Setup for New Developers

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone git@gitlab.com:<your-username>/<repo>.git
