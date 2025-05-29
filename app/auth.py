from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Simple authentication for demo purposes
# In a real application, you would use proper JWT authentication
security = HTTPBearer()


def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # For demo purposes, accept any token
    # In a real application, you would validate the token
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials
