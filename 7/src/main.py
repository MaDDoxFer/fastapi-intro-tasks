from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Цена продукта должна быть больше 0")
    quantity: int = Field(..., ge=0, description="Количество должно быть больше или равно 0")


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
