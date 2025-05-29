"""Stub file to for the bulk of the code challenge."""

from fastapi import APIRouter

# A few imports/Hints of what might be helpful here...
# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from sqlalchemy.exc import IntegrityError
# from ..schemas import Product as ProductSchema, ProductCreate, CategoryStats

# NOTE: This import is `required` here to successfully initialize the DB?
# Why? What could you change here?
from ..models import Product


# Setup The Router.
router = APIRouter()

# Your amazing code to go here.
