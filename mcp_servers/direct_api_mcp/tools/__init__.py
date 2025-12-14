from fastmcp import FastMCP

mcp = FastMCP(
    name="Direct_api_Server",
    instructions="""This is for conversation""",
    version="0.0.1"
)

from .direct_api import get_fb_verification_status, get_business_info, regenerate_jwt_bearer_token, get_waba_analytics, get_messaging_health_status
from .messages import send_message, send_marketing_lite_message, mark_message_as_read
from .templates import compare_template, edit_template, submit_whatsapp_template_message, get_templates, get_template_by_id, delete_wa_template_by_id
from .media import get_media_upload_session, upload_media, retrieve_media_by_id, create_upload_session, upload_media_to_session, delete_media_by_id
from .profile import get_profile, update_business_profile_picture, update_business_profile_details
from .phone_number import get_all_phone_numbers, get_display_name_status, get_single_phone_number
from .catalog import get_catalog, get_products, connect_catalog, create_catalog, create_product, disconnect_catalog
from .commerce import get_commerce_settings, show_hide_catalog
from .qr_codes_and_short_links import get_qr_codes, create_qr_code_and_short_link, update_qr_code
from .whatsp_business_encryption import get_whatsapp_business_encryption, set_business_public_key
from .flows import get_flows, get_flow_by_id, get_flow_assets, create_flow, update_flow_json, publish_flow, deprecate_flow, delete_flow, update_flow_metadata
from .whatsp_payments import get_payment_configurations, get_payment_configuration_by_name, create_payment_configuration, generate_payment_configuration_oauth_link

__all__ = [
    "mcp",
    # direct_api
    "get_fb_verification_status",
    "get_business_info",
    "regenerate_jwt_bearer_token",
    "get_waba_analytics",
    "get_messaging_health_status",
    # messages
    "send_message",
    "send_marketing_lite_message",
    "mark_message_as_read",
    # templates
    "compare_template",
    "edit_template",
    "submit_whatsapp_template_message",
    "get_templates",
    "get_template_by_id",
    "delete_wa_template_by_id",
    # media
    "get_media_upload_session",
    "upload_media",
    "retrieve_media_by_id",
    "create_upload_session",
    "upload_media_to_session",
    "delete_media_by_id",
    # profile
    "get_profile",
    "update_business_profile_picture",
    "update_business_profile_details",
    # phone_number
    "get_all_phone_numbers",
    "get_display_name_status",
    "get_single_phone_number",
    # catalog
    "get_catalog",
    "get_products",
    "connect_catalog",
    "create_catalog",
    "create_product",
    "disconnect_catalog",
    # commerce
    "get_commerce_settings",
    "show_hide_catalog",
    # qr_codes_and_short_links
    "get_qr_codes",
    "create_qr_code_and_short_link",
    "update_qr_code",
    # whatsp_business_encryption
    "get_whatsapp_business_encryption",
    "set_business_public_key",
    # flows
    "get_flows",
    "get_flow_by_id",
    "get_flow_assets",
    "create_flow",
    "update_flow_json",
    "publish_flow",
    "deprecate_flow",
    "delete_flow",
    "update_flow_metadata",
    # whatsp_payments
    "get_payment_configurations",
    "get_payment_configuration_by_name",
    "create_payment_configuration",
    "generate_payment_configuration_oauth_link",
]