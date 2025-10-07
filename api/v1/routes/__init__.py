from fastapi import APIRouter

from api.v1.routes.auth import auth_router
from api.v1.routes.apikey import apikey_router
from api.v1.routes.user import user_router
from api.v1.routes.organization import organization_router
from api.v1.routes.location import location_router
from api.v1.routes.contact_info import contact_info_router

v1_router = APIRouter(prefix='/api/v1')

# Register all routes
v1_router.include_router(auth_router)
v1_router.include_router(apikey_router)
v1_router.include_router(user_router)
v1_router.include_router(organization_router)
v1_router.include_router(location_router)
v1_router.include_router(contact_info_router)
