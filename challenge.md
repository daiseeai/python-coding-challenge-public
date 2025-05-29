# The Task(s)

* Your first challenge is to consider the whole existing stub structure of this repo.
* Consider what you know about using `FastAPI`, `RESTFul API` design and best practices for software projects in general.


## Part 1: Implement the `routers/products.py` endpoints
* See the Appendix for more detail if needed. 
* Your challenge is to implement as many as you can of the following endpoints.
> NOTE: Use the Appendix section for some hints on how this might look.

### CRUD
* `GET` all products.
    * Optional filtering/queries (see Appendix)
* `UPDATE` a specific (existing) product.
* `CREATE` a new product.
* `DELETE` a product.

### Bonus
* `GET` Products by category.
* `GET` Products within a price range.
* `GET` Useful Statistics on `Categories` of products.
* `GET` Products that are low in stock.


## Part 2: Generic Open Questions.
1. What would you add/improve or change here if you had more time?
> NOTE: this challenge was not engineered to be perfect. But rather have areas for improvement.

2. Can you spot any issues regarding `version and dependency management`?

3. Can you spot any current security issues with this repo?


# Appendix.
* Below are some example endpoints you may add or how some requests may look...

## New Endpoints

### Products: Basic CRUD...
- `GET /products`: List all products with optional filtering and pagination
  - Query parameters:
    - `skip`: Number of records to skip (default: 0)
    - `limit`: Maximum number of records to return (default: 100)
    - `category`: Filter by category name

- `GET /products/{product_id}`: Get a specific product by UUID
  - Path parameter: `product_id` (UUID string)

- `POST /products`: Create a new product
  - Request body: Product details (name, description, price, category, stock)

- `PUT /products/{product_id}`: Update an existing product
  - Path parameter: `product_id` (UUID string)
  - Request body: Updated product details

- `DELETE /products/{product_id}`: Delete a product
  - Path parameter: `product_id` (UUID string)

### Products: Extended/Optional
- `GET /products/category/{category}`: Get all products in a specific category
  - Path parameter: `category` (string)
  - Query parameters: `skip` and `limit` for pagination

- `GET /products/price-range`: Get products within a price range
  - Query parameters:
    - `min_price`: Minimum price (float)
    - `max_price`: Maximum price (float)
    - `skip` and `limit` for pagination

- `GET /products/low-stock`: Get products with low stock
  - Query parameters:
    - `threshold`: Stock threshold (default: 10)
    - `skip` and `limit` for pagination

- `GET /products/categories/stats`: Get statistics for each category
  - Returns: Product count, average price, minimum price, and maximum price per category

### Example Queries (not exhaustive)
```bash
# Get all products
curl -X GET "http://localhost:8000/products" -H "Authorization: Bearer test-token"

# Get product by specific uuid
curl -X GET "http://localhost:8000/products/{UUID}" -H "Authorization: Bearer test-token" 

# Get products by category
curl -X GET "http://localhost:8000/products?category=Electronics" -H "Authorization: Bearer test-token"

# Create a new product
curl -X POST "http://localhost:8000/products" \
  -H "Authorization: Bearer test-token" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Google Glass New Product",
    "description": "The Best Eyewear one could possibly hope for.",
    "price": 1500.00,
    "category": "Electronics",
    "stock": 999
  }'

# Update, delete etc...
```
