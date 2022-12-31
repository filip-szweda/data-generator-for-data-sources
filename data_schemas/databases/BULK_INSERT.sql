USE [baza-zamowien]

BULK INSERT dbo.DANIA
FROM 'D:\workspaces\data-generator-for-data-sources\out\database\dishes_t1.csv'
WITH ( FORMAT = 'CSV');

BULK INSERT dbo.REKLAMY
FROM 'D:\workspaces\data-generator-for-data-sources\out\database\ads_t1.csv'
WITH ( FORMAT = 'CSV');

BULK INSERT dbo.PROMOCJE
FROM 'D:\workspaces\data-generator-for-data-sources\out\database\promotions_t1.csv'
WITH ( FORMAT = 'CSV');

BULK INSERT dbo.ZAMOWIENIA
FROM 'D:\workspaces\data-generator-for-data-sources\out\database\orders_t1.csv'
WITH ( FORMAT = 'CSV');

BULK INSERT dbo.PRZEDMIOTY_ZAMOWIEN
FROM 'D:\workspaces\data-generator-for-data-sources\out\database\orders_items_t1.csv'
WITH ( FORMAT = 'CSV');