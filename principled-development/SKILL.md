---
name: principled-development
description: Enforces software engineering best practices for all code tasks. Use for ANY code writing, refactoring, debugging, or feature implementation. Applies TDD (write tests first), E2E testing, SOLID principles, KISS, DRY, and SOTA research. Triggers on requests to write code, implement features, fix bugs, refactor, or build applications.
---

# Principled Development

Apply these principles to ALL coding tasks. The workflow is mandatory, not optional.

## Required Workflow

For every code task, follow this sequence:

1. **Research SOTA** → Search current best practices for the problem domain
2. **Write tests first** → Define success criteria as executable tests
3. **Implement minimally** → Write simplest code that passes tests
4. **Refactor** → Apply SOLID/DRY while keeping tests green
5. **Add E2E tests** → Verify complete user flows work

## Principle Quick Reference

| Principle | Rule | Violation Check |
|-----------|------|-----------------|
| **TDD** | Tests before code | No test file = blocked |
| **E2E** | Test full user flows | Missing integration tests = incomplete |
| **SOLID** | See [references/solid.md](references/solid.md) | Class doing multiple things = refactor |
| **KISS** | Simplest working solution | Can it be simpler? = simplify |
| **DRY** | Extract duplicated logic | Same code twice = extract |
| **SOTA** | Research before implementing | No search = skipped step |

## TDD Workflow

```
1. Write failing test for desired behavior
2. Run test → confirm it fails (red)
3. Write minimum code to pass
4. Run test → confirm it passes (green)
5. Refactor while keeping green
6. Repeat for next behavior
```

**Test file naming:** `test_<module>.py` or `<module>.test.ts`

**Example - before writing any function:**
```python
# test_calculator.py - WRITE THIS FIRST
def test_add_returns_sum():
    assert add(2, 3) == 5

def test_add_handles_negatives():
    assert add(-1, 1) == 0
```

Then implement:
```python
# calculator.py - WRITE THIS SECOND
def add(a: int, b: int) -> int:
    return a + b
```

## SOTA Research Step

Before implementing any feature:

1. Search for current best practices: `"<problem> best practices 2024"`
2. Search for common pitfalls: `"<technology> antipatterns"`
3. Review top solutions and extract patterns
4. Document chosen approach and rationale

## E2E Testing Checklist

After unit tests pass, add E2E tests covering:
- [ ] Happy path (typical user flow)
- [ ] Edge cases (empty inputs, large data)
- [ ] Error handling (invalid inputs, failures)
- [ ] Integration points (APIs, databases)

## Decision Tree

```
New feature request?
├── Yes → Research SOTA → Write unit tests → Implement → Add E2E
└── Bug fix?
    ├── Yes → Write failing test reproducing bug → Fix → Verify E2E
    └── Refactoring?
        └── Yes → Ensure test coverage → Refactor → Run all tests
```

## Detailed References

For comprehensive guidance on each principle, see:
- [references/solid.md](references/solid.md) - SOLID principles with examples
- [references/testing-patterns.md](references/testing-patterns.md) - TDD and E2E patterns
