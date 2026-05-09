from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DB_NAME = 'database.db'


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():

    data = request.form

    event_name = data['event_name']
    event_type = data['event_type']
    venue = data['venue']
    start_datetime = data['start_datetime']
    end_datetime = data['end_datetime']
    organizer = data['organizer']
    email = data['email']
    requirements = data['requirements']

    conn = get_db_connection()

    conflict = conn.execute(
        '''
        SELECT * FROM bookings
        WHERE venue = ?
        AND (
            start_datetime < ?
            AND end_datetime > ?
        )
        ''',
        (venue, end_datetime, start_datetime)
    ).fetchone()

    conflict_value = 1 if conflict else 0

    conn.execute(
        '''
        INSERT INTO bookings (
            event_name,
            event_type,
            venue,
            start_datetime,
            end_datetime,
            organizer,
            email,
            requirements,
            conflict
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (
            event_name,
            event_type,
            venue,
            start_datetime,
            end_datetime,
            organizer,
            email,
            requirements,
            conflict_value
        )
    )

    conn.commit()
    conn.close()

    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():

    conn = get_db_connection()

    bookings = conn.execute(
        'SELECT * FROM bookings ORDER BY id DESC'
    ).fetchall()

    conn.close()

    return render_template(
        'dashboard.html',
        bookings=bookings
    )


@app.route('/approval/<int:id>')
def approval(id):

    conn = get_db_connection()

    booking = conn.execute(
        'SELECT * FROM bookings WHERE id = ?',
        (id,)
    ).fetchone()

    conn.close()

    return render_template(
        'approval.html',
        booking=booking
    )


@app.route('/update_status/<int:id>/<status>')
def update_status(id, status):

    conn = get_db_connection()

    conn.execute(
        'UPDATE bookings SET status = ? WHERE id = ?',
        (status, id)
    )

    conn.commit()
    conn.close()

    return redirect('/dashboard')


@app.route('/analytics')
def analytics():

    conn = get_db_connection()

    total = conn.execute(
        'SELECT COUNT(*) as count FROM bookings'
    ).fetchone()['count']

    approved = conn.execute(
        "SELECT COUNT(*) as count FROM bookings WHERE status='Approved'"
    ).fetchone()['count']

    rejected = conn.execute(
        "SELECT COUNT(*) as count FROM bookings WHERE status='Rejected'"
    ).fetchone()['count']

    pending = conn.execute(
        "SELECT COUNT(*) as count FROM bookings WHERE status='Pending'"
    ).fetchone()['count']

    conn.close()

    return render_template(
        'analytics.html',
        total=total,
        approved=approved,
        rejected=rejected,
        pending=pending
    )


if __name__ == '__main__':
    app.run(debug=True)