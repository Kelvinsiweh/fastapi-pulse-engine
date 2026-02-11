import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_timing_header():
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as c:
        res = await c.get('/health')
        assert 'X-Response-Time-Ms' in res.headers
