from agent.tools import run_sql


def get_cancellation_rate():

    sql = """
    SELECT ROUND(
        COUNT(
            CASE
                WHEN reservation_status = 'Cancelled'
                THEN 1
            END
        ) * 100.0 / COUNT(*),
        2
    )
    FROM reservations
    """

    return run_sql(sql)[0][0]


def get_average_adr():

    sql = """
    SELECT ROUND(
        AVG(adr_room)::numeric,
        2
    )
    FROM reservations
    WHERE reservation_status = 'Reserved'
    """

    return run_sql(sql)[0][0]


def get_total_reservations():

    sql = """
    SELECT COUNT(*)
    FROM reservations
    """

    return run_sql(sql)[0][0]


def get_cancelled_reservations():

    sql = """
    SELECT COUNT(*)
    FROM reservations
    WHERE reservation_status = 'Cancelled'
    """

    return run_sql(sql)[0][0]


def get_top_booking_source():

    sql = """
    SELECT source_name,
           COUNT(*) AS bookings
    FROM reservations
    GROUP BY source_name
    ORDER BY bookings DESC
    LIMIT 1
    """

    return run_sql(sql)


def get_top_guest_countries():

    sql = """
    SELECT guest_country,
           COUNT(*) AS bookings
    FROM reservations
    WHERE reservation_status = 'Reserved'
    GROUP BY guest_country
    ORDER BY bookings DESC
    LIMIT 5
    """

    return run_sql(sql)