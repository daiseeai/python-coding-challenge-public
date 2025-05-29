"""Stub file to for the bulk of the code challenge."""

# A few imports/Hints.
# Required for setting up the DB on init. Why?
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..models import Product
from ..schemas import Product as ProductSchema, ProductCreate, CategoryStats


# Setup The Router.
router = APIRouter()

# Your amazing code to go here.
