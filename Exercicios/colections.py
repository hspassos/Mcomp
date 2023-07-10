#Primer on Scientific Programming with Python, 5 edição, no capítulo 6, ex 6.5 na página 405
#name, distance from the sun in light years, apparent brightness, luminosity
data = [
('Alpha Centauri A', 4.3, 0.26, 1.56),
('Alpha Centauri B', 4.3, 0.77, 0.45),
('Alpha Centauri C', 4.2, 0.00001, 0.00006),
("Barnard’s Star", 6.0, 0.00004, 0.0005),
('Wolf 359', 7.7, 0.000001, 0.00002),
('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
('Luyten 726-8 A', 8.4, 0.000003, 0.00006),
('Luyten 726-8 B', 8.4, 0.000002, 0.00004),
('Sirius A', 8.6, 1.00, 23.6),
('Sirius B', 8.6, 0.001, 0.003),
('Ross 154', 9.4, 0.00002, 0.0005),
]

luminosity_dict = {star[0]: star[3] for star in data}

print(luminosity_dict)