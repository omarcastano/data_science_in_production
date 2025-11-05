import time

from prefect import flow, task


@task
def compute_sum(a: int, b: int) -> int:
    """Compute the sum of two numbers"""
    time.sleep(2)

    return a + b


@task
def compute_product(a: int, b: int) -> int:
    """Compute the product of two numbers"""
    time.sleep(2)

    return a * b


@flow
def my_flow() -> None:
    """My first workflow"""

    sum_state = compute_sum(a=1, b=2)
    product_state = compute_product(a=sum_state, b=2)

    print(f"Sum: {sum_state}, Product: {product_state}")


if __name__ == "__main__":
    my_flow()
    my_flow.visualize()
