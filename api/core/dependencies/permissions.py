from typing import Dict, List


ORG_PERMS = [
    "organization:delete", "organization:view", "organization:update", "organization:revoke-invite",
    "organization:invite-user", "organization:manage-members", "organization:view-members",
    "location:create", "location:update", "location:delete", "location:view", "contact_info:create",
    "contact_info:update", "contact_info:delete", "contact_info:view", "role:create",
    "role:update", "role:delete", "role:view", "organization:assign-role",
]

REPORT_PERMS = [
    "report:generate", "report:view", "report:export", "logs:view"
]

APIKEY_PERMS = [
    "apikey:create", "apikey:view", "apikey:delete"
]

FILE_PERMS = [
    "file:upload", "file:update", "file:delete", "file:view",
    "folder:create", "folder:update", "folder:delete", "folder:view",
]

EMAIL_TEMPLATE_PERMS = [
    "template:create", "template:update", "template:delete",
    "layout:create", "layout:update", "layout:delete",
    "email:create", "email:update", "email:delete",
    "email:receive", "email:send",
]

PRODUCT_AND_INVENTORY_PERMS = [
    "product:create", "product:update", "product:delete",
    "inventory:create", "inventory:update", "inventory:delete",
]

CATEGORY_PERMS = [
    "category:create", "category:update", "category:delete",
    "category:attach", "category:detatch",
]

FINANCIAL_PERMS = [
    "invoice:create", "invoice:update", "invoice:delete",
    "payment:create", "payment:update", "payment:delete",
    "receipt:create", "receipt:update", "receipt:delete",
]

PRESCRIPTION_PERMS = [
    "prescription:create", "prescription:update", "prescription:delete"
]

# Combined permission groups
ADMIN_PERMS = (
    ORG_PERMS + REPORT_PERMS + APIKEY_PERMS + FILE_PERMS + EMAIL_TEMPLATE_PERMS +
    PRODUCT_AND_INVENTORY_PERMS + FINANCIAL_PERMS + CATEGORY_PERMS
)

PATIENT_PERMS = [
    "payment:create", "payment:update", "payment:delete",
]

DOCTOR_PERMS = (
    FILE_PERMS + PRODUCT_AND_INVENTORY_PERMS + FINANCIAL_PERMS + CATEGORY_PERMS
    + PRESCRIPTION_PERMS
)

# Role to permissions mapping
ROLE_PERMISSIONS: Dict[str, List[str]] = {
    # System roles
    "Superadmin": ["*"],  # Wildcard for all permissions
    
    # Organization roles
    "Owner": ADMIN_PERMS,
    "Admin": ADMIN_PERMS[1:],  # All except org:delete
    "Patient": PATIENT_PERMS,
    "Doctor": DOCTOR_PERMS,
}
