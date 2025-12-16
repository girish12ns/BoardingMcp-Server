"""Tests for create_business_profile POST endpoint via MCP."""

import pytest
import pytest_asyncio
from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport


@pytest_asyncio.fixture
async def main_mcp_client():
    """Initialize MCP client for onboarding server."""
    async with Client("mcp_servers/onboardserver.py") as mcp_client:
        yield mcp_client


@pytest.mark.parametrize(
    "display_name,email,company,contact,timezone,currency,company_size,password",
    [
        (
            "CallHippo Support",
            "support@callhippo.com",
            "CallHippo",
            "918116856153",
            "Asia/Calcutta GMT+05:30",
            "INR",
            "10 - 20",
            "somerandompassword"
        ),
        (
            "TechStartup Inc",
            "hello@techstartup.com",
            "TechStartup",
            "919876543210",
            "Asia/Kolkata",
            "INR",
            "5 - 10",
            "anotherpassword123"
        ),
    ],
)
@pytest.mark.asyncio
async def test_create_business_profile(
    display_name: str,
    email: str,
    company: str,
    contact: str,
    timezone: str,
    currency: str,
    company_size: str,
    password: str,
    main_mcp_client: Client[FastMCPTransport],
):
    """Test creating a new business profile."""
    result = await main_mcp_client.call_tool(
        "create_business_profile",
        arguments={
            "display_name": display_name,
            "email": email,
            "company": company,
            "contact": contact,
            "timezone": timezone,
            "currency": currency,
            "company_size": company_size,
            "password": password,
        },
    )
    print(f"\n=== Create Business Profile: {display_name} ===")
    print(result.data)

    # Add assertions
    assert result.data is not None