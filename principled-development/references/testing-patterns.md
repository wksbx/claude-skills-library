# Testing Patterns Reference

## TDD Red-Green-Refactor Cycle

```
┌─────────────────────────────────────────────┐
│  RED: Write failing test                    │
│  ↓                                          │
│  GREEN: Write minimum code to pass          │
│  ↓                                          │
│  REFACTOR: Improve code, keep tests green   │
│  ↓                                          │
│  (repeat)                                   │
└─────────────────────────────────────────────┘
```

## Test Structure: Arrange-Act-Assert

```python
def test_user_can_update_email():
    # Arrange - Set up preconditions
    user = User(email="old@example.com")
    
    # Act - Perform the action
    user.update_email("new@example.com")
    
    # Assert - Verify outcomes
    assert user.email == "new@example.com"
```

## Unit Test Patterns

### Testing Pure Functions
```python
def test_calculate_total_with_discount():
    result = calculate_total(items=[100, 50], discount=0.1)
    assert result == 135.0
```

### Testing Side Effects with Mocks
```python
def test_send_notification_calls_email_service(mocker):
    mock_email = mocker.patch('services.email.send')
    notify_user(user_id=1, message="Hello")
    mock_email.assert_called_once_with(user_id=1, message="Hello")
```

### Testing Exceptions
```python
def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

## E2E Test Patterns

### Happy Path Testing
```python
def test_user_registration_flow(client):
    # Navigate to registration
    response = client.get("/register")
    assert response.status_code == 200
    
    # Submit registration form
    response = client.post("/register", data={
        "email": "test@example.com",
        "password": "SecurePass123"
    })
    assert response.status_code == 302  # Redirect
    
    # Verify user can log in
    response = client.post("/login", data={
        "email": "test@example.com",
        "password": "SecurePass123"
    })
    assert response.status_code == 200
    assert b"Welcome" in response.data
```

### Error State Testing
```python
def test_registration_with_invalid_email(client):
    response = client.post("/register", data={
        "email": "not-an-email",
        "password": "SecurePass123"
    })
    assert response.status_code == 400
    assert b"Invalid email" in response.data
```

### API Integration Testing
```python
def test_create_and_retrieve_resource(client, db):
    # Create
    create_response = client.post("/api/items", json={"name": "Test"})
    assert create_response.status_code == 201
    item_id = create_response.json["id"]
    
    # Retrieve
    get_response = client.get(f"/api/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json["name"] == "Test"
```

## Test Coverage Targets

| Test Type | Coverage Target | Focus |
|-----------|-----------------|-------|
| Unit | 80%+ lines | Logic, edge cases |
| Integration | Key paths | Service boundaries |
| E2E | Critical flows | User journeys |

## Test Naming Conventions

**Pattern:** `test_<action>_<expected_result>_<condition>`

```python
# Good names - descriptive and specific
def test_login_succeeds_with_valid_credentials(): ...
def test_login_fails_when_password_incorrect(): ...
def test_cart_total_includes_tax_when_taxable(): ...

# Bad names - vague and uninformative
def test_login(): ...
def test_it_works(): ...
def test_1(): ...
```

## Testing Checklist by Feature Type

### CRUD Operations
- [ ] Create with valid data
- [ ] Create with invalid data (validation errors)
- [ ] Read existing item
- [ ] Read non-existent item (404)
- [ ] Update existing item
- [ ] Update non-existent item
- [ ] Delete existing item
- [ ] Delete non-existent item

### Authentication
- [ ] Login with valid credentials
- [ ] Login with invalid credentials
- [ ] Session expiration
- [ ] Password reset flow
- [ ] Protected route access

### External API Integration
- [ ] Successful response handling
- [ ] Timeout handling
- [ ] Error response handling
- [ ] Retry logic
- [ ] Rate limiting
