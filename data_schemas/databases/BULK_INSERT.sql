BULK INSERT dbo.DANIA
FROM 'C:\workspaces\data-generator-for-data-sources\out\database\dishes_t1.csv'
WITH ( FORMAT = 'CSV');

BULK INSERT dbo.PROMOCJE
FROM 'C:\workspaces\data-generator-for-data-sources\out\database\promotions_t1.csv'
WITH ( FORMAT = 'CSV');

BULK INSERT dbo.PRZEDMIOTY_ZAMOWIEN
FROM 'C:\workspaces\data-generator-for-data-sources\out\database\orders_items_t1.csv'
WITH ( FORMAT = 'CSV');

BULK INSERT dbo.REKLAMY
FROM 'C:\workspaces\data-generator-for-data-sources\out\database\ads_t1.csv'
WITH ( FORMAT = 'CSV');

BULK INSERT dbo.ZAMOWIENIA
FROM 'C:\workspaces\data-generator-for-data-sources\out\database\orders_t1.csv'
WITH ( FORMAT = 'CSV');