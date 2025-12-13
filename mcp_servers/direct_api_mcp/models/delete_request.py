"""
Pydantic models for MCP tool request validation for DELETE requests.
"""
from pydantic import BaseModel, Field, field_validator


class TemplateNameRequest(BaseModel):
    """Model for requests that require a template_name."""
    
    template_name: str = Field(
        ...,
        description="The template name to delete",
        min_length=1,
        examples=["my_template", "welcome_message"]
    )
    
    @field_validator("template_name")
    @classmethod
    def validate_template_name(cls, v: str) -> str:
        """Validate and sanitize template_name."""
        v = v.strip()
        if not v:
            raise ValueError("template_name cannot be empty or whitespace")
        return v


class FlowIdRequest(BaseModel):
    """Model for requests that require a flow_id."""
    
    flow_id: str = Field(
        ...,
        description="The flow ID to delete",
        min_length=1,
        examples=["flow_abc123", "12345678"]
    )
    
    @field_validator("flow_id")
    @classmethod
    def validate_flow_id(cls, v: str) -> str:
        """Validate and sanitize flow_id."""
        v = v.strip()
        if not v:
            raise ValueError("flow_id cannot be empty or whitespace")
        return v