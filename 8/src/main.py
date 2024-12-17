from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


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


@app.post("/product")
def add_product(product: Product):
    global product_id_counter
    product_data = product.dict()
    product_data["id"] = product_id_counter
    product_list.append(product_data)
    product_id_counter += 1
    return {"message": "Product added successfully"}


@app.get("/products", response_model=List[dict])
def get_products():
    return product_list
# END
