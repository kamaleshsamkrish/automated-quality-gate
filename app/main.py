from fastapi import FastAPI

app = FastAPI(title="Automated Code Quality Gate")


@app.get("/")
def home():
    return {
        "application": "Automated Code Quality Gate",
        "version": "1.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


def calculate_total(price: float, quantity: int) -> float:
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative")

    return round(price * quantity, 2)
def faulty_example():
    unused_value = 10
    return "This change is faulty"