from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str = Field(..., description="Размер продукта, например, M, L, XL")
    color: str = Field(..., description="Цвет продукта")
    material: str = Field(..., description="Материал продукта, например, cotton или leather")

class Product(BaseModel):
    name: str = Field(..., description="Название продукта")
    price: float = Field(..., gt=0, description="Цена продукта должна быть больше 0")
    specifications: ProductSpecifications

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

class ProductDetailResponse(ProductResponse):
    specifications: ProductSpecifications

@app.post("/product", response_model=ProductResponse)
def add_product(product: Product):
    global product_id_counter
    new_product = {
        "id": product_id_counter,
        "name": product.name,
        "price": product.price,
        "specifications": product.specifications.dict(),
    }
    product_list.append(new_product)
    product_id_counter += 1
    return new_product

@app.get("/products", response_model=List[ProductResponse])
def get_products():
    return product_list

@app.get("/product/{product_id}", response_model=ProductDetailResponse)
def get_product_by_id(product_id: int):
    for product in product_list:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
# END