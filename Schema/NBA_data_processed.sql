create table if not exists NBA_data_processed(
    player text primary key, 
    pos text,
    age int,
    Tm text,
    FG float,
    threeP float,
    twoP float,
    FT float, 
    AST float,
    STL float, 
    BLK float, 
    Pts float
)