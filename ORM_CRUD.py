from db_connection import Session
from product_stocks import ProductStock

# Create:
product = ProductStock(category="Laptops", stock=999)

with Session() as sess:
    sess.add(product)
    sess.commit()

# Read
with Session() as sess:
    result1 = (
        sess.query(ProductStock).filter(ProductStock.stock_id == 1).first()
    )
    result2 = sess.query(ProductStock).filter_by(stock_id=1).first()
    result1 is result2
    # True
    print(result1.stock_id, result1.category, result1.stock)
    # 1 Laptops 999

# Update
with Session() as sess:
    result = (
        sess.query(ProductStock).filter(ProductStock.stock_id == 1).first()
    )
    result.stock = 1000
    sess.add(result)
    sess.commit()


with Session() as sess:
    product_new = ProductStock(stock_id=1, category="Laptops", stock=2000)
    # sess.add(product_new) will raise a Duplicate entry exception.
    sess.merge(product_new)
    sess.commit()


# Delete
with Session() as sess:
    result = (
        sess.query(ProductStock).filter(ProductStock.stock_id == 1).first()
    )
    sess.delete(result)
    sess.commit()
