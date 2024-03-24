# SELECT queries

select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex = 'F';
"""

select_alive_brown_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE alive = 1 AND color = 'Brown';
"""

select_dead_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE alive = 0;
"""

select_bears_return_all_columns_ordered_by_name_descending = """
    SELECT * FROM bears
    ORDER BY name DESC;
"""

select_youngest_bear_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE age = (SELECT MIN(age) FROM bears);
"""
