"""
Pydantic models for MCP tool request validation.
"""

# GET Request Models
from .get_request import (
    TemplateIdRequest,
    UploadSessionIdRequest,
    FlowIdRequest as GetFlowIdRequest,
    PaymentConfigurationNameRequest,
)

# POST Request Models
from .post_request import (
    RegenerateTokenRequest,
    WabaAnalyticsRequest,
    HealthStatusRequest,
    SendMessageRequest,
    SendMarketingMessageRequest,
    MarkMessageReadRequest,
    CreateTemplateRequest,
    EditTemplateRequest,
    CompareTemplateRequest,
    UploadMediaRequest,
    GetMediaRequest,
    CreateMediaSessionRequest,
    UploadMediaToSessionRequest,
    CreateCatalogRequest,
    ConnectCatalogRequest,
    CreateProductRequest,
    UpdateWhatsappCommerceSettingsRequest,
    CreateQrCodeRequest,
    SetWhatsappBusinessEncryptionRequest,
    CreateFlowRequest,
    UploadFlowAssetsRequest,
    FlowIdRequest as PostFlowIdRequest,
    CreatePaymentConfigurationRequest,
    GeneratePaymentConfigurationOAuthLinkRequest,
)

# DELETE Request Models
from .delete_request import (
    TemplateNameRequest,
    FlowIdRequest as DeleteFlowIdRequest,
)

# PATCH Request Models
from .patch_request import (
    UpdateProfilePictureRequest,
    UpdateProfileRequest,
    UpdateQrCodeRequest,
    UpdateFlowRequest,
)

__all__ = [
    # GET
    "TemplateIdRequest",
    "UploadSessionIdRequest",
    "GetFlowIdRequest",
    "PaymentConfigurationNameRequest",
    # POST
    "RegenerateTokenRequest",
    "WabaAnalyticsRequest",
    "HealthStatusRequest",
    "SendMessageRequest",
    "SendMarketingMessageRequest",
    "MarkMessageReadRequest",
    "CreateTemplateRequest",
    "EditTemplateRequest",
    "CompareTemplateRequest",
    "UploadMediaRequest",
    "GetMediaRequest",
    "CreateMediaSessionRequest",
    "UploadMediaToSessionRequest",
    "CreateCatalogRequest",
    "ConnectCatalogRequest",
    "CreateProductRequest",
    "UpdateWhatsappCommerceSettingsRequest",
    "CreateQrCodeRequest",
    "SetWhatsappBusinessEncryptionRequest",
    "CreateFlowRequest",
    "UploadFlowAssetsRequest",
    "PostFlowIdRequest",
    "CreatePaymentConfigurationRequest",
    "GeneratePaymentConfigurationOAuthLinkRequest",
    # DELETE
    "TemplateNameRequest",
    "DeleteFlowIdRequest",
    # PATCH
    "UpdateProfilePictureRequest",
    "UpdateProfileRequest",
    "UpdateQrCodeRequest",
    "UpdateFlowRequest",
]