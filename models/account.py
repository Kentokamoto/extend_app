from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class IssuerSanction(BaseModel):
    name: str
    status: str


class Organization(BaseModel):
    id: str
    role: str
    joinedAt: str
    lastLoggedInAt: str
    explicit: bool


class User(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str
    phone: str
    phoneIsoCountry: str
    avatarType: str
    avatarUrl: Optional[str] = None
    createdAt: str
    updatedAt: str
    currency: str
    locale: str
    timezone: str
    verified: bool
    hasExpensifyLink: Optional[bool] = None
    quickbooksTokenId: Optional[str] = None
    employeeId: Optional[str] = None
    issuerSanctions: Optional[List[IssuerSanction]] = None
    organization: Optional[Organization] = None
    organizationId: Optional[str] = None
    organizationRole: Optional[str] = None


class Account(BaseModel):
    user: User
    token: str
    refreshToken: str
