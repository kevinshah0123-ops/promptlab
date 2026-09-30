def test_generate_mock_response():
    response = generate_mock_response("Test prompt")
    assert response == "Mock response for: Test prompt"
