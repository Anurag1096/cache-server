from fastapi.testclient import TestClient
# Assuming your FastAPI app instance is named 'app' in 'main.py'
from main import app  
from unittest.mock import AsyncMock,patch
import pytest
from cache import set_cache,get_cache,clear_cache

client=TestClient(app)

@pytest.fixture(autouse=True)
def clear_cache_before_test():
    clear_cache()    



def test_proxy_url():
    with patch("httpx.AsyncClient.request", new_callable=AsyncMock) as mock_async:
        
        mock_async.return_value.status_code = 200
        mock_async.return_value.content = b'{"data": "mocked"}'
        mock_async.return_value.headers = {"content-type": "application/json"}
        
        response1 = client.get("/products")
        assert response1.status_code == 200
        assert response1.json() == {"data": "mocked"}
        assert response1.headers["X-Cache"] == "MISS"
        assert mock_async.await_count == 1

        # Second call - should return cached version
        response2 = client.get("/products")
        assert response2.status_code == 200
        assert response2.json() == {"data": "mocked"}
        assert response2.headers["X-Cache"] == "HIT"
        assert mock_async.await_count == 1 
        