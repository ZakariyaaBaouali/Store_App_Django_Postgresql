-- Insert dummy users
INSERT INTO User (user_name, user_email, user_profile_url, user_hash_password, created_at, updated_at)
VALUES
('John Doe', 'johndoe@example.com', 'http://example.com/johndoe', 'hashedpassword1', NOW(), NOW()),
('Jane Smith', 'janesmith@example.com', 'http://example.com/janesmith', 'hashedpassword2', NOW(), NOW()),
('Alice Johnson', 'alicejohnson@example.com', 'http://example.com/alice', 'hashedpassword3', NOW(), NOW()),
('Bob Brown', 'bobbrown@example.com', 'http://example.com/bobbrown', 'hashedpassword4', NOW(), NOW()),
('Charlie White', 'charliewhite@example.com', 'http://example.com/charlie', 'hashedpassword5', NOW(), NOW()),
('David Black', 'davidblack@example.com', 'http://example.com/david', 'hashedpassword6', NOW(), NOW()),
('Emma Green', 'emmagreen@example.com', 'http://example.com/emma', 'hashedpassword7', NOW(), NOW()),
('Frank Harris', 'frankharris@example.com', 'http://example.com/frank', 'hashedpassword8', NOW(), NOW()),
('Grace Lee', 'gracelee@example.com', 'http://example.com/grace', 'hashedpassword9', NOW(), NOW()),
('Henry Adams', 'henryadams@example.com', 'http://example.com/henry', 'hashedpassword10', NOW(), NOW());

-- Insert dummy collections
INSERT INTO Collection (collection_name, created_at, updated_at)
VALUES
('Electronics', NOW(), NOW()),
('Clothing', NOW(), NOW()),
('Home & Kitchen', NOW(), NOW()),
('Books', NOW(), NOW()),
('Toys', NOW(), NOW());

-- Insert dummy products
INSERT INTO Product (product_name, product_description, product_price, product_stock_quantity, product_category_id, created_at, updated_at)
VALUES
('Smartphone', 'Latest model smartphone with advanced features', 599.99, 50, 1, NOW(), NOW()),
('Laptop', 'High-performance laptop for gaming and work', 999.99, 30, 1, NOW(), NOW()),
('T-shirt', 'Comfortable cotton T-shirt', 19.99, 100, 2, NOW(), NOW()),
('Blender', 'Multi-purpose kitchen blender', 49.99, 40, 3, NOW(), NOW()),
('Novel', 'Bestselling fiction book', 14.99, 60, 4, NOW(), NOW()),
('Action Figure', 'Superhero action figure', 24.99, 80, 5, NOW(), NOW()),
('Headphones', 'Noise-canceling over-ear headphones', 129.99, 25, 1, NOW(), NOW()),
('Jeans', 'Stylish denim jeans', 39.99, 70, 2, NOW(), NOW()),
('Microwave', 'High-power microwave oven', 199.99, 15, 3, NOW(), NOW()),
('Board Game', 'Fun family board game', 29.99, 50, 5, NOW(), NOW());

-- Insert dummy reviews
INSERT INTO Review (user_id, product_id, review_rating, review_comment, created_at, updated_at)
VALUES
(1, 1, 5, 'Excellent phone, very fast!', NOW(), NOW()),
(2, 2, 4, 'Great laptop but battery life could be better.', NOW(), NOW()),
(3, 3, 5, 'Nice and comfy T-shirt.', NOW(), NOW()),
(4, 4, 3, 'Blender works fine but noisy.', NOW(), NOW()),
(5, 5, 5, 'Loved this book, very engaging.', NOW(), NOW()),
(6, 6, 4, 'Cool action figure, good details.', NOW(), NOW()),
(7, 7, 5, 'Best headphones ever, sound quality is amazing!', NOW(), NOW()),
(8, 8, 4, 'Good jeans, fit well.', NOW(), NOW()),
(9, 9, 3, 'Microwave is powerful but buttons feel cheap.', NOW(), NOW()),
(10, 10, 5, 'Our family enjoys this board game a lot!', NOW(), NOW());

-- Insert dummy orders
INSERT INTO Order (user_id, order_total_amount, order_status, created_at)
VALUES
(1, 599.99, 'C', NOW()),
(2, 1019.98, 'P', NOW()),
(3, 19.99, 'C', NOW()),
(4, 49.99, 'F', NOW()),
(5, 14.99, 'C', NOW()),
(6, 24.99, 'P', NOW()),
(7, 129.99, 'C', NOW()),
(8, 39.99, 'P', NOW()),
(9, 199.99, 'F', NOW()),
(10, 29.99, 'C', NOW());

-- Insert dummy order items
INSERT INTO OrderItems (order_id, product_id, order_item_quantity, order_item_price, created_at)
VALUES
(1, 1, 1, 599.99, NOW()),
(2, 2, 1, 999.99, NOW()),
(2, 3, 1, 19.99, NOW()),
(3, 3, 1, 19.99, NOW()),
(4, 4, 1, 49.99, NOW()),
(5, 5, 1, 14.99, NOW()),
(6, 6, 1, 24.99, NOW()),
(7, 7, 1, 129.99, NOW()),
(8, 8, 1, 39.99, NOW()),
(9, 9, 1, 199.99, NOW());

-- Insert dummy wishlist
INSERT INTO Wishlist (user_id, product_id, product_quantity, added_at)
VALUES
(1, 2, 1, NOW()),
(2, 3, 2, NOW()),
(3, 4, 1, NOW()),
(4, 5, 3, NOW()),
(5, 6, 1, NOW()),
(6, 7, 1, NOW()),
(7, 8, 2, NOW()),
(8, 9, 1, NOW()),
(9, 10, 1, NOW()),
(10, 1, 1, NOW());

-- Insert dummy discounts
INSERT INTO Discount (discount_code, discount_type, discount_value, discount_currency, discount_valid_from, discount_valid_until, discount_max_uses, discount_use_count, created_at, updated_at)
VALUES
('DISC10', 'P', 10.00, '$', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 100, 5, NOW(), NOW()),
('FIXED5', 'F', 5.00, '$', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 50, 2, NOW(), NOW()),
('SALE20', 'P', 20.00, '$', NOW(), DATE_ADD(NOW(), INTERVAL 15 DAY), 200, 10, NOW(), NOW());

-- Insert dummy order discounts
INSERT INTO OrderDiscount (order_id, discount_id, applied_at)
VALUES
(1, 1, NOW()),
(2, 2, NOW()),
(3, 3, NOW());
