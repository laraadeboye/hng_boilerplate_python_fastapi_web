from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from urllib.parse import urlparse, parse_qs
from api.v1.schemas import invitations
from api.db.database import get_db as get_session
from api.v1.services import invite
from api.v1.models.user import User
from api.utils.success_response import success_response
from api.v1.services.user import user_service
import logging

invites = APIRouter(prefix="/invite", tags=["Invitation Management"])

# Add other necessary imports


# generate invitation link to join organization
@invites.post("/create", tags=["Invitation Management"])
async def generate_invite_link(
    invite_schema: invitations.InvitationCreate, 
    request: Request, 
    session: Session = Depends(get_session), 
    current_user: User = Depends(user_service.get_current_user)
):
    return invite.InviteService.create(invite_schema, request, session)


# Add user to organization
@invites.post("/accept", tags=["Invitation Management"])
async def add_user_to_organization(
    request: Request, 
    user_data: invitations.UserAddToOrganization, 
    session: Session = Depends(get_session), 
    current_user: User = Depends(user_service.get_current_user)
):
    logging.info("Received request to accept invitation.")
    query_params = parse_qs(urlparse(user_data.invitation_link).query)
    invite_id = query_params.get("invitation_id", [None])[0]

    if not invite_id:
        logging.warning("Invitation ID not found in the link.")
        raise HTTPException(status_code=400, detail="Invalid invitation link")

    logging.info(f"Processing invitation ID: {invite_id}")

    return invite.InviteService.add_user_to_organization(invite_id, session)

@invites.delete("/{invite_id}", status_code=200, response_model=success_response)
def delete_invite(
    invite_id: str,
    db: Session = Depends(get_session), 
    admin: User = Depends(user_service.get_current_super_admin)
):
    """ Delete invite from database """
    if invite_id.strip() == "":
        logging.warning(f"Invitation ID not found in path parameter.")
        raise HTTPException(status_code=404, detail="Invite id is absent")
    
    invite_is_deleted = invite.InviteService.delete(db, invite_id)

    if not invite_is_deleted:
        raise HTTPException(status_code=404, detail="Invalid invitation id")

    logging.info(f"Deleted invite. ID: {invite_id}")

    return success_response(
        status_code=200,
        message='Invite deleted successfully',
    )