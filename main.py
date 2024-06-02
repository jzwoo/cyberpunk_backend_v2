import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.allowed_origins import allowed_origins
from microservices.cart_svc.routes.api.v1.cart import cart
from microservices.product_svc.routes.api.v1.product import product

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cart)
app.include_router(product)
# temporary disable auth and user routes
# app.include_router(auth)
# app.include_router(user)


@app.get("/")
async def root():
    return "Cyberpunk backend server is up and running"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
