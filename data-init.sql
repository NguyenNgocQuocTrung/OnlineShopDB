INSERT INTO [USER] (FirstName, LastName, Email, Phone, Password, Address, City, PostalCode)
VALUES ('Nguyen', 'Van Manh', 'elroydevops@gmail.com', '0900000009', '0900000009', 'Ha Noi', 'Ha Noi', '000084');

-- Thêm dữ liệu vào bảng PRODUCT
INSERT INTO PRODUCT (ProductID, Name, Brand, Description, ImageURL)
VALUES 
    (1, 'Nike Air Max 270', 'Nike', 'The Nike Air Max 270 combines elements from the Air Max family and modern styling for a sneaker that''s sure to turn heads.', 'https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/38321ec6-8c92-488d-924d-02dd07eaeceb/air-max-270-older-shoes-tnlrnr.png'),
    (2, 'Adidas Ultra Boost', 'Adidas', 'The Adidas Ultra Boost is a popular running shoe known for its comfort and style.', 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/f042b05ad1bf4d51b7dfaf1600054038_9366/Ultraboost_1.0_Shoes_White_HQ4202_01_standard.jpg'),
    (3, 'Converse Chuck Taylor All Star', 'Converse', 'The Converse Chuck Taylor All Star is a classic sneaker that''s been a staple for decades.', 'https://supersports.com.vn/cdn/shop/products/M7652C-1.jpg?v=1700128411&width=1920'),
    (4, 'Vans Old Skool', 'Vans', 'The Vans Old Skool is a timeless skate shoe with a durable canvas and suede upper.', 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/4896bd57f0894845b5c0ae8300eec549_9366/Grand_Court_Cloudfoam_Comfort_Shoes_White_GW9195_01_standard.jpg')
-- Thêm dữ liệu vào bảng PRODUCT_SIZE cho sản phẩm Nike Air Max 270
INSERT INTO PRODUCT_SIZE (ProductSizeID, Size, Price, Quantity, ProductID)
VALUES 
    (1, 36, 3109000, 10, 1),
    (2, 37, 3109000, 10, 1),
    (3, 38, 3109000, 10, 1),
    (4, 39, 3109000, 10, 1),
    (5, 40, 3109000, 10, 1),
    (6, 41, 3109000, 10, 1),
    (7, 42, 3109000, 10, 1),
    (8, 43, 3109000, 10, 1);

-- Thêm dữ liệu vào bảng PRODUCT_SIZE cho sản phẩm Adidas Ultra Boost
INSERT INTO PRODUCT_SIZE (ProductSizeID, Size, Price, Quantity, ProductID)
VALUES 
    (9, 36, 4500000, 10, 2),
    (10, 37, 4500000, 10, 2),
    (11, 38, 4500000, 10, 2),
    (12, 39, 4500000, 10, 2),
    (13, 40, 4500000, 10, 2),
    (14, 41, 4500000, 10, 2),
    (15, 42, 4500000, 10, 2),
    (16, 43, 4500000, 10, 2);

-- Thêm dữ liệu vào bảng PRODUCT_SIZE cho sản phẩm Converse Chuck Taylor All Star
INSERT INTO PRODUCT_SIZE (ProductSizeID, Size, Price, Quantity, ProductID)
VALUES 
    (17, 36, 1015000, 10, 3),
    (18, 37, 1015000, 10, 3),
    (19, 38, 1015000, 10, 3),
    (20, 39, 1015000, 10, 3),
    (21, 40, 1015000, 10, 3),
    (22, 41, 1015000, 10, 3),
    (23, 42, 1015000, 10, 3),
    (24, 43, 1015000, 10, 3);

-- Thêm dữ liệu vào bảng PRODUCT_SIZE cho sản phẩm Vans Old Skool
INSERT INTO PRODUCT_SIZE (ProductSizeID, Size, Price, Quantity, ProductID)
VALUES 
    (25, 36, 2000000, 10, 4),
    (26, 37, 2000000, 10, 4),
    (27, 38, 2000000, 10, 4),
    (28, 39, 2000000, 10, 4),
    (29, 40, 2000000, 10, 4),
    (30, 41, 2000000, 10, 4),
    (31, 42, 2000000, 10, 4),
    (32, 43, 2000000, 10, 4);


-- Thêm dữ liệu vào bảng PRODUCT
INSERT INTO PRODUCT (ProductID, Name, Brand, Description, ImageURL)
VALUES 
    (5, 'Adidas Questar Flow NXT "Core Black"', 'Adidas', 'Mẫu giày thể thao nam với thiết kế hiện đại, phù hợp cho hoạt động hàng ngày.', 'https://tse3.mm.bing.net/th?id=OIP.MlGESVS2tdsVopDWWjQMswHaFT&pid=Api'),
    (6, 'Adidas Alphacomfy "Core Black"', 'Adidas', 'Giày thể thao nam với đệm êm ái, mang lại sự thoải mái tối đa.', 'https://tse3.mm.bing.net/th?id=OIP.cQ-5ee-6m8QDk7e45lLAOQHaHa&pid=Api'),
    (7, 'Adidas Switch Run "Solar Red"', 'Adidas', 'Giày chạy bộ nam với màu sắc nổi bật, thiết kế năng động.', 'https://tse4.mm.bing.net/th?id=OIP.bg4kJgktlXPLGkdO6ucmJQHaHa&pid=Api'),
    (8, 'Adidas Stan Smith "Bold Pink"', 'Adidas', 'Giày thời trang nữ với thiết kế cổ điển, điểm nhấn màu hồng nổi bật.', 'https://tse1.mm.bing.net/th?id=OIP.l4jtro_UsRlbjHceMftRFAAAAA&pid=Api'),
    (9, 'Adidas Ultrabounce "Black White"', 'Adidas', 'Giày thể thao nữ với công nghệ đệm Ultrabounce, mang lại sự êm ái khi di chuyển.', 'https://tse4.mm.bing.net/th?id=OIP.XbkW2BdNtf-rSJWptTFP-QHaHa&pid=Api');

-- Thêm dữ liệu vào bảng PRODUCT_SIZE cho các sản phẩm Adidas mới
INSERT INTO PRODUCT_SIZE (ProductSizeID, Size, Price, Quantity, ProductID)
VALUES 
    (33, 35, 1090000, 10, 5),
    (34, 36, 1090000, 8, 5),
    (35, 37, 1090000, 5, 5),
    (36, 38, 1090000, 7, 5),
    (37, 39, 1090000, 9, 5),

    (38, 35, 1290000, 10, 6),
    (39, 37, 1290000, 7, 6),
    (40, 38, 1290000, 6, 6),
    (41, 39, 1290000, 5, 6),
    (42, 41, 1290000, 8, 6),

    (43, 36, 1350000, 5, 7),
    (44, 38, 1350000, 7, 7),
    (45, 40, 1350000, 4, 7),
    (46, 41, 1350000, 10, 7),

    (47, 35, 1290000, 8, 8),
    (48, 36, 1290000, 10, 8),
    (49, 39, 1290000, 5, 8),

    (50, 37, 1190000, 6, 9),
    (51, 39, 1190000, 7, 9),
    (52, 41, 1190000, 10, 9);


-- Thêm dữ liệu vào bảng PRODUCT
INSERT INTO PRODUCT (ProductID, Name, Brand, Description, ImageURL)
VALUES 
    (10, 'Adidas Ultrabounce "Cloud White"', 'Adidas', 'Phiên bản màu trắng tinh tế, phù hợp với nhiều phong cách thời trang.', 'https://tse2.mm.bing.net/th?id=OIP.9Ga00pVei3ZDbmjsqJv_vgHaHa&pid=Api'),
    (11, 'Adidas Alphacomfy "Clear Pink"', 'Adidas', 'Giày thể thao với tông màu hồng nhạt, thiết kế trẻ trung.', 'https://tse2.mm.bing.net/th?id=OIP.iOqwojPvRbKp2wulWDL0EAHaHa&pid=Api'),
    (12, 'Adidas Duramo RC "Grey Three"', 'Adidas', 'Giày thể thao nữ với màu xám trung tính, phù hợp cho luyện tập và đi bộ.', 'https://tse2.mm.bing.net/th?id=OIP.9rQ2hq-uEkAEQbsKn7Y97wHaHa&pid=Api'),
    (13, 'Adidas Run 60s 2.0 "Grey One"', 'Adidas', 'Giày thể thao nam với thiết kế lấy cảm hứng từ thập niên 60, mang lại vẻ ngoài cổ điển.', 'https://tse2.mm.bing.net/th?id=OIP._JxuFxCXimjL-TI9gyQqhwHaHa&pid=Api'),
    (14, 'Adidas Lite Racer Rebold "Shadow Navy"', 'Adidas', 'Giày thể thao nam với màu xanh navy, thiết kế nhẹ nhàng, thoải mái.', 'https://tse3.mm.bing.net/th?id=OIP.HEofcZOHdYAJzeYwQwtgCwHaHa&pid=Api');

-- Thêm dữ liệu vào bảng PRODUCT_SIZE cho các sản phẩm Adidas mới
INSERT INTO PRODUCT_SIZE (ProductSizeID, Size, Price, Quantity, ProductID)
VALUES 
    (53, 35, 1050000, 8, 10),
    (54, 36, 1050000, 10, 10),
    (55, 38, 1050000, 6, 10),
    (56, 39, 1050000, 4, 10),
    (57, 41, 1050000, 7, 10),

    (58, 37, 1250000, 10, 11),
    (59, 39, 1250000, 8, 11),
    (60, 40, 1250000, 5, 11),
    (61, 42, 1250000, 10, 11),

    (62, 35, 990000, 7, 12),
    (63, 36, 990000, 5, 12),
    (64, 38, 990000, 10, 12),
    (65, 40, 990000, 8, 12),

    (66, 36, 990000, 6, 13),
    (67, 37, 990000, 8, 13),
    (68, 39, 990000, 5, 13),
    (69, 41, 990000, 7, 13),

    (70, 35, 990000, 5, 14),
    (71, 36, 990000, 10, 14),
    (72, 38, 990000, 6, 14),
    (73, 39, 990000, 4, 14),
    (74, 41, 990000, 7, 14);


-- Thêm dữ liệu vào bảng PRODUCT
INSERT INTO PRODUCT (ProductID, Name, Brand, Description, ImageURL)
VALUES 
    (15, 'Adidas Lite Racer Rebold "Halo Silver"', 'Adidas', 'Giày thể thao nam với thiết kế hiện đại và màu bạc thanh lịch.', 'https://tse4.mm.bing.net/th?id=OIP.HEofcZOHdYAJzeYwQwtgCwHaHa&pid=Api'),
    (16, 'Adidas Questar Flow NXT "Cloud White"', 'Adidas', 'Giày thể thao nam với màu trắng sang trọng, phù hợp cho mọi phong cách.', 'https://tse3.mm.bing.net/th?id=OIP.MlGESVS2tdsVopDWWjQMswHaFT&pid=Api'),
    (17, 'Adidas Daily 3.0 "Cloud White"', 'Adidas', 'Giày thể thao nam phong cách hiện đại với màu trắng thanh lịch.', 'https://tse2.mm.bing.net/th?id=OIP.iOqwojPvRbKp2wulWDL0EAHaHa&pid=Api'),
    (18, 'Adidas Kantana "Cloud White"', 'Adidas', 'Giày thời trang với thiết kế đơn giản, phù hợp với mọi phong cách.', 'https://tse2.mm.bing.net/th?id=OIP.9Ga00pVei3ZDbmjsqJv_vgHaHa&pid=Api'),
    (19, 'Adidas VL Court Base "Cloud White"', 'Adidas', 'Thiết kế cổ điển với màu trắng trang nhã, phù hợp cho mọi phong cách.', 'https://tse3.mm.bing.net/th?id=OIP.9rQ2hq-uEkAEQbsKn7Y97wHaHa&pid=Api');

-- Thêm dữ liệu vào bảng PRODUCT_SIZE cho các sản phẩm Adidas mới
INSERT INTO PRODUCT_SIZE (ProductSizeID, Size, Price, Quantity, ProductID)
VALUES 
    (75, 36, 990000, 8, 15),
    (76, 38, 990000, 6, 15),
    (77, 39, 990000, 4, 15),
    (78, 41, 990000, 7, 15),

    (79, 35, 1050000, 8, 16),
    (80, 37, 1050000, 6, 16),
    (81, 38, 1050000, 5, 16),
    (82, 40, 1050000, 7, 16),

    (83, 36, 990000, 7, 17),
    (84, 37, 990000, 9, 17),
    (85, 39, 990000, 6, 17),
    (86, 42, 990000, 5, 17),

    (87, 35, 1290000, 8, 18),
    (88, 36, 1290000, 10, 18),
    (89, 38, 1290000, 7, 18),
    (90, 40, 1290000, 4, 18),

    (91, 35, 1200000, 8, 19),
    (92, 36, 1200000, 9, 19),
    (93, 39, 1200000, 5, 19),
    (94, 41, 1200000, 10, 19);

-- Thêm dữ liệu vào bảng PRODUCT
INSERT INTO PRODUCT (ProductID, Name, Brand, Description, ImageURL)
VALUES 
    (20, 'Adidas Ultraboost 1.0 x Disney 100 "Grey"', 'Adidas', 'Giày thể thao nữ với thiết kế đặc biệt kỷ niệm 100 năm Disney, màu xám tinh tế.', 'https://tse4.mm.bing.net/th?id=OIP.aRzLKRUswmwt9rfmELAk6AHaHa&pid=Api'),
    (21, 'Adidas Ultraboost 1.0 "Black White"', 'Adidas', 'Giày thể thao nam với phối màu đen trắng cổ điển, phù hợp cho nhiều hoạt động.', 'https://tse2.mm.bing.net/th?id=OIP.Lyjxpqky2yawyXHXq5r8bAHaHa&pid=Api'),
    (22, 'Adidas Ultraboost PB W "Black Pink"', 'Adidas', 'Giày thể thao nữ với phối màu đen hồng nổi bật, thiết kế nhẹ nhàng.', 'https://tse3.mm.bing.net/th?id=OIP.flXlNYiE6VjG_dFThAZ4iwHaHa&pid=Api'),
    (23, 'Adidas Ultraboost 20 Lab "Black"', 'Adidas', 'Giày thể thao nam với công nghệ tiên tiến, màu đen mạnh mẽ.', 'https://tse1.mm.bing.net/th?id=OIP.PtVKqKdw2fPqH1i0ukly7AHaEv&pid=Api'),
    (24, 'Adidas Ultraboost 20 "Black"', 'Adidas', 'Giày thể thao nam với thiết kế hiện đại, màu đen sang trọng.', 'https://tse2.mm.bing.net/th?id=OIP.8llhDfSwW3HNO9Rw3o-maQHaHa&pid=Api'),
    (25, 'Adidas Ultraboost Light "Blue"', 'Adidas', 'Giày thể thao nữ với màu xanh dịu nhẹ, thiết kế nhẹ nhàng.', 'https://tse4.mm.bing.net/th?id=OIP.7pzWjsBQ5WZLbZWO8IIhTAHaHa&pid=Api'),
    (26, 'Adidas Ultraboost Light "Grey/Pink"', 'Adidas', 'Giày thể thao nữ với phối màu xám hồng tinh tế, phù hợp cho nhiều hoạt động.', 'https://tse2.mm.bing.net/th?id=OIP._1jNrZJF0W5qq1EnMKISpwHaHa&pid=Api'),
    (27, 'Adidas Ultraboost Light "Solar Red"', 'Adidas', 'Giày thể thao nữ với màu đỏ rực rỡ, thiết kế năng động.', 'https://tse1.mm.bing.net/th?id=OIP.3P-fiuHUthGOjKQ6GrxlWwHaHa&pid=Api'),
    (28, 'Adidas Ultraboost 23 Light "Core Black"', 'Adidas', 'Giày thể thao nam với màu đen cổ điển, công nghệ đệm tiên tiến.', 'https://tse2.mm.bing.net/th?id=OIP.FPmhXX1ad3W5TSEIDgc3ewHaFL&pid=Api'),
    (29, 'Adidas Ultraboost Light "Dark Blue"', 'Adidas', 'Giày thể thao nữ với màu xanh đậm, thiết kế thanh lịch.', 'https://tse3.mm.bing.net/th?id=OIP.7OfZsgOuGZb0xhlW-YVaXwHaE8&pid=Api');

-- Thêm dữ liệu vào bảng PRODUCT_SIZE cho các sản phẩm Adidas mới
INSERT INTO PRODUCT_SIZE (ProductSizeID, Size, Price, Quantity, ProductID)
VALUES 
    (115, 36, 2500000, 10, 20),
    (116, 37, 2500000, 8, 20),
    (117, 38, 2500000, 5, 20),
    (118, 39, 2500000, 7, 20),
    (119, 40, 2500000, 9, 20),

    (120, 35, 2700000, 10, 21),
    (121, 37, 2700000, 7, 21),
    (122, 38, 2700000, 6, 21),
    (123, 40, 2700000, 5, 21),
    (124, 42, 2700000, 8, 21),

    (125, 36, 2600000, 5, 22),
    (126, 38, 2600000, 7, 22),
    (127, 39, 2600000, 4, 22),
    (128, 41, 2600000, 10, 22),

    (129, 35, 2750000, 8, 23),
    (130, 37, 2750000, 10, 23),
    (131, 39, 2750000, 5, 23),

    (132, 36, 2400000, 6, 24),
    (133, 39, 2400000, 7, 24),
    (134, 41, 2400000, 10, 24),

    (135, 36, 2300000, 8, 25),
    (136, 37, 2300000, 9, 25),
    (137, 39, 2300000, 6, 25),
    (138, 40, 2300000, 4, 25),

    (139, 35, 2450000, 8, 26),
    (140, 37, 2450000, 10, 26),
    (141, 38, 2450000, 5, 26),

    (142, 36, 2500000, 6, 27),
    (143, 38, 2500000, 8, 27),
    (144, 40, 2500000, 7, 27),

    (145, 37, 2750000, 8, 28),
    (146, 39, 2750000, 6, 28),
    (147, 41, 2750000, 9, 28),

    (148, 35, 2800000, 7, 29),
    (149, 36, 2800000, 10, 29),
    (150, 39, 2800000, 5, 29);

-- Thêm dữ liệu vào bảng PRODUCT
INSERT INTO PRODUCT (ProductID, Name, Brand, Description, ImageURL)
VALUES 
    (30, 'Adidas Ultraboost 1.0 x Disney 100 "Grey"', 'Adidas', 'Giày thể thao nữ với thiết kế đặc biệt kỷ niệm 100 năm Disney, màu xám tinh tế.', 'https://tse4.mm.bing.net/th?id=OIP.aRzLKRUswmwt9rfmELAk6AHaHa&pid=Api'),
    (31, 'Adidas Ultraboost 1.0 "Black White"', 'Adidas', 'Giày thể thao nam với phối màu đen trắng cổ điển, phù hợp cho nhiều hoạt động.', 'https://tse2.mm.bing.net/th?id=OIP.Lyjxpqky2yawyXHXq5r8bAHaHa&pid=Api'),
    (32, 'Adidas Ultraboost PB W "Black Pink"', 'Adidas', 'Giày thể thao nữ với phối màu đen hồng nổi bật, thiết kế nhẹ nhàng.', 'https://tse3.mm.bing.net/th?id=OIP.flXlNYiE6VjG_dFThAZ4iwHaHa&pid=Api'),
    (33, 'Adidas Ultraboost 20 Lab "Black"', 'Adidas', 'Giày thể thao nam với công nghệ tiên tiến, màu đen mạnh mẽ.', 'https://tse1.mm.bing.net/th?id=OIP.PtVKqKdw2fPqH1i0ukly7AHaEv&pid=Api'),
    (34, 'Adidas Ultraboost 20 "Black"', 'Adidas', 'Giày thể thao nam với thiết kế hiện đại, màu đen sang trọng.', 'https://tse2.mm.bing.net/th?id=OIP.8llhDfSwW3HNO9Rw3o-maQHaHa&pid=Api'),
    (35, 'Adidas Ultraboost Light "Blue"', 'Adidas', 'Giày thể thao nữ với màu xanh dịu nhẹ, thiết kế nhẹ nhàng.', 'https://tse4.mm.bing.net/th?id=OIP.7pzWjsBQ5WZLbZWO8IIhTAHaHa&pid=Api'),
    (36, 'Adidas Ultraboost Light "Grey/Pink"', 'Adidas', 'Giày thể thao nữ với phối màu xám hồng tinh tế, phù hợp cho nhiều hoạt động.', 'https://tse2.mm.bing.net/th?id=OIP._1jNrZJF0W5qq1EnMKISpwHaHa&pid=Api'),
    (37, 'Adidas Ultraboost 23 Light "Core Black"', 'Adidas', 'Giày thể thao nam với màu đen cổ điển, công nghệ đệm tiên tiến.', 'https://tse2.mm.bing.net/th?id=OIP.FPmhXX1ad3W5TSEIDgc3ewHaFL&pid=Api'),
    (38, 'Adidas Ultraboost Light "Dark Blue"', 'Adidas', 'Giày thể thao nữ với màu xanh đậm, thiết kế thanh lịch.', 'https://tse3.mm.bing.net/th?id=OIP.7OfZsgOuGZb0xhlW-YVaXwHaE8&pid=Api');

-- Thêm dữ liệu vào bảng PRODUCT_SIZE cho các sản phẩm Adidas mới
INSERT INTO PRODUCT_SIZE (ProductSizeID, Size, Price, Quantity, ProductID)
VALUES 
    (151, 36, 2750000, 10, 30),
    (152, 37, 2750000, 8, 30),
    (153, 39, 2750000, 5, 30),

    (154, 35, 2850000, 9, 31),
    (155, 37, 2850000, 6, 31),
    (156, 40, 2850000, 4, 31),

    (157, 36, 2600000, 10, 32),
    (158, 38, 2600000, 5, 32),
    (159, 40, 2600000, 7, 32),

    (160, 35, 2900000, 8, 33),
    (161, 38, 2900000, 6, 33),
    (162, 41, 2900000, 5, 33),

    (163, 36, 2700000, 10, 34),
    (164, 37, 2700000, 7, 34),
    (165, 39, 2700000, 5, 34),

    (166, 35, 2550000, 6, 35),
    (167, 36, 2550000, 9, 35),
    (168, 38, 2550000, 7, 35),

    (169, 35, 2500000, 10, 36),
    (170, 37, 2500000, 8, 36),
    (171, 40, 2500000, 4, 36),

    (172, 36, 2800000, 9, 37),
    (173, 38, 2800000, 6, 37),
    (174, 42, 2800000, 5, 37),

    (175, 36, 2600000, 10, 38),
    (176, 37, 2600000, 8, 38),
    (177, 39, 2600000, 6, 38);
